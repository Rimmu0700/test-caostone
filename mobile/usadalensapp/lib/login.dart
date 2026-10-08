import 'package:flutter/material.dart';
import 'home.dart';
import 'theme/theme.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final _formKey = GlobalKey<FormState>();
  final _namaController = TextEditingController();
  final _sandiController = TextEditingController();
  bool _sembunyikanSandi = true;
  bool _ingatSaya = true;

  @override
  void dispose() {
    _namaController.dispose();
    _sandiController.dispose();
    super.dispose();
  }

  void _masuk() {
    if (_formKey.currentState!.validate()) {
      // TODO: ganti dengan proses login ke backend
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(
          builder: (context) => const MyHomePage(title: 'Usada Lens'),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: SingleChildScrollView(
          padding: AppSpacing.screenPadding,
          child: Center(
            child: ConstrainedBox(
              constraints: const BoxConstraints(maxWidth: 400),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const SizedBox(height: AppSpacing.space3),
                  InkWell(
                    onTap: () => Navigator.maybePop(context),
                    customBorder: const CircleBorder(),
                    child: Container(
                      width: 40,
                      height: 40,
                      decoration: BoxDecoration(
                        color: AppColors.border.withValues(alpha: 0.2),
                        shape: BoxShape.circle,
                      ),
                      child: const Icon(
                        Icons.chevron_left,
                        color: AppColors.primary900,
                      ),
                    ),
                  ),
                  const SizedBox(height: AppSpacing.space6),
                  Center(
                    child: Image.asset(
                      'assets/images/logo2.png',
                      width: 170,
                      errorBuilder: (context, error, stackTrace) =>
                          const FlutterLogo(size: 100),
                    ),
                  ),
                  const SizedBox(height: AppSpacing.space7),
                  Center(
                    child: Text(
                      'Masuk ke akun Anda',
                      style: AppTypography.h3.copyWith(
                        color: AppColors.textPrimary,
                      ),
                    ),
                  ),
                  const SizedBox(height: AppSpacing.space4),
                  Form(
                    key: _formKey,
                    child: Column(
                      children: [
                        TextFormField(
                          controller: _namaController,
                          style: AppTypography.body,
                          decoration: const InputDecoration(
                            hintText: 'Nama Lengkap',
                            prefixIcon: Icon(
                              Icons.person_outline,
                              color: AppColors.primary900,
                            ),
                          ),
                          validator: (v) => (v == null || v.trim().isEmpty)
                              ? 'Nama lengkap wajib diisi'
                              : null,
                        ),
                        const SizedBox(height: AppSpacing.space3),
                        TextFormField(
                          controller: _sandiController,
                          obscureText: _sembunyikanSandi,
                          style: AppTypography.body,
                          decoration: InputDecoration(
                            hintText: 'Kata Sandi',
                            prefixIcon: const Icon(
                              Icons.lock_outline,
                              color: AppColors.primary900,
                            ),
                            suffixIcon: IconButton(
                              tooltip: _sembunyikanSandi
                                  ? 'Tampilkan kata sandi'
                                  : 'Sembunyikan kata sandi',
                              icon: Icon(
                                _sembunyikanSandi
                                    ? Icons.visibility_off_outlined
                                    : Icons.visibility_outlined,
                                color: AppColors.textSecondary,
                              ),
                              onPressed: () => setState(
                                () => _sembunyikanSandi = !_sembunyikanSandi,
                              ),
                            ),
                          ),
                          validator: (v) {
                            if (v == null || v.isEmpty) {
                              return 'Kata sandi wajib diisi';
                            }
                            if (v.length < 6) {
                              return 'Kata sandi minimal 6 karakter';
                            }
                            return null;
                          },
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(height: AppSpacing.space3),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      InkWell(
                        onTap: () => setState(() => _ingatSaya = !_ingatSaya),
                        child: Row(
                          children: [
                            Icon(
                              _ingatSaya
                                  ? Icons.check_circle
                                  : Icons.circle_outlined,
                              size: 18,
                              color: AppColors.primary700,
                            ),
                            const SizedBox(width: AppSpacing.space2),
                            Text('Ingat saya', style: AppTypography.caption),
                          ],
                        ),
                      ),
                      GestureDetector(
                        onTap: () {
                          // TODO: halaman lupa kata sandi
                        },
                        child: Text(
                          'Lupa Kata Sandi?',
                          style: AppTypography.caption.copyWith(
                            color: AppColors.primary700,
                            decoration: TextDecoration.underline,
                          ),
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: AppSpacing.space6),
                  ElevatedButton(
                    onPressed: _masuk,
                    child: const Text('Masuk'),
                  ),
                  const SizedBox(height: AppSpacing.space3),
                  Center(
                    child: Row(
                      mainAxisSize: MainAxisSize.min,
                      children: [
                        Text(
                          'Belum punya akun? ',
                          style: AppTypography.caption.copyWith(
                            color: AppColors.textSecondary,
                          ),
                        ),
                        GestureDetector(
                          onTap: () {
                            // TODO: Navigator.push ke RegisterPage
                          },
                          child: Text(
                            'Daftar',
                            style: AppTypography.caption.copyWith(
                              fontWeight: AppTypography.bold,
                              color: AppColors.primary700,
                              decoration: TextDecoration.underline,
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(height: AppSpacing.space4),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }
}