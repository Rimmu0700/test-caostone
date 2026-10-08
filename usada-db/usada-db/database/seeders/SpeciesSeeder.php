<?php

namespace Database\Seeders;

use App\Models\Species;
use Illuminate\Database\Seeder;

class SpeciesSeeder extends Seeder
{
    /**
     * 17 spesies tanaman obat Usada Bali (sesuai folder dataset).
     * Urutan = urutan folder pada dataset. local_name yang null perlu dilengkapi/diverifikasi.
     */
    public function run(): void
    {
        $species = [
            ['scientific_name' => 'Alpinia galanga (L.) Willd.', 'local_name' => 'Lengkuas'],
            ['scientific_name' => 'Amomum compactum Sol. ex Maton', 'local_name' => 'Kapulaga'],
            ['scientific_name' => 'Anredera cordifolia (Ten.) Steenis', 'local_name' => 'Binahong'],
            ['scientific_name' => 'Antidesma bunius (L.) Spreng.', 'local_name' => 'Buni'],
            ['scientific_name' => 'Blumea balsamifera (L.) DC.', 'local_name' => 'Sembung'],
            ['scientific_name' => 'Cinnamomum verum J.Presl', 'local_name' => 'Kayu manis'],
            ['scientific_name' => 'Curcuma sylvatica Valeton', 'local_name' => null],
            ['scientific_name' => 'Erythrina hypaphorus Boerl. ex Koord.', 'local_name' => 'Dadap'],
            ['scientific_name' => 'Euchresta horsfieldii (Lesch.) Benn.', 'local_name' => null],
            ['scientific_name' => 'Graptophyllum pictum (L.) Griff.', 'local_name' => 'Daun ungu'],
            ['scientific_name' => 'Justicia gendarussa Burm.f.', 'local_name' => 'Gandarusa'],
            ['scientific_name' => 'Piper betle L.', 'local_name' => 'Sirih'],
            ['scientific_name' => 'Plantago major L.', 'local_name' => 'Sendok-sendok'],
            ['scientific_name' => 'Symphytum officinale L.', 'local_name' => 'Comfrey'],
            ['scientific_name' => 'Tabernaemontana sp.', 'local_name' => null],
            ['scientific_name' => 'Zingiber officinale Roxb.', 'local_name' => 'Jahe'],
            ['scientific_name' => 'Zingiber purpureum Roxb.', 'local_name' => 'Bangle'],
        ];

        foreach ($species as $row) {
            Species::updateOrCreate(
                ['scientific_name' => $row['scientific_name']],
                ['local_name' => $row['local_name'], 'is_active' => true]
            );
        }
    }
}
