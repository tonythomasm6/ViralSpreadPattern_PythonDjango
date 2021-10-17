"""
Created by: Tony Thomas Manthuruthil
Student ID: 31296149
Assignment 2 - Task1
Start Date: 22-Mau-2020
Last updated Date : 6-June-2020
Description: This program loads all person and their friend from the input file a2_sample_set.txt

"""


class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.friends = []

    # Method to add the list of friends of a person
    def add_friend(self, friend):
        self.friends.append(friend)

    # To get name of the person
    def get_name(self):
        name = self.first_name + " " + self.last_name
        return name

    # To get the list of all friends of person
    def get_friends(self):
        return self.friends

    def __str__(self):
        p = self.first_name + " " + self.last_name
        return p


# Method to check if a Person object is already created for one Person or friend. If already present, it is returned
# If not present None returned
def check_existing_person(list_person, name):
    for person in list_person:
        friends_of_person = person.get_friends()  #
        if person.get_name() == name:  # Checking if the person is already created
            return person
        else:
            for friend in friends_of_person:  # Checking if person is already created as a friend
                if friend.get_name() == name:
                    return friend
    return None


# Method to load all persons from the list. Returns the list of fall persons in the input file
def load_people():
    file = open("ViralSpreadPattern/a2_sample_set.txt", "r")  # To get all person and their friends from a2_sample_set.txt file
    person_list = []  # List of all person objects
    for i in range(200):  # Total 200 entries in the list
        row = file.readline().strip()  # To get all record for each person
        row_split = row.split(": ")  # To split between the person and his friends
        person_name = row_split[0]  # Getting the name of person
        # Creating person object
        person_name_split = person_name.split(" ")  # Splitting the person name to first and last name
        p = check_existing_person(person_list, person_name)  # Returns Person object with name person_name if exists

        if p is None:  # Person object with name person_name already not present
            p = Person(person_name_split[0],
                       person_name_split[1])  # Creating person object with input args as first and last name

        # Creating friend object
        friends_list = row_split[1].split(", ")  # Getting the list of all friends
        for friend_name in friends_list:  # Iterating through every friends of a person
            friend_name_split = friend_name.split(" ")  # Splitting name into first and last name
            f = check_existing_person(person_list, friend_name)  # Returns Person object with name friend_name if exists
            if f is None:  # Person object with name friend_name already not present
                f = Person(friend_name_split[0], friend_name_split[1])  # Creating a person object for friend
            p.add_friend(f)  # Adding the friend for the person
        person_list.append(p)  # Adding the person to the person list
    file.close()  # Closing file after reading all data
    return person_list


if __name__ == '__main__':
    persons_list = load_people()
    for person in persons_list:
        print(person.get_name())
        friends = person.get_friends()
        for friend_person in friends:
            print(" -- ", friend_person.get_name())


