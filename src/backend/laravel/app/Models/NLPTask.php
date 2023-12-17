<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use MongoDB\Laravel\Eloquent\Model;
use App\Models\Dataset;
use App\Models\MLModel;

class NLPTask extends Model
{
    use HasFactory;

    # The attributes that are mass assignable.
    protected $fillable = [
        '_id',
        'name',
        'acronym',
        'papers_with_code_ids',
    ];

    # One NLPTask belongs to many Datasets.
    public function datasets()
    {
        return $this->belongsToMany(Dataset::class);
    }

    public function ml_models()
    {
        return $this->belongsToMany(MLModel::class);
    }
}
