from lib.user import User  # Import User correctly

class Student(User):  # Inherit from User
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # Call User constructor
        self.knowledge = []

    def learn(self, new_knowledge):
        self.knowledge.append(new_knowledge)


