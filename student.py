students = {}

def add_student(roll, name):
    students[roll] = name

def remove_student(roll):
    if roll in students:
        del students[roll]

def search_student(roll):
    return students.get(roll)

def update_student(roll, name):
    if roll in students:
        students[roll] = name