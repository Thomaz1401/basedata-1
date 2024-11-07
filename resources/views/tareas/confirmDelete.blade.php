<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<h2>¿Estás seguro de que deseas eliminar esta tarea?</h2>
<p><strong>Nombre:</strong> {{ $tarea->nombre }}</p>
<p><strong>Descripción:</strong> {{ $tarea->descripcion }}</p>

<form action="{{ route('tareas.confirmDelete', $tarea->id) }}" method="POST">
    @csrf
    <button type="submit">Confirmar Eliminación</button>
    <a href="{{ route('tareas.index') }}">Cancelar</a>
</form>

</body>
</html>