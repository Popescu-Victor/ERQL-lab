import pandas as pd
import pickle
# Creating a one-to-many relationship between teacher and students at the begining of a course for further reference.


class Teacher2Student():
    def __init__(self, teacher_name):
        self.teacher_name = teacher_name
        self.students = []

    def add_student(self, student_name):
        self.students.append(student_name)

    def get_students(self):
        return self.students

    def save_to_file(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load_from_file(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
