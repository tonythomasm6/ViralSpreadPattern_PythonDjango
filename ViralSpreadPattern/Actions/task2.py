"""
Created by: Tony Thomas Manthuruthil
Student ID: 31296149
Assignment 2 - Task2
Start Date: 22-Mau-2020
Last updated Date : 6-June-2020
Description: This program loads all person and their friend from the input file a2_sample_set.txt.
             Then it will simulate the daily spreading pattern based on meeting probability.

"""
import numpy as np
from ..Actions.task1 import *


#  Patient class which inherits Person class from Task 1
class Patient(Person):
    def __init__(self, first_name, last_name, health):
        self.first_name = first_name
        self.last_name = last_name
        self.friends = []
        self.health = float(health)  # Health of each employee

    # To get current Health Point of the patient
    def get_health(self):
        return self.health

    # To set health of patient to new input value
    def set_health(self, new_health):
        self.health = float(new_health)

    # check to see if patient is contagious
    def is_contagious(self):
        if self.health < 50:
            return True
        else:
            return False

    #  This infect method changes health point of patient based on current health and viral load
    def infect(self, viral_load):
        if self.health <= 29:
            self.health = round((self.health - (0.1 * viral_load)), 2)
        elif 29 < self.health < 50:
            self.health = round((self.health - (1 * viral_load)), 2)
        elif self.health >= 50:
            self.health = round((self.health - (2 * viral_load)), 2)
        if self.health < 0:  # Minimum health is 0
            self.health = 0

    # Sleep method increase patient health by 5 every night
    def sleep(self):
        self.health += 5  # On sleeping health increase by 5
        if self.health > 100:  # Maximum health is 100
            self.health = 100
        return self.health

    def __str__(self):
        p = self.first_name + " " + self.last_name + " " + str(self.health)
        return p


# Method which sleeps everyone at end of day
# Method to check if a person has already slept. To avoid sleep for a person twice in same day
# Ensures that sleep function is called for a patient or friend only once for a day
def sleep_patients(patient_list):
    slept_patient_list = []  # List containing patients who already slept for a day
    for patient in patient_list:
        if patient.get_name() not in slept_patient_list:  # Checking to see if patient already slept
            patient.sleep()  # If not already handled, then calling sleep function
            slept_patient_list.append(patient.get_name())  # Adding it to list to avoid sleep again

        friends_list = patient.get_friends()
        for friend in friends_list:  # iterating through every friend to see if slept
            if friend.get_name() not in slept_patient_list:
                friend.sleep()
                slept_patient_list.append(friend.get_name())  # Adding friends name to list of slept persons


#  Method to get total contagious patient count for a day
#  Also ensures that same patient is not added twice.
def get_daily_contagious_count(patient_list):
    counted_list = []
    count = 0
    for patient in patient_list:
        if patient.get_name() not in counted_list:  # If patient is not in counted list, then its counted
            if patient.is_contagious():
                count += 1
                counted_list.append(patient.get_name())  # Added to list of counted patient
        friends_list = patient.get_friends()  # Handling for friends
        for friend in friends_list:
            if friend.get_name() not in counted_list:  # If friend is not in counted list, then its counted
                if friend.is_contagious():
                    count += 1
                    counted_list.append(friend.get_name())  # Added to list of counted patient
    return count  # Returning total count of contagious patient for the day


