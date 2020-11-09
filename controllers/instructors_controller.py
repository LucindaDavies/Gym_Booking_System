from flask import Blueprint, Flask, redirect, render_template, request

from models.instructor import Instructor
import repositories.instructor_repository as instructor_repository
import repositories.member_repository as member_repository
import repositories.fitness_class_repository as fitness_class_repository

instructors_blueprint = Blueprint("instructors", __name__)

@instructors_blueprint.route("/instructors")
def instructors():
    instructors = instructor_repository.select_all()
    return render_template("instructors/index.html", instructors=instructors)

@instructors_blueprint.route("/instructors/new")
def new_instructor():
    return render_template("/instructors/new.html")

@instructors_blueprint.route("/instructors", methods=["POST"])
def create_instructor():
    name = request.form["name"]
    new_instructor = Instructor(name)
    instructor_repository.save(new_instructor)
    return redirect("/instructors")

@instructors_blueprint.route("/instructors/<id>/delete", methods=["POST"])
def delete_instructor(id):
    instructor_repository.delete(id)
    return redirect("/instructors")

@instructors_blueprint.route("/instructors/<id>/edit", methods = ["GET"])
def edit_instructor(id):
    instructor = instructor_repository.select(id)
    return render_template("/instructors/edit.html", instructor=instructor)

@instructors_blueprint.route("/instructors/<id>", methods = ["POST"])
def update_instructor(id):
    name = request.form["name"]
    instructor = Instructor(name)
    instructor_repository.update(instructor)
    return redirect("/instructors")
