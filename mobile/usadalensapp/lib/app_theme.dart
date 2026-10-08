import 'package:flutter/material.dart';
import 'theme/theme.dart';

ThemeData buildAppTheme() {
  final base = ThemeData(
    useMaterial3: true,
    colorScheme: ColorScheme.fromSeed(
      seedColor: AppColors.primary700,
      primary: AppColors.primary700,
      onPrimary: Colors.white,
      error: AppColors.error,
      surface: AppColors.surface,
    ),
    scaffoldBackgroundColor: AppColors.background,
  );

  OutlineInputBorder border(Color color, [double width = 1]) {
    return OutlineInputBorder(
      borderRadius: AppRadius.borderInput,
      borderSide: BorderSide(color: color, width: width),
    );
  }

  return base.copyWith(
    textTheme: base.textTheme.apply(
      fontFamily: AppTypography.fontFamily,
      bodyColor: AppColors.textPrimary,
      displayColor: AppColors.textPrimary,
    ),
    inputDecorationTheme: InputDecorationTheme(
      filled: true,
      fillColor: AppColors.surface,
      hintStyle: AppTypography.body.copyWith(color: AppColors.textSecondary),
      errorStyle: AppTypography.caption.copyWith(color: AppColors.error),
      contentPadding: AppSpacing.inputPadding.copyWith(top: 14, bottom: 14),
      border: border(AppColors.border),
      enabledBorder: border(AppColors.border),
      focusedBorder: border(AppColors.primary700, 2),
      errorBorder: border(AppColors.error),
      focusedErrorBorder: border(AppColors.error, 2),
    ),
    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ButtonStyle(
        minimumSize:
            const WidgetStatePropertyAll(Size.fromHeight(AppSpacing.controlHeight)),
        padding: const WidgetStatePropertyAll(AppSpacing.buttonPadding),
        shape: const WidgetStatePropertyAll(
          RoundedRectangleBorder(borderRadius: AppRadius.borderButton),
        ),
        textStyle: const WidgetStatePropertyAll(AppTypography.button),
        foregroundColor: const WidgetStatePropertyAll(Colors.white),
        backgroundColor: WidgetStateProperty.resolveWith((states) {
          if (states.contains(WidgetState.disabled)) {
            return AppColors.border.withValues(alpha: 0.25);
          }
          if (states.contains(WidgetState.pressed)) return AppColors.primary900;
          if (states.contains(WidgetState.hovered)) return AppColors.primary800;
          return AppColors.primary700;
        }),
      ),
    ),
    appBarTheme: AppBarTheme(
      backgroundColor: AppColors.primary900,
      foregroundColor: Colors.white,
      titleTextStyle: AppTypography.h3.copyWith(color: Colors.white),
    ),
  );
}