<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\{BelongsTo, HasMany, HasOne};

class ClassificationResult extends Model
{
    protected $table = 'classification_results';
    protected $primaryKey = 'classification_id';
    public $timestamps = false;
    protected $fillable = ['session_id', 'species_id', 'confidence_score', 'result_status', 'model_name', 'model_version'];
    protected function casts(): array
    {
        return [
            'confidence_score' => 'decimal:4',
            'classified_at' => 'datetime',
        ];
    }

public function session(): BelongsTo
    {
        return $this->belongsTo(IdentificationSession::class, 'session_id');
    }

    public function species(): BelongsTo
    {
        return $this->belongsTo(Species::class, 'species_id');
    }

    public function gradcam(): HasOne
    {
        return $this->hasOne(GradcamResult::class, 'classification_id');
    }

    public function feedbackCorrections(): HasMany
    {
        return $this->hasMany(FeedbackCorrection::class, 'classification_id');
    }
}
