from tkinter import *  
from tkinter.ttk import Checkbutton
from tkinter import messagebox as mb
import googletrans as gt 
from googletrans import Translator
import random as rnd

root = Tk()
translator = Translator()

#VARIABLES
themes = ['MEETING', 'FAMILY', 'PRODUCTS', 'RESTAURANT', 'FURNITURE', 'SCHEDULE', 'HOBBY', 'WORK', 'ROAD', 'HEALTH', 'CLOTHES','WEATHER', 'PLANS', 'QUESTIONS', 'BODY']

wordsMeeting = ['Hello', 'Good morning', 'Good afternoon', 'Good evening', 'Good night', 'Welcome', 'Goodbye', 'Bye', 'See you tomorrow', 'My name is', 'I am from Russia', 'I am sorry', 'Please', 'Thanks', 'Good luck']
wordsFamily = ['Family', 'Parents', 'Mom', 'Dad', 'Sister', 'Brother', 'Son', 'Daughter', 'Boy', 'Girl', 'Grandmother', 'Grandfather', 'Children', 'Child', 'Simblings','Husband','Wife']
wordsProducts = ['Water', 'Food', 'Milk', 'Juice', 'Tea', 'Bread', 'Egg', 'Potato', 'Rice', 'Mushroom', 'Meat', 'Tomato', 'Cucumber', 'Squash', 'Carrot', 'Onion', 'Garlic', 'Apple', 'Banana', 'Yogurt', 'Cheese', 'Salt', 'Sugar']
wordsRestaurant = ['Restaurant', 'Order', 'Food', 'Drinks', 'Appetizer', 'Side dish', 'Dessert', 'Waiter', 'Soup', 'Salad', 'Tea']
wordsFurniture = ['Bed', 'Sofa', 'Chair', 'Table', 'Armchair', 'Carpet', 'Wardrobe', 'House', 'Flat', 'Furniture', 'Window', 'Door', 'Wall', 'Roof', 'Floor', 'Kitchen', 'Living room', 'Canteen', 'Bedroom', 'Toilet', 'Ceiling']
wordsSchedule = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Week', 'Month', 'Weekends', 'Holidays']
wordsHobby = ['Bike', 'Skateboard', 'Ski', 'Snowboard', 'Chess', 'Basketball', 'Football', 'Domino', 'Cards', 'Board games', 'Computer games', 'Guitar', 'Piano', 'Book']
wordsWork = ['Worker', 'Doctor','Baker','postman','Engineer','Chef','Teacher','musician','policeman','sportsman','writer','dancer','seller','assistant','farmer','artist','butcher','clown','fisher']
wordsRoad = ['departure','airport','arrival','terminal','autobus','taxi','train','ticker office','bike','speed','road','traffic light','car','bus stop']
wordsHealth = ['Health','Pharmacy','Medic','patient','Doctor','diagnosis','dentist','oculist','operation','pills','medicine','bandage','injection','infection','temperature','pain','flu','cut']
wordsClothes = ['socks','boot','sneaker','shoe','pants','shorts','jeans','trousers','underwear','belt','shirt','t-shirt','hoodie','long-sleeve','sweater','scarf','glasses','hat','fedora','cap','coat','jacket']
wordsWeather = ['rain','fog','cloud','sun','snow','blizzard','heat','shadow','cold','frost','snowfall','storm','wind']
wordsPlans = ['Clinic', 'Pharmacy', 'Cinema', 'Theater', 'Zoo', 'Park', 'Aquapark', 'Botanic Garden', 'Planetarium', 'Seaquarium', 'Opera']
wordsQuestions = ['Who is it', 'Where is it', 'When is it', 'What is it', 'Where', 'Why', 'How', 'Which', 'How much', 'Whose']
wordsBody = ['head','eye','forehead','nose','nostril','lip','mouth','tongue','tooth','skull','chin','neck','chest','arm','shoulder','elbow','wrist','hand','finger','palm','belly','body','hip','knee','foot','toe','nail']

wordsDict = {'MEETING':wordsMeeting, 'FAMILY':wordsFamily, 'PRODUCTS':wordsProducts, 'RESTAURANT':wordsRestaurant, 'FURNITURE':wordsFurniture, 'SCHEDULE':wordsSchedule, 'HOBBY':wordsHobby, 'WORK':wordsWork, 'ROAD':wordsRoad, 'HEALTH':wordsHealth, 'CLOTHES':wordsClothes, 'WEATHER':wordsWeather, 'PLANS':wordsPlans, 'QUESTIONS':wordsQuestions, 'BODY':wordsBody}

nouns = 1
number = 0
userChosed = 0
correctAnswerText = ''
correctAnswerTextAI = ''
translateWord = 'Press >>> button to start'
isChecked = 0

message = StringVar()


userChoose = StringVar(root) # need for optionmenu work
userChoose.set("- - - - - - - - - - - - - -")

# BEGIN GUI

root.resizable(False, False)
root.geometry('400x600')
root.title('Deutsch Learning Helper')
root[ 'bg' ] = '#454545'
root.iconbitmap( 'icon.ico' )

# === BUTTONS FUNCTIONS ===

def guessTheList(userList):
    global nouns
    global userChosed
    if userList == 'MEETING':
        nouns = 0
        userChosed = userList
    elif userList == 'QUESTIONS':
        nouns = 2
        userChosed = userList
    else:
        nouns = 1
        userChosed = userList

