import pdb
from db.run_sql import run_sql
from models.fitness_class import Fitness_Class
from models.instructor import Instructor
from models.member import Member
from models.booking import Booking


import repositories.member_repository as member_repository
import repositories.instructor_repository as instructor_repository
import repositories.booking_repository as booking_repository

def delete_all():
    sql = "DELETE FROM fitness_classes"
    run_sql(sql)

def save(fitness_class):
    sql = "INSERT INTO fitness_classes (name, start_time, end_time, class_type, instructor_id) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [fitness_class.name, fitness_class.start_time, fitness_class.end_time, fitness_class.class_type, fitness_class.instructor.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    fitness_class.id = id

def select_all():
    fitness_classes = []
    sql = "SELECT * FROM fitness_classes"
    results = run_sql(sql)
    for result in results:
        fitness_class = Fitness_Class(result["name"], result['start_time'], result['end_time'], result['class_type'], result['instructor_id'], result['id'])
        fitness_classes.append(fitness_class)
    return fitness_classes

def select(id):
    fitness_class = None 
    sql = "SELECT * FROM fitness_classes WHERE id= %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        fitness_class = Fitness_Class(result["name"], result ['start_time'], result['end_time'], result['class_type'], result['instructor_id'], result['id'] )
    return fitness_class 

def update(fitness_class):
    sql = "UPDATE fitness_classes SET (name, start_time, end_time, class_type, instructor_id) = (%s, %s, %s, %s, %s) WHERE id = %s "
    values = [fitness_class.name, fitness_class.start_time, fitness_class.end_time, fitness_class.class_type, fitness_class.instructor.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM fitness_classes WHERE id =%s"
    values = [id]
    run_sql(sql, values)

def select_upcoming():
    fitness_classes = []
    sql = "SELECT * FROM fitness_classes WHERE start_time >= NOW() "
    results = run_sql(sql)
    for result in results:
        fitness_class = Fitness_Class(result["name"], result['start_time'], result['end_time'], result['class_type'], result['instructor_id'], result['id'])
        fitness_classes.append(fitness_class)
    return fitness_classes

def members(fitness_class):
    members = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE fitness_class_id = %s"
    values = [fitness_class.id]
    results = run_sql(sql, values)
    for row in results:
        member = Member(row["name"], row["gender"], row["age"], row["id"])
        members.append(member)
    return members