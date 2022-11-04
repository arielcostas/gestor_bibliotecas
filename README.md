# Gestor de bibliotecas

Aplicación web desarrollada para el módulo Diseño de Interfaces de 2º de DAM.

Consiste de una aplicación Django que permitirá gestionar bibliotecas: libros disponibles, socios, préstamos y plazos de
devolución, así como un buscador público de libros disponibles.

## Variables de entorno

- **SECRET_KEY**: Clave secreta de Django.

## Reglas de "negocio"

- Para cada libro solo se puede tener un ejemplar.
- Los socios deben tener un DNI o NIE de 9 caracteres (DNI 8 dígitos + letra, NIE letra + 7 dígitos + letra).
- Los socios pueden tener un máximo de 3 libros prestados.
- Los libros se pueden prestar hasta 30 días.
- Opcionalmente, los préstamos pueden prolongarse hasta un total de 60 días.
- Los libros se pueden devolver antes de la fecha de devolución.
- Cuando un socio haya devuelto tres libros con retraso, recibirá una penalización de 180 días sin poder tomar prestado
  ningún libro.
- Dicha penalización puede ser anulada por el administrador.
- El administrador puede eliminar libros, socios y préstamos.
- El administrador puede penalizar a un socio manualmente por un tiempo determinado.

## Cosas por hacer

- [ ] Página de inicio (listado de libros)
- [ ] Crear libro
- [ ] Editar libro
- [ ] Eliminar libro

- [ ] Listado de socios (con buscador)
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
