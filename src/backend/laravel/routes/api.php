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



Route::group(['middleware' => ['auth:sanctum']], function () {
    Route::apiResource('models', App\Http\Controllers\MLModelController::class)->only(['store', 'show']);
    Route::get('models/', [App\Http\Controllers\MLModelController::class, 'index_api']);
    Route::apiResource('datasets', App\Http\Controllers\DatasetController::class)->only(['store', 'show']);
    Route::get('datasets/', [App\Http\Controllers\DatasetController::class, 'index_api']);
    Route::apiResource('authors', App\Http\Controllers\AuthorController::class)->only(['store', 'index', 'show']);
    Route::apiResource('languages', App\Http\Controllers\LanguageController::class)->only(['store', 'index', 'show']);
    Route::apiResource('nlp_tasks', App\Http\Controllers\NLPTaskController::class)->only(['store', 'index', 'show']);
});
