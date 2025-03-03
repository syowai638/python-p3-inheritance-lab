from lib.student import Student
from lib.user import User

class TestStudent:
    '''Class "Student" in student.py'''

    def test_is_subclass(self):
        '''is a subclass of "User".'''
        assert issubclass(Student, User)

    def test_initializes_with_names(self):
        '''initializes with first and last name.'''
        my_student = Student("My", "Student")
        assert (my_student.first_name, my_student.last_name) == ("My", "Student")

    def test_initializes_with_knowledge(self):
        '''initializes with empty list attribute "knowledge".'''
        my_student = Student("My", "Student")
        assert hasattr(my_student, "knowledge") and isinstance(my_student.knowledge, list) and len(my_student.knowledge) == 0

    def test_can_learn(self):
       '''learns from a string and adds to self.knowledge.'''

