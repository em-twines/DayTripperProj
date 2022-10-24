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
restaurants = ["Nau Nau", "Josephine Chez Dumonet", "Sketch Lecure Room & Library", "Amelia", "Cafe Franz Kafka", "Onyx"]
transportation = ["Airbus A330", "Boeing 767","Boeing 787", "Danube Delta Discovery", "Mediterranean Cruise", "Airbus A330, Malasian Cruise", "Boeing 787, Tokyo Cruise"]
entertainment_options = ["River Tour", "Fine Dining Tour", "Street Food Tour", "Scooter Tour of the City", "Amusement Park", "Historic Library Pass", "Museums Pass"]

user_input_1 = ""     
options = tuple(set(["destination", "restaurant", "transportation", "entertainment"]))

#choose destination

def generate_destination():
    rand_int = random.randrange(6)             
    return rand_int

def match_destination_index():
    destination_number = generate_destination()
    destination_index = 0
    for destination in destinations:
        if destination_number == destination_index:
            return destinations[destination_index]
            
        else: 
            destination_index+=1


#choose restaurant

def generate_restaurant():
    rand_int = random.randrange(5)
    return rand_int

def match_restaurant_index():
    restaurant_index = 0
    restaurant_number = generate_restaurant()

    for restaurant in restaurants:
        if restaurant_number == restaurant_index:
            return restaurants[restaurant_index]
            
        else: 
            restaurant_index+=1



#choose transportation

def generate_transport():
    rand_int = random.randrange(6)
    return rand_int

def match_transport_index():
    transport_number = generate_transport()

    transport_index = 0
    for method in transportation:
        if transport_number == transport_index:
            return transportation[transport_index]
            
        else: 
            transport_index+=1

#choose entertainment
# def get_random(my_list):
#     random_value = random.choice(my_list)
#     return random_value

def generate_entertainment():
    rand_int = random.randrange(6)
    return rand_int

def match_entertainment_index():
    entertainment_index = 0
    entertainment_number = generate_entertainment()
    for activity in entertainment_options:
        if entertainment_number == entertainment_index:
            return entertainment_options[entertainment_index]
            
        else: 
            entertainment_index+=1

def reply_wonderful():
    print("Wonderful! Have a great trip!")
    exit()

def ok_later():
    print("Ok, maybe leter then!") 
    exit()

def reply_else():
    print("I'm sorry, I didn't understand that message!")

def sorry():
    print('''I'm sorry, I didn't understand that message! Let's try again. Which option(s) would you like to re-visit? 
        (destination, restaurant, transportation, or entertainment?''')

def reply_let_us_try_again():
    input_1 = input('''Ok, let's try again! Which option(s) would you like to re-visit? 
    (destination, restaurant, transportation, or entertainment?''')
    return input_1

def get_request(user_input):
    if user_input == "y":
        destination_choice = match_destination_index()
        restaurant_choice = match_restaurant_index()
        transport_choice = match_transport_index()
        entertainment_choice = match_entertainment_index()
        print(f'''{destination_choice}, 
        {restaurant_choice},
        {transport_choice},
        {entertainment_choice}''')
        return "y"

    elif user_input == "n":
        ok_later()
        
    else:
        reply_else() 
        return

def split_input(user_input):
    user_input_1_split = tuple(set([user_input]))
    user_input_1_split = user_input.split(", ")
    intersection_outcome = tuple(set(user_input_1_split) & set(options))
    return intersection_outcome

   
def if_no_match(intersection):
    if intersection == 0:
        print(sorry())

def find_requested_changes(intersection):
    requested_changes = len(intersection)
    return requested_changes

def return_matches(intersection1, int_requested_changes):
    option_index = 0
    while option_index < int_requested_changes:
        if intersection1[option_index] == "destination":
            destination_choice = match_destination_index()
            option_index += 1
            if option_index >= int_requested_changes: 
                return destination_choice

        if intersection1[option_index] == "restaurant":
            restaurant_choice = match_restaurant_index()
            option_index += 1
            if option_index >= int_requested_changes: 
                return restaurant_choice

        if intersection1[option_index] == "transportation":
            transport_choice = match_transport_index()
            option_index += 1
            if option_index >= int_requested_changes: 
                return transport_choice
        if intersection1[option_index] == "entertainment":
            entertainment_choice = match_entertainment_index()
            option_index += 1 
            if option_index >= int_requested_changes: 
                return entertainment_choice


def while_no(response):
    while response == "n": 
        desired_changes = reply_let_us_try_again()
        split_list_outcome = split_input(desired_changes)
        int_requested_changes = len(split_list_outcome)       
        if_no_match(int_requested_changes)
        int_changes = find_requested_changes(split_list_outcome)
        result = return_matches(split_list_outcome, int_changes)
        print(result)
        response = "y"
    # while booking_complete_response or final_satisfaction_response == "n":
    # ask_intitial_satisfaction(find_a_new_option)




def ask_intitial_satisfaction(user_input):
    if user_input == "y":
        reply_wonderful()
    elif user_input == 'n':
        return "n"
    else:
        reply_else()
        

def ask_booking_complete(user_input):
    if user_input == "y":
        reply_wonderful()
    elif user_input == 'n':
        return "n"
    else:
        reply_else()



def ask_final_satisfaction(user_input):
    if user_input == "y":
        reply_wonderful()
    elif user_input == "n":
        return "n"
    else:
        reply_else()


               
def print_final_satisfaction(user_input):
    if user_input == "y":
        print("Wonderful! Have a great trip!")
    elif user_input == "n":
        return user_input
    else:
        sorry()






first_options = get_request(input("Welcome! Would you like to start your booking now? (y/n)"))

initial_response = ask_intitial_satisfaction(input("Are you happy with these selections? (y/n)"))

find_a_new_option = while_no(initial_response)

booking_complete_response = ask_booking_complete(input('Is your booking now complete? (y/n)'))

find_a_new_option = while_no(booking_complete_response)

final_satisfaction_response = ask_final_satisfaction(input("Are you happy with your trip details now?"))

try_again = while_no(final_satisfaction_response)



    
    
            






    
            













