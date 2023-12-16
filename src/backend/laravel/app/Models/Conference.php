<?php

namespace App\Models;

use MongoDB\Laravel\Eloquent\Model;

class Conference extends Model
{
    # The attributes that are mass assignable.
    protected $fillable = [
        'name',
        'year',
        'location',
        'url'
    ];
}
