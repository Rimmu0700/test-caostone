# Sistem Identifikasi dan Edukasi Tanaman Obat Usada Bali

Capstone Project Kelompok 10, Program Studi Teknologi Informasi, Undiknas 2026.
Jalur GovTech, pilar AI. Mitra: BRIN Kebun Raya Eka Karya Bali.

## Struktur Repositori

| Folder | Isi | Penanggung jawab |
|---|---|---|
| backend | REST API, pipeline YOLO11, MobileNetV3-Small, Grad-CAM | Backend 1 dan Backend 2 |
| mobile | Aplikasi Flutter untuk Android | Frontend 1 |
| admin | Dasbor admin dan kurator | Frontend 2 |
| docs | SRS, SAD, ERD, openapi.yaml, tautan Figma | Seluruh tim |

## Menjalankan Secara Lokal

1. Salin `.env.example` menjadi `.env` lalu isi nilainya.
2. Jalankan `docker compose up --build`.
3. API tersedia di `http://localhost:8000`.

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