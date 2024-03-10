<?php

namespace App\Http\Controllers;

use App\Http\Requests\ResultStoreRequest;
use App\Http\Requests\ResultUpdateRequest;
use App\Http\Resources\ResultCollection;
use App\Http\Resources\ResultResource;
use App\Models\Result;
use Illuminate\Http\Request;
use Illuminate\Http\Response;

class ResultController extends Controller
{
    public function index(Request $request): ResultCollection
    {
        $results = Result::all();

        return new ResultCollection($results);
    }

    public function store(ResultStoreRequest $request): ResultResource
    {
        $result = Result::create($request->validated());

        return new ResultResource($result);
    }

    public function show(Request $request, Result $result): ResultResource
    {
        return new ResultResource($result);
    }

    public function update(ResultUpdateRequest $request, Result $result): ResultResource
    {
        $result->update($request->validated());

        return new ResultResource($result);
    }

    public function destroy(Request $request, Result $result): Response
    {
        $result->delete();

        return response()->noContent();
    }
}
