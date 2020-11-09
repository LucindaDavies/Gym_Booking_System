  
from flask import Blueprint, Flask, redirect, render_template, request

from models.fitness_class import Fitness_class
import repositories.instructor_repository as instructor_repository
import repositories.member_repository as member_repository
import repositories.fitness_class_repository as fitness_class_repository

fitness_classes_blueprint = Blueprint("fitness_classes", __name__)