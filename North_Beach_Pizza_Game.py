import time
import random
import sys

#FAIL FUNCTION
def fail():
    """
DocString

This function will enter if the player looses and will finish the program.

    """
    print("You lost all your customers, your business is falling faster than a skydiver")
    sys.exit(0)

#START OF THE GAME
def disclaimer():
    """
DocString

This should be the first function of the game, asking to the player to open window widely to be able to see the graphics correctly.

    """
    print("\n\n\nBefore starting, to enhance your experience, please open the console window widely, Thank you :D")
    time.sleep(1)
    input("\n\t\t\t\t\t\t\t\t\033[1m<Press ENTER to continue>")
    intro()

#INTRO
def intro():
    """
DocString

In this function, the game will present the title as well as a bit of story.

The function takes no inputs and is called after disclaimer()

    """
    global name
    print("""
    ██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗
    ██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗
    ██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║
    ██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║
    ╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝
     ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝ """, end= ""), time.sleep(0.3), print(""" ██╗""", end=""), time.sleep(0.6) ,print(""" ██╗""", end=""), time.sleep(0.9), print(""" ██╗""", end= " ")
    time.sleep(1)
    print("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
                                               \033[1;33m___
                                               \033[1;33m|\033[1;31m  ~~--\033[1;33m.
                                               \033[1;33m|\033[1;31m%=\033[1;32m@\033[1;31m%%\033[1;33m/
                                               \033[1;33m|\033[1;31mo%%%\033[1;33m/
                                            \033[1;33m__ |\033[1;31m%%o\033[1;33m/
                                      \033[1;33m_,--~~ \033[1;33m| |\033[1;32m(\033[1;31m_\033[1;33m/ .\033[1;33m_
                                   \033[1;33m,/'  \033[1;31mm%%%%\033[1;33m| |\033[1;31mo\033[1;33m/ /  \033[1;33m`\.
                                  \033[1;33m/' \033[1;31mm%\033[1;32m%o(\033[1;31m_)%\033[1;33m| |/ /\033[1;31mo%%m \033[1;33m`\\
                                \033[1;33m/' \033[1;31m%%@=%o%%%o\033[1;33m|   /\033[1;31m(_)o%%% \033[1;33m`\\
                               \033[1;33m/  \033[1;31m%o\033[1;32m%%%%%\033[1;31m=@%%\033[1;33m|  /\033[1;31m%%o%%@=%%  \033[1;33m\\
                              \033[1;33m|  \033[1;31m(_)%(_)%%o%%\033[1;33m| /\033[1;31m%%%=\033[1;32m@(_\033[1;31m)%%%  \033[1;33m|
                              \033[1;33m| \033[1;31m%%o%%\033[1;32m%%\033[1;31mo%%%(_\033[1;33m|/\033[1;31m%o%%o%%%%o%%% \033[1;33m|
                              \033[1;33m| \033[1;31m%%o%(_)%%%%%o%(_)%%%o%\033[1;32m%o\033[1;31m%o%% \033[1;33m|
                              \033[1;33m|  \033[1;31m(_)\033[1;32m%%\033[1;31m=@%(_)%o%o%%(_)%o(_)%  \033[1;33m|
                               \033[1;33m\ \033[1;31m~%%o%%%%%o%o%=\033[1;32m@%%o\033[1;31m%%@%%o%~ \033[1;33m/
                                \033[1;33m\. \033[1;31m~o%%(_\033[1;32m)%%\033[1;31m%o%(_)%%(_)o~ \033[1;33m,/
                                  \033[1;33m\_ \033[1;31m~o%=@%(_)%o%%(_)%~ \033[1;33m_/
                                    \033[1;33m`\_\033[1;31m~~o%%%\033[1;32mo%\033[1;31m%%%%~~\033[1;33m_/'
                                       \033[1;33m`--..____,,--'

    \033[1;32m _   _            _   _      \033[1;37m ____                  _      \033[1;31m ____  _     _____
    \033[1;32m| \ | | ___  _ __| |_| |__   \033[1;37m| __ )  ___  __ _  ___| |__   \033[1;31m|  _ \(_)___|__  /______ _
    \033[1;32m|  \| |/ _ \| '__| __| '_ \  \033[1;37m|  _ \ / _ \/ _` |/ __| '_ \  \033[1;31m| |_) | |_  / / /|_  / _` |
    \033[1;32m| |\  | (_) | |  | |_| | | | \033[1;37m| |_) |  __/ (_| | (__| | | | \033[1;31m|  __/| |/ / / /_ / / (_| |
    \033[1;32m|_| \_|\___/|_|   \__|_| |_| \033[1;37m|____/ \___|\__,_|\___|_| |_| \033[1;31m|_|   |_/___/____/___\__,_|""")
    time.sleep(2)
    print("""                         \033[1;32m_____ _    \033[1;37m          ___
                        \033[1;32m/__   \ |__  \033[1;37m ___    / _ \__ _ \033[1;31m_ __ ___   ___
                          \033[1;32m/ /\/ '_ \ \033[1;37m/ _ \  / /_\/ _` |\033[1;31m '_ ` _ \ / _ \\
                         \033[1;32m/ /  | | | |\033[1;37m  __/ / /_\\\\ (_| |\033[1;31m | | | | |  __/
                         \033[1;32m\/   |_| |_|\033[1;37m\___| \____/\__,_|\033[1;31m_| |_| |_|\___|

    """)
    input("\t\t\t\t\t\t\t\t\t<Press ENTER to start>\033[0m")

    name = input("Tell me Chef, what is your name?").capitalize()
    ###########EASTER EGG###############
    if name == "Donatello":
        print("""NINJA TURTLES LOVE PIZZA""")

    intro_text = f"""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nYou are {name} the Pizzaioli, a renowned pizza maker with a restaurant in a hilly, foggy city.
In your restaurant, you have 3 kinds of pizzas to make: Margherita, Peperoni, and Napoletana.
You will receive a random order of the pizzas and for each one, you will need to prepare the ingredients.
Each ingredient is prepared differently so make sure you read the instructions on how to do it.
The customers are very exigent. Make sure to mix the ingredients correctly and to put the right amount.
When you finish the order, you will receive feedback from the demanding customers.
You only have 4 minutes to make as many pizzas you can.
At the end, you will receive points depending on how well you did. Feel free to share it with friends and compete against each other.

..Ah! Very important {name}: In the kitchen there are many things that can happen, be careful to not get injured or stuck your head in the fridge.

            """
    while True:
        continue1 = input("\n\n\n\nDo you want to skip the intro? \n\n [1] Read\n [2] Skip")

        if continue1 == "1": ####################CORRECT THIS CODE FOR OTHER INPUTS

            for letter in intro_text:
                print(letter, end= '')
                time.sleep(.05)
                if letter == ",":
                    time.sleep(0.15)
                elif letter == ".":
                    time.sleep(0.4)

            break

        elif continue1 == "2":
            print(intro_text)
            break
        else:
            print("\n\n\n\nSelect 1 or 2 please \n\n [1] Read\n [2] Skip")


    skill_choice()

#SKILLS
def skill_choice():
    """
DocString

In this, function, the player will be asked to chose to divide 10 points between 3 main categories: Cutting Speed, Seasoning Master and Heat Control.

The assigned value of each category will be stored in the list 'skills'. Each index of the list will correspond to a different skill.

The function takes no inputs and is called after intro()

    """

    print(f"""\n\n\n\n\n\n\n\n\n\nEvery pizza maker is unique in their style,
    usually, there are 3 main skills that are the most defining ones:

    -Cutting Speed

    -Seasoning Master

    -Heat Control

    In order to conquer the arena of Chefs of the world, here you have 10 skill points. Divide them into these 3 main categories:""")

    print("""
    \t\t\t  #1\t\t\t\t\t#2\t\t\t\t\t  #3
    \t\t\t"""+ """\033[1m""" + """Cutting\t\t\t\t Seasoning\t\t\t\t Heat
    \t\t\t Speed \t\t\t\t  Master \t\t\t\tControl""" + """\033[0m
    """)
    time.sleep(1)

    points_left = 10
    i=0
    while i<3:
        print(f"\nHow many skill points would you like to spend in skill number {(i+1)}? (Please type value between 0 and {points_left})")
        answer = input('>')

        # Handdling the error of the using input not being an integer and assigning a value to each skill in a for loop
        try:
            answer = int(answer)
            if points_left >= answer >= 0:
                points_left -= answer
                skills[i] = answer
                print(f"Great! {answer} points to skill number {(i+1)}\n")
                i += 1
            else:
                print(f"Please give a number between 0 and {points_left}, try again.\n")

        except ValueError:
            print("Sorry, no words or decimals, please. Just a Number (1,2,3, etc...), nothing else :D\n")
        if i == 3:
            print(f"""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\tBelow is your skill choice. You have {points_left} points left to spend.


                    \t\t\t  #1\t\t\t\t\t#2\t\t\t\t\t  #3
                    \t\t\tCutting \t\t\t Seasoning  \t\t\t Heat
                    \t\t\t Speed \t\t\t\t   Master \t\t\t\tControl
                    \t\t\t   {skills[0]} \t\t\t\t\t {skills[1]} \t\t\t\t\t   {skills[2]}""")
            time.sleep(1)

            while True:
                continue1 = input("\n\t\t\t\t\t\tIs this your final choice?\n [YES]\n [NO]").lower()
                if "yes" in continue1 and not "maybe" in continue1:
                    break

                elif "no" in continue1:
                    print("Rectify is wise... give it another try")
                    time.sleep(1.5)
                    skill_choice()
                    break
                else:
                    print("Let's try again..")

#CUSTOMER ORDER
def customer_order():
    """
DocString:

This function sets the start of each round.
A random number between 0 and 2 is generated and to chose a random pizza from the list 'possible_order'. This is how 'order_number' and 'order_pizza_name' are created.
The function combines dictionary methods, together with list indexing ot compare what the cusotmer ordered to wha the player build and give a feed back.

This function takes no inputs:
This function returns 2 outputs:
    - order_number: This number will be used at the end of each round to receive the feedback.
    - order_pizza_name: It will be used to show the player which pizza is needed.

        """
    possible_order = ["Margherita", "Peperoni", "Napoletana"]
    customer_coming = """\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThere they come... new customers"""
    for letter in customer_coming:
        print(letter, end='')
        time.sleep(.1)
        if letter == ",":
            time.sleep(0.3)
        elif letter == ".":
            time.sleep(0.3)
    input("\033[1m\n<Press ENTER to ask what do they want to order>\033[0m")
    order_number = random.randint(0,2)
    order_pizza_name = possible_order[order_number]

    customer_speaks = f"""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nHi! How are you? I would like to order a {order_pizza_name} pizza. \nThanks!
    """
    for letter in customer_speaks:
        print(letter, end='')
        time.sleep(0.1)
        if letter == ",":
            time.sleep(0.3)
        elif letter == ".":

            time.sleep(0.3)

    input("\033[1m<Press ENTER to accept the order>\033[0m")
    return order_pizza_name , order_number

#DESICION TREE
def decision(order_number, order_pizza_name):
    """
DocString:

This is one of the main functions of the game. It acts as a central point to guide the player towards the rest of the game.
It is based on a while loop that iterates as long as the dictionary 'preparation' doesn't have the key "Cook the Pizza".

While the loop is running, the program will print the options on what to do, i.e.: 'grate the cheese' or 'smash the tomatoes'.
The player might chose in two ways:
    1.- They type a number. In this case, the program will try to convert it to an integer. If it doesn't give an error (for which case, we go to option 2), the program will take the number typed by the user and use it as the index to access a list containing the functions for each ingredient.

    2.- They type the verb or the noun they want to chose. For that the program will evaluate the string and if the conditions are made, the function of the selected ingredient will be launched.

This function takes two inputs:
    - order_number: originally generated in the function 'customer_order()'. Making this vale an input makes it possible to transfer it through the program until the function 'customer_feedback()' is launched.
    - order_pizza_name: originally generated in the function 'customer_order()'. As an input, it is possible to use it inside the this function.

This function returns one output:
    - order_number: originally generated in the function 'customer_order()'. Making this vale an output makes it possible to transfer it through the program until the function 'customer_feedback()' is launched.

    """

    if len(preparation) < 1:
        print(f"""Welcome to the kitchen of North Beach Restaurant {name}!

Now that we have an order, we need to be quick, we don't want our customers to starve.

Look, in this case we have a {order_pizza_name.upper()} pizza, we need to start preparing it by selecting the correct ingredients that go in.

Take always into account which pizza the customer asks because it will be different each time.

You are free in this kitchen and you could put Anchovies to a Margherita pizza... but then customers will be more annoyed than an Intalian nonna!
""")
        input("\033[1m\n<Press ENTER to continue>\033[0m")

        print("\nNow I will show you what we can do in the kitchen, and you can pick what ever you what, just remember: Keep your customers happier than a bambini with cannoli")
        input("\033[1m\n<Press ENTER to continue>\033[0m")
    decision_list = ["Knead the Dough", "Salt", "Put Olive Oil", "Smash Tomatoes", "Grate the Cheese", "Cut Peperoni", "Put the Anchovies", "Cook the Pizza"]

    while True:
        if preparation.get("Cook the Pizza") is not None:

            return order_number
        else:

            time.sleep(0.5)
            print(preparation)
            print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n{name}! the customer wants a {order_pizza_name} Pizza. We can do all of this:\n" )
            i = 1
            for action in decision_list:
                time.sleep(0.01)
                print(i,end="")
                print(") " + action + "\n")
                i += 1

            print("Chef! What do we do now?")
            time.sleep(0.2)

            answer = input(">").lower()
            actions_list = [kneading, salt, oil, tomatoes, cheese, peperoni, anchovies, cook]  # Here we evaluate if the number they typed is a correct choice
            #Trying to check if the user used a number or typed something
            try:
                answer = int(answer) -1

                if len(actions_list)-1 >= answer >= 0:
                    if answer == 7:
                        cook(order_number)
                    else:
                        actions_list[answer]()
                else:
                    print("This is not a valid option.")

            except ValueError:
                if "dough" in answer or "knead" in answer:
                    kneading()
                elif "smash" in answer or "tomatoes" in answer:
                    tomatoes()
                elif "grate" in answer or "cheese" in answer:
                    cheese()
                elif "cut" in answer or "peperoni" in answer:
                    peperoni()
                elif "prepare" in answer or "anchovies" in answer:
                    anchovies()
                elif "salt" in answer:
                    salt()
                elif "olive" in answer or "oil" in answer:
                    oil()
                elif "cook" in answer:
                    order_number = cook(order_number)
                else:
                    print("That doesn't seem like a possible option in this kitchen, Chef")

#CUSTOMER FEEDBACK
def customer_feedback(Menu, order_number, preparation):
    """
DocString:

This is one of the main functions of the game. It acts as a wrap up for each pizza to finish and receive feedback.
The function combines dictionary methods, together with list indexing ot compare what the cusotmer ordered to wha the player build and give a feed back.

--------------------------------------------------------------------------------------------------
For example, in the lines:

if Menu[order_number].get("Cook the Pizza") - preparation.get("Cook the Pizza") > 2:
    print("This pizza is raw!")

We do the following to compare the two dictionaries:
type(order_menu) >> int
type(Menu) >> list
type(Menu[order_menu]) >> dict
type(preparation) >> dics
type(Menu[order_number].get("Cook the Pizza")) >> int
type(preparation.get("Cook the Pizza")) >> int

Then, the method .get gives us the value of for a give key in a dictionary.
.get gives a None value type if there is no assigned key in the dictionary. Because it's not possible to do operations with None types, all is controlled by a try, except structure.

--------------------------------------------------------------------------------------------------

This function takes three inputs:
    - Menu: a list containing dictiaries with the possible orders
    - order_number: originally generated in the function 'customer_order()'. Making this vale an input makes it possible to access the desired dictionary for each order.
    - preparation: this dict stores every completed step of the player in a dictionary.

    """

    print("\n\nTHIS IS THE FEEDBACK FROM YOUR CUSTOMER")
    input("\033[1m<Press ENTER to continue>\033[0m\n\n\n")
    points = 0
    try: #If a certain key is not in a dictionary, the .get method, returns None. In this case a substraction will give us error and that's why we control for it with try, except.
        if Menu[order_number].get("Cook the Pizza") - preparation.get("Cook the Pizza") > 2:
            print(f"Per la mia Mammaaa {name}! This pizza is not cooked")
            points -= 12
        elif Menu[order_number].get("Cook the Pizza") - preparation.get("Cook the Pizza") < -2:
            print("CAll the firefighters... this pizza is burned!")
            points -= 12
        else:
            print("This is a great cooked pizza")
            points += 7
    except TypeError:
        print("This pizza is not even cooked!!")
        fail()

    try:
        if Menu[order_number].get("Salt") - preparation.get("Salt") > 2:
            print(f"This pizza is tasteless... {name.upper()}!! DID YOU PUT ANY SALT IN HERE?")
            points -= 4
        elif Menu[order_number].get("Salt") - preparation.get("Salt") < -2:
            print("EEWWWW.... I can't eat this... where is this from? The dead see? Too much salt")
            points -= 6
        else:
            print("Nice taste balacing.. very good though")
            points +=10
    except TypeError:
        print("This pizza is as tasteless!!")
        fail()

    try:
        if Menu[order_number].get("Put Olive Oil") - preparation.get("Put Olive Oil") > 2:
            print("[Gnam] [Gnam] [Gnam]... this is soooo thick, didn't you put a little oil in here?")
            points -= 2
        elif Menu[order_number].get("Put Olive Oil") - preparation.get("Put Olive Oil") < -2:
            print("Siiiinging in the raain! I'm signing in the rain!! This pizza rains oil...")
            points -= 7
        else:
            print("Mmmmmmh Sooo yuummyyy!!")
            points += 9
    except TypeError:
        print("This pizza as dry as the Sahara... OMG...")
        fail()


    if "Smash Tomatoes" not in preparation:
        print("Pizza bianca!? I don't remember ordering a pizza without tomatoes")
        points -= 8
    else:
        points += 4

    if "Grate the Cheese" not in preparation:
        print("I have seen many things in my live, but never a pizza without cheese. Donatello! What happened?")
        points -= 17
    else:
        points += 4

#Evaluating if the pizza is Peperoni or Anchovies
    if "Cut Peperoni" in Menu[order_number]: #Controling when the order is a peperoni pizza
        if "Cut Peperoni" in preparation:
            print("Nice Peperoni, where is it from?")
            points += 7
        else:
            print("I ordered a Peperoni Pizza, WHERE IS MY PEPERONI!?")
            points -= 9

    elif "Cut Peperoni" in preparation and "Cut Peperoni" not in Menu[order_number]: #Controling when the order is NOT a peperoni pizza
        print("Why did you put Peperoni in my Pizza?")
        points -= 17


    if "Put the Anchovies" in Menu[order_number]: #Controling when the order is NOT a napoletana pizza:
        if "Put the Anchovies" in preparation:
            print("Nice Anchovies, where are they from?")
            points += 7
        else:
            print("I ordered a Anchovies Pizza, WHERE ARE MY ANCHOVIES!?")
            points -= 9

    elif "Put the Anchovies" in preparation  and "Put the Anchovies" not in Menu[order_number]: #Controling when the order is NOT a napoletana pizza:
        print("Why did you put Anchovies in my Pizza?")
        points -= 17

    print(f"\n\n\nFor the pizza {order_pizza_name}. You got a total of {points} points!!\n\n\n")
    time.sleep(5)
    input("Press [Enter] to continue")

##########################################
#       ACTIONS IN THE KITCHEN           #
##########################################


#KNEADING DOUGH
def kneading():
    count = 0
    if "Knead the Dough" in preparation:
        print("The Dough is already Knead! ")
        decision(order_number, order_pizza_name)
    elif "Knead the Dough" not in preparation:
        print("""Now you are going to knead the dough.
        In order to do it, you need to press 'Q' and all the letters of the keyboard from left to right until letter 'P'
        Kinda like... kneading.
        You should get something like: 'qwertyuiop' """)
        input("\033[1m<Press ENTER to continue>\033[0m")

        print(""" /$$$$$$$                            /$$
| $$__  $$                          | $$
| $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$$ /$$   /$$
| $$$$$$$/ /$$__  $$ |____  $$ /$$__  $$| $$  | $$
| $$__  $$| $$$$$$$$  /$$$$$$$| $$  | $$| $$  | $$
| $$  \ $$| $$_____/ /$$__  $$| $$  | $$| $$  | $$
| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$$ /$$ /$$ /$$
|__/  |__/ \_______/ \_______/ \_______/ \____  $$|__/|__/|__/
                                         /$$  | $$
                                        |  $$$$$$/
                                         \______/             """)
        time.sleep(3)
        print("""        GGGGGGGGGGGGG     OOOOOOOOO           !!!
     GGG::::::::::::G   OO:::::::::OO        !!:!!
   GG:::::::::::::::G OO:::::::::::::OO      !:::!
  G:::::GGGGGGGG::::GO:::::::OOO:::::::O     !:::!
 G:::::G       GGGGGGO::::::O   O::::::O     !:::!
G:::::G              O:::::O     O:::::O     !:::!
G:::::G              O:::::O     O:::::O     !:::!
G:::::G    GGGGGGGGGGO:::::O     O:::::O     !:::!
G:::::G    G::::::::GO:::::O     O:::::O     !:::!
G:::::G    GGGGG::::GO:::::O     O:::::O     !:::!
G:::::G        G::::GO:::::O     O:::::O     !!:!!
 G:::::G       G::::GO::::::O   O::::::O      !!!
  G:::::GGGGGGGG::::GO:::::::OOO:::::::O
   GG:::::::::::::::G OO:::::::::::::OO       !!!
     GGG::::::GGG:::G   OO:::::::::OO        !!:!!
        GGGGGG   GGGG     OOOOOOOOO           !!! """)
        while True:
            x = input("KNEAD THE DOUGH! \n\n (PRES 'Q' AND THEN PRESS ALL THE LETTERS OF THE KEYBOARD FROM LEFT TO RIGHT UNTIL THE LETTER 'P', THEN PRESS ENTER. \n You should get: 'qwertyuiop'  )").lower()
            if x != "qwertyuiop":
                print("\n\nYou are not kneading correctly! ")

            else:
                count += 1
                if count == 9:
                    print("Almost there!")
                if count == 11 - skills[0]:
                    print("\n\n\n\n\t\t\tヘ( ^o^)ノ＼(^_^ ) \n Good job! The Dough is now a Pizza base!")
                    decisions_taken.append("Dough")
                    preparation.update({"Knead the Dough": 1})
                    input("\033[1m<Press ENTER to continue>\033[0m")
                    decision(order_number, order_pizza_name)
                    break
    else:
        print("Something went wrong")
#CUT TOMATOES
def tomatoes():
    count = 0
    if "Smash Tomatoes" in preparation:
        print("You have already smashed the tomatoes! ")
        decision(order_number, order_pizza_name)
    elif "Smash Tomatoes" not in preparation:
        print("""Now you are going to smash the tomatoes for the pizza.
In order to do it, you need to press [SPACE BAR] and [ENTER] repetitively
Kinda like... smashing tomatoes""")
        input("\033[1m<Press ENTER to continue>\033[0m")

        print("""/$$$$$$$                            /$$
| $$__  $$                          | $$
| $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$$ /$$   /$$
| $$$$$$$/ /$$__  $$ |____  $$ /$$__  $$| $$  | $$
| $$__  $$| $$$$$$$$  /$$$$$$$| $$  | $$| $$  | $$
| $$  \ $$| $$_____/ /$$__  $$| $$  | $$| $$  | $$
| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$$ /$$ /$$ /$$
|__/  |__/ \_______/ \_______/ \_______/ \____  $$|__/|__/|__/
                                         /$$  | $$
                                        |  $$$$$$/
                                         \______/             """)
        time.sleep(3)
        print("""GGGGGGGGGGGGG     OOOOOOOOO           !!!
     GGG::::::::::::G   OO:::::::::OO        !!:!!
   GG:::::::::::::::G OO:::::::::::::OO      !:::!
  G:::::GGGGGGGG::::GO:::::::OOO:::::::O     !:::!
 G:::::G       GGGGGGO::::::O   O::::::O     !:::!
G:::::G              O:::::O     O:::::O     !:::!
G:::::G              O:::::O     O:::::O     !:::!
G:::::G    GGGGGGGGGGO:::::O     O:::::O     !:::!
G:::::G    G::::::::GO:::::O     O:::::O     !:::!
G:::::G    GGGGG::::GO:::::O     O:::::O     !:::!
G:::::G        G::::GO:::::O     O:::::O     !!:!!
 G:::::G       G::::GO::::::O   O::::::O      !!!
  G:::::GGGGGGGG::::GO:::::::OOO:::::::O
   GG:::::::::::::::G OO:::::::::::::OO       !!!
     GGG::::::GGG:::G   OO:::::::::OO        !!:!!
        GGGGGG   GGGG     OOOOOOOOO           !!! """)
        while True:
            x = input("SMASH THE TOMATOES! FAST! (PRESS SPACE BAR AND ENTER TO SMASH)")
            if x != " ":
                print("You are not smashing the tomatoes! (DON'T DO IT ANYMORE)")
                import random
                rand = random.randint(0,20)
                if rand > skills[0]:
                    count -= 10
                    print("\t\t\t\t\tლ(ಠ益ಠ)ლ \n OH NOO... YOU CUT YOUR FINGER... IT WILL TAKE LONGER TO CUT THE TOMATOES")
                    time.sleep(3)
            else:
                count += 1
                if count == 9:
                    print("Almost there!")
                if count > 11 - skills[0]*0.75:
                    print("\t\t\t\t\tヘ( ^o^)ノ＼(^_^ ) \n Good job! The Tomatoes are now smashed! ")
                    decisions_taken.append("Tomatoes")
                    preparation.update({"Smash Tomatoes": 1})
                    time.sleep(5)
                    input("\033[1m<Press ENTER to continue>\033[0m")
                    decision(order_number, order_pizza_name)
                    break
    else:
        print("Something went wrong")
#CUT PEPERONI
def peperoni():
    count = 0
    print("""Now you are going to cut the peperonni for the pizza.
In order to do it, you need to press [SPACE BAR] and [ENTER] repetitively
Kinda like... cuttin peperoni""")
    input("\033[1m<Press ENTER to continue>\033[0m")

    print("""/$$$$$$$                            /$$
| $$__  $$                          | $$
| $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$$ /$$   /$$
| $$$$$$$/ /$$__  $$ |____  $$ /$$__  $$| $$  | $$
| $$__  $$| $$$$$$$$  /$$$$$$$| $$  | $$| $$  | $$
| $$  \ $$| $$_____/ /$$__  $$| $$  | $$| $$  | $$
| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$$ /$$ /$$ /$$
|__/  |__/ \_______/ \_______/ \_______/ \____  $$|__/|__/|__/
                                         /$$  | $$
                                        |  $$$$$$/
                                         \______/             """)
    time.sleep(3)
    print("""GGGGGGGGGGGGG     OOOOOOOOO           !!!
     GGG::::::::::::G   OO:::::::::OO        !!:!!
   GG:::::::::::::::G OO:::::::::::::OO      !:::!
  G:::::GGGGGGGG::::GO:::::::OOO:::::::O     !:::!
 G:::::G       GGGGGGO::::::O   O::::::O     !:::!
G:::::G              O:::::O     O:::::O     !:::!
G:::::G              O:::::O     O:::::O     !:::!
G:::::G    GGGGGGGGGGO:::::O     O:::::O     !:::!
G:::::G    G::::::::GO:::::O     O:::::O     !:::!
G:::::G    GGGGG::::GO:::::O     O:::::O     !:::!
G:::::G        G::::GO:::::O     O:::::O     !!:!!
 G:::::G       G::::GO::::::O   O::::::O      !!!
  G:::::GGGGGGGG::::GO:::::::OOO:::::::O
   GG:::::::::::::::G OO:::::::::::::OO       !!!
     GGG::::::GGG:::G   OO:::::::::OO        !!:!!
        GGGGGG   GGGG     OOOOOOOOO           !!! """)
    if "Cut Peperoni" in preparation:
        print("You have already cut the Peperoni! ")
        decision(order_number, order_pizza_name)
    elif "Cut Peperoni" not in preparation:
        while True:
            x = input("CUT THE PEPERONI! FAST! (PRESS SPACE BAR AND ENTER TO CUT)")
            if x != " ":
                print("You are not cutting the peperoni! (DON'T DO IT ANYMORE)")
                import random
                rand = random.randint(0,20)
                if rand > skills[0]:
                    count -= 10
                    print("\t\t\t\t\tლ(ಠ益ಠ)ლ \n OH NOO... YOU CUT YOUR FINGER... IT WILL TAKE LONGER TO CUT THE PEPERONI")
                    time.sleep(3)
            else:
                count += 1
                if count == 9:
                    print("Almost there!")
                if count > 10 - skills[0]*0.75:
                    print("\t\t\t\t\tヘ( ^o^)ノ＼(^_^ ) \n Good job! The Peperoni is now sliced! ")
                    decisions_taken.append("Peperoni")
                    preparation.update({"Cut Peperoni": 1})
                    input("\033[1m<Press ENTER to continue>\033[0m")
                    decision(order_number, order_pizza_name)
                    break
    else:
        print("Something went wrong")
#CHEESE
def cheese():
    count = 0
    print("""Now you are going to grate the cheese for the pizza.
In order to do it, you need to press 'Q', then 'A', then 'Z', then 'W', then 'S', then 'X', finally press [ENTER]
Kinda like... grating.
You should get something like: 'qazwsx' """)
    input("\033[1m<Press ENTER to continue>\033[0m")

    print("""/$$$$$$$                            /$$
| $$__  $$                          | $$
| $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$$ /$$   /$$
| $$$$$$$/ /$$__  $$ |____  $$ /$$__  $$| $$  | $$
| $$__  $$| $$$$$$$$  /$$$$$$$| $$  | $$| $$  | $$
| $$  \ $$| $$_____/ /$$__  $$| $$  | $$| $$  | $$
| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$$ /$$ /$$ /$$
|__/  |__/ \_______/ \_______/ \_______/ \____  $$|__/|__/|__/
                                         /$$  | $$
                                        |  $$$$$$/
                                         \______/             """)
    time.sleep(3)
    print("""GGGGGGGGGGGGG     OOOOOOOOO           !!!
     GGG::::::::::::G   OO:::::::::OO        !!:!!
   GG:::::::::::::::G OO:::::::::::::OO      !:::!
  G:::::GGGGGGGG::::GO:::::::OOO:::::::O     !:::!
 G:::::G       GGGGGGO::::::O   O::::::O     !:::!
G:::::G              O:::::O     O:::::O     !:::!
G:::::G              O:::::O     O:::::O     !:::!
G:::::G    GGGGGGGGGGO:::::O     O:::::O     !:::!
G:::::G    G::::::::GO:::::O     O:::::O     !:::!
G:::::G    GGGGG::::GO:::::O     O:::::O     !:::!
G:::::G        G::::GO:::::O     O:::::O     !!:!!
 G:::::G       G::::GO::::::O   O::::::O      !!!
  G:::::GGGGGGGG::::GO:::::::OOO:::::::O
   GG:::::::::::::::G OO:::::::::::::OO       !!!
     GGG::::::GGG:::G   OO:::::::::OO        !!:!!
        GGGGGG   GGGG     OOOOOOOOO           !!! """)
    if "Grate the Cheese" in preparation:
        print("You have already grated the Cheese! ")
        decision(order_number, order_pizza_name)
    elif "Grate the Cheese" not in preparation:
        while True:
            x = input("\n\n\nGRATE THE CHEESE! FAST! \n\n (PRES 'Q' AND THEN PRESS ALL THE LETTERS OF THE KEYBOARD FROM TOP TO BOTTOM UNTIL THE LETTER 'Z', THEN REPEAT STARTING AT THE 'W' UNTIL THE 'X'. FINALLY PRESS ENTER. \n hint:(You should get: 'qazwsx')  )").lower()
            print(x)
            if "e" in x or "d" in x or "c" in x or "1" in x or "2" in x:
                count -= 5
                print(count)
                print("\n\n\t\t\t\t\tლ(ಠ益ಠ)ლ \n\n\n OH NOO... YOU GRATED YOUR FINGER OUCH!... IT WILL TAKE LONGER TO GRATE THE CHEESE")
            elif x == "qazwsx":
                count += 1
                if count == 2:
                    print("Almost there!")
                if count == 3:
                    print("\n\n\t\t\t\t\tヘ( ^o^)ノ＼(^_^ ) \n Good job! The Cheese is grated now!")
                    decisions_taken.append("Cheese")
                    preparation.update({"Grate the Cheese": 1})
                    input("\033[1m<Press ENTER to continue>\033[0m")
                    decision(order_number, order_pizza_name)

                    break
            else:
                import random
                random_list = ["the soap",
                               "my thing",
                               "the phone",
                               "that rat",
                               "your hair",
                               "the soda",
                               "our food",
                               "my hat",
                               "your head in the oven",
                               "your hands in the soup",
                               "your feet in the freezer",
                               ]
                rand = random.randint(0,len(random_list)-1)
                print(f"\t\t\t\t\t(ಠ_ಠ)\nWhat are you doing with {random_list[rand]}? Come on grate the Cheese, the customers are waiting!")
                time.sleep(5)
    else:
        print("Something went wrong")
#POUR SALT
def salt():
    if "Salt" in preparation:
        print("You have already salted it! ")
        decision(order_number, order_pizza_name)
    elif "Salt" not in preparation:
        print("""Ok, so you now are going to put some salt on it...
SALT BAE STYLE ! \n¯\_(▀̿Ĺ̯▀̿ ̿ \n You know
In order to do it, you need to press 'S' as many times as you want.""")
        input("\033[1m<Press ENTER to continue>\033[0m")

        print("""/$$$$$$$                            /$$
| $$__  $$                          | $$
| $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$$ /$$   /$$
| $$$$$$$/ /$$__  $$ |____  $$ /$$__  $$| $$  | $$
| $$__  $$| $$$$$$$$  /$$$$$$$| $$  | $$| $$  | $$
| $$  \ $$| $$_____/ /$$__  $$| $$  | $$| $$  | $$
| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$$ /$$ /$$ /$$
|__/  |__/ \_______/ \_______/ \_______/ \____  $$|__/|__/|__/
                                         /$$  | $$
                                        |  $$$$$$/
                                         \______/             """)
        time.sleep(3)
        print("""GGGGGGGGGGGGG     OOOOOOOOO           !!!
     GGG::::::::::::G   OO:::::::::OO        !!:!!
   GG:::::::::::::::G OO:::::::::::::OO      !:::!
  G:::::GGGGGGGG::::GO:::::::OOO:::::::O     !:::!
 G:::::G       GGGGGGO::::::O   O::::::O     !:::!
G:::::G              O:::::O     O:::::O     !:::!
G:::::G              O:::::O     O:::::O     !:::!
G:::::G    GGGGGGGGGGO:::::O     O:::::O     !:::!
G:::::G    G::::::::GO:::::O     O:::::O     !:::!
G:::::G    GGGGG::::GO:::::O     O:::::O     !:::!
G:::::G        G::::GO:::::O     O:::::O     !!:!!
 G:::::G       G::::GO::::::O   O::::::O      !!!
  G:::::GGGGGGGG::::GO:::::::OOO:::::::O
   GG:::::::::::::::G OO:::::::::::::OO       !!!
     GGG::::::GGG:::G   OO:::::::::OO        !!:!!
        GGGGGG   GGGG     OOOOOOOOO           !!! """)
        while True:
            x = input("PUT SOME SALT! SALT BAE STYLE ! \n¯\_(▀̿Ĺ̯▀̿ ̿)\n (PRESS 'SSSS..' AS MANY TIMES YOU WANT, BUT REMEMBER, DON'T MAKE IT TOO SALTY!\n hint:(between 3 and 7 's' is best)").lower()
            if "s" not in x:
                import random
                random_list = ["the soap",
                               "my thing",
                               "the phone",
                               "that rat",
                               "your hair",
                               "the soda",
                               "our food",
                               "my hat",
                               "your head in the oven",
                               "your hands in the soup",
                               "your feet in the freezer",
                               ]
                rand = random.randint(0, len(random_list))
                print(
                    f"\t\t\t\t\t(ಠ_ಠ)\nWhat are you doing with {random_list[rand]}?\n The customers are waiting!")
                time.sleep(5)
            else:

                count = x.count("s")
                print("\t\t\t\t\tヘ( ^o^)ノ＼(^_^ ) \n Good job! You put some salt on it!")
                decisions_taken.append("Salt")
                preparation.update({"Salt": count})
                input("\033[1m<Press ENTER to continue>\033[0m")
                decision(order_number, order_pizza_name)
                break
    else:
        print("Something went wrong")
#PUT ANCHOVIES
def anchovies():
    count = 0
    print("""Ok, so you now are going to put some anchovies on it...
Spread them away
In order to do it, press 'R', then 'D', then 'C', then 'B', then 'H', then 'Y' and finally [ENTER]'""")
    input("\033[1m<Press ENTER to continue>\033[0m")

    print("""/$$$$$$$                            /$$
| $$__  $$                          | $$
| $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$$ /$$   /$$
| $$$$$$$/ /$$__  $$ |____  $$ /$$__  $$| $$  | $$
| $$__  $$| $$$$$$$$  /$$$$$$$| $$  | $$| $$  | $$
| $$  \ $$| $$_____/ /$$__  $$| $$  | $$| $$  | $$
| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$$ /$$ /$$ /$$
|__/  |__/ \_______/ \_______/ \_______/ \____  $$|__/|__/|__/
                                         /$$  | $$
                                        |  $$$$$$/
                                         \______/             """)
    time.sleep(3)
    print("""GGGGGGGGGGGGG     OOOOOOOOO           !!!
     GGG::::::::::::G   OO:::::::::OO        !!:!!
   GG:::::::::::::::G OO:::::::::::::OO      !:::!
  G:::::GGGGGGGG::::GO:::::::OOO:::::::O     !:::!
 G:::::G       GGGGGGO::::::O   O::::::O     !:::!
G:::::G              O:::::O     O:::::O     !:::!
G:::::G              O:::::O     O:::::O     !:::!
G:::::G    GGGGGGGGGGO:::::O     O:::::O     !:::!
G:::::G    G::::::::GO:::::O     O:::::O     !:::!
G:::::G    GGGGG::::GO:::::O     O:::::O     !:::!
G:::::G        G::::GO:::::O     O:::::O     !!:!!
 G:::::G       G::::GO::::::O   O::::::O      !!!
  G:::::GGGGGGGG::::GO:::::::OOO:::::::O
   GG:::::::::::::::G OO:::::::::::::OO       !!!
     GGG::::::GGG:::G   OO:::::::::OO        !!:!!
        GGGGGG   GGGG     OOOOOOOOO           !!! """)
    if "Knead the Dough" not in preparation:
        print("How can you put the anchovies!! The dough is not ready")
        decision(order_number, order_pizza_name)
    if "Put the Anchovies" in preparation:
        print("You have already placed the anchovies! ")
        decision(order_number, order_pizza_name)
    elif "Put the Anchovies" not in preparation:
        while True:
            x = input(
                "\n\n\nPLACE THE ANCHOVIES! \n\n (PRES 'R', then 'D', then 'C', then 'B', then 'H', finally 'Y' TO PLACE THE ANCHOVIES. FINALLY PRESS ENTER. \n hint:(You should get: 'rdcbhy')  )").lower()
            print(x)
            if x == "rdcbhy":
                count += 1
                if count == 1:
                    print("\n\n\t\t\t\t\tヘ( ^o^)ノ＼(^_^ ) \n Good job! The anchovies are in the pizza now!")
                    decisions_taken.append("Cheese")
                    preparation.update({"Put the Anchovies": 1})
                    input("\033[1m<Press ENTER to continue>\033[0m")
                    decision(order_number, order_pizza_name)
                    break
            else:
                import random
                random_list = ["the soap",
                               "my thing",
                               "the phone",
                               "that rat",
                               "your hair",
                               "the soda",
                               "our food",
                               "my hat",
                               "your head in the oven",
                               "your hands in the soup",
                               "your feet in the freezer",
                               ]
                rand = random.randint(0, len(random_list) - 1)
                print(
                    f"\t\t\t\t\t(ಠ_ಠ)\nThis is not how you place the anchovies.\nWhat are you doing with {random_list[rand]}? Come on grate the Cheese, the customers are waiting!")
                time.sleep(5)
    else:
        print("Something went wrong")
#PUT OIL
def oil():
    if "Put Olive Oil" in preparation:
        print("You have already put oil on it! ")
        decision(order_number, order_pizza_name)
    elif "Put Olive Oil" not in preparation:
        print("""Ok, so you now are going to put some oil on it...
In order to do it, you need to press 'O' as many times as you want.""")
        input("\033[1m<Press ENTER to continue>\033[0m")

        print("""/$$$$$$$                            /$$
| $$__  $$                          | $$
| $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$$ /$$   /$$
| $$$$$$$/ /$$__  $$ |____  $$ /$$__  $$| $$  | $$
| $$__  $$| $$$$$$$$  /$$$$$$$| $$  | $$| $$  | $$
| $$  \ $$| $$_____/ /$$__  $$| $$  | $$| $$  | $$
| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$$ /$$ /$$ /$$
|__/  |__/ \_______/ \_______/ \_______/ \____  $$|__/|__/|__/
                                         /$$  | $$
                                        |  $$$$$$/
                                         \______/             """)
        time.sleep(3)
        print("""GGGGGGGGGGGGG     OOOOOOOOO           !!!
     GGG::::::::::::G   OO:::::::::OO        !!:!!
   GG:::::::::::::::G OO:::::::::::::OO      !:::!
  G:::::GGGGGGGG::::GO:::::::OOO:::::::O     !:::!
 G:::::G       GGGGGGO::::::O   O::::::O     !:::!
G:::::G              O:::::O     O:::::O     !:::!
G:::::G              O:::::O     O:::::O     !:::!
G:::::G    GGGGGGGGGGO:::::O     O:::::O     !:::!
G:::::G    G::::::::GO:::::O     O:::::O     !:::!
G:::::G    GGGGG::::GO:::::O     O:::::O     !:::!
G:::::G        G::::GO:::::O     O:::::O     !!:!!
 G:::::G       G::::GO::::::O   O::::::O      !!!
  G:::::GGGGGGGG::::GO:::::::OOO:::::::O
   GG:::::::::::::::G OO:::::::::::::OO       !!!
     GGG::::::GGG:::G   OO:::::::::OO        !!:!!
        GGGGGG   GGGG     OOOOOOOOO           !!! """)
        while True:
            x = input(
                "POUR SOME OIL ON IT! (PRESS 'OOOO..' AS MANY TIMES YOU WANT, BUT REMEMBER, DON'T MAKE IT TOO OILY!\n hint:(between 3 and 7 'O' is best)").lower()
            if "o" not in x:
                import random
                random_list = ["the soap",
                               "my thing",
                               "the phone",
                               "that rat",
                               "your hair",
                               "the soda",
                               "our food",
                               "my hat",
                               "your head in the oven",
                               "your hands in the soup",
                               "your feet in the freezer",
                               ]
                rand = random.randint(0, len(random_list))
                print(
                    f"\t\t\t\t\t(ಠ_ಠ)\nWhat are you doing with {random_list[rand]}?\n The customers are waiting!")
            else:
                count = x.count("o")
                print("\t\t\t\t\tヘ( ^o^)ノ＼(^_^ ) \n Good job! You put some oil on it!")
                decisions_taken.append("Oil")
                preparation.update({"Put Olive Oil": count})
                input("\033[1m<Press ENTER to continue>\033[0m")
                decision(order_number, order_pizza_name)
                break
    else:
        print("Something went wrong")
#COOKING
def cook(order_number):

    while True:
        cook_time = input(f"""How much time do we cook the pizza, {name}?
2 minutes

5 minutes

10 minutes""")
        if "2" or "two" in cook_time:
            cook_time = 2
            break
        elif "5" or "five" in cook_time:
            cook_time = 5
            break
        elif "10" or "ten" in cook_time:
            cook_time = 10
            break
        else:
            print("Could you please repeat?")

    input("\033[1m<Press ENTER to cook the pizza in the oven>\033[0m")

    start_cooking = time.time()
    time_to_cook = 11 - skills[2] #The time to cook will be reduced depending on how many skills points the player puts in cooking master
    ends_cooking = start_cooking + time_to_cook
    while time.time() < ends_cooking:
        print("""\033[31m
                        /\\
                       /  \\
                      /    \\
                     '-.__.-'
                      |    |
                      |    |
                      |    |
          ____________'____'___________
       .'                              )
     .'                              .'
   .' /                            .' )
 .' (_)                          .' ).(
.'_____________________________ .' ).' (
(      `..-_______________`..)_.' (.' )(
.-')_.--.'.---------------.(.'.'.' ).' )
'.-._|      |            [=]-._) ).' (.'
( _.'|      |_____________|(_.-..' ).' (
'._ |     .'              |.--.' (.' ) )
'.--|   .' \033[1mCOOKING        \033[31m|'.__).' (.'.(
(.-.| .'                 [=] '-.' ).'( )
'._)|'____________________|(_.-..' ).' (
|.'=-._.-.'---------------'--._' ).' (.'_____
.(.-. .-. .'     ) `.(     `.   ) (.' .'    .|
.' (_.'(_.'(_.-._.''-._)`._.-_.).'-.' .'  .' |
.' .'//////////////////////////////.'   .'   |
.'_.'__________ _ ______________ _.'_ .'  .' |
|  |(())  (()) | | .---------.  | |  |  .'  .|
|  | ||    ||  | | |         [] | |  |.'  .' |
|  | ||    ||  | | | ]       |  | |  |  .'  .|
|  | ||    ||  | | |         |  | |  |.'  .'.
|  |.--.  .--. | | |         [] | |  |  .'.'
|  |\ __\ \\\\ | | '---------'  | |  |.'.'
|__|___________|_|______________|_|__|.'""")
        time.sleep(time_to_cook)
    print("""\033[32m
                            /\\
                           /  \\
                          /    \\
                         '-.__.-'
                          |    |
                          |    |
                          |    |
              ____________'____'___________
           .'                              )
         .'                              .'
       .' /                            .' )
     .' (_)                          .' ).(
    .'_____________________________ .' ).' (
    (      `..-_______________`..)_.' (.' )(
    .-')_.--.'.---------------.(.'.'.' ).' )
    '.-._|      |            [=]-._) ).' (.'
    ( _.'|      |_____________|(_.-..' ).' (
    '._ |     .'              |.--.' (.' ) )
    '.--|   .'   \033[1mREADY  \033[32m   |'.__).' (.'.(
    (.-.| .'                 [=] '-.' ).'( )
    '._)|'____________________|(_.-..' ).' (
    |.'=-._.-.'---------------'--._' ).' (.'_____
    .(.-. .-. .'     ) `.(     `.   ) (.' .'    .|
    .' (_.'(_.'(_.-._.''-._)`._.-_.).'-.' .'  .' |
    .' .'//////////////////////////////.'   .'   |
    .'_.'__________ _ ______________ _.'_ .'  .' |
    |  |(())  (()) | | .---------.  | |  |  .'  .|
    |  | ||    ||  | | |         [] | |  |.'  .' |
    |  | ||    ||  | | | ]       |  | |  |  .'  .|
    |  | ||    ||  | | |         |  | |  |.'  .'.
    |  |.--.  .--. | | |         [] | |  |  .'.'
    |  |\ __\ \\\\ | | '---------'  | |  |.'.'
    |__|___________|_|______________|_|__|.'""")

    input("\033[1m<Press ENTER to deliver the pizza to the customer>\033[0m")
    preparation.update({"Cook the Pizza":cook_time})


#MAIN
#Creating the dictionaries of the pizzas. These dictionaries will be the reference to compare what the player built against the ideal, which are these dictionaries.
Margherita = {
    "Knead the Dough": 1,
    "Salt": 5,
    "Put Olive Oil": 5,
    "Smash Tomatoes": 1,
    "Grate the Cheese": 1,
    "Cook the Pizza": 4
}

Peperoni = {
    "Knead the Dough": 1,
    "Salt": 5,
    "Put Olive Oil": 3,
    "Smash Tomatoes": 1,
    "Grate the Cheese": 1,
    "Cut Peperoni": 1,
    "Cook the Pizza": 6
}

Napoletana = {
    "Knead the Dough": 1,
    "Salt": 3,
    "Put Olive Oil": 5,
    "Smash Tomatoes": 1,
    "Grate the Cheese": 1,
    "Put the Anchovies": 1,
    "Cook the Pizza": 5
}

Menu = [Margherita, Peperoni, Napoletana] #The list will store the dictionaries, it will be handy to randomly pick an order and to refer to access to each dicctionary in customer_feedback()
decisions_taken = []
skills = [0, 0, 0] #Where the skill points will be stored.
#decision_list = ["Knead the Dough", "Salt", "Put Olive Oil", "Smash Tomatoes", "Grate the Cheese", "Cut Peperoni", "Put the Anchovies", "Cook the Pizza"]

while True:
    disclaimer()
    start = time.time()
    time_to_play = 420.0 #Time to play in seconds
    end_time = start + time_to_play
    while time.time() < end_time:
        preparation = {}  # This dictionary will store what pizza the player builds
        order_pizza_name, order_number = customer_order()
        order_number = decision(order_number, order_pizza_name)
        customer_feedback(Menu, order_number, preparation)

        answer = input("\n\nWould you like to take another customer, start over or finish the game?\n\n 1) Take another customer\n 2) Start over\n 3) Finish the game").lower()
        if "1" in answer or "another" in answer or "customer" in answer:
            pass

        elif "2" in answer or "start" in answer or "over" in answer:
            break

        elif "3" in answer or "finish" in answer or "game" in answer:
            sys.exit(0)

        else:
            sys.exit(0)
