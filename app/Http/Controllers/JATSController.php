<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\JATS;

class JATSController extends Controller
{
    // Función para mostrar el formulario
    public function create()
    {
        return view('PROYECTO.pagina1');
    }

    // Función para almacenar la solicitud en la base de datos
    public function store(Request $request)
    {
        // Validar los datos del formulario
        $request->validate([
            'name' => 'required|string|max:255',
            'email' => 'required|email|max:255',
            'phone' => 'required|string|max:20',
            'service_type' => 'required|string',
            'vehicle' => 'required|string|max:255',
            'details' => 'nullable|string'
        ]);

        // Crear y guardar la solicitud en la base de datos
        JATS::create([
            'name' => $request->input('name'),
            'email' => $request->input('email'),
            'phone' => $request->input('phone'),
            'service_type' => $request->input('service_type'),
            'vehicle' => $request->input('vehicle'),
            'details' => $request->input('details')
        ]);

        // Redirigir con un mensaje de éxito
        return redirect()->back()->with('success', '¡Solicitud enviada con éxito!');
    }
}

