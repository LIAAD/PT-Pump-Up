<?php

namespace App\Http\Controllers;

use App\Models\MachineLearningModel;
use App\Models\Author;
use App\Traits\StoreAuthorTrait;
use App\Traits\StoreLinkTrait;
use App\Traits\StoreResourceStatsTrait;
use App\Http\Requests\StoreMachineLearningModelRequest;
use Illuminate\Support\Facades\DB;

use Illuminate\Http\Request;

class MachineLearningModelController extends Controller
{
    use StoreAuthorTrait;
    use StoreLinkTrait;
    use StoreResourceStatsTrait;    
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        return MachineLearningModel::with(['authors', 'link', 'resourceStats'])->get();
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(StoreMachineLearningModelRequest $request)
    {
        $validated = $request->validated();

        DB::beginTransaction();

        try {
            if($validated['authors']){
                foreach($validated['authors'] as $key => $author){
                    $response = StoreAuthorTrait::store($author);
                    #Load Authors object from json response
                    $authors[] = $response->original;            
                }                        
            }else{
                foreach($validated['author_ids'] as $key => $author_id){
                    $authors[] = Author::find($author_id);
                }
            }

            $link = StoreLinkTrait::store($validated);
            $validated['link_id'] = $link->id;

            $resource_stats = StoreResourceStatsTrait::store($validated);
            $validated['resource_stats_id'] = $resource_stats->id;

            $machineLearningModel = MachineLearningModel::create($validated);

            $machineLearningModel->authors()->saveMany($authors);

            DB::commit();

            return response()->json($machineLearningModel, 201);

        } catch (\Throwable $th) {
            DB::rollBack();
            throw $th;
        } catch (\Exception $e) {
            DB::rollBack();
            throw $e;
        }

        abort(500, 'An error occurred while creating the machine learning model');
    }

    /**
     * Display the specified resource.
     */
    public function show(MachineLearningModel $machineLearningModel)
    {
        abort(501, 'Not implemented');
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, MachineLearningModel $machineLearningModel)
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
