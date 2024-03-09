<?php

namespace App\Http\Controllers;

use App\Http\Requests\LinkStoreRequest;
use App\Http\Requests\LinkUpdateRequest;
use App\Http\Resources\LinkCollection;
use App\Http\Resources\LinkResource;
use App\Models\Link;
use Illuminate\Http\Request;
use Illuminate\Http\Response;

class LinkController extends Controller
{
    public function index(Request $request): LinkCollection
    {
        $links = Link::all();

        return new LinkCollection($links);
    }

    public function store(LinkStoreRequest $request): LinkResource
    {
        $link = Link::create($request->validated());

        return new LinkResource($link);
    }

    public function show(Request $request, Link $link): LinkResource
    {
        return new LinkResource($link);
    }

    public function update(LinkUpdateRequest $request, Link $link): LinkResource
    {
        $link->update($request->validated());

        return new LinkResource($link);
    }

    public function destroy(Request $request, Link $link): Response
    {
        $link->delete();

        return response()->noContent();
    }
}
