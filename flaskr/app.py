# from datetime import datetime
# from flask import Flask, render_template, url_for, request, redirect
# from flask_sqlalchemy import SQLAlchemy
# from bs4 import BeautifulSoup as bs
# import requests
# from __init__ import db, create_app

# app = create_app()

# @app.route('/', methods=['POST', 'GET'])
# def index():
#     if request.method == 'POST':
#         task_content = request.form['content']
#         new_task = Todo(content=task_content)
#         # try:
#         db.session.add(new_task)
#         db.session.commit()
#         return redirect('/')
#         # except:
#         #     return('failure')

#     else:
#         tasks = Todo.query.order_by(Todo.date_created).all()
#         return render_template('index.html', tasks=tasks)


# if __name__ == '__main__':
#     app.run(debug=True)