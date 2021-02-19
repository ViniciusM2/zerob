#!/usr/bin/env python3

import cgitb
import cgi

from save_user import UserSchema

from datetime import date

import json

cgitb.enable()

schema = UserSchema()

form = cgi.FieldStorage()

nome = form.getvalue('nome')
data_nascimento = date.fromisoformat(form.getvalue('data_nascimento'))
email = form.getvalue('email')
idade = form.getvalue('idade')
peso = form.getvalue('peso')
altura = form.getvalue('altura')

dados_do_usuario = {
    'nome': nome,
    'data_nascimento': data_nascimento,
    'email': email,
    'idade': idade,
    'peso': peso,
    'altura': altura
}

dados_antigos = None

with open('data.json') as json_file:
    try:
        dados_antigos = json.load(json_file)
    except:
        print('does not have data')

with open('data.json', 'w') as outfile:
    if dados_antigos:
        dados_atualizados = [dados_do_usuario]
        if isinstance(dados_antigos, list):
            dados_atualizados = dados_atualizados + dados_antigos
        if isinstance(dados_antigos,dict):
            dados_atualizados = [dados_antigos, dados_do_usuario]
            
        outfile.write(json.dumps(schema.dump(dados_do_usuario, many=True)))
    else:
        outfile.write(json.dumps(schema.dump(dados_do_usuario)))

# with open('data.json', 'w') as outfile:
#     outfile.write(json.dumps(schema.dump(dados)))

print("Content-type:text/html\r\n\r\n")
print("""<html>
            <head>
                <meta charset=\"UTF-8\">
                <title>Título</title>
            </head>
            <body>""")

print("<h1>Confirmação de Dados</h1><hr>")
print('<div class="center">')
print('<h2> Esses são mesmo os seus dados?</h2>')
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
print("""<tr>
         <td>{}</td>
         <td>{}</td>
         <td>{}</td>
         <td>{}</td>
         <td>{}</td>
         <td>{}</td>
        </tr>""".format(nome, data_nascimento, email, idade, peso, altura))
print("</table>")
print("""
            <input type="submit" style="margin-top: 20px" value="confirmar"></input>
       """)
# print("""<form action="/cgi-bin/save_user.py" method="post">
#             <input type="submit" style="margin-top: 20px" value="confirmar"></input>
#         </form>""")
print('')
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
