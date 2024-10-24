<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ProductController;
use App\Http\Controllers\OperacionesController;
use App\Http\Controllers\ProviderController;

Route::get('/provid', [ProviderController::class, 'create2']);
Route::get('/providers', [ProviderController::class, 'index2']);
Route::get('/sumar/{num1}/{num2}',[OperacionesController::class,'suma']);
Route::get('/restar/{num1}/{num2}',[OperacionesController::class,'resta']);
Route::get('/X/{num1}/{num2}',[OperacionesController::class,'multi']);
Route::get('/%/{num1}/{num2}',[OperacionesController::class,'divi']);
Route::get('/saludo',[ProductController::class,'saludo']);
Route::get('/cuadratica',[ProductController::class,'cuadratica']);
Route::get('/create',[ProductController::class,'create']);
Route::post('/store',[ProductController::class,'store'])->name('store');
Route::get('/products',[ProductController::class,'index']);


