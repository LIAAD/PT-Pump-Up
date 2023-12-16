<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use MongoDB\Laravel\Eloquent\Model;

class Language extends Model
{
    use HasFactory;

    # The attributes that are mass assignable.
    protected $fillable = [
        '_id',
        'name',
        'iso_code',
        'papers_with_code_id',
    ];
}
