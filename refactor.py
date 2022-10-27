#Project Description: 


# 3 commits
# store destinations, restaurants, modes of transport, and enterntainment as lists
# randomly select each of the above (4 things)
# randomly reselect any of the above uniquely
# confirm that it is complete once all te selections are approved
# display the completed trip in the console
# abide by the Single Responsibility principle

import random
from data import destinations


# destinations = ["Vietnam", "Paris", "San Sebastian", "London", "Dublin", "Prague", "Budapest"]
# restaurants = ["Nau Nau", "Josephine Chez Dumonet", "Sketch Lecture Room & Library", "Amelia", "Cafe Franz Kafka", "Onyx"]
# transportation = ["Airbus A330", "Boeing 767","Boeing 787", "Danube Delta Discovery", "Mediterranean Cruise", "Airbus A330, Malaysian Cruise", "Boeing 787, Tokyo Cruise"]
# entertainment_options = ["River Tour", "Fine Dining Tour", "Street Food Tour", "Scooter Tour of the City", "Amusement Park", "Historic Library Pass", "Museums Pass"]

user_input_1 = ""     
# options = tuple(set(["destination", "restaurant", "transportation", "entertainment"]))
# options = tuple(set(destinations))

#choose destination


def generate_destination_dict(destinations):
    rand_int = random.randrange(len(destinations))  
    destination_dict = destinations[rand_int]
    return destination_dict
    

# def generate_destination_dict(destinations):
#     rand_int = random.randrange(len(destinations))  
#     restaurant_dict = destinations[rand_int]
#     return restaurant_dict

# def generate_destination_dict(destinations):
#     rand_int = random.randrange(len(destinations))  
#     transportation_dict = destinations[rand_int]
#     return transportation_dict

# def generate_destination_dict(destinations):
#     rand_int = random.randrange(len(destinations))  
#     entertainment_dict = destinations[rand_int]
#     return entertainment_dict



def generate_destination(destination_dict):
    location = destination_dict["Location"]       
    return location
           
# def generate_destination(restaurant_dict):
#     restaurants = restaurant_dict["Restaurants"]       
#     return restaurants

# def generate_destination(transportation_dict):
#     transportations = transportation_dict["Transportations"]       
#     return transportations

# def generate_destination(entertainment_dict):
#     entertainments = entertainment_dict["Entertainments"]       
#     return entertainments


def match_index():
        destination = destination_dict.get("Location")
        restaurants = destination_dict.get("Restaurants")
        transportations = destination_dict.get("Transportations")
        entertainments = destination_dict.get("Entertainments")

        rand_int = random.randrange(len(restaurants))
        rand_int1 = random.randrange(len(transportations))
        rand_int2 = random.randrange(len(entertainments))
       
        restaurant = restaurants[rand_int]
        transportation = transportations[rand_int1]
        entertainment = entertainments[rand_int2]

        print(f"You are going to {destination}, where you will dine at{restaurant}. You'll get around {transportation}, and you'll get to {entertainment}.")
        return destination, restaurant, transportation, entertainment


# #choose restaurant

# def generate_restaurant():
#     rand_int = random.randrange(5)
#     return rand_int

# def match_restaurant_index():
#     restaurant_index = 0
#     restaurant_number = generate_restaurant()

#     for restaurant in restaurants:
#         if restaurant_number == restaurant_index:
#             return restaurants[restaurant_index]
            
#         else: 
#             restaurant_index+=1



# #choose transportation

# def generate_transport():
#     rand_int = random.randrange(6)
#     return rand_int

# def match_transport_index():
#     transport_number = generate_transport()

#     transport_index = 0
#     for method in transportation:
#         if transport_number == transport_index:
#             return transportation[transport_index]
            
#         else: 
#             transport_index+=1

# #choose entertainment
# # def get_random(my_list):
# #     random_value = random.choice(my_list)
# #     return random_value

# def generate_entertainment():
#     rand_int = random.randrange(6)
#     return rand_int

# def match_entertainment_index():
#     entertainment_index = 0
#     entertainment_number = generate_entertainment()
#     for activity in entertainment_options:
#         if entertainment_number == entertainment_index:
#             return entertainment_options[entertainment_index]
            
#         else: 
#             entertainment_index+=1



def ok_later():
    print("Ok, maybe later then!") 
    exit()

