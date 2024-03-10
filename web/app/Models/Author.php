<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

class Author extends Model
{
    use HasFactory;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'name',
        'institution',
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

    public function link(): BelongsTo
    {
        return $this->belongsTo(Link::class);
    }

    public function datasets(): BelongsToMany
    {
        return $this->belongsToMany(Dataset::class);
    }

    public function machineLearningModels(): BelongsToMany
    {
        return $this->belongsToMany(MachineLearningModel::class);
    }
}
