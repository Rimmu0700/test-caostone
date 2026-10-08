<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\{BelongsTo, HasMany, HasOne};

class GradcamResult extends Model
{
    protected $table = 'gradcam_results';
    protected $primaryKey = 'gradcam_id';
    public $timestamps = false;
    protected $fillable = ['classification_id', 'heatmap_url'];
    protected function casts(): array
    {
        return [
            'generated_at' => 'datetime',
        ];
    }

public function classification(): BelongsTo
    {
        return $this->belongsTo(ClassificationResult::class, 'classification_id');
    }
}
