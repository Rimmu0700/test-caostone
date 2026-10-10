<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\{BelongsTo, HasMany, HasOne};

class IdentificationSession extends Model
{
    protected $table = 'identification_sessions';
    protected $primaryKey = 'session_id';
    const UPDATED_AT = null;
    protected $fillable = ['user_id', 'captured_at', 'session_status', 'detection_status', 'photo_consent'];
    protected function casts(): array
    {
        return [
            'captured_at' => 'datetime',
            'photo_consent' => 'boolean',
        ];
    }

public function user(): BelongsTo
    {
        return $this->belongsTo(User::class, 'user_id');
    }

    public function images(): HasMany
    {
        return $this->hasMany(Image::class, 'session_id');
    }

    public function leafDetections(): HasMany
    {
        return $this->hasMany(LeafDetection::class, 'session_id');
    }

    public function greenPixelValidation(): HasOne
    {
        return $this->hasOne(GreenPixelValidation::class, 'session_id');
    }

    public function classificationResult(): HasOne
    {
        return $this->hasOne(ClassificationResult::class, 'session_id');
    }

    public function notifications(): HasMany
    {
        return $this->hasMany(Notification::class, 'session_id');
    }
}
