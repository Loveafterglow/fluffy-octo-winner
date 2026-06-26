• Desarrolla un programa para administrar hábitos personales. El objetivo es reforzar el uso
de funciones, validaciones, búsquedas lineales y actualización automática de estados.
• El sistema debe trabajar con una lista llamada habitos, la cual se crea vacía al iniciar el
programa y permanece disponible durante toda la ejecución.
• Cada hábito se representa mediante un diccionario con cuatro campos: habito,
dias_objetivo, minutos_diarios y consistente.
• La validación del campo habito debe cumplir la siguiente regla: No puede estar vacío ni
tener solo espacios.
• La validación del campo dias_objetivo debe cumplir la siguiente regla: Debe ser un entero
entre 1 y 7.
• La validación del campo minutos_diarios debe cumplir la siguiente regla: Debe ser un
número decimal mayor que cero.
• El campo consistente se asigna automáticamente con valor False cuando se registra el
elemento y luego se actualiza para todos los registros según la siguiente condición: si el
objetivo semanal es mayor o igual a 5 días, el hábito se considera consistente; de lo
contrario queda en progreso.
• El menú principal debe tener seis opciones: agregar, buscar, eliminar, actualizar estado,
mostrar registros y salir.
• Debes crear funciones separadas para mostrar el menú, leer la opción, validar cada dato,
agregar registros, buscar por coincidencia exacta, actualizar el estado de toda la lista y
mostrar la información final en pantalla.
