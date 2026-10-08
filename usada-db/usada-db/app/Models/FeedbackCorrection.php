<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\{BelongsTo, HasMany, HasOne};

class FeedbackCorrection extends Model
{
    protected $table = 'feedback_corrections';
    protected $primaryKey = 'feedback_id';
    const UPDATED_AT = null;
    protected $fillable = ['classification_id', 'curator_id', 'corrected_species_id', 'correction_note'];

public function classification(): BelongsTo
    {
        return $this->belongsTo(ClassificationResult::class, 'classification_id');
    }

    public function curator(): BelongsTo
    {
        return $this->belongsTo(User::class, 'curator_id');
    }

    public function correctedSpecies(): BelongsTo
    {
        return $this->belongsTo(Species::class, 'corrected_species_id');
    }
}