def reply_else():
    print("I'm sorry, I didn't understand that message! Let's try again")
    response = get_request(input("Welcome! Would you like to start your booking now? (y/n)"))
    if response == "y":
        # choose_trip()
        match_index()

def sorry():
    print('''I'm sorry, I didn't understand that message! ''')

def reply_let_us_try_again():
    input_1 = input('''Let's try again! Which option(s) would you like to re-visit? (Please separate your responses using commas)
    (destination, restaurant, transportation, or entertainment?''')
    return input_1

# def choose_trip():
#         destination_choice = match_destination_index()
#         restaurant_choice = match_restaurant_index()
#         transport_choice = match_transport_index()
#         entertainment_choice = match_entertainment_index()
#         final_list = [destination_choice, restaurant_choice, transport_choice, entertainment_choice]
#         print(final_list)
#         return final_list

def get_request(user_input):
    if user_input == "y":
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


def return_matches(intersection1, int_requested_changes, final_list):
    option_index = 0
    list_new = []
    destination_index = ""
    restaurant_index = ""
    transport_index = ""
    entertainment_index = ""

    while option_index < int_requested_changes:
        if intersection1[option_index] == "destination":
            destination_index = match_destination_index()
            option_index += 1
        elif intersection1[option_index] == "restaurant":
            restaurant_index = match_restaurant_index()
            option_index += 1
        elif intersection1[option_index] == "transportation":
            transport_index = match_transport_index()
            option_index += 1
        elif intersection1[option_index] == "entertainment":
            entertainment_index = match_entertainment_index()
            option_index += 1
        
        else:
            sorry()

    list_new = [destination_index, restaurant_index, transport_index, entertainment_index] 
    position = 0
    length_at_zero = len(list_new[0])
    length_at_one = len(list_new[1])
    length_at_two = len(list_new[2])
    length_at_three = len(list_new[3])

    if length_at_zero >= 1 :
        final_list[position] = list_new[0]
        position += 1
    else:
        final_list[position] == True
        position += 1

    if length_at_one >= 1 :
        final_list[position] = list_new[1]
        position += 1
    else:
        final_list[position]== True
        position += 1

    if length_at_two >= 1 :
        final_list[position] = list_new[2]
        position += 1
    else:
        final_list[position]== True
        position += 1

    if length_at_three >= 1 :
        final_list[position] = list_new[3]
        position += 1
    else:
        final_list[position]== True
        position += 1

    print(final_list)
    return final_list


    
def while_loop(response, final_list):
    while response == "y":
        final_list_aggregate = final_list
        print(final_list_aggregate)
        return final_list_aggregate
    i = 1
    while response == "n" and i > 0:
        desired_changes = reply_let_us_try_again()
        split_list_outcome = split_input(desired_changes)
        int_requested_changes = len(split_list_outcome)         
        if int_requested_changes == 0:
            sorry()
            response == "n"
            i = 1
            # if_no_match(int_requested_changes)    
        else:
            int_changes = find_requested_changes(split_list_outcome)
            final_list_aggregate = return_matches(split_list_outcome, int_changes, final_list)
            response = ask_initial_satisfaction(input("Are you happy with these selections? (y/n)"))


def reply_wonderful(final_list):
    print(f'''Wonderful, have a great trip!
    {final_list}''')
    exit()


def ask_booking_complete(final_list):
    print(final_list)
    user_input = input('Is your booking now complete? (y/n)')
    if user_input == "y":
        reply_wonderful(final_list)
    elif user_input == 'n':
        return "n"
    else:
        reply_else()


def ask_initial_satisfaction(user_input):
    if user_input == "y":
        ask_booking_complete(final_list)
        #return "y"

    elif user_input == 'n':
        return "n"
    else:
        reply_else()
        

answer = get_request(input("Welcome! Would you like to start your booking now? (y/n)"))

destination_dict = generate_destination_dict((destinations))
location = generate_destination(destination_dict)

# destination_dict = generate_destination_dict((restaurants))
# l
# destination_dict = generate_destination_dict((transportations))
# location = generate_destination(destination_dict)

# destination_dict = generate_destination_dict((restaurants))
# location = generate_destination(destination_dict)

final_list = match_index()

answer = ask_initial_satisfaction(input("Are you happy with these selections? (y/n)"))

final_aggregate = while_loop(answer, final_list)

while answer == "n":
    final_aggregate = while_loop(answer, final_list)
   
ask_booking_complete(final_aggregate)



