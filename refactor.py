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


user_input_1 = ""     

def generate_destination_dict(destinations):
    rand_int = random.randrange(len(destinations))  
    destination_dict = destinations[rand_int]
    return destination_dict
  

# def generate_destination(destination_dict):
#     location = destination_dict["Location"]       
#     return location 


def match_index(destination_dict):
        destination = destination_dict["Location"]
        restaurants = destination_dict["Restaurants"]
        transportations = destination_dict["Transportations"]
        entertainments = destination_dict["Entertainments"]

        rand_int = random.randrange(len(restaurants))
        rand_int1 = random.randrange(len(transportations))
        rand_int2 = random.randrange(len(entertainments))
       
        restaurant = restaurants[rand_int]
        transportation = transportations[rand_int1]
        entertainment = entertainments[rand_int2]

        return destination, restaurant, transportation, entertainment


def ok_later():
    print("Ok, maybe later then!") 
    exit()

def reply_else():
    print("I'm sorry, I didn't understand that message! Let's try again")
    response = get_request(input("Welcome! Would you like to start your booking now? (y/n)"))
    if response == "y":
        # choose_trip()
        match_index(destination_dict)

def sorry():
    print('''I'm sorry, I didn't understand that message! ''')

def reply_let_us_try_again():
    input_1 = input('''Let's try again! Which option(s) would you like to re-visit? (Please separate your responses using commas)
    (destination, restaurant, transportation, or entertainment?''')
    return input_1


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
    options = tuple(set(["destination", "restaurant", "transportation", "entertainment"]))
    intersection_outcome = tuple(set(user_input_1_split) & set(options))
    return intersection_outcome

   
def if_no_match(intersection):
    if intersection == 0:
        print(sorry())

def find_requested_changes(intersection):
    requested_changes = len(intersection)
    return requested_changes


def return_matches(intersection1, int_requested_changes, final_list, destination_dict):

    while int_requested_changes > 0:
        if  "destination" in intersection1:
            destination_dict = generate_destination_dict((destinations))

            final_list = match_index(destination_dict)

            final_list = list(final_list)

            print(f'''
    You are going to {final_list [0]}, where you will dine at {final_list [1]}. 
    You'll get around {final_list [2]}, and you'll get to {final_list [3]}.''')            
            return final_list, destination_dict

        else:
               
            list_new = match_index(destination_dict)
            list_new = list(list_new)
            
            if "restaurant" in intersection1:
                final_list[1] = list_new[1]
                int_requested_changes -= 1
            else:
                final_list[1] = final_list[1]

            if "transportation" in intersection1:
                final_list[2] = list_new[2]
                int_requested_changes -= 1
            else:
                final_list[2] = final_list[2]  

            if "entertainment" in intersection1:
                final_list[3] = list_new[3]
                int_requested_changes -= 1
            else:
                final_list[3] = final_list[3]  
        
        print(f'''
    You are going to {final_list [0]}, where you will dine at {final_list [1]}. 
    You'll get around {final_list [2]}, and you'll get to {final_list [3]}.''')
        return final_list, destination_dict

    
def while_loop(response, final_list, destination_dict):
    # while response == "y":
    #     # final_list_aggregate = final_list
    #     # print(final_list_aggregate)
    #     # return final_list_aggregate
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
            # final_list_aggregate = return_matches(split_list_outcome, int_changes, final_list, destination_dict)
            final_list_tuple = return_matches(split_list_outcome, int_changes, final_list, destination_dict)
            final_list = final_list_tuple[0]
            destination_dict = final_list_tuple[1]
            
            response = ask_initial_satisfaction(input("Are you happy with these selections? (y/n)"), final_list)
            return final_list


def reply_wonderful(final_list):
    print(f'''Wonderful, have a great trip!
    {final_list}''')
    exit()


def ask_booking_complete(final_list):
    # print(final_list)
    user_input = input('Is your booking now complete? (y/n)')
    if user_input == "y":
        reply_wonderful(final_list)
    elif user_input == 'n':
        return "n"
    else:
        # reply_else()
        reply_let_us_try_again()


def ask_initial_satisfaction(user_input, final_list):
    if user_input == "y":
        ask_booking_complete(final_list)
        #return "y"

    elif user_input == 'n':
        return "n"
    else:
        # reply_else()
        reply_let_us_try_again()


destination_dict = generate_destination_dict((destinations))

answer = get_request(input("Welcome! Would you like to start your booking now? (y/n)"))

# location = generate_destination(destination_dict)

final_list = match_index(destination_dict)

final_list = list(final_list)

print(f'''
    You are going to {final_list [0]}, where you will dine at {final_list [1]}. 
    You'll get around {final_list [2]}, and you'll get to {final_list [3]}.''')

answer = ask_initial_satisfaction(input("Are you happy with these selections? (y/n)"), final_list)

final_list = while_loop(answer, final_list, destination_dict)

while answer == "n":
    final_list = while_loop(answer, final_list, destination_dict)
   
ask_booking_complete(final_list)



