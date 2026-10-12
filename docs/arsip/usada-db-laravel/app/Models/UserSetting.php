<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\{BelongsTo, HasMany, HasOne};

class UserSetting extends Model
{
    protected $table = 'user_settings';
    protected $primaryKey = 'setting_id';
    const CREATED_AT = null;
    protected $fillable = ['user_id', 'notification_enabled'];
    protected function casts(): array
    {
        return [
            'notification_enabled' => 'boolean',
        ];
    }

public function user(): BelongsTo
    {
        return $this->belongsTo(User::class, 'user_id');
    }
}
