<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\ProductController;
use App\Http\Controllers\OperacionesController;

Route::get('/sumar/{num1}/{num2}',[OperacionesController::class,'suma']);
Route::get('/restar/{num1}/{num2}',[OperacionesController::class,'resta']);
Route::get('/X/{num1}/{num2}',[OperacionesController::class,'multi']);
Route::get('/%/{num1}/{num2}',[OperacionesController::class,'divi']);
Route::get('/saludo',[ProductController::class,'saludo']);
Route::get('/cuadratica',[ProductController::class,'cuadratica']);
Route::get('/product/create',[ProductController::class,'create']);
Route::post('/product/store',[ProductController::class,'store'])->name('product.store');


