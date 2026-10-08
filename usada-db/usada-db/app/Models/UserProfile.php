<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\{BelongsTo, HasMany, HasOne};

class UserProfile extends Model
{
    protected $table = 'user_profiles';
    protected $primaryKey = 'user_id';
    public $incrementing = false;
    const CREATED_AT = null;
    protected $fillable = ['user_id', 'full_name', 'photo_url'];

public function user(): BelongsTo
    {
        return $this->belongsTo(User::class, 'user_id');
    }
}
