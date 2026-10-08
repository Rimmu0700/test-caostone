import 'package:flutter/material.dart';
import 'theme/theme.dart';

class MyHomePage extends StatelessWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.background,
      body: const SafeArea(
        child: SizedBox.expand(), // kosong, isi nanti sesuai Figma
      ),
    );
  }
}