
from db.run_sql import run_sql
from models.instructor import Instructor
from models.member import Member
from models.fitness_class import Fitness_Class
from models.booking import Booking

import repositories.fitness_class_repository as fitness_class_repository
import repositories.instructor_repository as instructor_repository
import repositories.member_repository as member_repository

def delete_all():
    sql = "DELETE from bookings"
    run_sql(sql)

def delete(id):
     sql = "DELETE FROM bookings WHERE id =%s"
     values = [id]
     run_sql(sql, values)

def select(id):
    booking = None
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        member = member_repository.select(result["member_id"])
        fitness_class = fitness_class_repository.select(result["fitness_class_id"])
        booking = Booking(member, fitness_class, result["id"])
    return booking 


def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for result in results: 
        member = member_repository.select(result["member_id"])
        fitness_class = fitness_class_repository.select(result["fitness_class_id"])
        booking = Booking(member, fitness_class, result["id"])
        bookings.append(booking)
    return bookings

def save(booking):
    sql = "INSERT INTO bookings (member_id, fitness_class_id) VALUES (%s,%s) returning *"
    values = [booking.member.id, booking.fitness_class.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    booking.id = id
    return booking



