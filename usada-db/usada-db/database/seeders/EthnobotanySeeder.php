<?php

namespace Database\Seeders;

use App\Models\Ethnobotany;
use App\Models\Species;
use Illuminate\Database\Seeder;

class EthnobotanySeeder extends Seeder
{
    /**
     * Membuat 1 baris ethnobotany per spesies (relasi 1:1) dengan status 'pending'.
     * Isi manfaat, bagian tanaman, dan cara penggunaan sengaja dikosongkan:
     * harus diisi dari sumber Usada/literatur lalu diverifikasi kurator.
     */
    public function run(): void
    {
        Species::all()->each(function (Species $species) {
            Ethnobotany::firstOrCreate(
                ['species_id' => $species->species_id],
                ['verification_status' => 'pending']
            );
        });
    }
}
