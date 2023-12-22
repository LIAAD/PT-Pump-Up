<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;
use Illuminate\Database\Eloquent\Relations\HasMany;

/**
 * @property int $id
 * @property string $english_name
 * @property string $full_portuguese_name
 * @property string $description
 * @property int $year
 * @property string $architecture
 * @property int $href_id
 * @property int $resource_stats_id
 * @property int $add_by_id
 * @property \Carbon\Carbon $created_at
 * @property \Carbon\Carbon $updated_at
 */
class MlModel extends Model
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
        'architecture',
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
        return $this->belongsToMany(Author::class)->with('href');
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

    public function benchmarks(): HasMany
    {
        return $this->hasMany(Benchmark::class);
    }
}
