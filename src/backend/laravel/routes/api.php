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

Route::group(['middleware' => ['auth:sanctum']], function () {
    Route::apiResources([
        'models' => App\Http\Controllers\ModelController::class,
        'datasets' => App\Http\Controllers\DatasetController::class,
    ]);
    Route::get('/tokens/create', function (Request $request) {
        $token = $request->user()->createToken("general");

        return ['token' => $token->plainTextToken];
    });
});
