#Project Description: 


# 3 commits
# store destinations, restaurants, modes of transport, and enterntainment as lists
# randomly select each of the above (4 things)
# randomly reselect any of the above uniquely
# confirm that it is complete once all te selections are approved
# display the completed trip in the console
# abide by the Single Responsibility principle

import random


destinations = ["Vietnam", "Paris", "San Sebastian", "London", "Dublin", "Prague", "Budapest"]
restaurants = ["Nau Nau", "Josephine Chez Dumonet", "Sketch Lecure Room & Library", "Amelia", "Cafe Franz Kafka" "Onyx"]
transportation = ["Airbus A330 through", "Boeing 767","Boeing 787", "Danube Delta Discovery", "Mediterranean Cruise", "Airbus A330, Malasian Cruise", "Boeing 787, Tokyo Cruise"]
entertainment = ["River Tour", "Fine Dining Tour", "Street Food Tour", "Scooter Tour of the City", "Amusement Park", "Historic Library Pass", "Museums Pass"]


#choose destination

def generate_destination():
    rand_int = random.randrange(6)
    return rand_int

def match_destination_index():
    destination_index = 0
    for destination in destinations:
        if destination_number == destination_index:
            print(destinations[destination_index])
            return
        else: 
            destination_index+=1

destination_number = generate_destination()
destination_choice = match_destination_index()



#choose restaurant

def generate_restaurant():
    rand_int = random.randrange(5)
    return rand_int

def match_restaurant_index():
    restaurant_index = 0
    for restaurant in restaurants:
        if restaurant_number == restaurant_index:
            print(restaurants[restaurant_index])
            return
        else: 
            restaurant_index+=1


restaurant_number = generate_restaurant()
restaurant_choice = match_restaurant_index()



#choose transportation

def generate_transport():
    rand_int = random.randrange(6)
    return rand_int

def match_transport_index():
    transport_index = 0
    for method in transportation:
        if transport_number == transport_index:
            print(transportation[transport_index])
            return
        else: 
            transport_index+=1


transport_number = generate_transport()
transport_choice = match_transport_index()


#choose entertainment

def generate_entertainment():
    rand_int = random.randrange(6)
    return rand_int

def match_entertainment_index():
    entertainment_index = 0
    for activity in entertainment:
        if entertainment_number == entertainment_index:
            print(entertainment[entertainment_index])
            return
        else: 
            entertainment_index+=1


entertainment_number = generate_entertainment()
entertainment_choice = match_entertainment_index()