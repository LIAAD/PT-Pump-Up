<?php

namespace App\Http\Controllers;

use App\Http\Requests\StoreMLModelRequest;
use App\Http\Requests\UpdateMLModelRequest;
use App\Models\MLModel;

class MLModelController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        //
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(StoreMLModelRequest $request)
    {
        //
    }

    /**
     * Display the specified resource.
     */
    public function show(MLModel $mLModel)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(MLModel $mLModel)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(UpdateMLModelRequest $request, MLModel $mLModel)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(MLModel $mLModel)
    {
        //
    }
}
