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
transportation = ["Airbus A330 through", "Boeing 767","Boeing 787", "Danube Delta Discovery", "Mediterranean Cruise", "Airbus A330, Malasian Cruise", "Boeing 787, Tokyo Cruise"]
entertainment_options = ["River Tour", "Fine Dining Tour", "Street Food Tour", "Scooter Tour of the City", "Amusement Park", "Historic Library Pass", "Museums Pass"]


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




#run user-facing dialogue

def get_request():

    options = tuple(set(["destination", "restaurant", "transportation", "entertainment"]))

    user_input_0 = input("Welcome! Would you like to start your booking now? (y/n)")
    if user_input_0 == "y":
        destination_choice = match_destination_index()
        restaurant_choice = match_restaurant_index()
        transport_choice = match_transport_index()
        entertainment_choice = match_entertainment_index()
        print(f'''
        {destination_choice} 
        {restaurant_choice} 
        {transport_choice} 
        {entertainment_choice}''')
    elif user_input_0 == "n":
        print("Ok, maybe leter then!") 
        return    

    else: 
        print("I'm sorry, I didn't understand that request!")
        return


    user_input_1 = input("Are you happy with these selections? (y/n)")

    if user_input_1 == "y":
        user_input_1 = input(f'''Is your booking now complete? (y/n)
        {destination_choice}
        {restaurant_choice} 
        {transport_choice} 
        {entertainment_choice}''')

           
        if user_input_1 == "y":
            print("Wonderful! Have a great trip!")

    while user_input_1 == "n":
       
        while user_input_1 == "n":
                
            user_input_1 = []
            user_input_1 = input('''Ok, let's try again! Which option(s) would you like to re-visit? 
            (destination, restaurant, transportation, or entertainment?''')
            user_input_1_split = tuple(set([]))
            user_input_1_split = user_input_1.split(", ")
            intersection = tuple(set(user_input_1_split) & set(options))
            requested_changes = len(intersection)
            

            if len(intersection) == 0:
                user_input_1 = input('''I'm sorry, I didn't understand that message! Let's try again. Which option(s) would you like to re-visit? 
            (destination, restaurant, transportation, or entertainment?''')
            
            user_input_1_split = tuple(set([]))
            user_input_1_split = user_input_1.split(", ")
            intersection = tuple(set(user_input_1_split) & set(options))
            requested_changes = len(intersection)

            option_index = 0
            while option_index < requested_changes:
                if intersection[option_index] == "destination":
                    destination_choice = match_destination_index()
                    print(destination_choice)
                    option_index += 1
                    if option_index >= requested_changes: 
                        break
                if intersection[option_index] == "restaurant":
                    restaurant_choice = match_restaurant_index()
                    print(restaurant_choice)
                    option_index += 1
                    if option_index >= requested_changes: 
                        break
                if intersection[option_index] == "transportation":
                    transport_choice = match_transport_index()
                    print(transport_choice)
                    option_index += 1
                    if option_index >= requested_changes: 
                        break
                if intersection[option_index] == "entertainment":
                    entertainment_choice = match_entertainment_index()
                    print(entertainment_choice)
                    option_index += 1 
                    if option_index >= requested_changes: 
                        break
                        
                        
        user_input_1 = input("Are you happy with your trip details now?")

        if user_input_1 == "y":

            user_input_1 = input(f'''Is your booking now complete? (y/n)
            {destination_choice}
            {restaurant_choice} 
            {transport_choice} 
            {entertainment_choice}''')
                
        if user_input_1 == "y":
            print("Wonderful! Have a great trip!")
    
    
            






    
            


        
    
get_request()