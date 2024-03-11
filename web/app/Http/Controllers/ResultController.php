<?php

namespace App\Http\Controllers;

use App\Models\Result;
use Illuminate\Http\Request;
use App\Http\Requests\StoreResultRequest;

class ResultController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return Result::all();
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(StoreResultRequest $request)
    {
        return Result::create($request->validated());
    }

    /**
     * Display the specified resource.
     */
    public function show(Result $result)
    {
        return $result;
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Result $result)
    {
        abort(501, 'Not implemented');
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Result $result)
    {
        $result->delete();
        
        return response()->noContent();
    }
}
