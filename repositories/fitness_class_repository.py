from db.run_sql import run_sql
from models.fitness_class import Fitness_Class
from models.instructor import Instructor
from models.member import Member

import repositories.member_repository as member_repository
import repositories.instructor_repository as instructor_repository

def delete_all():
    sql = "DELETE FROM fitness_classes"
    run_sql(sql)

def save(fitness_class):
    sql = "INSERT INTO fitness_class (name, class_time, duration, class_type) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [fitness_class.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    fitness_class.id = id