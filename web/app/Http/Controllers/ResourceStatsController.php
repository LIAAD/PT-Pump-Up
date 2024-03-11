<?php

namespace App\Http\Controllers;

use App\Models\ResourceStats;
use Illuminate\Http\Request;
use App\Traits\StoreResourceStatsTrait;
use App\Http\Requests\StoreResourceStatsRequest;

class ResourceStatsController extends Controller
{
    use StoreResourceStatsTrait;

    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return ResourceStats::all();
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(StoreResourceStatsRequest $request)
    {
        return StoreResourceStatsTrait::store($request->validated());
    }

    /**
     * Display the specified resource.
     */
    public function show(ResourceStats $resourceStats)
    {
        return $resourceStats;
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, ResourceStats $resourceStats)
    {
        abort(501, 'Not implemented');
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(ResourceStats $resourceStats)
    {
        $resourceStats->delete();

        return response()->noContent();
    }
}
