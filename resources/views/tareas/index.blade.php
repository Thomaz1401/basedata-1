<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<table>
    <tr>
        <th>Nombre</th>
        <th>Descripción</th>
        <th>Acciones</th>
    </tr>
    @foreach($tareas as $tarea)
    <tr>
        <td>{{ $tarea->nombre }}</td>
        <td>{{ $tarea->descripcion }}</td>
        <td>
            <a href="{{ route('tareas.edit', $tarea->id) }}">Editar</a>
            <a href="{{ route('tareas.confirmDelete', $tarea->id) }}">Eliminar</a>
            <a href="{{ route('tareas.confirmUpdate', $tarea->id) }}">Confirmar Actualización</a>
        </td>
    </tr>
    @endforeach
</table>

</body>
</html>