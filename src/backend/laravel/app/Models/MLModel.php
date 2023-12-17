<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use MongoDB\Laravel\Eloquent\Model;
use App\Models\Helpers\Hrefs;
use App\Models\Helpers\ResourceStats;
use App\Models\Helpers\Benchmark;

class MLModel extends Model
{
    use HasFactory;

    # The attributes that are mass assignable.

    protected $fillable = [
        '_id',
        'name',
        'description',
        'year',
    ];

    # One MLModel has many Authors.
    public function authors()
    {
        return $this->belongsToMany(Author::class);
    }

    # One MLModel has one ResourceStats.
    public function model_stats()
    {
        return $this->hasOne(ResourceStats::class);
    }

    # One MLModel has one HRefs.
    public function hrefs()
    {
        return $this->hasOne(HRefs::class);
    }

    # One MLModel has many Benchmarks.
    public function benchmarks()
    {
        return $this->hasMany(Benchmark::class);
    }

    # One MLModel has many Publications.
    public function publications()
    {
        return $this->hasMany(Publication::class);
    }

    public function nlp_tasks()
    {
        return $this->belongsToMany(NLPTask::class);
    }
}
