<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\{BelongsTo, HasMany, HasOne};

class Species extends Model
{
    protected $table = 'species';
    protected $primaryKey = 'species_id';
    protected $fillable = ['scientific_name', 'local_name', 'is_active'];
    protected function casts(): array
    {
        return [
            'is_active' => 'boolean',
        ];
    }

public function ethnobotany(): HasOne
    {
        return $this->hasOne(Ethnobotany::class, 'species_id');
    }

    public function classificationResults(): HasMany
    {
        return $this->hasMany(ClassificationResult::class, 'species_id');
    }

    public function correctionsReceived(): HasMany
    {
        return $this->hasMany(FeedbackCorrection::class, 'corrected_species_id');
    }
}
