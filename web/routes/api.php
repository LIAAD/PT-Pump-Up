<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use Illuminate\Support\Facades\Artisan;

use App\Http\Controllers\AuthorController;
use App\Http\Controllers\LinkController;
use App\Http\Controllers\DatasetController;
use App\Http\Controllers\MachineLearningModelController;
use App\Http\Controllers\NLPTaskController;
use App\Http\Controllers\ResourceStatsController;
use App\Http\Controllers\DatabaseController;

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

Route::apiResource('author', AuthorController::class);
Route::apiResource('link', LinkController::class);
Route::apiResource('dataset', DatasetController::class);
Route::apiResource('machine-learning-model', MachineLearningModelController::class);
Route::apiResource('nlp-task', NLPTaskController::class);
Route::apiResource('resource-stats', ResourceStatsController::class);
Route::delete('database', [DatabaseController::class, 'destroy'])->name('database.destroy');