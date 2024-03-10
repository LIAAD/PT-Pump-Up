<?php

namespace App\Http\Controllers;

use App\Http\Requests\ResourceStatsStoreRequest;
use App\Http\Requests\ResourceStatsUpdateRequest;
use App\Http\Resources\ResourceStatCollection;
use App\Http\Resources\ResourceStatResource;
use App\Models\ResourceStats;
use Illuminate\Http\Request;
use Illuminate\Http\Response;

class ResourceStatsController extends Controller
{
    public function index(Request $request): ResourceStatCollection
    {
        $resourceStats = ResourceStat::all();

        return new ResourceStatCollection($resourceStats);
    }

    public function store(ResourceStatsStoreRequest $request): ResourceStatResource
    {
        $resourceStat = ResourceStat::create($request->validated());

        return new ResourceStatResource($resourceStat);
    }

    public function show(Request $request, ResourceStat $resourceStat): ResourceStatResource
    {
        return new ResourceStatResource($resourceStat);
    }

    public function update(ResourceStatsUpdateRequest $request, ResourceStat $resourceStat): ResourceStatResource
    {
        $resourceStat->update($request->validated());

        return new ResourceStatResource($resourceStat);
    }

    public function destroy(Request $request, ResourceStat $resourceStat): Response
    {
        $resourceStat->delete();

        return response()->noContent();
    }
}
