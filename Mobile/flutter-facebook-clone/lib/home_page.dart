import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';

class home_page extends StatefulWidget {
  const home_page({super.key});

  @override
  State<home_page> createState() => _home_pageState();
}

class _home_pageState extends State<home_page> {
  final postTextController = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: ListView(
        children: [
          SizedBox(
            height: 10,
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.start,
            children: <Widget>[
              SizedBox(
                width: 10,
              ),
              CircleAvatar(
                  radius: 21,
                  backgroundImage: AssetImage("assets/images/eli.jpg")),
              SizedBox(
                width: 10,
              ),
              Expanded(
                child: TextButton(
                  onPressed: () {},
                  child: Text(
                    "What's on your mind?",
                    textDirection: TextDirection.ltr,
                    textAlign: TextAlign.left,
                    style: TextStyle(fontSize: 16),
                  ),
                  style: TextButton.styleFrom(
                    shape: StadiumBorder(),
                    backgroundColor: Colors.white,
                    foregroundColor: Color.fromARGB(137, 43, 42, 42),
                    side: BorderSide(color: Colors.black54, width: 0.5),
                  ),
                ),
              ),
              IconButton(
                  onPressed: () {},
                  icon: Icon(
                    Icons.image,
                    color: Colors.green,
                  )),
              SizedBox(
                width: 5,
              ),
            ],
          ),
          Divider(
            color: Color.fromARGB(255, 210, 208, 208),
            height: 20,
            thickness: 10,
          ),
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
