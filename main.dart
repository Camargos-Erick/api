import 'package:web/web.dart' as web;
import 'dart:html';
void main() async{
  final input = web.document.querySelector('#url') as web.HTMLInputElement;
  final button = web.document.querySelector('#get');

 
 button?.onClick.listen((event)
 {
    final now = input.value;
    final api = Uri.parse('http://127.0.0.1:5000/download?url=$now');
    AnchorElement(href: api.toString())
    ..target = 'blank'
    ..download = ''
    ..click();    
  });
  
}
