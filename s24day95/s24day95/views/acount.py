from flask import Blueprint,render_template

ac = Blueprint('ac',__name__)


@ac.route('/login')
def login():
    return render_template('acount/login.html')





@ac.route('/register')
def register():
    return render_template('acount/register.html')