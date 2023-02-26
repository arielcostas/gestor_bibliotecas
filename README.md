# Gestor de bibliotecas

Aplicación web desarrollada para el módulo Diseño de Interfaces de 2º de DAM.

Consiste de una aplicación Django que permitirá gestionar bibliotecas: libros disponibles, socios,
préstamos y plazos de
devolución, así como un buscador público de libros disponibles.

## Variables de entorno

| Clave        | Valor predeterminado                                                 |
|--------------|----------------------------------------------------------------------|
| `SECRET_KEY` | `django-insecure-j91vn+cndujqh2+24pn*q=6klh9qz4mt=yb+j8@1w790+wl3v$` |
| `DB_ENGINE`  | `mysql`                                                              |
| `DBNAME`    | `gestorBibliotecas`                                                  |
| `DBUSER`    | `django`                                                             |
| `DBPASS`    | `django`                                                             |
| `DBHOST`    | `localhost`                                                          |
| `DBPORT`    | `3306`                                                               |

## Reglas de "negocio"

- Cualquiera puede buscar libros disponibles por título, autor o ISBN.
- Los libros disponibles se muestran en una página de resultados, con un enlace a la ficha del
  libro.
- Los libros disponibles se pueden ordenar por título, autor o fecha de adquisición.

- El administrador puede dar de alta nuevos libros y socios.
- El administrador puede modificar los datos de los libros y socios.
- El administrador puede penalizar a un socio manualmente por un tiempo determinado.
- El administrador puede eliminar la penalización de un socio.

- El administrador puede realizar préstamos de libros a socios.
- El administrador puede ver todos los préstamos activos.
- El administrador puede ver todos los préstamos relativos a un socio.
- El administrador puede marcar como devuelto un préstamo.
