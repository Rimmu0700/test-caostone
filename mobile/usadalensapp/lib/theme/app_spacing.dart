import 'package:flutter/material.dart';

abstract class AppSpacing {
  static const double space1 = 4.0;  // Micro gap
  static const double space2 = 8.0;  // Gap ikon-label
  static const double space3 = 16.0; // Padding card & screen horizontal
  static const double space4 = 24.0; // Padding modal / gap section
  static const double space5 = 32.0; // Section spacing
  static const double space6 = 40.0; // Large section spacing
  static const double space7 = 48.0; // Tinggi kontrol / page spacing
  static const double space8 = 64.0; // Page spacing besar
  

  static const double controlHeight = 48.0; // Tinggi Field Form & CTA (Input/Button)
  static const double gridGap = 16.0; // Grid gap Card tanaman (Kamus Usada)
 
 // Padding Komponen/// Screen / Page: 16 px kiri-kanan (Mobile) 
  static const EdgeInsets screenPadding = EdgeInsets.symmetric(horizontal: space3);

  /// Card: 16 px (Konten kartu)
  static const EdgeInsets cardPadding = EdgeInsets.all(space3);

  /// Input: 16 px horizontal
  static const EdgeInsets inputPadding = EdgeInsets.symmetric(horizontal: space3);

  /// Button: 24 px horizontal
  static const EdgeInsets buttonPadding = EdgeInsets.symmetric(horizontal: space4);

  /// Modal: 24 px (Konten dialog)
  static const EdgeInsets modalPadding = EdgeInsets.all(space4);

  /// Bottom Navigation: 8-16 px vertical
  static const EdgeInsets bottomNavPadding = EdgeInsets.symmetric(vertical: space2);
}

      