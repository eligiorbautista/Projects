import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:flutter/services.dart';
import 'navigation.dart';
//import 'package:url_launcher/url_launcher.dart';
//import 'home_page.dart';

void main() {
  // disable landscape mode / disable app rotation
  WidgetsFlutterBinding.ensureInitialized();
  SystemChrome.setPreferredOrientations(
      [DeviceOrientation.portraitUp, DeviceOrientation.portraitDown]);
  runApp(const MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  static const app_title = "Facebook";

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      debugShowCheckedModeBanner: false,
      title: app_title,
      home: const Scaffold(
        appBar: null,
        body: MyStatefulWidget(),
        backgroundColor: Colors.blueAccent,
      ),
    );
  }
}
// End of the app bar

// Start of main body
class MyStatefulWidget extends StatefulWidget {
  const MyStatefulWidget({Key? key}) : super(key: key);

  @override
  State<MyStatefulWidget> createState() => _MyStatefulWidgetState();
}

class _MyStatefulWidgetState extends State<MyStatefulWidget> {
  @override
  Widget build(BuildContext context) {
    return LoginPage();
  }
}

class LoginPage extends StatefulWidget {
  const LoginPage({Key? key}) : super(key: key);

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  TextEditingController nameController = TextEditingController();
  TextEditingController passwordController = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(10.0),
      child: ListView(
        children: <Widget>[
          // FIRST ITEM IN THE LIST VIEW
          Container(
            alignment: Alignment.center,
            padding: const EdgeInsets.all(10),
            child: const Text(
              "\nfacebook\n",
              style: TextStyle(
                  color: Colors.white,
                  fontWeight: FontWeight.w800,
                  fontSize: 60,
                  fontFamily: "Klavika"),
            ),
          ),
          // SECOND ITEM IN THE LIST VIEW
          Container(
              //height: 70,
              alignment: Alignment.center,
              padding: const EdgeInsets.all(10),
              child: TextField(
                controller: nameController,
                decoration: const InputDecoration(
                    border: OutlineInputBorder(),
                    hintText: "Email address or phone number",
                    filled: true,
                    fillColor: Colors.white,
                    contentPadding: const EdgeInsets.only(top: 10.0, left: 10)),
              )),
          Container(
            height: 65,
            alignment: Alignment.bottomCenter,
            padding: const EdgeInsets.all(10),
            child: TextField(
              controller: passwordController,
              decoration: const InputDecoration(
                  border: OutlineInputBorder(),
                  hintText: "Password",
                  filled: true,
                  fillColor: Colors.white,
                  contentPadding: const EdgeInsets.only(top: 10.0, left: 10)),
              obscureText: true, // makes input not visible
            ),
          ),
          TextButton(
              onPressed: () {
                Fluttertoast.showToast(
                  msg: "Something went wrong.\nPlease try again later.",
                  backgroundColor: Colors.white,
                  fontSize: 12,
                  gravity: ToastGravity.BOTTOM,
                  textColor: Colors.black,
                  toastLength: Toast.LENGTH_SHORT,
                  timeInSecForIosWeb: 2,
                ); // toast
              },
              child: const Text("Forgot Password?",
                  style: TextStyle(
                      color: Colors.white,
                      decoration: TextDecoration.underline))),
          Container(
            height: 60,
            alignment: Alignment.center,
            padding: const EdgeInsets.all(10),
            child: ElevatedButton(
              child: Text(
                "Log In",
                style: TextStyle(fontSize: 16),
              ),
              onPressed: () {
                ///
                Navigator.of(context)
                    .push(// context is basically a bridge between every widgets
                        MaterialPageRoute(builder: (BuildContext context) {
                  return const navigation();
                }));

                ///
              },
              style: ElevatedButton.styleFrom(
                minimumSize: Size(700, 60),
                backgroundColor: Colors.indigo,
              ),
            ),
          ),
          Center(
              child: Text(
            "\n──────────────────   or   ──────────────────\n",
            style: TextStyle(color: Colors.white, fontSize: 11),
          )),
          Container(
            height: 60,
            alignment: Alignment.bottomCenter,
            padding: const EdgeInsets.all(10),
            child: ElevatedButton(
                child: Text(
                  "Create new account",
                  style: TextStyle(fontSize: 16),
                ),
                onPressed: () {},
                style: ElevatedButton.styleFrom(
                  minimumSize: Size(700, 60),
                  backgroundColor: Colors.green,
                )),
          )
        ],
      ),
    );
  }
}
