<?php

namespace App\Traits;
use App\Models\Link;

trait StoreLinkTrait
{
    public static function store($validated)
    {
        return Link::create($validated['link']);
    }
}