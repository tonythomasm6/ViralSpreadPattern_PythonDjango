"""
Created by: Tony Thomas Manthuruthil
Student ID: 31296149
Assignment 2 - Task3
Start Date: 22-Mau-2020
Last updated Date : 6-June-2020
Description: This program loads the list of contagious cases per day and plots it to graph
Explanation: The output graph is concurrent with the input values. The graph becomes more exponential with the increase
    in probability of meet since if probability is higher, then people meet more often and as a result the contagious
    person can spead the disease to more people.
"""

from .task2 import *
import matplotlib.pyplot as plt
import mpld3


#  Method to draw the visual graph
def visual_curve(days, meeting_probability, patient_zero_health):
    daily_list = run_simulation(days, meeting_probability, patient_zero_health)  # Calling method from task 2 to get
    # list of contagious patients
    print("Daily contingency list for given period is ", daily_list)  # Printing daily contagious count

    # Plot graph
    y_coordinate = daily_list  # Count of contagious list used in y axis
    x_coordinate = []  # x axis is number of days per day
    for i in range(len(daily_list)):
        x_coordinate.append(i + 1)  # X axis is number of days list from 1 to number of days (1,2,3 ..... days)

    plt.plot(x_coordinate, y_coordinate)  # Plotting x and y coordinate
    plt.xlabel("Days")  # label of x axis
    plt.ylabel("Count")  # label of y axis
    #plt.show()
    plots = plt.bar(x_coordinate, y_coordinate, width=0.5)
    fig = plots[0].figure
    plt_html = mpld3.fig_to_html(fig)
    print(plt_html)

def visual_curve_web(days, meeting_probability, patient_zero_health):
    daily_list = run_simulation(days, meeting_probability, patient_zero_health)  # Calling method from task 2 to get
    # list of contagious patients
    print("Daily contingency list for given period is ", daily_list)  # Printing daily contagious count

    # Plot graph
    y_coordinate = daily_list  # Count of contagious list used in y axis
    x_coordinate = []  # x axis is number of days per day
    for i in range(len(daily_list)):
        x_coordinate.append(i + 1)  # X axis is number of days list from 1 to number of days (1,2,3 ..... days)

    plt.plot(x_coordinate, y_coordinate)  # Plotting x and y coordinate
    plt.xlabel("Days")  # label of x axis
    plt.ylabel("Count")  # label of y axis
    plt.savefig("ViralSpreadPattern/static/graph.png")
    plt.close()
    # plt.show()
    #plots = plt.bar(x_coordinate, y_coordinate, width=0.5)
    #fig = plots[0].figure
    #plt_html = mpld3.fig_to_html(fig)
    #return plt_html

if __name__ == '__main__':
    # visual_curve(15, 0.8, 49)
    # visual_curve(40, 1, 1)

    day = int(input("Input number of days "))
    prob = float(input("Input Probability of meeting "))
    zero_health = float(input("Input patient zero health "))
    visual_curve(day, prob, zero_health)

def loadgraph(days, probability, inithealth):
    plt_html = visual_curve_web(days, probability, inithealth)
    #return plt_html
