<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use MongoDB\Laravel\Eloquent\Model;

class Publication extends Model
{
    use HasFactory;

    # The attributes that are mass assignable.
    protected $fillable = [
        '_id',
        'english_name',
        'full_portuguese_name',
        'description',
        'introduction_date',
    ];
    
    
}


/*


_id
656cd66b39de0e94c0e85934
english_name
"Primeiro HAREM"
full_portuguese_name
""
description
""
introduction_date
"2006/01/01"

language_stats
Array (2)
conference
null

hrefs
Object

status
Object
overall_dataset_stats
null

authors
Array (1)
license
null

nlp_tasks
Array (1)
*/