<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\{BelongsTo, HasMany, HasOne};

class Ethnobotany extends Model
{
    protected $table = 'ethnobotany';
    protected $primaryKey = 'ethnobotany_id';
    const CREATED_AT = null;
    protected $fillable = ['species_id', 'traditional_benefits', 'plant_parts_used', 'usage_method', 'verification_status', 'verified_by', 'verified_at'];
    protected function casts(): array
    {
        return [
            'verified_at' => 'datetime',
        ];
    }

public function species(): BelongsTo
    {
        return $this->belongsTo(Species::class, 'species_id');
    }

    public function verifier(): BelongsTo
    {
        return $this->belongsTo(User::class, 'verified_by');
    }
}
