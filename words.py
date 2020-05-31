import googletrans as gt 
import random as rnd
from googletrans import Translator

# ===START===
translator = Translator()
themes = ['Meeting', 'Family', 'Products', 'In the restaurant', 'Furniture', 'Schedule', 'Entertainment', 'Work', 'Road', 'Health', 'Clothes', 'Holidays', 'Weather', 'Plans']

wordsMeeting = ['Hello!', 'Good morning', 'Good day', 'Good evening', 'Good night', 'Welcome', 'Goodbye', 'Bye!', 'See you tomorrow!', 'My name is', 'I am from Russia', 'I am sorry', 'Please', 'Thank you', 'Good luck!']
wordsFamily = ['Family', 'Parents', 'Mom', 'Dad', 'Sister', 'Brother', 'Son', 'Daughter', 'Boy', 'Girl', 'Grandmother', 'Grandfather', 'Children', 'Child', 'Simblings','Husband','Wife']
wordsProducts = ['Water', 'Food', 'Milk', 'Juice', 'Tea', 'Bread', 'Egg', 'Patato', 'Rice', 'Mushroom', 'Meat', 'Tomato', 'Cucumber', 'Squash', 'Carrot', 'Onion', 'Garlic', 'Apple', 'Banana', 'Yogurt', 'Cheeze', 'Salt', 'Sugar']
wordsRestaurant = ['Restaurant', 'to order', 'to eat', 'to drink', 'Appetizer', 'Side dish', 'Dessert', 'to pay', 'Waiter', 'Soup', 'Salad', 'Tea']
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

wordsDict = {0:wordsMeeting, 1:wordsFamily, 2:wordsProducts, 3:wordsRestaurant, 4:wordsSchedule, 5:wordsHobby, 6:wordsWork, 7:wordsRoad, 8:wordsHealth, 9:wordsClothes, 10:wordsWeather, 11:wordsPlans}

def start():
    counter = 0
    nouns = 1

    for i in themes:
        print(f'{counter} - {i}')
        counter += 1

    print("\n")
    userChoose = int(input("Choose the topic: "))
    print("\n")

    if userChoose == 0:
        nouns = 0
    
    def question():
        while True:
            words = wordsDict[userChoose]
            length = len(words) - 1
            number = rnd.randint(0, length) # randoming a word from the list
            
            if nouns == 1:
                print(f'Translate the word: the {words[number]}')
                print()
                userAnswer = input("Type: ")
                print()
            elif nouns == 0:
                print(f'Translate the word: {words[number]}')
                print()
                userAnswer = input("Type: ")
                print()
            
            if nouns == 1:
                result = translator.translate(f'the {words[number]}', src='en', dest='de')
            elif nouns == 0:
                result = translator.translate(f'{words[number]}', src='en', dest='de')
            aiAnswer = result.text.casefold() # lowercasing the word
            userAnswer = userAnswer.casefold() # lowercasing the answer


            if userAnswer == aiAnswer:
                print("Correct!")
                print("\n")
            elif userAnswer == 'back':
                start()
            else:
                print(f"Incorrect! The right answer is: {aiAnswer}")
                print("\n")
    question()

start()



# rAlt: ü - 0252, ä - 0228, ö - 0246