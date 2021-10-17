from . import *
from . import task3, task1


def loadPeople():
    persons_list = task1.load_people()
    all_people = {}
    for person in persons_list:
        #print(person.get_name())
        friends = person.get_friends()
        friend_list = []
        for friend_person in friends:
            friend_list.append(friend_person.get_name())
            #print(" -- ", friend_person.get_name())
            #name = friend_person.get_name()
        all_people[person.get_name()] = friend_list
    return all_people

def loadgraph(days, probability, inithealth):
    task3.loadgraph(days, probability, inithealth)
    #return plt_html
