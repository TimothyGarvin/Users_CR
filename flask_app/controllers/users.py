
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.users import Users


@app.route('/')
def index():
    users = Users.read_all()
    return render_template("read_all.html",users=users)

@app.route('/user/new')
def create_new():
    return render_template('create.html')

@app.route('/create', methods = ['POST'])
def create():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }
    Users.create(data)
    return redirect('/')

@app.route('/user/show/<int:id>')
def show_one(id):
    data={
        "id":id
    }
    return render_template("show.html",user=Users.show_one(data))

@app.route('/user/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit.html",user=Users.show_one(data))

@app.route('/edit',methods=['POST'])
def update():
    Users.edit(request.form)
    return redirect('/')

@app.route('/user/delete/<int:id>')
def delete(id):
    data ={
        'id': id
    }
    Users.delete(data)
    return redirect('/')