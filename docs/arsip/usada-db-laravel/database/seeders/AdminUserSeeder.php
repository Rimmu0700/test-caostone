<?php

namespace Database\Seeders;

use App\Models\Role;
use App\Models\User;
use Illuminate\Database\Seeder;

class AdminUserSeeder extends Seeder
{
    public function run(): void
    {
        $email    = env('ADMIN_EMAIL', 'admin@usada.test');
        $password = env('ADMIN_PASSWORD', 'ChangeMe!123'); // WAJIB diganti di .env

        $admin = User::firstOrCreate(
            ['email' => $email],
            [
                'role_id'        => Role::where('role_name', 'admin')->value('role_id'),
                'password_hash'  => $password, // di-hash otomatis lewat cast 'hashed'
                'email_verified' => true,
            ]
        );

        $admin->profile()->firstOrCreate([], ['full_name' => 'Administrator']);
        $admin->settings()->firstOrCreate([], ['notification_enabled' => true]);
    }
}
