# Gestor de bibliotecas

Aplicación web desarrollada para el módulo Diseño de Interfaces de 2º de DAM.

Consiste de una aplicación Django que permitirá gestionar bibliotecas: libros disponibles, socios,
préstamos y plazos de
devolución, así como un buscador público de libros disponibles.

## Variables de entorno

- **SECRET_KEY**: Clave secreta de Django.

## Reglas de "negocio"

- Cualquiera puede buscar libros disponibles por título, autor o ISBN.
- Los libros disponibles se muestran en una página de resultados, con un enlace a la ficha del libro.
- Los libros disponibles se pueden ordenar por título, autor o fecha de adquisición.

- El administrador puede dar de alta nuevos libros, socios y préstamos.
- El administrador puede modificar los datos de los libros, socios y préstamos.
- El administrador puede eliminar libros, socios y préstamos.
- El administrador puede penalizar a un socio manualmente por un tiempo determinado.
- El administrador puede eliminar la penalización de un socio.

## Cosas por hacer

- [X] Página de inicio (listado de libros y socios, con buscador)
- [ ] Detalle de libro
- [X] Crear libro
- [ ] Editar libro
- [ ] Eliminar libro

- [ ] Detalle de socio
- [X] Crear socio
- [ ] Editar socio
- [ ] Eliminar socio
- [ ] Penalizar socio
- [ ] Despenalizar socio

- [ ] Detalle de préstamo
- [ ] Crear préstamo
- [ ] Prorrogar préstamo (30 días)
- [ ] Devolver préstamo
- [ ] Eliminar préstamo
- [ ] Listado de préstamos (con buscador)
