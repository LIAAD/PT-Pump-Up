<?php

namespace App\Models\Helpers;

use MongoDB\Laravel\Eloquent\Model;
use App\Models\Language;

class LanguageStats extends Model
{
    # The attributes that are mass assignable.
    protected $fillable = [
        'number_documents',
        'number_tokens',
        'number_chars',
    ];

    # One LanguageStats belongs to one Language.
    public function language()
    {
        return $this->belongsTo(Language::class);
    }
}
