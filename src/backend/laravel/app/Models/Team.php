<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsTo;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

/**
 * @property int $id
 * @property string $img
 * @property string $name
 * @property string $title
 * @property string $affiliation
 * @property int $href_id
 * @property int $user_id
 * @property \Carbon\Carbon $created_at
 * @property \Carbon\Carbon $updated_at
 */
class Team extends Model
{
    use HasFactory;

    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'img',
        'name',
        'title',
        'affiliation',
        'href_id',
        'user_id',
    ];

    /**
     * The attributes that should be cast to native types.
     *
     * @var array
     */
    protected $casts = [
        'id' => 'integer',
        'href_id' => 'integer',
        'user_id' => 'integer',
    ];

    public function publications(): BelongsToMany
    {
        return $this->belongsToMany(Publication::class);
    }

    public function href(): BelongsTo
    {
        return $this->belongsTo(Href::class);
    }

    public function user(): BelongsTo
    {
        return $this->belongsTo(User::class);
    }
}
