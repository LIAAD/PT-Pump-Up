<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class ResourceStats extends Model
{
    use HasFactory;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'broken_link',
        'author_response',
        'standard_format',
        'backup',
        'size_gb',
        'preservation_rating',
        'state',
    ];

    /**
     * The attributes that should be cast to native types.
     *
     * @var array
     */
    protected $casts = [
        'id' => 'integer',
        'broken_link' => 'boolean',
        'author_response' => 'boolean',
        'standard_format' => 'boolean',
        'backup' => 'boolean',
        'size_gb' => 'float',
    ];
}
