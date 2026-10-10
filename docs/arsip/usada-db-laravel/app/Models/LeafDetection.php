<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\{BelongsTo, HasMany, HasOne};

class LeafDetection extends Model
{
    protected $table = 'leaf_detections';
    protected $primaryKey = 'detection_id';
    public $timestamps = false;
    protected $fillable = ['session_id', 'confidence', 'bbox_x', 'bbox_y', 'bbox_width', 'bbox_height', 'detection_status', 'crop_image_url'];
    protected function casts(): array
    {
        return [
            'confidence' => 'decimal:4',
            'bbox_x' => 'decimal:4',
            'bbox_y' => 'decimal:4',
            'bbox_width' => 'decimal:4',
            'bbox_height' => 'decimal:4',
            'detected_at' => 'datetime',
        ];
    }

public function session(): BelongsTo
    {
        return $this->belongsTo(IdentificationSession::class, 'session_id');
    }
}
