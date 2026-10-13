import 'package:flutter/material.dart';

abstract class AppTypography {

  // Font Family Utama
  static const String fontFamily = 'Inter';

  // Font Weights (Ketebalan Font)
  static const FontWeight regular = FontWeight.w400;  // Regular
  static const FontWeight medium = FontWeight.w500;   // Medium
  static const FontWeight semiBold = FontWeight.w600; // Semi Bold
  static const FontWeight bold = FontWeight.w700;     // Bold

  /// Display / H1 (32px / 40px, Bold)
  /// Judul besar, splash
  static const TextStyle displayH1 = TextStyle(
    fontFamily: fontFamily,
    fontSize: 32,
    height: 40 / 32, // 1.25
    fontWeight: bold,
  );

  /// H2 (24px / 32px, Semi Bold)
  /// Judul section / layar
  static const TextStyle h2 = TextStyle(
    fontFamily: fontFamily,
    fontSize: 24,
    height: 32 / 24, // 1.33
    fontWeight: semiBold,
  );

  /// H3 (20px / 28px, Semi Bold)
  /// Judul card, nama spesies
  static const TextStyle h3 = TextStyle(
    fontFamily: fontFamily,
    fontSize: 20,
    height: 28 / 20, // 1.4
    fontWeight: semiBold,
  );

  /// Body Large (16px / 24px, Regular)
  /// Deskripsi utama
  static const TextStyle bodyLarge = TextStyle(
    fontFamily: fontFamily,
    fontSize: 16,
    height: 24 / 16, // 1.5
    fontWeight: regular,
  );

  /// Body (14px / 20px, Regular)
  /// Konten umum
  static const TextStyle body = TextStyle(
    fontFamily: fontFamily,
    fontSize: 14,
    height: 20 / 14, // 1.43
    fontWeight: regular,
  );

  /// Label (14px / 20px, Medium)
  /// Form / input
  static const TextStyle label = TextStyle(
    fontFamily: fontFamily,
    fontSize: 14,
    height: 20 / 14, // 1.43
    fontWeight: medium,
  );

  /// Button (14px / 20px, Semi Bold)
  /// CTA utama / sekunder
  static const TextStyle button = TextStyle(
    fontFamily: fontFamily,
    fontSize: 14,
    height: 20 / 14, // 1.43
    fontWeight: semiBold,
  );

  /// Caption (12px / 16px, Regular)
  /// Helper text, timestamp, label tab bar
  static const TextStyle caption = TextStyle(
    fontFamily: fontFamily,
    fontSize: 12,
    height: 16 / 12, // 1.33
    fontWeight: regular,
  );
}
