#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        # Inherit first_name and last_name from User
        super().__init__(first_name, last_name)
        # Initialize knowledge as an empty list
        self.knowledge = []

    def learn(self, new_knowledge):
        # Add new knowledge to the list
        self.knowledge.append(new_knowledge)
