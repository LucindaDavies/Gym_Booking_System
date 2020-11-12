import pdb
import datetime

from models.instructor import Instructor
import repositories.instructor_repository as instructor_repository

from models.member import Member
import repositories.member_repository as member_repository

from models.fitness_class import Fitness_Class
import repositories.fitness_class_repository as fitness_class_repository

from models.booking import Booking
import repositories.booking_repository as booking_repository

fitness_class_repository.delete_all()
instructor_repository.delete_all()
member_repository.delete_all()

# INSTRUCTORS

instructor1 = Instructor("Harvey")
instructor_repository.save(instructor1)

all_instructors = instructor_repository.select_all()
print(all_instructors)

# MEMBERS

member1 = Member("Harry", "male", 30)
member_repository.save(member1)

member2 = Member("Olivia", "female", 22)
member_repository.save(member2)

member3 = Member("Lizzie", "female", 45)
member_repository.save(member3)


all_members = member_repository.select_all()
print(all_members)

# FITNESS_CLASSES

fitness_class1 = Fitness_Class("Grit", datetime.datetime(2020, 11, 13, 6, 0), datetime.datetime(2020, 11, 13, 7, 0), "high intensity cardio", instructor1)
fitness_class_repository.save(fitness_class1)

# fitness_class2 = Fitness_Class("spin", "9am", "60 mins", "cardio")
# fitness_class_repository.save(fitness_class2)

# fitness_class3 = Fitness_Class("pump", "8pm", "30 mins", "cardio weight")
# fitness_class_repository.save(fitness_class3)

booking1 = Booking(member1, fitness_class1)
booking_repository.save(booking1)

booking2 = Booking(member3, fitness_class1)
booking_repository.save(booking2)