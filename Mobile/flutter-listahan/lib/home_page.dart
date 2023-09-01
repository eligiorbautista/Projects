import 'package:flutter/material.dart';

import 'debt_manager_page.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
          title: const Text(" Home Page"),
          backgroundColor: const Color.fromARGB(255, 38, 37, 37)),
      body:
          Column(mainAxisAlignment: MainAxisAlignment.center, children: const [
        Text(
          "Debt List Manager",
          style: TextStyle(
              fontSize: 28,
              fontWeight: FontWeight.bold,
              fontStyle: FontStyle.italic),
          textAlign: TextAlign.center,
        ),
        Text(
          "Final Project in CP105 by Jhudielle Mark Bautista",
          style: TextStyle(
            fontSize: 18,
          ),
          textAlign: TextAlign.center,
        )
      ]),
      drawer: NavigationDrawer(children: [
        SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              buildMenuHeader(context),
              buildMenuItems(context),
            ],
          ),
        )
      ]),
    );
  }

  Widget buildMenuHeader(BuildContext context) => SizedBox(
        height: 150,
        child: Padding(
            padding: const EdgeInsets.all(10),
            child: Image.asset(
              "assets/logo-rect.png",
            )),
      );
  Widget buildMenuItems(BuildContext context) => Padding(
        padding: const EdgeInsets.all((8)),
        child: Wrap(
          runSpacing: 10, // Vertical Spacing
          children: [
            const Divider(
              color: Color.fromARGB(255, 91, 86, 86),
            ),
            ListTile(
              leading: const Icon(Icons.home),
              title: const Text("Home"),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (BuildContext context) => const HomePage(),
                  ),
                );
              },
            ),
            ListTile(
              leading: const Icon(Icons.note_add),
              title: const Text("Debt Manager"),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (BuildContext context) => const DebtManagerPage(),
                  ),
                );
              },
            ),
          ],
        ),
      );
}
