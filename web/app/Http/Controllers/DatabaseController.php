<?php

namespace App\Http\Controllers;

use App\Http\Requests\DestroyDatabaseRequest;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Artisan;


class DatabaseController extends Controller
{
    public function destroy(DestroyDatabaseRequest $request)
    {
        $request->validated();
        Artisan::call('migrate:fresh');
        return response()->json(['message' => 'Database erased and reseeded!']);
    }
}
