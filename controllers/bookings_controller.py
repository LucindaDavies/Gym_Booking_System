import pdb
from flask import Blueprint, Flask, redirect, render_template, request

from models.booking import Booking
import repositories.instructor_repository as instructor_repository
import repositories.member_repository as member_repository
import repositories.fitness_class_repository as fitness_class_repository
import repositories.booking_repository as booking_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings=bookings)

@bookings_blueprint.route("/bookings/<id>/delete", methods=["POST"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")

@bookings_blueprint.route("/bookings/new")
def new_bookings():
    members = member_repository.select_all()
    fitness_classes = fitness_class_repository.select_all()
    return render_template("/bookings/new.html", members=members, fitness_classes=fitness_classes)

@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
    member_id = request.form["member_id"]
    fitness_class_id = request.form["fitness_class_id"]
    member = member_repository.select(member_id)
    fitness_class = fitness_class_repository.select(fitness_class_id)
    new_booking = Booking(member, fitness_class)
    booking_repository.save(new_booking)
    return redirect("/bookings")

@bookings_blueprint.route("/bookings/<id>/edit", methods = ["GET"])
def edit_booking(id):
    booking = booking_repository.select(id)
    members = member_repository.select_all()
    fitness_classes = fitness_class_repository.select_all()
    return render_template('bookings/edit.html', booking=booking, members=members, fitness_classes=fitness_classes)

@bookings_blueprint.route("/bookings/<id>", methods=["POST"])
def update_booking(id):
    member_id = request.form["member_id"]
    fitness_class_id = request.form["fitness_class_id"]
    member = member_repository.select(member_id)
    fitness_class = fitness_class_repository.select(fitness_class_id)
    booking = Booking(member, fitness_class, id)
    booking_repository.update(booking)
    return redirect("/bookings")




