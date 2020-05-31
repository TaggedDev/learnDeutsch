from tkinter import *  
from tkinter.ttk import Checkbutton
from tkinter import messagebox
import googletrans as gt 
from googletrans import Translator
import random as rnd

root = Tk()
translator = Translator()

#VARIABLES
themes = ['MEETING', 'FAMILY', 'PRODUCTS', 'RESTAURANT', 'FURNITURE', 'SCHEDULE', 'HOBBY', 'WORK', 'ROAD', 'HEALTH', 'CLOTHES', 'HOLIDAYS', 'WEATHER', 'PLANS']

wordsMeeting = ['Hello', 'Good morning', 'Good afternoon', 'Good evening', 'Good night', 'Welcome', 'Goodbye', 'Bye', 'See you tomorrow', 'My name is', 'I am from Russia', 'I am sorry', 'Please', 'Thanks', 'Good luck']
wordsFamily = ['Family', 'Parents', 'Mom', 'Dad', 'Sister', 'Brother', 'Son', 'Daughter', 'Boy', 'Girl', 'Grandmother', 'Grandfather', 'Children', 'Child', 'Simblings','Husband','Wife']
wordsProducts = ['Water', 'Food', 'Milk', 'Juice', 'Tea', 'Bread', 'Egg', 'Potato', 'Rice', 'Mushroom', 'Meat', 'Tomato', 'Cucumber', 'Squash', 'Carrot', 'Onion', 'Garlic', 'Apple', 'Banana', 'Yogurt', 'Cheese', 'Salt', 'Sugar']
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

wordsDict = {'MEETING':wordsMeeting, 'FAMILY':wordsFamily, 'PRODUCTS':wordsProducts, 'RESTAURANT':wordsRestaurant, 'FURNITURE':wordsFurniture, 'SCHEDULE':wordsSchedule, 'HOBBY':wordsHobby, 'WORK':wordsWork, 'ROAD':wordsRoad, 'HEALTH':wordsHealth, 'CLOTHES':wordsClothes, 'HOLIDAYS':wordsHolidays, 'WEATHER':wordsWeather, 'PLANS':wordsPlans}

number = rnd.randint(0, len(wordsFamily)-1)
nouns = 1
userChosed = 0
correctAnswerText = ''
message = StringVar()


userChoose = StringVar(root) # need for optionmenu work
userChoose.set("MEETING")

# BEGIN GUI

root.resizable(False, False)
root.geometry('400x500')
root.title('Deutsch Learning Helper')
root[ 'bg' ] = '#454545'
root.iconbitmap( 'E:\!CODE\Deutsch\LearnRU-DE\icon.ico' )

# === BUTTONS FUNCTIONS ===

def guessTheList(userList):
    global nouns
    global userChosed
    if userList == 'MEETING':
        nouns = 0
        userChosed = userList
    else:
        nouns = 1
        userChosed = userList

def checkTheAnswer():  
    global correctAnswerText
    words = wordsDict[userChosed]
    userAnswer = message.get()

    correctAnswerText = 'Smthing'

    if nouns == 1:
        result = translator.translate(f'the {words[number]}', src='en', dest='de')
    elif nouns == 0:
        result = translator.translate(f'{words[number]}', src='en', dest='de')
    
    aiAnswer = result.text.casefold() # lowercasing the word
    userAnswer = userAnswer.casefold() # lowercasing the answer

    if userAnswer == aiAnswer:
        correctAnswerText = "Correct!"
        print(correctAnswerText)
    else:
        correctAnswerText = "Incorrect! The right answer is"
        



# === GIU INTERFACE FIELDS ===

navTitle = Label(text="WORDS TRANSLATE & REMEMBER", fg="#919191", bg="#454545", font="Roboto 15", pady="7")
themesMenu = OptionMenu(root, userChoose, *themes, command=guessTheList)
translateWord = Label(text=f"{wordsFamily[number].upper()}", fg="#abedff", bg="#454545", font="Roboto 15", pady="7", padx='18',bd="2", relief="solid", width="30")
inputTranslate = Entry(fg="#fff", bg="#666666", font="Roboto 15", relief="solid", textvariable=message)
inputTranslate.focus()
checkButton = Button( text="Check", font="Roboto 15", bg="#cfcfcf", fg="#404040", activebackground="#454545", activeforeground="#cfcfcf", relief="solid", width="12", command=checkTheAnswer)
correctAnswer = Label(text=correctAnswerText, fg="#fff", bg="#454545", font="Roboto 15", pady="7", padx='18')
nextButton = Button( text="►►►", font="20", bg="#cfcfcf", fg="#168a1c", activebackground="#454545", activeforeground="#168a1c", height="1")

navTitle.pack()
themesMenu.pack()
themesMenu.config(font='Roboto 12', bg="#cfcfcf", fg="#000", activebackground="#454545", activeforeground="#fff", width="15")
themesMenu['menu'].config(font='Roboto 15', bg='white')
translateWord.pack(pady="13")
inputTranslate.pack(pady="60")
checkButton.pack()
correctAnswer.pack(pady="22")
nextButton.pack()

root.mainloop()