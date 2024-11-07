<?php

namespace App\Http\Controllers;

use App\Models\Tarea;
use Illuminate\Http\Request;

class TareaController extends Controller
{
    public function index()
    {
        $tareas = Tarea::all();
        return view('tareas.index', compact('tareas'));
    }

    public function create()
    {
        return view('tareas.create');
    }

    public function store(Request $request)
    {
        $request->validate(['nombre' => 'required']);
        Tarea::create($request->all());
        return redirect()->route('tareas.index');
    }

    public function edit(Tarea $tarea)
    {
        return view('tareas.edit', compact('tarea'));
    }

    public function update(Request $request, Tarea $tarea)
    {
        $request->validate(['nombre' => 'required']);
        $tarea->update($request->all());
        return redirect()->route('tareas.index');
    }

    public function destroy(Tarea $tarea)
    {
        // Redirecciona a la vista de confirmación de eliminación
        return view('tareas.confirmDelete', compact('tarea'));
    }

    public function confirmDelete(Tarea $tarea)
    {
        // Aquí se elimina la tarea una vez confirmada
        $tarea->delete();
        return redirect()->route('tareas.index')->with('success', 'Tarea eliminada');
    }

    public function confirmUpdate(Tarea $tarea)
    {
        // Cambiar el estado de confirmación antes de actualizar
        $tarea->confirmado = true;
        $tarea->save();

        return redirect()->route('tareas.index')->with('success', 'Tarea confirmada y actualizada');
    }
}
