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

Route::apiResource('author', App\Http\Controllers\AuthorController::class);
Route::apiResource('link', App\Http\Controllers\LinkController::class);
Route::apiResource('dataset', App\Http\Controllers\DatasetController::class);
Route::apiResource('machine-learning-model', App\Http\Controllers\MachineLearningModelController::class);
Route::apiResource('nlp-task', App\Http\Controllers\NLPTaskController::class);
Route::apiResource('resource-stats', App\Http\Controllers\ResourceStatsController::class);