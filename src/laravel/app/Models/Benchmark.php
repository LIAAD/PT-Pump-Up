<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;


class Benchmark extends Model
{
    use HasFactory;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'metric',
        'performance',
        'ml_model_id',
        'train_dataset_id',
        'validation_dataset_id',
        'test_dataset_id',
    ];

    /**
     * The attributes that should be cast to native types.
     *
     * @var array
     */
    protected $casts = [
        'id' => 'integer',
        'performance' => 'float',
        'ml_model_id' => 'integer',
        'train_dataset_id' => 'integer',
        'validation_dataset_id' => 'integer',
        'test_dataset_id' => 'integer',
    ];

    public function train_dataset(): BelongsTo
    {
        return $this->belongsTo(Dataset::class, 'train_dataset_id', 'id', 'datasets');
    }

    public function validation_dataset(): BelongsTo
    {
        return $this->belongsTo(Dataset::class, 'validation_dataset_id', 'id', 'datasets');
    }

    public function test_dataset(): BelongsTo
    {
        return $this->belongsTo(Dataset::class, 'test_dataset_id', 'id', 'datasets');
    }

    public function mlModel(): BelongsTo
    {
        return $this->belongsTo(MlModel::class);
    }
}
