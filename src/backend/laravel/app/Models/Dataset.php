<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

class Dataset extends Model
{
    use HasFactory;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'english_name',
        'full_portuguese_name',
        'description',
        'year',
        'href_id',
        'resource_stats_id',
        'add_by_id',
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
        'add_by_id' => 'integer',
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

    public function addBy(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }
}
