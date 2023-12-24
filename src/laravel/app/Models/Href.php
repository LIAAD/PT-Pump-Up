<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

/**
 * @property int $id
 * @property string $email
 * @property string $website
 * @property string $orcid
 * @property string $github
 * @property string $twitter
 * @property string $google_scholar
 * @property string $linkedin
 * @property string $link_source
 * @property string $link_hf
 * @property string $link_papers_with_code
 * @property string $doi
 * @property \Carbon\Carbon $created_at
 * @property \Carbon\Carbon $updated_at
 */
class Href extends Model
{
    use HasFactory;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'email',
        'website',
        'orcid',
        'github',
        'twitter',
        'google_scholar',
        'linkedin',
        'link_source',
        'link_hf',
        'link_papers_with_code',
        'doi',
    ];

    /**
     * The attributes that should be cast to native types.
     *
     * @var array
     */
    protected $casts = [
        'id' => 'integer',
    ];
}
