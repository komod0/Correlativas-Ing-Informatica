# Correlativas-Ing.Inormatica

Pequeño programa para ver que materias se pueden cursar en base a las materias aprobadas.
Funciona para la carrera Ingenieria en Informatica (Plan 86) de la Facultad de Ingenieria de la UBA.
Incluye optativas y materias de la orientacion en sistemas distribuidos.

## Comandos

- __agregar_materia [codigo_materia]__
  - *Agrega una materia al listado de materias aprobadas, se usa el codigo de la materia incluyendo puntuacion
segun aparece en el [plan de estudios de la carrera](http://www.fi.uba.ar/sites/default/files/Ingenieria%20en%20Informatica%201986.pdf)*

- __quitar_materia [codigo_materia]__
  - *Quita una materia de el listado de materias aprobadas*
  
- __que_curso__
  - *Muestra un listado de las materias que es posible cursar, junto con el codigo y su carga horaria*
  
  ---
  
 ## Para correr el programa
  
 Bajar el archivo main y el archivo de materias en el mismo directorio y ejecutar desde la terminal:
 `python3 main.py materias.txt`
