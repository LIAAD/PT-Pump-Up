<?php

namespace App\Traits;

use App\Models\ResourceStats;

trait StoreResourceStatsTrait
{
   public static function store($validated)
   {
       return ResourceStats::create($validated);
   }
}