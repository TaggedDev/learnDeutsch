import googletrans as gt 
import random as rnd
from colorama import Fore, Back, Style
from colorama import init
from googletrans import Translator

init()

# ===START===
translator = Translator()
themes = ['Meeting', 'Family', 'Products', 'In the restaurant', 'Furniture', 'Schedule', 'Entertainment', 'Work', 'Road', 'Health', 'Clothes', 'Holidays', 'Weather', 'Plans']

wordsMeeting = ['Hello', 'Good morning', 'Good afternoon', 'Good evening', 'Good night', 'Welcome', 'Goodbye', 'Bye', 'See you tomorrow', 'My name is', 'I am from Russia', 'I am sorry', 'Please', 'Thanks', 'Good luck']
wordsFamily = ['Family', 'Parents', 'Mom', 'Dad', 'Sister', 'Brother', 'Son', 'Daughter', 'Boy', 'Girl', 'Grandmother', 'Grandfather', 'Children', 'Child', 'Simblings','Husband','Wife']
wordsProducts = ['Water', 'Food', 'Milk', 'Juice', 'Tea', 'Bread', 'Egg', 'Patato', 'Rice', 'Mushroom', 'Meat', 'Tomato', 'Cucumber', 'Squash', 'Carrot', 'Onion', 'Garlic', 'Apple', 'Banana', 'Yogurt', 'Cheeze', 'Salt', 'Sugar']
wordsRestaurant = ['Restaurant', 'Order', 'Food', 'Drinks', 'Appetizer', 'Side dish', 'Dessert', 'Waiter', 'Soup', 'Salad', 'Tea']
wordsFurniture = ['Bed', 'Sofa', 'Chair', 'Table', 'Armchair', 'Carpet', 'Wardrobe', 'House', 'Flat', 'Furniture', 'Window', 'Door', 'Wall', 'Roof', 'Floor', 'Kitchen', 'Living room', 'Canteen', 'Bedroom', 'Toilet', 'Ceiling']
wordsSchedule = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Week', 'Month', 'Weekends', 'Holidays']
wordsHobby = []
wordsWork = []
wordsRoad = []
wordsHealth = []
wordsClothes = []
wordsHolidays = []
wordsWeather = []
wordsPlans = ['Clinic', 'Pharmacy', 'Cinema', 'Theater', 'Zoo', 'Park', 'Aquapark', 'Botanic Garden', 'Planetarium', 'Seaquarium', 'Opera']

wordsDict = {0:wordsMeeting, 1:wordsFamily, 2:wordsProducts, 3:wordsRestaurant, 4:wordsFurniture, 5:wordsSchedule, 6:wordsHobby, 7:wordsWork, 8:wordsRoad, 9:wordsHealth, 10:wordsClothes, 11:wordsHolidays, 12:wordsWeather, 13:wordsPlans}

def start():
    counter = 0
    nouns = 1

    for i in themes:
        print(f'{counter} - {i}')
        counter += 1
    
    print("\n")
    print(Fore.CYAN)
    userChoose = int(input("Choose the topic: "))
    print(Fore.RESET)
    print("\n")

    if userChoose == 0:
        nouns = 0
    
    def question():
        while True:
            words = wordsDict[userChoose]
            length = len(words) - 1
            number = rnd.randint(0, length) # randoming a word from the list
            
            if nouns == 1:
                print(Fore.GREEN, Style.BRIGHT)
                print(f'Translate the word: the {words[number]}')
                print(Fore.BLUE)
                userAnswer = input("Type: ")
                print(Fore.RESET, Style.NORMAL)
            elif nouns == 0:
                print(Fore.GREEN, Style.BRIGHT)
                print(f'Translate the word: {words[number]}')
                print(Fore.BLUE)
                userAnswer = input("Type: ")
                print(Fore.RESET, Style.NORMAL)
            
            if nouns == 1:
                print(Fore.CYAN)
                result = translator.translate(f'the {words[number]}', src='en', dest='de')
                print(Fore.RESET)
            elif nouns == 0:
                print(Fore.CYAN)
                result = translator.translate(f'{words[number]}', src='en', dest='de')
                print(Fore.RESET)
            aiAnswer = result.text.casefold() # lowercasing the word
            userAnswer = userAnswer.casefold() # lowercasing the answer


            if userAnswer == aiAnswer:
                print(Back.GREEN)
                print("Correct!")
                print(Back.RESET)
                print("\n")
            elif userAnswer == 'back':
                start()
            else:
                print(Fore.RED, Style.BRIGHT)
                print(f"Incorrect! The right answer is: {aiAnswer}")
                print("\n")
                print(Fore.RESET, Style.NORMAL)
    question()

start()



# rAlt: ü - 0252, ä - 0228, ö - 0246