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
    Route::post('models/', [App\Http\Controllers\MLModelController::class, 'store_api'])->name('models.store_api');
    Route::get('models/', [App\Http\Controllers\MLModelController::class, 'index_api'])->name('models.index_api');

    Route::post('datasets/', [App\Http\Controllers\DatasetController::class, 'store_api'])->name('datasets.store_api');
    Route::get('datasets/', [App\Http\Controllers\DatasetController::class, 'index_api'])->name('datasets.index_api');

    Route::apiResource('authors', App\Http\Controllers\AuthorController::class)->only(['store', 'index']);
    Route::apiResource('languages', App\Http\Controllers\LanguageController::class)->only(['store', 'index']);
    Route::apiResource('nlp_tasks', App\Http\Controllers\NLPTaskController::class)->only(['store', 'index']);
});
