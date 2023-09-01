import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:login_with_signup/gaming_page.dart';
import 'package:login_with_signup/watch_page.dart';
import 'package:login_with_signup/marketplace_page.dart';
import 'package:login_with_signup/notifications_page.dart';
import 'package:login_with_signup/menu_page.dart';

import 'home_page.dart';

class navigation extends StatefulWidget {
  const navigation({Key? key}) : super(key: key);

  @override
  State<navigation> createState() => _navigationState();
}

class _navigationState extends State<navigation>
    with SingleTickerProviderStateMixin {
  late final TabController controller;

  bool showAppBar = true;
  List pages = [
    home_page(),
    watch_page(),
    marketplace_page(),
    gaming_page(),
    notifications_page(),
    menu_page()
  ];
  int pageIndex = 0;
  @override
  void initState() {
    controller = TabController(length: 6, vsync: this);
    super.initState();
  }

  TextEditingController postTextController = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: showAppBar
            ? AppBar(
                automaticallyImplyLeading: false, // removes default back button
                title: const Text("facebook",
                    style: TextStyle(
                        color: Colors.blueAccent,
                        fontFamily: "Klavika",
                        fontSize: 30,
                        fontWeight: FontWeight.w800)),
                //centerTitle: true,
                backgroundColor: Colors.white,
                actions: <Widget>[
                  Row(
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      CircleAvatar(
                        backgroundColor: Colors.black12,
                        maxRadius: 21.0,
                        child: IconButton(
                            icon: Icon(
                              Icons.add_rounded,
                              color: Colors.black,
                              size: 26,
                            ),
                            onPressed: () {
                              // do something
                            }),
                      ),
                      SizedBox(
                        width: 10,
                      ),
                      CircleAvatar(
                        backgroundColor: Colors.black12,
                        maxRadius: 21.0,
                        child: Center(
                          child: IconButton(
                              icon: Icon(
                                Icons.search_rounded,
                                color: Colors.black,
                                size: 26,
                              ),
                              onPressed: () {
                                // do something
                              }),
                        ),
                      ),
                      SizedBox(
                        width: 10,
                      ),
                      CircleAvatar(
                        backgroundColor: Colors.black12,
                        maxRadius: 21.0,
                        child: Center(
                          child: IconButton(
                              icon: ImageIcon(
                                AssetImage("assets/images/messenger-32.png"),
                                color: Colors.black,
                                size: 20,
                              ),
                              onPressed: () {}),
                        ),
                      ),
                      SizedBox(
                        width: 10,
                      ),
                    ],
                  )
                ],
                bottom: TabBar(
                  onTap: (int index) {
                    setState(() {
                      if (index == 0) {
                        showAppBar = true;
                      } else {
                        showAppBar = false;
                      }
                      pageIndex = index;
                    });
                  },
                  controller: controller,
                  unselectedLabelColor: Colors.black54,
                  labelColor: Colors.blueAccent,
                  tabs: const [
                    Tab(icon: Icon(Icons.home_outlined, size: 30)),
                    Tab(icon: Icon(Icons.ondemand_video, size: 30)),
                    Tab(icon: Icon(Icons.storefront, size: 30)),
                    Tab(icon: Icon(Icons.videogame_asset, size: 30)),
                    Tab(icon: Icon(Icons.notifications_outlined, size: 30)),
                    Tab(icon: Icon(Icons.menu, size: 30)),
                  ],
                ),
              )
            : // Hidden app bar
            AppBar(
                automaticallyImplyLeading: false, // removes default back button
                backgroundColor: Colors.white,
                title: TabBar(
                  onTap: (int index) {
                    setState(() {
                      if (index == 0) {
                        showAppBar = true;
                      } else {
                        showAppBar = false;
                      }
                      pageIndex = index;
                    });
                  },
                  controller: controller,
                  unselectedLabelColor: Colors.black54,
                  labelColor: Colors.blueAccent,
                  tabs: const [
                    Tab(icon: Icon(Icons.home_outlined, size: 30)),
                    Tab(icon: Icon(Icons.ondemand_video, size: 30)),
                    Tab(icon: Icon(Icons.storefront, size: 30)),
                    Tab(icon: Icon(Icons.videogame_asset, size: 30)),
                    Tab(icon: Icon(Icons.notifications_outlined, size: 30)),
                    Tab(icon: Icon(Icons.menu, size: 30)),
                  ],
                ),
              ),
        body: pages[pageIndex]);
  }
}
