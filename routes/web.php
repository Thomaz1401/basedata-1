<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ProductController;
use App\Http\Controllers\OperacionesController;
use App\Http\Controllers\ProviderController;
use App\Http\Controllers\JATSController;

use App\Http\Controllers\TareaController;

Route::resource('tareas', TareaController::class);
Route::get('tareas/{tarea}/confirmDelete', [TareaController::class, 'confirmDelete'])->name('tareas.confirmDelete');
Route::get('tareas/{tarea}/confirmUpdate', [TareaController::class, 'confirmUpdate'])->name('tareas.confirmUpdate');



Route::get('/provid', [ProviderController::class, 'create2']);
Route::get('/store2', [ProviderController::class, 'store2']);
Route::get('/providers', [ProviderController::class, 'index2']);
Route::post('/provid/store2', [ProviderController::class, 'store2'])->name('store2');
Route::get('/sumar/{num1}/{num2}',[OperacionesController::class,'suma']);
Route::get('/restar/{num1}/{num2}',[OperacionesController::class,'resta']);
Route::get('/X/{num1}/{num2}',[OperacionesController::class,'multi']);
Route::get('/%/{num1}/{num2}',[OperacionesController::class,'divi']);
Route::get('/saludo',[ProductController::class,'saludo']);
Route::get('/cuadratica',[ProductController::class,'cuadratica']);
Route::get('/create',[ProductController::class,'create']);
Route::post('/store',[ProductController::class,'store'])->name('store');
Route::get('/products',[ProductController::class,'index']);
Route::get('/solicitar-servicio', [JATSController::class, 'create'])->name('JATS.create');
Route::post('/solicitar-servicio', [JATSController::class, 'store'])->name('JATS.store');


