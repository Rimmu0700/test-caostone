# Arsitektur dan Aturan Kode

Aturan ini berlaku untuk seluruh anggota tim dan menjadi acuan reviewer saat Pull Request.

## Frontend Flutter (frontend/mobile dan frontend/admin)

Prinsip Zero-Trust dan Dumb UI:

- Layar hanya merender state dari ViewModel dan meneruskan aksi pengguna.
- Tidak ada logika bisnis, validasi aturan bisnis, kalkulasi, manipulasi string, atau filter data kompleks di widget.
- Semua data dari luar diperlakukan sebagai data mentah. Validasi dan otorisasi diputuskan backend.

Lapisan: presentation (screens, components, viewmodels), domain (use case, entity), data (repository implementation, DTO, klien HTTP).

Styling hanya memakai token pada `shared/theme`. Dilarang menulis warna, ukuran, atau radius bebas di widget.

## Backend FastAPI

Pola Controller, Service, Repository dengan coupling rendah, dikelompokkan per modul bisnis di `backend/api/src/modules` (auth, curator, identification, species, health). Tiap modul berisi:

- `controller.py` menerima request HTTP, memvalidasi skema dasar lewat schema Pydantic, lalu meneruskan ke service. Tidak ada query atau algoritma di sini.
- `service.py` berisi logika bisnis, aturan otorisasi, dan orkestrasi adapter. Service bergantung pada abstraksi, bukan pada SQLAlchemy.
- `repository.py` berisi akses basis data saja.
- `schemas.py` kontrak request dan response, selaras dengan `openapi.yaml`.

Bagian bersama:

- `src/core` konfigurasi, keamanan, JWT, middleware RBAC, dan error handler.
- `src/database` basis deklaratif, sesi, `models` sesuai ERD 3NF, dan `seeders`.
- `src/adapters` pembungkus layanan luar: Inference Service, Object Storage, SMTP, FCM.
- `alembic` migration resmi. Dilarang mengubah skema secara manual di klien basis data.

Inference Service berdiri sendiri di `backend/inference` dan hanya dipanggil API lewat adapter.

## Kontrak dan Perubahan Skema

Perubahan endpoint dimulai dari `openapi.yaml`. Perubahan tabel dimulai dari model, lalu dibuat migration baru. Tes `test_migration_matches_models` menggagalkan CI bila model dan migration tidak sama.
