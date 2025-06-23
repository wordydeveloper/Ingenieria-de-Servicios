import psycopg2
from pydantic import EmailStr

from shared.utils import formartear_secuencia_insertar_sql, execute_query


def registrar_usuario_pg(
        nombre: str,
        correo: EmailStr,
        clave: str,
        estado: str,
        conexion: psycopg2.extensions.connection | None = None
):
    fields = [
        'nombre',
        'correo',
        'clave',
        'estado']

    values = [nombre, correo, clave, estado]

    sql = "insert into usuario"

    query = formartear_secuencia_insertar_sql(sql, fields)

    query += " returning usuario_id"

    query += " ;"

    results = execute_query(query, values, conn=conexion)

    return next((item['usuarioId'] for item in results), None)


def obtener_usuario_pg(
        correo: EmailStr,
        conexion: psycopg2.extensions.connection | None = None
):

    query = "select * from usuario where correo = %s;"

    results = execute_query(query, [correo], conn=conexion)

    return next((item for item in results), None)







