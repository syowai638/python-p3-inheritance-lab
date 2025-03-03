from lib.teacher import Teacher
from lib.user import User

class TestTeacher:
    '''Class "Teacher" in teacher.py'''

    def test_is_subclass(self):
        '''is a subclass of "User".'''
        assert issubclass(Teacher, User)

    def test_initializes_with_names(self):
        '''initializes with first and last name.'''
        my_teacher = Teacher("My", "Teacher")
        assert (my_teacher.first_name, my_teacher.last_name) == ("My", "Teacher")

    def test_has_attribute_knowledge(self):
        '''has an attribute called "knowledge", a list with len > 0.'''
        my_teacher = Teacher("My", "Teacher")
        assert isinstance(my_teacher.knowledge, list) and len(my_teacher.knowledge) > 0

    def test_can_teach(self):
        '''teaches from list of knowledge.'''
        my_teacher = Teacher("My", "Teacher")
        assert my_teacher.teach() in my_teacher.knowledge
