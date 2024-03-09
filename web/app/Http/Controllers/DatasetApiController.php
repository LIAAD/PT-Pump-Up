<?php

namespace App\Http\Controllers;

use App\DatasetApi;
use App\Http\Requests\DatasetApiStoreRequest;
use App\Http\Requests\DatasetApiUpdateRequest;
use App\Http\Resources\DatasetApiCollection;
use App\Http\Resources\DatasetApiResource;
use Illuminate\Http\Request;
use Illuminate\Http\Response;

class DatasetApiController extends Controller
{
    public function index(Request $request): DatasetApiCollection
    {
        $datasetApis = DatasetApi::all();

        return new DatasetApiCollection($datasetApis);
    }

    public function store(DatasetApiStoreRequest $request): DatasetApiResource
    {
        $datasetApi = DatasetApi::create($request->validated());

        return new DatasetApiResource($datasetApi);
    }

    public function show(Request $request, DatasetApi $datasetApi): DatasetApiResource
    {
        return new DatasetApiResource($datasetApi);
    }

    public function update(DatasetApiUpdateRequest $request, DatasetApi $datasetApi): DatasetApiResource
    {
        $datasetApi->update($request->validated());

        return new DatasetApiResource($datasetApi);
    }

    public function destroy(Request $request, DatasetApi $datasetApi): Response
    {
        $datasetApi->delete();

        return response()->noContent();
    }
}
