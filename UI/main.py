from flask import Flask, flash, render_template, request, redirect, url_for
import sqlite3 
import sys

app = Flask(__name__)
app.secret_key = 'abcd'

USER_NAME="qw"
@app.route('/',methods=['GET','POST'])
def first_page():    
    db = sqlite3.connect("DB.db")
    db.row_factory = sqlite3.Row
    query = db.execute("SELECT * FROM eyes").fetchall()
    db.close()
    return render_template('test.html',datas=query)


if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
