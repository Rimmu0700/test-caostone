<?php

namespace Database\Seeders;

use App\Models\Role;
use Illuminate\Support\Facades\DB;
use Illuminate\Database\Seeder;

class RoleSeeder extends Seeder
{
    public function run(): void
    {
        $roles = [
            1 => 'admin',    // kelola sistem, audit log
            2 => 'curator',  // verifikasi ethnobotany & koreksi hasil klasifikasi
            3 => 'user',     // pengguna identifikasi
        ];

        foreach ($roles as $id => $name) {
            Role::updateOrCreate(['role_id' => $id], ['role_name' => $name]);
        }

        // PostgreSQL: insert dengan ID eksplisit tidak memajukan sequence,
        // jadi sinkronkan agar insert role berikutnya tidak bentrok.
        if (DB::getDriverName() === 'pgsql') {
            DB::statement("SELECT setval(pg_get_serial_sequence('roles', 'role_id'), (SELECT MAX(role_id) FROM roles))");
        }
    }
}
