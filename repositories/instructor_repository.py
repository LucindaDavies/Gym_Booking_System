from db.run_sql import run_sql
from models.fitness_class import Fitness_Class
from models.instructor import Instructor
from models.member import Member
from models.booking import Booking

import repositories.fitness_class_repository as fitness_class_repository
import repositories.member_repository as member_repository
import repositories.booking_repository as booking_repository



def delete_all():
    sql = "DELETE FROM instructors"
    run_sql(sql)

def save(instructor):
    sql = "INSERT INTO instructors (name) VALUES (%s) RETURNING id"
    values = [instructor.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    instructor.id = id

def select_all():
    instructors = []
    sql = "SELECT * FROM instructors"
    results = run_sql(sql)
    for result in results:
        instructor = Instructor(result["name"], result['id'])
        instructors.append(instructor)
    return instructors

def update(instructor):
    sql = "UPDATE instructors SET (name) = (%s) WHERE id = %s "
    values = [instructor.name]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM instructors WHERE id =%s"
    values = [id]
    run_sql(sql, values)

def select(id):
    instructor = None 
    sql = "SELECT * FROM instructors WHERE id= %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        instructor = Instructor(result["name"], result['id'])
    return instructor 