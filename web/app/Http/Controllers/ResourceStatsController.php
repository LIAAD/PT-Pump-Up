<?php

namespace App\Http\Controllers;

use App\Models\ResourceStats;
use Illuminate\Http\Request;
use App\Traits\StoreResourceStatsTrait;
use App\Http\Requests\StoreResourceStats;

class ResourceStatsController extends Controller
{
    use StoreResourceStatsTrait;

    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(StoreResourceStats $request)
    {
        return StoreResourceStatsTrait::store($request->validated());
    }

    /**
     * Display the specified resource.
     */
    public function show(ResourceStats $resourceStats)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, ResourceStats $resourceStats)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(ResourceStats $resourceStats)
    {
        //
    }
}
