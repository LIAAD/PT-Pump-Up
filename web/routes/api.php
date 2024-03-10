<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
|
*/

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});

Route::get('/helloworld', function () {
    return response()->json(['message' => 'Hello World!']);
});

Route::apiResource('author', 'App\Http\Controllers\AuthorController');
Route::apiResource('link', 'App\Http\Controllers\LinkController');
Route::apiResource('dataset', 'App\Http\Controllers\DatasetController');
Route::apiResource('machine-learning-model', 'App\Http\Controllers\MachineLearningModelController');
Route::apiResource('nlp-task', 'App\Http\Controllers\NlpTaskController');