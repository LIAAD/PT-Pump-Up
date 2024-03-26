<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;

class Result extends Model
{
    use HasFactory;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'metric',
        'value',
        'machine_learning_model_id',
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
        'value' => 'float',
        'machine_learning_model_id' => 'integer',
        'train_dataset_id' => 'integer',
        'validation_dataset_id' => 'integer',
        'test_dataset_id' => 'integer',
    ];

    public function machineLearningModel(): BelongsTo
    {
        return $this->belongsTo(MachineLearningModel::class);
    }

    public function trainDataset(): BelongsTo
    {
        return $this->belongsTo(Dataset::class);
    }

    public function validationDataset(): BelongsTo
    {
        return $this->belongsTo(Dataset::class);
    }

    public function testDataset(): BelongsTo
    {
        return $this->belongsTo(Dataset::class);
    }
}
