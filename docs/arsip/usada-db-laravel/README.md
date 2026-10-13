# DB Usada Bali - Migration & Seeder (Laravel 10/11/12, PostgreSQL)

Disusun dari ERD 3NF "Sistem Identifikasi dan Edukasi Tanaman Obat Usada Bali" (15 tabel).

## Pemasangan
1. Salin folder `app/Models` dan `database/` ke root proyek Laravel (timpa `DatabaseSeeder.php`).
2. **Hapus** migration bawaan `0001_01_01_000000_create_users_table.php` dan model `app/Models/User.php` bawaan
   (digantikan oleh versi ini; PK `user_id`, kolom `password_hash`).
3. Di `.env` set:
   ```
   DB_CONNECTION=pgsql
   DB_HOST=127.0.0.1
   DB_PORT=5432
   DB_DATABASE=usada_bali
   DB_USERNAME=postgres
   DB_PASSWORD=...
   SESSION_DRIVER=file
   ADMIN_EMAIL=emailanda@contoh.com
   ADMIN_PASSWORD=passwordkuat
   ```
   (`SESSION_DRIVER=file` agar tidak butuh tabel `sessions` bawaan.)
4. Jalankan: `php artisan migrate:fresh --seed`

## Urutan migration (sesuai dependensi FK)
roles, users, user_profiles, user_settings, audit_logs, species, ethnobotany, identification_sessions,
images, leaf_detections, green_pixel_validations, classification_results, gradcam_results,
feedback_corrections, notifications.

## Catatan desain
- Relasi 1:0..1 / 1:1 pada ERD diberi `unique`: user_settings.user_id, ethnobotany.species_id,
  green_pixel_validations.session_id, classification_results.session_id, gradcam_results.classification_id.
- Hapus data: anak data sesi ikut terhapus (cascade); roles, species, dan user yang dirujuk audit/koreksi
  dilindungi (restrict); ethnobotany.verified_by menjadi NULL jika kurator dihapus.
- Kolom status (VARCHAR) tidak dibatasi enum agar fleksibel; nilai disarankan dijaga di level aplikasi.

## Catatan PostgreSQL
- Buat database dulu: `CREATE DATABASE usada_bali;`. Pastikan ekstensi PHP `pdo_pgsql` aktif.
- PostgreSQL tidak mendukung `ON UPDATE CURRENT_TIMESTAMP`; kolom `updated_at` diisi otomatis oleh Eloquent
  (jangan update lewat query builder/SQL mentah tanpa mengisi `updated_at`).
- `RoleSeeder` menyinkronkan sequence `roles.role_id` setelah insert ID eksplisit.
- Unique index (email, scientific_name) bersifat case-sensitive di PostgreSQL.
