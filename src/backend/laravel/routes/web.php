<?php

use App\Http\Controllers\DatasetController;
use App\Http\Controllers\HomepageController;
use App\Http\Controllers\ProfileController;
use Illuminate\Support\Facades\Route;
use Inertia\Inertia;


/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/


Route::get('/dashboard', function () {
    return Inertia::render('Dashboard', [
        'api_token' => auth()->user()->tokens->first()->plainTextToken
    ]);
})->middleware(['auth', 'verified'])->name('dashboard');

Route::middleware('auth')->group(function () {
    Route::get('/profile', [ProfileController::class, 'edit'])->name('profile.edit');
    Route::patch('/profile', [ProfileController::class, 'update'])->name('profile.update');
    Route::delete('/profile', [ProfileController::class, 'destroy'])->name('profile.destroy');
});


// Defined by us
Route::get('/', [HomepageController::class, 'index'])->name('home');
Route::get('/datasets', [DatasetController::class, 'index_web'])->name('index_web');

/*
Route::get('/tokens/create', function (Request $request) {
    $token = $request->user()->createToken("general");

    return ['token' => $token->plainTextToken];
});
*/

require __DIR__ . '/auth.php';
