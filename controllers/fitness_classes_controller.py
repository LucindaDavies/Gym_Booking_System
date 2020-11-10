  
import pdb
from flask import Blueprint, Flask, redirect, render_template, request

from models.fitness_class import Fitness_Class
import repositories.instructor_repository as instructor_repository
import repositories.member_repository as member_repository
import repositories.fitness_class_repository as fitness_class_repository
import repositories.booking_repository as booking_repository
import datetime

fitness_classes_blueprint = Blueprint("fitness_classes", __name__)


def date_from_string(date, time):
        # date_as_list = date.split("-")
        # year = int(date_as_list[0]))
        # month = int(date_as_list[1])
        # day = int(date_as_list[2])

        # time_as_list = time.split(":")
        # hour = int(time_as_list[0])
        # minutes = int(time_as_list[1])

    return f"{date} {time}"
        # return "2020-06-22 19:10:00"

@fitness_classes_blueprint.route("/fitness_classes")
def fitness_classes():
    fitness_classes = fitness_class_repository.select_all()
    return render_template("fitness_classes/index.html", fitness_classes=fitness_classes)

@fitness_classes_blueprint.route("/fitness_classes/new")
def new_fitness_class():
    instructors = instructor_repository.select_all()
    return render_template("/fitness_classes/new.html", instructors=instructors)

@fitness_classes_blueprint.route("/fitness_classes", methods=["POST"])
def create_fitness_class():
    name = request.form["name"]
    start_date = request.form["start_date"]
    end_date = request.form["end_date"]
    start_time = request.form["start_time"]
    end_time = request.form["end_time"]
    class_type = request.form["class_type"]
    instructor_id = request.form["instructor"]
    instructor = instructor_repository.select(instructor_id)
    new_fitness_class = Fitness_Class(name, f"{start_date} {start_time}", f"{end_date} {end_time}", class_type, instructor)
    fitness_class_repository.save(new_fitness_class)
    return redirect("/fitness_classes")


@fitness_classes_blueprint.route("/fitness_classes/<id>/delete", methods=["POST"])
def delete_fitness_class(id):
    fitness_class_repository.delete(id)
    return redirect("/fitness_classes")

  


