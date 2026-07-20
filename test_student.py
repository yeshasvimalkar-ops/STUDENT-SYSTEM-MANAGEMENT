from student import *

def setup_function():
    students.clear()

def test_add1():
    add_student(1,"Rahul")
    assert students[1]=="Rahul"

def test_add2():
    add_student(2,"Aman")
    assert search_student(2)=="Aman"

def test_remove():
    add_student(1,"Rahul")
    remove_student(1)
    assert search_student(1)==None

def test_search():
    add_student(3,"Riya")
    assert search_student(3)=="Riya"

def test_update():
    add_student(1,"Rahul")
    update_student(1,"Raj")
    assert search_student(1)=="Raj"

def test_not_found():
    assert search_student(10)==None

def test_remove_missing():
    remove_student(20)
    assert True

def test_update_missing():
    update_student(5,"ABC")
    assert search_student(5)==None

def test_multiple():
    add_student(1,"A")
    add_student(2,"B")
    assert len(students)==2

def test_dictionary():
    assert isinstance(students,dict)