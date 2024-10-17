<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class OperacionesController extends Controller
{
    public function suma($num1, $num2){
        
        $resultado= $num1 + $num2;
        return $resultado;
        return view('operaciones.suma',compact('resultado'));
    }
    public function resta($num1, $num2){
        
        $resultado2= $num1 - $num2;
        return $resultado2;
        return view('operaciones.resta',compact('resultado2'));
    }
    public function multi($num1, $num2){
        
        $resultado3= $num1 * $num2;
        return $resultado3;
        return view('operaciones.multi',compact('resultado3'));
    }
    public function divi($num1, $num2){
        
        $resultado4= $num1 / $num2;
        return $resultado4;
        return view('operaciones.divi',compact('resultado4'));
    }
    public function cuadratica(){
        
        return hola;
       
    }
}
