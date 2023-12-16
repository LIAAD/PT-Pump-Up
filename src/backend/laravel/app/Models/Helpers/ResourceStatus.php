<?php

namespace App\Models\Helpers;

use MongoDB\Laravel\Eloquent\Model;


class ResourceStatus extends Model
{
    # The attributes that are mass assignable.
    protected $fillable = [
        'broken_link',
        'author_response',
        'standard_format',
        'backup',
        'preservation_rating',
        'off_the_shelf',
    ];
}
