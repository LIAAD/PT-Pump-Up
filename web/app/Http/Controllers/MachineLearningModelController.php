<?php

namespace App\Http\Controllers;

use App\Models\MachineLearningModel;
use App\Models\Link;
use App\Models\ResourceStats;
use Illuminate\Http\Request;
use App\Http\Requests\MachineLearningModelStoreRequest;
use App\Http\Requests\MachineLearningModelUpdateRequest;
use App\Http\Resources\MachineLearningModelCollection;
use App\Http\Resources\MachineLearningModelResource;

class MachineLearningModelController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        $machineLearningModels = MachineLearningModel::all();
        
        return new MachineLearningModelCollection($machineLearningModels);
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(MachineLearningModelStoreRequest $request)
    {
        $request = $request->validated();

        $link = Link::create($request['link']);
        
        $resourceStats = ResourceStats::create($request['resource_stats']);
        
        // Add Foreign Keys
        $request['link_id'] = $link->id;
        $request['resource_stats_id'] = $resourceStats->id;
        
        $machineLearningModel = MachineLearningModel::create($request);
        
        foreach ($request['results'] as $result)
            $machineLearningModel->results()->create($result);
        
        return new MachineLearningModelResource($machineLearningModel);
    }

    /**
     * Display the specified resource.
     */
    public function show(MachineLearningModel $machineLearningModel)
    {
        return new MachineLearningModelResource($machineLearningModel);
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(MachineLearningModelUpdateRequest $request, MachineLearningModel $machineLearningModel)
    {
        abort(501, 'Not implemented');
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(MachineLearningModel $machineLearningModel)
    {
        $machineLearningModel->delete();

        return response()->noContent();
    }
}
