import 'package:flutter/material.dart';

abstract class AppRadius { 
  // Radius Values
  static const double badge = 8.0;    // Chip / Badge
  static const double button = 12.0;  // Button
  static const double input = 12.0;   // Input field
  static const double card = 16.0;    // Card
  static const double modal = 16.0;   // Modal
  static const double pill = 999.0;   // Pill & Tombol kamera (FAB)

  // BorderRadius
  static const BorderRadius borderBadge = BorderRadius.all(Radius.circular(badge));
  static const BorderRadius borderButton = BorderRadius.all(Radius.circular(button));
  static const BorderRadius borderInput = BorderRadius.all(Radius.circular(input));
  static const BorderRadius borderCard = BorderRadius.all(Radius.circular(card));
  static const BorderRadius borderModal = BorderRadius.all(Radius.circular(modal));
  static const BorderRadius borderPill = BorderRadius.all(Radius.circular(pill));
}