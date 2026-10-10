# Usada Lens Mobile

Aplikasi Flutter untuk Android, target API level 24 ke atas. Aplikasi hanya menampilkan data dan meneruskan aksi pengguna ke backend. Aturan arsitektur lengkap ada di `docs/ARSITEKTUR.md`.

## Struktur lib

- `core/network` klien HTTP dan penanganan error payload baku
- `core/utils` helper murni non-bisnis
- `features/<fitur>/data` repository implementation, DTO, sumber data
- `features/<fitur>/domain` use case dan entity
- `features/<fitur>/presentation/screens` layar yang hanya merender state
- `features/<fitur>/presentation/components` komponen UI per fitur
- `features/<fitur>/presentation/viewmodels` state dan pemanggil use case
- `shared/components` komponen UI yang dipakai lintas fitur
- `shared/theme` token warna, tipografi, spasi, dan radius dari Figma Variables
