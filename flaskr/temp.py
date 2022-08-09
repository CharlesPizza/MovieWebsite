from datetime import datetime
from flask import (Blueprint, flash, g, redirect, render_template, request,
    url_for)
from flask_sqlalchemy import SQLAlchemy
from flaskr.db import get_db
from bs4 import BeautifulSoup as bs
import requests

bp = Blueprint('test', __name__, url_prefix = '/test')

@bp.route('/testing', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # task_content = request.form['content']
        # new_task = Todo(content=task_content)
        # try:
        # db.session.add(new_task)
        # db.session.commit()
        return redirect('/')
        # except:
        #     return('failure')

    else:
        # tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html')#tasks=tasks)
