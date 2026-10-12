import 'package:flutter_test/flutter_test.dart';
import 'package:usadalensapp/shared/theme/app_theme.dart';
import 'package:usadalensapp/shared/theme/theme.dart';

void main() {
  test('tema memakai token warna dari design system', () {
    final theme = buildAppTheme();

    expect(theme.colorScheme.primary, AppColors.primary700);
    expect(theme.scaffoldBackgroundColor, AppColors.background);
  });
}
