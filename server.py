from flask import Flask, request, render_template, redirect, session, flash
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)
mysql = MySQLConnector(app, 'books')
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():
    books = mysql.query_db("select id, title, author, date_added from books")
    return render_template('index.html', books=books)

@app.route('/add', methods=["POST"])
def add():
    query = "insert into books (title, author, date_added) values (:title, :author, now())"
    print query
    result = mysql.query_db(query, request.form)
    print result
    return redirect('/')

@app.route('/delete/<bookid>')
def delete(bookid):
    query = "DELETE FROM books WHERE id=:id"
    data = {'id': bookid}
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/show/<bookid>')
def show(bookid):
    print 'here'
    query = "select id, title, author, date_added from books where id=:id"
    data = {
        'id': bookid
    }
    book=mysql.query_db(query, data)[0]
    return render_template('show.html', book=book)

@app.route('/update/<bookid>', methods=['POST'])
def update(bookid):
    query = "UPDATE books SET title = :title, author = :author WHERE id = :id"
    data = {
             'title': request.form['title'],
             'author':  request.form['author'],
             'id': bookid
           }
    changes=mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)
