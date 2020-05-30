import googletrans as gt 
import random as rnd
from googletrans import Translator

# ===START===
translator = Translator()
themes = ['Meeting', 'Family', 'Products', 'In the restaurant', 'Furniture', 'Schedule', 'Entertainment', 'Work', 'Road', 'Health', 'Clothes', 'Holidays', 'Weather', 'Plans']

wordsMeeting = ['Hello!', 'Good morning', 'Good day', 'Good evening', 'Good night', 'Welcome', 'Goodbye', 'Bye!', 'See you tomorrow!', 'My name is', 'I am from Russia', 'I am sorry', 'Please', 'Thank you', 'Good luck!']
wordsFamily = ['Family', 'Parents', 'Mom', 'Dad', 'Sister', 'Brother', 'Son', 'Daughter', 'Boy', 'Girl', 'Grandmother', 'Grandfather', 'Children', 'Child', 'Siblings','Husband','Wife']
wordsProducts = ['Water', 'Food', 'Milk', 'Juice', 'Tea', 'Bread', 'Egg', 'Patato', 'Rice', 'Mushroom', 'Meat', 'Tomato', 'Cucumber', 'Кабачок', 'Carrot', 'Onion', 'Garlic', 'Apple', 'Банан', 'Yogurt', 'Cheeze', 'Salt', 'Sugar']
wordsRestaurant = []
wordsFurniture = []
wordsSchedule = []
wordsHobby = []
wordsWork = []
wordsRoad = []
wordsHealth = []
wordsClothes = []
wordsHolidays = []
wordsWeather = []
wordsPlans = []

wordsDict = {0:wordsMeeting, 1:wordsFamily, 2:wordsProducts, 3:wordsRestaurant, 4:wordsSchedule, 5:wordsHobby, 6:wordsWork, 7:wordsRoad, 8:wordsHealth, 9:wordsClothes, 10:wordsWeather, 11:wordsPlans}

def start():
    counter = 0

    for i in themes:
        print(f'{counter} - {i}')
        counter += 1

    print("\n")
    userChoose = int(input("Choose the topic: "))
    print("\n")
    
    def question():
        while True:
            words = wordsDict[userChoose]
            length = len(words) - 1
            number = rnd.randint(0, length) # рандомим слово из списка
            
            print(f'Translate the word: the {words[number]}')
            print()
            userAnswer = input("Type: ")
            print()
                
            result = translator.translate(f'the {words[number]}', src='en', dest='de')
            aiAnswer = result.text.casefold()
            userAnswer = userAnswer.casefold()
            
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

#comments