def checkTheAnswer():  
    global isChecked
    words = wordsDict[userChosed]
    userAnswer = message.get()

    if nouns == 1:
        result = translator.translate(f'the {words[number-1]}', src='en', dest='de')
    elif nouns == 0:
        result = translator.translate(f'{words[number-1]}', src='en', dest='de')
    elif nouns == 2:
        result = translator.translate(f'{words[number-1]}?', src='en', dest='de')
    
    if result.text.casefold() == userAnswer.casefold(): # COMPARING THE LOWERCASED ANSWERS
        correctAnswer.config(text="")
        correctAnswerAI.config(fg="#168a1c")
        correctAnswerAI.config(text='Correct!')
    else:
        correctAnswer.config(text="Incorrect! The right answer is:", fg="#fff")
        correctAnswerAI.config(text=f"{result.text.upper()}", fg="#c4002b")
    isChecked = 1
    
def nextWord():
    global translateWord
    global number

    try:
        words = wordsDict[userChosed]
        number = rnd.randint(0, len(words))
        length = number-1
        # RANDOMING A WORD FROM A [USERCHOSED] LIST  AND PUTTING IT IN [TRANSLATEWORD] VAR
        translateWord.config(text=words[length].upper())
        correctAnswerAI.config(text="")
        correctAnswer.config(text="")
        inputTranslate.delete(0, 'end')
    except:
        translateWord.config(text="CHOOSE THE (DIFFERENT) THEME")
    
def helpButton():
    mb.showerror('Help ALT-CODES commands', '0252 - ü, 0246 - ö, 0228 - ä')

def nextWordEnter(event): # ON ENTER PRESSED SKIPPING THE WORD
    global translateWord
    global number
    global isChecked

    try:
        if isChecked == 1:
            words = wordsDict[userChosed]
            number = rnd.randint(0, len(words))
            length = number-1
            # RANDOMING A WORD FROM A [USERCHOSED] LIST  AND PUTTING IT IN [TRANSLATEWORD] VAR
            translateWord.config(text=words[length].upper())
            correctAnswerAI.config(text="")
            correctAnswer.config(text="")
            inputTranslate.delete(0, 'end')
            isChecked = 0
        elif isChecked == 0:
            words = wordsDict[userChosed]
            userAnswer = message.get()

            if nouns == 1:
                result = translator.translate(f'the {words[number-1]}', src='en', dest='de')
            elif nouns == 0:
                result = translator.translate(f'{words[number-1]}', src='en', dest='de')
            elif nouns == 2:
                result = translator.translate(f'{words[number-1]}?', src='en', dest='de')
            
            if result.text.casefold() == userAnswer.casefold(): # COMPARING THE LOWERCASED ANSWERS
                correctAnswer.config(text="")
                correctAnswerAI.config(fg="#168a1c")
                correctAnswerAI.config(text='Correct!')
                isChecked = 1
            else:
                correctAnswer.config(text="Incorrect! The right answer is:", fg="#fff")
                correctAnswerAI.config(text=f"{result.text.upper()}", fg="#c4002b")
                isChecked = 1
    except:
        translateWord.config(text="CHOOSE THE (DIFFERENT) THEME")



# === GIU INTERFACE FIELDS ===

navTitle = Label(text="WORDS TRANSLATE & REMEMBER", fg="#919191", bg="#454545", font="Roboto 15", pady="7")
themesMenu = OptionMenu(root, userChoose, *themes, command=guessTheList)
translateWord = Label(text=f"{translateWord}", fg="#abedff", bg="#454545", font="Roboto 15", pady="7", padx='18',bd="2", relief="solid", width="30")
inputTranslate = Entry(fg="#fff", bg="#666666", font="Roboto 15", relief="solid", textvariable=message)
inputTranslate.focus()
checkButton = Button( text="Check", font="Roboto 15", bg="#cfcfcf", fg="#404040", activebackground="#454545", activeforeground="#cfcfcf", relief="solid", width="12", command=checkTheAnswer)
correctAnswer = Label(text=correctAnswerText, fg="#fff", bg="#454545", font="Roboto 15")
correctAnswerAI = Label(text=correctAnswerTextAI, fg="#fff", bg="#454545", font="Roboto 15", pady="7", padx='18')
nextButton = Button( text="►►►", font="20", bg="#cfcfcf", fg="#168a1c", activebackground="#454545", activeforeground="#168a1c", height="1", command=nextWord)
helpButton = Button(text='               ?               ', font="20", bg="#454545", fg="#525252", activebackground="#454545", activeforeground="#454545", height="1", command=helpButton)

navTitle.pack(pady="5")
themesMenu.pack(pady="10")
themesMenu.config(font='Roboto 12', bg="#cfcfcf", fg="#000", activebackground="#454545", activeforeground="#fff", width="15")
themesMenu['menu'].config(font='Roboto 15', bg='white')
translateWord.pack(pady="13")
inputTranslate.pack(pady="60")
checkButton.pack()
correctAnswer.pack()
correctAnswerAI.pack(pady="5")
nextButton.pack(pady="10")
helpButton.pack(side='bottom')

root.bind('<Return>', nextWordEnter)

root.mainloop()
