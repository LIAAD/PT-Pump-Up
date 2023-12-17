<?php

namespace App\Models\Helpers;

use MongoDB\Laravel\Eloquent\Model;

class Score extends Model
{
    # The attributes that are mass assignable.
    protected $fillable = [
        'metric',
        'value'
    ];
}
