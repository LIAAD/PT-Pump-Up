<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Http\Requests\StoreUserRequest;
use Inertia\Inertia;
use App\Models\User;
use Faker\Factory;

class UserController extends Controller
{
    public function create(){
        return Inertia::render('Users/Create');
    }
    
    public function store(StoreUserRequest $request){
        $validated = $request->validated();
        $validated['password'] = Factory::create()->password();
        
        User::create($validated);
        
        return redirect()->route('homepage');
    }
}
