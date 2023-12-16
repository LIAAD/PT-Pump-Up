<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use App\Models\Helpers\Hrefs;

class Author extends Model
{
    use HasFactory;

    # The attributes that are mass assignable.~
    protected $fillable = [
        '_id',
        'name',
        'affiliation',
    ];

    # One author has one Hrefs.
    public function hrefs()
    {
        return $this->hasOne(Hrefs::class);
    }

    # One author has many publications.
    public function publications()
    {
        return $this->hasMany(Publication::class);
    }
}