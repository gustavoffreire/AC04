
# MYSQL_HOST = 'root'
# MYSQL_USER = 'cleriston'
# MYSQL_PASSWORD = 'mudar123'
# MYSQL_DB = 'pessoas'

from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        genero = request.form['genero']

        conn = mysql.connector.connect(user='cleriston', password='mudar123', host='172.17.0.0', database='db')
        cursor = conn.cursor()
        query = "INSERT INTO pessoas (nome, idade, genero) VALUES (%s, %s, %s)"
        values = (nome, idade, genero)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

    return render_template('gravar.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

