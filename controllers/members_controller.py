from flask import Blueprint, Flask, redirect, render_template, request

from models.member import Member
import repositories.instructor_repository as instructor_repository
import repositories.member_repository as member_repository
import repositories.fitness_class_repository as fitness_class_repository
import repositories.booking_repository as booking_repository


members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)

@members_blueprint.route("/members/new")
def new_members():
    return render_template("/members/new.html")

@members_blueprint.route("/members", methods=["POST"])
def create_member():
    name = request.form["name"]
    gender = request.form["gender"]
    age = request.form["age"]
    new_member = Member(name, gender, age)
    member_repository.save(new_member)
    return redirect("/members")

@members_blueprint.route("/members/<id>/delete", methods=["POST"])
def delete_member(id):
    member_repository.delete(id)
    return redirect("/members")

@members_blueprint.route("/members/<id>/edit", methods = ["GET"])
def edit_member(id):
    member = member_repository.select(id)
    return render_template("/members/edit.html", member=member)

@members_blueprint.route("/members/<id>", methods = ["POST"])
def update_member(id):
    name = request.form["name"]
    gender = request.form["gender"]
    age = request.form["age"]
    member = Member(name, gender, age, id)
    member_repository.update(member)
    return redirect("/members")

