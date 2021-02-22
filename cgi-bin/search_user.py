#!/usr/bin/env python3

import cgitb
import cgi

from schema import UserSchema

from datetime import date
import os.path


import json

cgitb.enable()

schema = UserSchema()

form = cgi.FieldStorage()

nome = form.getvalue('nome')

users = None
filtered_users = None

if os.path.exists('data.json'):
    with open('data.json') as json_file:
        try:
            data = json.load(json_file)
            if isinstance(data, dict):
                users = [data]
            elif isinstance(data, list):
                users = data
            filtered_users = filter(lambda user: user['nome'] == nome, users)
        except:
            print('does not have data')

if(filtered_users):

    print("Content-type:text/html\r\n\r\n")
    print("""<html>
                <head>
                    <meta charset=\"UTF-8\">
                    <title>Título</title>
                </head>
                <body>""")
    print('<div class="center">')

    print("</table>")
    print('<table border=1>')
    print("""
            <tr>
            <th>Nome</th>
            <th>Data de Nascimento</th>
            <th>Email</th>
            <th>Idade</th>
            <th>Peso</th>
            <th>Altura</th>
            </tr>""")
    for user in filtered_users:
        print("""<tr>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            </tr>""".format(user['nome'], user['data_nascimento'], user['email'], user['idade'], user['peso'], user['altura']))

    print('</div>')

    print("</table>")
    print('<a style="margin-top: 5vh" href="../index.html">Ir para menu principal</a>')
    print('</div>')

    # print(form.keys())
    # print(form.value)

    print("</body></html>")

    # estilos

    print("""
        <style>
        .texto {
            color: mediumblue;
            box-shadow: midnightblue;
            /* text-align: center; */
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .center {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        </style>
        """)
