<?php

namespace App\Models\Helpers;

use Illuminate\Database\Eloquent\Model;
use App\Models\MLModel;
use App\Models\Dataset;
use App\Models\Helpers\Score;

class Benchmark extends Model
{
    # One Benchmark belongs to one Model.
    public function ml_model()
    {
        return $this->belongsTo(MLModel::class);
    }

    # One Benchmark has one Training Dataset.
    public function training_dataset()
    {
        return $this->hasOne(Dataset::class);
    }

    # One Benchmark has one Test Dataset.
    public function test_dataset()
    {
        return $this->hasOne(Dataset::class);
    }

    # One Benchmark has many Scores.
    public function scores()
    {
        return $this->hasMany(Score::class);
    }
}
