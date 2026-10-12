import 'package:flutter_test/flutter_test.dart';
import 'package:usadalensapp/app.dart';
import 'package:usadalensapp/features/auth/presentation/screens/login_page.dart';
import 'package:usadalensapp/features/splash/presentation/screens/splash_page.dart';

void main() {
  testWidgets('splash tampil lalu berpindah ke halaman login', (tester) async {
    await tester.pumpWidget(const MyApp());

    expect(find.byType(SplashPage), findsOneWidget);

    await tester.pump(const Duration(seconds: 3));
    await tester.pumpAndSettle();

    expect(find.byType(LoginPage), findsOneWidget);
  });
}