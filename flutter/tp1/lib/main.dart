import 'dart:ffi';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(Root());
}

class Root extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return MaterialApp(
      home: MyApp(),
    );
  }
}
class MyApp extends StatefulWidget {
  
  @override
  State<MyApp> createState() => Home();
  
}

class Home extends State<MyApp> {
 
 @override
  Widget build(BuildContext context) {
      return Scaffold(
        appBar: AppBar(
          title: const Text('TP1 App'),
          backgroundColor: Colors.purpleAccent,
        ),
        body: const Center(child:  
          TextField(
            decoration: InputDecoration(labelText: "Montant"),
            )
        ),
      );
  }

}