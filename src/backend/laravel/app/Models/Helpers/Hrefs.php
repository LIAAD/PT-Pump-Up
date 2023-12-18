<?php

namespace App\Models\Helpers;

use Illuminate\Database\Eloquent\Model;

class Hrefs extends Model
{
    # The attributes that are mass assignable.
    protected $fillable = [
        'email',
        'website',
        'orcid',
        'github',
        'twitter',
        'googleScholar',
        'linkedin',
        'link_source',
        'link_hf',
        'doi'
    ];
}
