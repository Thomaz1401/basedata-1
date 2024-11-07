<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <!-- resources/views/tareas/create.blade.php -->

<h2>Crear Nueva Tarea</h2>

@if ($errors->any())
    <div>
        <strong>¡Atención!</strong> Hay algunos problemas con tu entrada.<br><br>
        <ul>
            @foreach ($errors->all() as $error)
                <li>{{ $error }}</li>
            @endforeach
        </ul>
    </div>
@endif

<form action="{{ route('tareas.store') }}" method="POST">
    @csrf
    <div>
        <label for="nombre">Nombre:</label>
        <input type="text" name="nombre" id="nombre" value="{{ old('nombre') }}" required>
    </div>

    <div>
        <label for="descripcion">Descripción:</label>
        <textarea name="descripcion" id="descripcion">{{ old('descripcion') }}</textarea>
    </div>

    <button type="submit">Guardar Tarea</button>
    <a href="{{ route('tareas.index') }}">Cancelar</a>
</form>

</body>
</html>