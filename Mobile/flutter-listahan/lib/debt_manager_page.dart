import 'package:flutter/material.dart';

import 'home_page.dart';

import 'package:collection/collection.dart';

List<String> nameList = [
  "No Data has been added yet.",
];
List<String> emailList = [
  "-",
];

List<double> debtAmountList = [0];
List<String> transactionNoteList = [
  "If new data has been added, please delete this data.",
];
List<String> transactionDateList = [
  "-",
];

List debtList = [
  nameList,
  emailList,
  debtAmountList,
  transactionNoteList,
  transactionDateList,
];

List newDebtList = [];

final nameController = TextEditingController();
final emailController = TextEditingController();
final amountController = TextEditingController();
final noteController = TextEditingController();

int currentIndex = 0;
int validation = 0;
double totalDebt = debtAmountList.sum;

class DebtManagerPage extends StatefulWidget {
  const DebtManagerPage({super.key});

  @override
  State<DebtManagerPage> createState() => _DebtManagerPageState();
}

class _DebtManagerPageState extends State<DebtManagerPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Debt Manager"),
        backgroundColor: const Color.fromARGB(255, 38, 37, 37),
        bottom: Tab(
            child: Row(
          children: [
            const SizedBox(
              width: 10,
            ),
            Card(
              color: const Color.fromARGB(255, 75, 74, 74),
              child: Padding(
                padding: const EdgeInsets.all(8.0),
                child: Text(
                  "Total Debt: ₱$totalDebt",
                  style: const TextStyle(
                      color: Colors.white,
                      fontSize: 18,
                      fontWeight: FontWeight.bold),
                ),
              ),
            ),
          ],
        )),
      ),
      body: debtsListView(context),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          addData(context);
        },
        backgroundColor: const Color.fromARGB(255, 38, 37, 37),
        child: const Icon(Icons.add),
      ),
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

  viewDebtDialog(BuildContext context, String name, String email,
      String debtAmount, String transactionNote, String transactionDate) {
    return showDialog(
        context: context,
        builder: (context) => StatefulBuilder(
                builder: (BuildContext? context, StateSetter setState) {
              return AlertDialog(
                title: Flexible(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        name,
                        style: const TextStyle(fontSize: 18),
                      ),
                      Text(
                        email,
                        style: const TextStyle(fontSize: 16),
                      ),
                    ],
                  ),
                ),
                content: SingleChildScrollView(
                  child: Column(
                    children: [
                      Row(
                        children: [
                          Flexible(
                            child: Text(
                              "₱ $debtAmount",
                              style: const TextStyle(fontSize: 22),
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(
                        height: 8,
                      ),
                      Row(
                        children: [
                          Flexible(
                            child: Text(
                              "Note: \n$transactionNote",
                              style: const TextStyle(fontSize: 16),
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(
                        height: 5,
                      ),
                      Row(
                        children: [
                          Flexible(
                            child: Text(
                              "Datetime: \n$transactionDate",
                              style: const TextStyle(fontSize: 16),
                            ),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
              );
            }));
  }

  removeDebt() {
    setState(() {
      debtList.removeAt(currentIndex);
    });
  }

  Widget debtsListView(BuildContext context) => Padding(
        padding: const EdgeInsets.fromLTRB(8, 0, 8, 0),
        child: ListView.builder(
            itemCount: nameList.length,
            itemBuilder: (context, index) {
              return Card(
                color: Colors.white,
                elevation: 2,
                shadowColor: Colors.black,
                child: ListTile(
                    onTap: () {
                      setState(() {
                        currentIndex = index;
                      });
                      viewDebtDialog(
                        context,
                        debtList[0][index],
                        debtList[1][index],
                        (debtList[2][index]).toString(),
                        debtList[3][index],
                        debtList[4][index],
                      );
                    },
                    title: Text(nameList[index],
                        style: const TextStyle(
                            fontWeight: FontWeight.bold, fontSize: 20)),
                    subtitle: Text(transactionNoteList[index],
                        style: const TextStyle(fontSize: 16)),
                    leading: null,
                    trailing: IconButton(
                        onPressed: () {
                          setState(() {
                            showDialog(
                              context: context,
                              builder: (
                                BuildContext context,
                              ) {
                                return AlertDialog(
                                  title: null,
                                  content: const SizedBox(
                                    height: 100,
                                    child: Center(
                                        child: Text(
                                      "Are you sure you want to remove this transaction?",
                                      style: TextStyle(
                                          fontSize: 25,
                                          fontWeight: FontWeight.bold),
                                    )),
                                  ),
                                  actions: [
                                    ElevatedButton(
                                        onPressed: () {
                                          debugPrint(debtList.toString());
                                          nameList.removeAt(index);
                                          emailList.removeAt(index);
                                          debtAmountList.removeAt(index);
                                          transactionNoteList.removeAt(index);
                                          transactionDateList.removeAt(index);

                                          totalDebt = debtAmountList.sum;
                                          closeContext(context);
                                          refreshPage(context);
                                        },
                                        child: const Text("Yes")),
                                    ElevatedButton(
                                        onPressed: () {
                                          closeContext(context);
                                          refreshPage(context);
                                        },
                                        child: const Text("Cancel"))
                                  ],
                                );
                              },
                            );
                          });
                        },
                        icon: const Icon(Icons.close_rounded))),
              );
            }),
      );

  refreshPage(BuildContext context) {
    Navigator.pushReplacement(
      context,
      PageRouteBuilder(
        pageBuilder: (context, animation1, animation2) =>
            const DebtManagerPage(),
        transitionDuration: Duration.zero,
        reverseTransitionDuration: Duration.zero,
      ),
    );
  }

  closeContext(BuildContext context) {
    refreshPage(context);
    Navigator.pop(context);
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

  addData(BuildContext context) async {
    showDialog<Widget>(
        context: context,
        builder: (BuildContext context) {
          return StatefulBuilder(
              builder: (BuildContext context, StateSetter setState) {
            return AlertDialog(
              title: const Text("Add new debt"),
              content: SingleChildScrollView(
                padding: const EdgeInsets.all(5),
                scrollDirection: Axis.vertical,
                child: Form(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      TextFormField(
                        controller: nameController,
                        decoration: const InputDecoration(
                            border: OutlineInputBorder(
                                borderSide: BorderSide(color: Colors.black)),
                            hintText: "Name",
                            icon: Icon(
                              Icons.person,
                              color: Colors.black,
                            ),
                            filled: true,
                            fillColor: Colors.white),
                        keyboardType: TextInputType.name,
                      ),
                      const SizedBox(
                        height: 10,
                      ),
                      TextFormField(
                        controller: emailController,
                        decoration: const InputDecoration(
                            border: OutlineInputBorder(
                                borderSide: BorderSide(color: Colors.black)),
                            icon: Icon(
                              Icons.email_rounded,
                              color: Colors.black,
                            ),
                            hintText: "Email",
                            filled: true,
                            fillColor: Colors.white),
                        keyboardType: TextInputType.emailAddress,
                      ),
                      const SizedBox(
                        height: 10,
                      ),
                      TextFormField(
                        controller: amountController,
                        decoration: const InputDecoration(
                            border: OutlineInputBorder(
                                borderSide: BorderSide(color: Colors.black)),
                            hintText: "Amount",
                            icon: Text(
                              "₱  ",
                              style: TextStyle(
                                  fontSize: 20, fontWeight: FontWeight.bold),
                            ),
                            filled: true,
                            fillColor: Colors.white),
                        keyboardType: TextInputType.number,
                      ),
                      const SizedBox(
                        height: 10,
                      ),
                      TextFormField(
                        controller: noteController,
                        decoration: const InputDecoration(
                            border: OutlineInputBorder(
                                borderSide: BorderSide(color: Colors.black)),
                            icon: Icon(
                              Icons.list_alt_sharp,
                              color: Colors.black,
                            ),
                            hintText: "note",
                            filled: true,
                            fillColor: Colors.white),
                        keyboardType: TextInputType.multiline,
                        minLines: 5,
                        maxLines: 5,
                      ),
                      const SizedBox(
                        height: 10,
                      ),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.end,
                        children: [
                          ElevatedButton(
                              onPressed: () {
                                addToList(
                                  nameController.text,
                                  emailController.text,
                                  amountController.text,
                                  noteController.text,
                                );

                                closeContext(context);
                              },
                              style: ElevatedButton.styleFrom(
                                  padding:
                                      const EdgeInsets.fromLTRB(15, 8, 15, 8),
                                  backgroundColor:
                                      const Color.fromARGB(255, 38, 37, 37)),
                              child: Row(
                                children: const [
                                  Icon(
                                    Icons.add_circle,
                                    color: Colors.white,
                                  ),
                                  SizedBox(
                                    width: 5,
                                  ),
                                  Text("Add Data"),
                                ],
                              )),
                        ],
                      )
                    ],
                  ),
                ),
              ),
            );
          });
        });
  }

  addToList(String name, String email, String amount, String note) {
    setState(() {
      nameList.add(name);
      emailList.add(email);
      debtAmountList.add(double.parse(amount));
      transactionNoteList.add(note);
      transactionDateList.add((DateTime.now()).toString());

      nameController.clear();
      emailController.clear();
      amountController.clear();
      noteController.clear();
      totalDebt = debtAmountList.sum;
    });
  }
}
