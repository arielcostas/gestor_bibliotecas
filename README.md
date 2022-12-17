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
| `DB_NAME`    | `gestorBibliotecas`                                                  |
| `DB_USER`    | `django`                                                             |
| `DB_PASS`    | `django`                                                             |
| `DB_HOST`    | `localhost`                                                          |
| `DB_PORT`    | `3306`                                                               |

## Reglas de "negocio"

- Cualquiera puede buscar libros disponibles por título, autor o ISBN.
- Los libros disponibles se muestran en una página de resultados, con un enlace a la ficha del
  libro.
- Los libros disponibles se pueden ordenar por título, autor o fecha de adquisición.

- El administrador puede dar de alta nuevos libros, socios y préstamos.
- El administrador puede modificar los datos de los libros, socios y préstamos.
- El administrador puede eliminar libros, socios y préstamos.
- El administrador puede penalizar a un socio manualmente por un tiempo determinado.
- El administrador puede eliminar la penalización de un socio.

## Cosas por hacer

- [X] Página de inicio (listado de libros y socios, con buscador)
- [X] Crear libro
- [ ] Editar libro
- [ ] Eliminar libro

- [ ] Detalle de socio
- [X] Crear socio
- [X] Editar socio
- [ ] Eliminar socio
- [X] Penalizar socio
- [X] Despenalizar socio

- [ ] Detalle de préstamo
- [ ] Crear préstamo
- [ ] Prorrogar préstamo (30 días)
- [ ] Devolver préstamo
- [ ] Eliminar préstamo
- [ ] Listado de préstamos (con buscador)
