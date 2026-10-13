<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\{BelongsTo, HasMany, HasOne};

class Image extends Model
{
    protected $table = 'images';
    protected $primaryKey = 'image_id';
    public $timestamps = false;
    protected $fillable = ['session_id', 'image_type', 'storage_url', 'file_format', 'file_size'];
    protected function casts(): array
    {
        return [
            'uploaded_at' => 'datetime',
        ];
    }

public function session(): BelongsTo
    {
        return $this->belongsTo(IdentificationSession::class, 'session_id');
    }
}
