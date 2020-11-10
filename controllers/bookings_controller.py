import pdb
from flask import Blueprint, Flask, redirect, render_template, request

from models.booking import Booking
import repositories.instructor_repository as instructor_repository
import repositories.member_repository as member_repository
import repositories.fitness_class_repository as fitness_class_repository