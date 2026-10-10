import 'package:flutter/material.dart';
import 'package:usadalensapp/features/splash/presentation/screens/splash_page.dart';
import 'package:usadalensapp/shared/theme/app_theme.dart';

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Usada Lens',
      debugShowCheckedModeBanner: false,
      theme: buildAppTheme(),
      home: const SplashPage(),
    );
  }
}
