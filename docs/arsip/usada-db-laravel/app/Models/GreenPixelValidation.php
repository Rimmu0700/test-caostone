<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\{BelongsTo, HasMany, HasOne};

class GreenPixelValidation extends Model
{
    protected $table = 'green_pixel_validations';
    protected $primaryKey = 'validation_id';
    public $timestamps = false;
    protected $fillable = ['session_id', 'green_pixel_ratio', 'threshold', 'validation_status'];
    protected function casts(): array
    {
        return [
            'green_pixel_ratio' => 'decimal:4',
            'threshold' => 'decimal:4',
            'validated_at' => 'datetime',
        ];
    }

public function session(): BelongsTo
    {
        return $this->belongsTo(IdentificationSession::class, 'session_id');
    }
}
