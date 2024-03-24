<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

class NlpTask extends Model
{
    use HasFactory;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'short_name',
        'full_name',
        'description',
        'standard_format',
        'papers_with_code_id',
        'link_id',
    ];

    /**
     * The attributes that should be cast to native types.
     *
     * @var array
     */
    protected $casts = [
        'id' => 'integer',
        'link_id' => 'integer',
    ];

    public function datasets(): BelongsToMany
    {
        return $this->belongsToMany(Dataset::class);
    }

    public function machineLearningModels(): BelongsToMany
    {
        return $this->belongsToMany(MachineLearningModel::class);
    }

    public function link(): BelongsTo
    {
        return $this->belongsTo(Link::class);
    }
}
