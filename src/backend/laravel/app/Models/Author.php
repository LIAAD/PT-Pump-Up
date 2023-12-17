<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use MongoDB\Laravel\Eloquent\Model;
use App\Models\Helpers\Hrefs;
use App\Models\Publication;
use App\Models\Dataset;
use App\Models\MLModel;

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

    public function datasets()
    {
        return $this->belongsToMany(Dataset::class);
    }

    public function ml_models()
    {
        return $this->belongsToMany(MLModel::class);
    }
}
