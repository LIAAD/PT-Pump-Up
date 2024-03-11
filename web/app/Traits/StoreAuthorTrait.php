<?php

namespace App\Traits;

use App\Http\Requests\StoreAuthorRequest;
use App\Models\Author;
use App\Models\Link;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Log;


trait StoreAuthorTrait{
    use StoreLinkTrait;

    public static function store($validated){
    
        try {

            DB::beginTransaction();

            $author = Author::with('link')->where('email', $validated['email'])->first();

            if($author){
                Log::warning('Author already exists');
                return response()->json($author, 409);
            }
                
            if($validated['link']){
                $link = StoreLinkTrait::store($validated);
                $validated['link_id'] = $link->id;
            }

            $author = Author::create($validated);

            DB::commit();

            return response()->json($author, 201);

        } catch (\Throwable $th) {
            DB::rollBack();
            throw $th;
        } catch (\Exception $e) {
            DB::rollBack();
            throw $e;
        }

        return abort(500, 'An error occurred while processing your request');
    }
}