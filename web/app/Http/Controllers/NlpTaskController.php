<?php

namespace App\Http\Controllers;

use App\Http\Requests\NlpTaskStoreRequest;
use App\Http\Requests\NlpTaskUpdateRequest;
use App\Http\Resources\NlpTaskCollection;
use App\Http\Resources\NlpTaskResource;
use App\Models\NlpTask;
use Illuminate\Http\Request;
use Illuminate\Http\Response;

class NlpTaskController extends Controller
{
    public function index(Request $request): NlpTaskCollection
    {
        $nlpTasks = NlpTask::all();

        return new NlpTaskCollection($nlpTasks);
    }

    public function store(NlpTaskStoreRequest $request): NlpTaskResource
    {
        $nlpTask = NlpTask::create($request->validated());

        return new NlpTaskResource($nlpTask);
    }

    public function show(Request $request, NlpTask $nlpTask): NlpTaskResource
    {
        return new NlpTaskResource($nlpTask);
    }

    public function update(NlpTaskUpdateRequest $request, NlpTask $nlpTask): NlpTaskResource
    {
        $nlpTask->update($request->validated());

        return new NlpTaskResource($nlpTask);
    }

    public function destroy(Request $request, NlpTask $nlpTask): Response
    {
        $nlpTask->delete();

        return response()->noContent();
    }
}
