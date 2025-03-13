from os import name
from flask import render_template, flash, redirect, jsonify
from WebApp import app, db
from WebApp.forms.subscriptionForm import SubscriptionForm
from .models import Course, Student


test_courses = [
        {'id': 1, "code" : "VEMISAB254ZF", 'name': 'Python programozas',   'students': [ 
                                                                    { "neptun" : "JJJJJJ", "name" : "John"},
                                                                    { "neptun" : "RRRRRR", "name" : "Robert"},
                                                                    { "neptun" : "MMMMMM", "name" : "Mary"}
                                                                ]},
        {'id': 2, "code" : "VEMISAB146AP",'name': 'Programozas alapjai',  'students': [ 
                                                                    { "neptun" : "KKKKKK", "name" : "Kevin"},
                                                                    { "neptun" : "WWWWWW", "name" : "William"},
                                                                    { "neptun" : "TTTTTT", "name" : "Thomas"}
                                                                ]},
        {'id': 3, "code" : "VEMISAB156GF",'name': 'Programozas I.',       'students': [
                                                                    { "neptun" : "BBBBBB", "name" : "Bob"}
                                                                ]} 
    ]


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", name="Moodle Lite", page = "index", cnt = len(test_courses))



@app.route('/courses')
def listItems():  
    ### Write your solution here!
    courses= Course.query.all()
    return render_template("courses.html", name="Moodle Lite", courses=courses, page = "courses" )

    ###
    # return render_template("courses.html", name="Moodle Lite", courses=test_courses, page = "courses" )
    

@app.route('/subscription', methods=["GET", "POST"])
def order():
    ### Write your solution here!
    form = SubscriptionForm()
    if form.validate_on_submit():
        result = db.session.query(Course).filter(Course.code == form.coursecode.data)      

        if list(result):
            students = { "neptun" : form.neptun.data, "name" : form.name.data}
            db.session.add(Course(name = form.name.data, code = form.coursecode.data, students = students ))
            db.session.commit()

            flash('You have successfully subscribed!')

            return redirect('/index')
        else:
            flash("{} not found! Check the list!".format(form.coursecode.data))
            return redirect("/courses")
    ##
    return render_template('subscription.html', name='Moodle Lite', form = form ,page="subscription")



### Write your solution here!
@app.route('/students/<coursecode>', methods=["GET"])
def students(coursecode):
    result = db.session.query(Course).filter(Course.code == str(coursecode))
    if list(result):
        student_list = list(list(result)[0].students)
        return [student.jsonify for student in student_list]
    else:
        return {}
###