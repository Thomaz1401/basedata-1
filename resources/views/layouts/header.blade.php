<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>@yield('title', 'Mi Página')</title>
    <!-- Puedes agregar tus archivos CSS aquí -->
    <link rel="stylesheet" href="{{ asset('css/app.css') }}">
</head>
<body>

    <!-- Incluye el header -->
    @include('partials.header')

    <!-- Aquí va el contenido específico de cada página -->
    <div class="container">
        @yield('content')
    </div>

    <!-- Puedes agregar tu footer aquí si lo deseas -->
    <footer>
        <p>&copy; {{ date('Y') }} Mi Página. Todos los derechos reservados.</p>
    </footer>

</body>
</html>
