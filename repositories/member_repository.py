from db.run_sql import run_sql
from models.fitness_class import Fitness_Class
from models.instructor import Instructor
from models.member import Member
from models.booking import Booking

import repositories.fitness_class_repository as fitness_class_repository
import repositories.instructor_repository as instructor_repository
import repositories.booking_repository as booking_repository


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM members WHERE id =%s"
    values = [id]
    run_sql(sql, values)

def save(member):
    sql = "INSERT INTO members (name, gender, age) VALUES (%s, %s, %s) RETURNING id"
    values = [member.name, member.gender, member.age]
    results = run_sql(sql, values)
    id = results[0]["id"]
    member.id = id

def select(id):
    member = None 
    sql = "SELECT * FROM members WHERE id= %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        member = Member(result["name"], result["gender"], result["age"], result["id"])
    return member 

def select_all():
    members = []
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for result in results:
        member = Member(result["name"], result["gender"], result["age"], result["id"])
        members.append(member)
    return members

def update(member):
    sql = "UPDATE members SET (name, gender, age) = (%s, %s, %s) WHERE id = %s "
    values = [member.name, member.gender, member.age, member.id]
    run_sql(sql, values)



