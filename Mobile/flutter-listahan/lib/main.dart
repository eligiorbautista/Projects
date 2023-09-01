import 'package:flutter/material.dart';
import 'home_page.dart';

void main() {
  runApp(const ListahanApp());
}

class ListahanApp extends StatelessWidget {
  const ListahanApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      debugShowCheckedModeBanner: false,
      home: HomePage(),
    );
  }
}
