<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

class MlModel extends Model
{
    use HasFactory;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'name',
        'description',
        'year',
        'href_id',
        'resource_stats_id',
    ];

    /**
     * The attributes that should be cast to native types.
     *
     * @var array
     */
    protected $casts = [
        'id' => 'integer',
        'href_id' => 'integer',
        'resource_stats_id' => 'integer',
    ];

    public function authors(): BelongsToMany
    {
        return $this->belongsToMany(Author::class);
    }

    public function nlpTasks(): BelongsToMany
    {
        return $this->belongsToMany(NlpTask::class);
    }

    public function href(): BelongsTo
    {
        return $this->belongsTo(Href::class);
    }

    public function resourceStats(): BelongsTo
    {
        return $this->belongsTo(ResourceStats::class);
    }
}
