# Sistem Identifikasi dan Edukasi Tanaman Obat Usada Bali

Capstone Project Kelompok 10, Program Studi Teknologi Informasi, Undiknas 2026.
Jalur GovTech, pilar AI. Mitra: BRIN Kebun Raya Eka Karya Bali.

## Struktur Repositori

| Folder | Isi | Penanggung jawab |
|---|---|---|
| backend/api | REST API FastAPI per modul, migration Alembic, seeder | Backend 1 dan Backend 2 |
| backend/inference | Inference Service: YOLO11, validasi piksel hijau, MobileNetV3-Small, Grad-CAM | Backend 1 dan Backend 2 |
| frontend/mobile | Aplikasi Flutter untuk Android | Frontend 1 |
| frontend/admin | Dasbor admin dan kurator, juga Flutter, dikerjakan belakangan | Frontend 2 |
| infrastructure | Konfigurasi Nginx dan Certbot | DevOps |
| docs | SRS, SAD, ERD, design system, arsip | Seluruh tim |

Kontrak API ada di `openapi.yaml` pada root. Aturan arsitektur kode ada di `docs/ARSITEKTUR.md`.

## Menjalankan Secara Lokal

1. Salin `.env.example` menjadi `.env` lalu isi nilainya, termasuk `CURATOR_EMAIL` dan `CURATOR_PASSWORD` untuk akun kurator awal.
2. Jalankan `docker compose up --build`. Layanan `migrate` menjalankan migration dan seeding lebih dulu, baru layanan `api` start.
3. API tersedia di `http://localhost:8000` dan pemeriksaan kesehatan di `http://localhost:8000/health`.
4. Untuk menjalankan tes atau Alembic langsung dari `backend/api` tanpa Docker, isi `DB_HOST=localhost` pada `.env`. Berkas `.env` di root otomatis dibaca.

## Basis Data

Skema mengikuti ERD 3NF pada `docs/ERD USADA.png` (15 tabel). Migration resmi ada di `backend/api/alembic/versions`, seeder di `backend/api/src/database/seeders`. Seeder aman dijalankan berulang dan tidak menimpa data yang sudah diubah kurator.

## Aturan Git

- Dilarang direct push ke `main` dan `staging`.
- Satu tiket satu branch dengan format `feature/<nomor-issue>-<nama-fitur>`.
- Merge ke `staging` wajib lewat Pull Request, minimal 1 approval, dan CI hijau.
- Dilarang commit `.env`, kata sandi, kunci JWT, atau token API.
- Batas WIP adalah 1 sampai 2 tiket In Progress per orang.

## Alur Board

Product Backlog, Sprint Backlog, In Progress, In Review, Done.

## Tim

| Peran | Nama |
|---|---|
| UI/UX Designer | Nyoman Gede Putra Narotama |
| Frontend 1 | Dewa Ayu Astrid Pradnya Paramita |
| Frontend 2 | Darryl Ezekiel Simanjuntak |
| Backend 1 | Maximillian Ebert Susanto |
| Backend 2 | Ni Wayan Putri Mahadewi |
| DevOps, QA, Sprint Facilitator | Dewa Putu Sealtiel Armeza Diandra |

Dosen Pembimbing: Ngakan Nyoman Kutha Krisnawijaya