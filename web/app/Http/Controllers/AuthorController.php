<?php

namespace App\Http\Controllers;

use App\Http\Requests\AuthorStoreRequest;
use App\Http\Requests\AuthorUpdateRequest;
use App\Http\Resources\AuthorCollection;
use App\Http\Resources\AuthorResource;
use App\Models\Author;
use Illuminate\Http\Request;
use Illuminate\Http\Response;

class AuthorController extends Controller
{
    public function index(Request $request): AuthorCollection
    {
        $authors = Author::all();

        return new AuthorCollection($authors);
    }

    public function store(AuthorStoreRequest $request): AuthorResource
    {
        $author = Author::create($request->validated());

        return new AuthorResource($author);
    }

    public function show(Request $request, Author $author): AuthorResource
    {
        return new AuthorResource($author);
    }

    public function update(AuthorUpdateRequest $request, Author $author): AuthorResource
    {
        $author->update($request->validated());

        return new AuthorResource($author);
    }

    public function destroy(Request $request, Author $author): Response
    {
        $author->delete();

        return response()->noContent();
    }
}
