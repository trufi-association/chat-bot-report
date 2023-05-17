import json
import psycopg2
import requests
from datetime import datetime  # Asegúrate de agregar esta línea

AIRTABLE_BASE_ID = "AIRTABLE_BASE_ID"
AIRTABLE_API_KEY = "AIRTABLE_API_KEY"
POSTGRES_DBNAME = "POSTGRES_DBNAME"
POSTGRES_USER = "POSTGRES_USER"
POSTGRES_PASSWORD = "POSTGRES_PASSWORD"
POSTGRES_HOST = "POSTGRES_HOST"
POSTGRES_PORT = 54321

AIRTABLE_TABLE_NAME = "Reportes"
PG_TABLE_NAME = "reportes"
FIELDS_MAP = {
    "nombre_categoria": "nombre_categoria",
    "Descripción del evento": "descripcion_evento",
    "Coordenadas": "coordenadas",
    "Archivo": "archivo",
    "url_small": "url_small",
    "url_large": "url_large",
    "Fechadia": "fechadia",  
}


def create_pg_table():
    query = f"""CREATE TABLE IF NOT EXISTS {PG_TABLE_NAME} (
                nombre_categoria VARCHAR(255),
                descripcion_evento TEXT,
                coordenadas VARCHAR(255),
                archivo TEXT,
                url_small TEXT,
                url_large TEXT,
                fechadia date
                );"""
    with psycopg2.connect(
        dbname=POSTGRES_DBNAME,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()


def get_airtable_records(base_id, table_name, api_key):
    url = f"https://api.airtable.com/v0/{base_id}/{table_name}"
    headers = {"Authorization": f"Bearer {api_key}"}
    params = {"view": "Grid view", "filterByFormula": "NOT({sync_pg})"}

    records = []
    while True:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = json.loads(response.text)
            records.extend(data.get("records", []))
            offset = data.get("offset")
            if offset:
                params["offset"] = offset
            else:
                break
        else:
            return None
    return records

def update_airtable_sync_status(record_id, base_id, table_name, api_key):
    url = f"https://api.airtable.com/v0/{base_id}/{table_name}/{record_id}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "fields": {
            "sync_pg": True
        }
    }

    response = requests.patch(url, headers=headers, data=json.dumps(data))
    if response.status_code != 200:
        print(f"Error al actualizar el registro {record_id}: {response.text}")


def insert_pg_records(records):
    with psycopg2.connect(
        dbname=POSTGRES_DBNAME,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_HOST,
        port=POSTGRES_PORT
    ) as conn:
        with conn.cursor() as cur:
            for record in records:
                fields = record.get("fields", {})
                nombre_categoria = fields.get("nombre_categoria")
                if nombre_categoria:
                    fields["nombre_categoria"] = nombre_categoria[0]  # Extraer el valor de la lista
                filtered_fields = {pg_field: fields.get(at_field) for at_field, pg_field in FIELDS_MAP.items()}

                archivo = filtered_fields.get("archivo")
                if archivo:
                    filtered_fields["url_small"] = archivo[0].get("thumbnails", {}).get("small", {}).get("url")
                    filtered_fields["url_large"] = archivo[0].get("thumbnails", {}).get("large", {}).get("url")

                column_names = ", ".join(filtered_fields.keys())
                values = []

                for val in filtered_fields.values():
                    if isinstance(val, (dict, list)):
                        values.append(json.dumps(val))
                    else:
                        values.append(val)

                placeholders = ", ".join(["%s"] * len(values))
                query = f"INSERT INTO {PG_TABLE_NAME} ({column_names}) VALUES ({placeholders})"
                try:
                    cur.execute(query, values)
                    conn.commit()  # Asegúrate de hacer commit aquí, antes de actualizar el registro en Airtable
                    update_airtable_sync_status(record["id"], AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME, AIRTABLE_API_KEY)
                except psycopg2.ProgrammingError as e:
                    print(f"Error al insertar el registro: {e}")
                    print(f"Tabla: {PG_TABLE_NAME}")
                    print(f"Campos: {filtered_fields}")
                    conn.rollback()
                    continue
            conn.commit()



if __name__ == "__main__":
    create_pg_table()
    records = get_airtable_records(AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME, AIRTABLE_API_KEY)
    if records is not None:
        insert_pg_records(records)