<?php

namespace App\Models;

use Illuminate\Foundation\Auth\User as Authenticatable;
use Illuminate\Database\Eloquent\Relations\{BelongsTo, HasMany, HasOne};

class User extends Authenticatable
{
    protected $hidden = ['password_hash'];

    protected $table = 'users';
    protected $primaryKey = 'user_id';
    protected $fillable = ['role_id', 'email', 'password_hash', 'email_verified'];
    protected function casts(): array
    {
        return [
            'email_verified' => 'boolean',
            'password_hash' => 'hashed',
        ];
    }

    public function getAuthPasswordName(): string
    {
        return 'password_hash';
    }

    public function isAdmin(): bool
    {
        return $this->role?->role_name === 'admin';
    }

    public function role(): BelongsTo
    {
        return $this->belongsTo(Role::class, 'role_id');
    }

    public function profile(): HasOne
    {
        return $this->hasOne(UserProfile::class, 'user_id');
    }

    public function settings(): HasOne
    {
        return $this->hasOne(UserSetting::class, 'user_id');
    }

    public function identificationSessions(): HasMany
    {
        return $this->hasMany(IdentificationSession::class, 'user_id');
    }

    public function auditLogs(): HasMany
    {
        return $this->hasMany(AuditLog::class, 'admin_id');
    }

    public function notifications(): HasMany
    {
        return $this->hasMany(Notification::class, 'user_id');
    }

    public function verifiedEthnobotany(): HasMany
    {
        return $this->hasMany(Ethnobotany::class, 'verified_by');
    }

    public function feedbackCorrections(): HasMany
    {
        return $this->hasMany(FeedbackCorrection::class, 'curator_id');
    }
}
