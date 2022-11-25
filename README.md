# Gestor de bibliotecas

Aplicación web desarrollada para el módulo Diseño de Interfaces de 2º de DAM.

Consiste de una aplicación Django que permitirá gestionar bibliotecas: libros disponibles, socios,
préstamos y plazos de
devolución, así como un buscador público de libros disponibles.

## Variables de entorno

- **SECRET_KEY**: Clave secreta de Django.

## Reglas de "negocio"

- Cada libro está identificado por un código único, que se genera automáticamente al crearlo.
- Para cada libro se almacena el ISBN (puede haber varios libros con el mismo ISBN), título, autor,
  editorial y fecha de adquisición.

- Los socios deben tener un DNI o NIE de 9 caracteres (DNI 8 dígitos + letra, NIE letra + 7 dígitos
  y letra).
- Para los socios se almacena el nombre, apellidos, DNI o NIE, dirección, teléfono y correo electrónico.
- Los socios pueden tener un máximo de 3 libros prestados.
- Para cada socio se almacena también un número de avisos (inicialmente 0) y en caso penalizado, la fecha
  en la que termina.

- Los libros se pueden prestar hasta 30 días.
- Opcionalmente, los préstamos pueden prolongarse hasta un total de 60 días.
- Los libros se pueden devolver antes de la fecha de devolución.
- Cuando un socio haya devuelto cinco libros con retraso, recibirá una penalización de 60 días sin
  poder tomar prestado ningún libro.

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
- [ ] Crear libro
- [ ] Editar libro
- [ ] Eliminar libro

- [ ] Detalle de socio
- [ ] Crear socio
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
