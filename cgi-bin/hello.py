#!/usr/bin/env python3

import cgitb, cgi
cgitb.enable(display=0, logdir="./")

form = cgi.FieldStorage()

nome = form.getvalue('nome')

print("Content-type:text/html\r\n\r\n")
print('Hello, ',nome)