#  Method to run disease spread simulation. Returns the contagious patient count per day for input number of days
def run_simulation(days, meeting_probability, patient_zero_health):
    default_health = patient_zero_health
    patients_list = load_patients(default_health)  # Method to load all patient and friends with default health input

    patient_health = patient_zero_health  # Health of patient one.
    daily_contag_count_list = []  # Initializing array for storing contagious person count for each day

    # Setting health for everyone in list
    for patient in patients_list:
        patient.set_health(patient_health)  # Health of first patient is patient_zero_health
        patient_health = 75  # After first patient, everyone have 75 health

    # Iterating through everyday of number of input days
    for i in range(days):
        for patient in patients_list:  # Iterating through every patient in list

            friends_list = patient.get_friends()  # List of all friends of the patient

            for friend in friends_list:  # Iterating through every friend of a particular person
                # random.choice is used to calculate the probability. 'True' will happen with probability of
                # meeting_probability and 'False' on (1- meeting_probability) . Reference url :
                # https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.random.choice.html
                # retrieved on : 23-May2020
                meet_friend = np.random.choice([True, False], 1, p=[meeting_probability, 1 - meeting_probability])
                if meet_friend:
                    viral_load = 0  # Initializing viral load of patient
                    if patient.is_contagious():  # Check if patient is already contagious
                        viral_load = 5 + (((patient.get_health() - 25) ** 2) / 62)  # Calculation of viral load

                    friend_viral_load = 0  # Initializing viral load for friend
                    if friend.is_contagious():  # Check if friend is already contagious
                        friend_viral_load = (5 + ((friend.get_health() - 25) ** 2) / 62)  # Calculation of
                        # viral_load for friend

                    friend.infect(viral_load)  # infecting friend with patients viral load
                    patient.infect(friend_viral_load)  # If friend was also contagious, then patients health is
                    # also affected

        daily_count = get_daily_contagious_count(patients_list)  # Method to get daily count of contagious patients
        daily_contag_count_list.append(daily_count)  # Appending daily count to list for input number of days
        # Seep at the end of day
        sleep_patients(patients_list)  # method to handle health on sleep at end of day

    return daily_contag_count_list


#  Method to load patients from the input file. Returns list of all patient and friend with default_health
def load_patients(default_health):
    file = open("ViralSpreadPattern/a2_sample_set.txt", "r")  # To get all patient and their friends from a2_sample_set.txt file
    patient_list = []  # List of all patient objects

    for i in range(200):  # Total 200 entries in the list
        row = file.readline().strip()  # To get all record for each patient
        row_split = row.split(": ")  # To split between the patient and his friends
        patient_name = row_split[0]  # Getting the name of patient
        # Creating patient object patient
        patient_name_split = patient_name.split(" ")  # Splitting the patient name to first and last name
        p = check_existing_person(patient_list, patient_name)  # Returns patient object with name patient_name if
        # exists. Method inherited from task 11

        if p is None:  # patient object with name patient_name already not present
            p = Patient(patient_name_split[0],
                        patient_name_split[1],
                        default_health)  # Creating patient object with input args as first and last name

        # Creating friend object
        friends_list = row_split[1].split(", ")  # Getting the list of all friends
        for friend_name in friends_list:  # Iterating through every friends of a patient
            friend_name_split = friend_name.split(" ")  # Splitting name into first and last name
            f = check_existing_person(patient_list, friend_name)  # Returns patient object with name friend_name if
            # exists. Method inherited from task 1
            if f is None:  # Patient object with name friend_name already not present
                f = Patient(friend_name_split[0], friend_name_split[1],
                            default_health)  # Creating a patient object for friend
            p.add_friend(f)  # Adding the friend for the patient
            p.set_health(default_health)
        patient_list.append(p)  # Adding the patient to the patient list
    file.close()

    return patient_list


if __name__ == '__main__':

    # for patient in patients_list:
    #     # print("-------Patient name == ", patient.get_name(), " HP =", patient.get_health())
    #     friends_list = patient.get_friends()
    #     for friend in friends_list:
    #         # print(" ************Friends == ", friend.get_name(), " hp =", friend.get_health())
    #         pass

    # test_result = run_simulation(15, 0.2, 49)
    # print("15, 0.2, 49 ", test_result)
    # test_result = run_simulation(15, 0.4, 49)
    # print("15, 0.4, 49" , test_result)
    # test_result = run_simulation(15, 0.6, 49)
    # print("15, 0.6, 49", test_result)
    test_result = run_simulation(15, 0.8, 49)
    print("Test case : (15, 0.8, 49)")
    print(test_result)
    test_result = run_simulation(40, 1, 1)
    print("Test case : (40,  1 ,  1)")
    print(test_result)


