<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

/**
 * @property int $id
 * @property string $name
 * @property string $affiliation
 * @property int $href_id
 * @property \Carbon\Carbon $created_at
 * @property \Carbon\Carbon $updated_at
 */
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
        'affiliation',
        'href_id',
    ];

    /**
     * The attributes that should be cast to native types.
     *
     * @var array
     */
    protected $casts = [
        'id' => 'integer',
        'href_id' => 'integer',
    ];

    public function datasets(): BelongsToMany
    {
        return $this->belongsToMany(Dataset::class);
    }

    public function mlModels(): BelongsToMany
    {
        return $this->belongsToMany(MlModel::class);
    }

    public function href(): BelongsTo
    {
        return $this->belongsTo(Href::class);
    }
}
