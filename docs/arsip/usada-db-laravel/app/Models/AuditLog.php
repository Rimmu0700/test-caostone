<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\{BelongsTo, HasMany, HasOne};

class AuditLog extends Model
{
    protected $table = 'audit_logs';
    protected $primaryKey = 'audit_id';
    const UPDATED_AT = null;
    protected $fillable = ['admin_id', 'action', 'table_name', 'record_id', 'description'];

public function admin(): BelongsTo
    {
        return $this->belongsTo(User::class, 'admin_id');
    }
}
