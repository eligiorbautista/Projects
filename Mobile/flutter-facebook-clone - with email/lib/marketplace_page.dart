import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';

class marketplace_page extends StatefulWidget {
  const marketplace_page({super.key});

  @override
  State<marketplace_page> createState() => _marketplace_pageState();
}

class _marketplace_pageState extends State<marketplace_page> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: ListView(
        children: [
          Column(children: [
            SizedBox(
              height: 10,
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.start,
              children: [
                SizedBox(
                  width: 10,
                ),
                Text(
                  "Marketplace",
                  style: TextStyle(fontSize: 30, fontFamily: "Klavika"),
                )
              ],
            ),
          ]),
          Column(
              mainAxisAlignment: MainAxisAlignment.center,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Column(
                  children: [
                    Icon(Icons.construction, size: 90, color: Colors.grey),
                    Text("This Page Isn't Available Right Now\n",
                        style: TextStyle(
                            color: Colors.grey, fontWeight: FontWeight.bold)),
                    Text("Work in progress...\n",
                        style: TextStyle(color: Colors.grey)),
                    ElevatedButton(
                      onPressed: () {
                        Fluttertoast.showToast(
                            msg:
                                'Something went wrong.\nPlease try again later.',
                            toastLength: Toast.LENGTH_SHORT,
                            gravity: ToastGravity.BOTTOM,
                            timeInSecForIosWeb: 2,
                            backgroundColor: Colors.grey,
                            textColor: Colors.white,
                            fontSize: 12);
                      },
                      child: Text("Reload Page"),
                      style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.blueAccent,
                          foregroundColor: Colors.white),
                    ),
                    Text("\nFacebook Clone By Eli Bautista\n",
                        style: TextStyle(
                            color: Colors.grey,
                            fontSize: 12,
                            fontWeight: FontWeight.bold)),
                    Text("DISCLAIMER:",
                        style: TextStyle(
                            color: Colors.grey,
                            fontSize: 10,
                            fontWeight: FontWeight.bold)),
                    Text("This project is for educational purposes only.",
                        style: TextStyle(color: Colors.grey, fontSize: 10))
                  ],
                )
              ]),
        ],
      ),
    );
  }
}
