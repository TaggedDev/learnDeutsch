from tkinter import *  
from tkinter.ttk import Checkbutton
from tkinter import messagebox as mb
import googletrans as gt 
from googletrans import Translator
import random as rnd
from PIL import ImageTk, Image

translator = Translator()



# BEGIN GUI

class Main(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = Frame(bg='#757575', bd=2)
        toolbar.pack(side="top", fill="x")
        self.translateImage = PhotoImage(file="translate.gif")
        translateButton = Button(toolbar, text="Nouns translator", command=self.openTranslate, bg="#757575", bd=0, compound=TOP, image=self.translateImage)
        translateButton.pack(side=LEFT)
        self.verbImage = PhotoImage(file="verb.gif")
        verbButton = Button(toolbar, text="Verbs conjugator", command=self.openVerb, bg="#757575", bd=0, compound=TOP, image=self.verbImage)
        verbButton.pack(side=LEFT)

    def openTranslate(self):
        Child()

    def openVerb(self):
        Verbs()

class Child(Toplevel):

    def __init__(self):
        super().__init__(root)
        self.init_child()
    
    def init_child(self):

        nouns = 1
        number = 0
        userChosed = 0
        correctAnswerText = ''
        correctAnswerTextAI = ''
        isChecked = 0
        translateWord = 'Press >>> button to start'

            # WORDS LISTS

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
            

        message = StringVar()


        userChoose = StringVar(root) # need for optionmenu work
        userChoose.set("- - - - - - - - - - - - - -")

        # CHILD GUI SETTINGS
        

        self.title('Words Remembering')
        self.geometry('400x600')
        self.resizable(False, False)
        self[ 'bg' ] = '#454545'
        self.focus_set()
        self.iconbitmap( 'icon.ico' )
    
        def guessTheList(userList):
            nonlocal nouns
            nonlocal userChosed
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
            nonlocal isChecked
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
            nonlocal translateWord
            nonlocal number

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
            nonlocal translateWord
            nonlocal number
            nonlocal isChecked

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

        navTitle = Label(self, text="WORDS TRANSLATE & REMEMBER", fg="#919191", bg="#454545", font="Roboto 15", pady="7")
        themesMenu = OptionMenu(self, userChoose, *themes, command=guessTheList)
        translateWord = Label(self, text=f"{translateWord}", fg="#abedff", bg="#454545", font="Roboto 15", pady="7", padx='18',bd="2", relief="solid", width="30")
        inputTranslate = Entry(self, fg="#fff", bg="#666666", font="Roboto 15", relief="solid", textvariable=message)
        inputTranslate.focus()
        checkButton = Button(self, text="Check", font="Roboto 15", bg="#cfcfcf", fg="#404040", activebackground="#454545", activeforeground="#cfcfcf", relief="solid", width="12", command=checkTheAnswer)
        correctAnswer = Label(self, text=correctAnswerText, fg="#fff", bg="#454545", font="Roboto 15")
        correctAnswerAI = Label(self, text=correctAnswerTextAI, fg="#fff", bg="#454545", font="Roboto 15", pady="7", padx='18')
        nextButton = Button(self, text="►►►", font="20", bg="#cfcfcf", fg="#168a1c", activebackground="#454545", activeforeground="#168a1c", height="1", command=nextWord)
        helpButton = Button(self, text='               ?               ', font="20", bg="#454545", fg="#525252", activebackground="#454545", activeforeground="#454545", height="1", command=helpButton)

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

        self.bind('<Return>', nextWordEnter)

class Verbs(Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_verbs()

    def init_verbs(self):

        # WINDOW SETTINGS

        pronoun = ['Я', 'Ты', 'Мы', 'Вы', 'Он', 'Она', 'Они']
        verb = ['dance', 'sing', 'play', 'do', 'hear', 'speak', 'understand', 'buy', 'have', 'build', 'ask', 'love', 'answer', 'work', 'want', 'give', 'drink', 'come', 'write', 'draw', 'know', 'fly', 'call', 'go', 'speak', 'bring']
        message = StringVar()
        correctAnswerText = ''
        correctAnswerTextAI = ''
        pronounTranslate = ''
        verbNumber = 0
        pronounNumber = 0
        sentence = ''
        isChecked = 0
        

        def CheckVerb():
            try:
                result = translator.translate(f'{sentence}', src='en', dest='de')
                result = result.text.casefold()

                userAnswer = message.get()
                userAnswer = userAnswer.casefold()
                

                if result == userAnswer: # COMPARING THE LOWERCASED ANSWERS
                    correctAnswer.config(text="")
                    correctAnswerAI.config(fg="#168a1c")
                    correctAnswerAI.config(text='Correct!')
                else:
                    correctAnswer.config(text="Incorrect! The right answer is:", fg="#fff")
                    correctAnswerAI.config(text=f"{result.upper()}", fg="#c4002b")
            except:
                verbLabel.config(text="PRESS THE ►►► BUTTON FIRST!")

        def NextVerb(): # === FIRST & TRANSLATE ===
            nonlocal pronounNumber
            nonlocal verbNumber
            nonlocal sentence
            try:
                verbNumber = rnd.randint(0, len(verb)-1)
                pronounNumber = rnd.randint(0, len(pronoun)-1)
                    

                pronounTranslate = translator.translate(f'{pronoun[pronounNumber]}', src='ru', dest='en')
                pronounTranslate = pronounTranslate.text.casefold()
                

                if pronounTranslate == 'i am' or pronounTranslate == 'am i':
                    pronounTranslate = 'I'
                elif pronounTranslate == 'you are' or pronounTranslate == 'are you':
                    pronounTranslate = 'You'
                elif pronounTranslate == 'we are' or pronounTranslate ==  'are we':
                    pronounTranslate = 'We'
                elif pronounTranslate == 'he is' or pronounTranslate == 'is he':
                    pronounTranslate = 'He'
                elif pronounTranslate == 'she is' or pronounTranslate == 'is she':
                    pronounTranslate = 'She'
                elif pronounTranslate == 'it is' or pronounTranslate == 'is it':
                    pronounTranslate = 'It'
                elif pronounTranslate == 'they are' or pronounTranslate == 'are they':
                    pronounTranslate = 'They'

                if pronounTranslate == 'he' or pronounTranslate == 'she' or pronounTranslate == 'it' or pronounTranslate == 'He' or pronounTranslate == 'She' or pronounTranslate == 'It':
                    if verb[verbNumber] == 'do' or verb[verbNumber] == 'go':
                        sentence = f'{pronounTranslate} {verb[verbNumber]}es'
                        verbLabel.config(text=f'{sentence.upper()}')
                    elif (pronounTranslate == 'he' or pronounTranslate == 'she' or pronounTranslate == 'it' or pronounTranslate == 'He' or pronounTranslate == 'She' or pronounTranslate == 'It') and verb[verbNumber] == 'fly':
                        sentence = f'{pronounTranslate} flies'
                        verbLabel.config(text=f'{sentence.upper()}')
                    elif (pronounTranslate == 'he' or pronounTranslate == 'she' or pronounTranslate == 'it' or pronounTranslate == 'He' or pronounTranslate == 'She' or pronounTranslate == 'It') and verb[verbNumber] == 'have':
                        sentence = f'{pronounTranslate} has'
                        verbLabel.config(text=f'{sentence.upper()}')
                    else:
                        sentence = f'{pronounTranslate} {verb[verbNumber]}s'
                        verbLabel.config(text=f'{sentence.upper()}')
                else:
                    sentence = f'{pronounTranslate} {verb[verbNumber]}'
                    verbLabel.config(text=f'{sentence.upper()}')


                correctAnswerAI.config(text="")
                correctAnswer.config(text="")
                verbEntry.delete(0, 'end')
            except:
                verbLabel.config(text="PRESS THE ►►► BUTTON FIRST!")

        def NextVerbEnter(event):
            nonlocal pronounNumber
            nonlocal verbNumber
            nonlocal sentence
            nonlocal isChecked

            if isChecked == 0:
                try:
                    result = translator.translate(f'{sentence}', src='en', dest='de')
                    result = result.text.casefold()

                    userAnswer = message.get()
                    userAnswer = userAnswer.casefold()
                    

                    if result == userAnswer: # COMPARING THE LOWERCASED ANSWERS
                        correctAnswer.config(text="")
                        correctAnswerAI.config(fg="#168a1c")
                        correctAnswerAI.config(text='Correct!')
                    else:
                        correctAnswer.config(text="Incorrect! The right answer is:", fg="#fff")
                        correctAnswerAI.config(text=f"{result.upper()}", fg="#c4002b")
                    isChecked = 1
                except:
                    verbLabel.config(text="PRESS THE GREEN BUTTON BEFORE START!!!")
                    

            elif isChecked == 1:
                try:
                    verbNumber = rnd.randint(0, len(verb)-1)
                    pronounNumber = rnd.randint(0, len(pronoun)-1)
                        

                    pronounTranslate = translator.translate(f'{pronoun[pronounNumber]}', src='ru', dest='en')
                    pronounTranslate = pronounTranslate.text.casefold()
                    

                    if pronounTranslate == 'i am' or pronounTranslate == 'am i':
                        pronounTranslate = 'I'
                    elif pronounTranslate == 'you are' or pronounTranslate == 'are you':
                        pronounTranslate = 'You'
                    elif pronounTranslate == 'we are' or pronounTranslate ==  'are we':
                        pronounTranslate = 'We'
                    elif pronounTranslate == 'he is' or pronounTranslate == 'is he':
                        pronounTranslate = 'He'
                    elif pronounTranslate == 'she is' or pronounTranslate == 'is she':
                        pronounTranslate = 'She'
                    elif pronounTranslate == 'it is' or pronounTranslate == 'is it':
                        pronounTranslate = 'It'
                    elif pronounTranslate == 'they are' or pronounTranslate == 'are they':
                        pronounTranslate = 'They'

                    if pronounTranslate == 'he' or pronounTranslate == 'she' or pronounTranslate == 'it' or pronounTranslate == 'He' or pronounTranslate == 'She' or pronounTranslate == 'It':
                        if verb[verbNumber] == 'do' or verb[verbNumber] == 'go':
                            sentence = f'{pronounTranslate} {verb[verbNumber]}es'
                            verbLabel.config(text=f'{sentence.upper()}')
                        elif (pronounTranslate == 'he' or pronounTranslate == 'she' or pronounTranslate == 'it' or pronounTranslate == 'He' or pronounTranslate == 'She' or pronounTranslate == 'It') and verb[verbNumber] == 'fly':
                            sentence = f'{pronounTranslate} flies'
                            verbLabel.config(text=f'{sentence.upper()}')
                        elif (pronounTranslate == 'he' or pronounTranslate == 'she' or pronounTranslate == 'it' or pronounTranslate == 'He' or pronounTranslate == 'She' or pronounTranslate == 'It') and verb[verbNumber] == 'have':
                            sentence = f'{pronounTranslate} has'
                            verbLabel.config(text=f'{sentence.upper()}')
                        else:
                            sentence = f'{pronounTranslate} {verb[verbNumber]}s'
                            verbLabel.config(text=f'{sentence.upper()}')
                    else:
                        sentence = f'{pronounTranslate} {verb[verbNumber]}'
                        verbLabel.config(text=f'{sentence.upper()}')


                    correctAnswerAI.config(text="")
                    correctAnswer.config(text="")
                    verbEntry.delete(0, 'end')
                except:
                    verbLabel.config(text="PRESS THE ►►► BUTTON FIRST!")
                isChecked = 0


        def helpButton():
            mb.showerror('Help ALT-CODES commands', '0252 - ü, 0246 - ö, 0228 - ä')

        self.title('Words Remembering')
        self.geometry('450x600')
        self.resizable(False, False)
        self[ 'bg' ] = '#454545'
        self.focus_set()
        self.iconbitmap( 'icon.ico' )

        # GUI

        verbTitle = Label(self, text="VERBS CONJUGATION", fg="#919191", bg="#454545", font="Roboto 15", pady="7")
        verbLabel = Label(self, text="PRESS ►►► BUTTON TO START", fg="#fff", bg="#666666", font="Roboto 15", width='40', height='1')
        verbEntry = Entry(self, fg="#fff", bg="#666666", font="Roboto 15", relief="solid", textvariable=message)
        verbCheckBTN = Button(self, text="Check", font="Roboto 15", bg="#cfcfcf", fg="#404040", activebackground="#454545", activeforeground="#cfcfcf", relief="solid", width="12", command=CheckVerb)
        correctAnswer = Label(self, text=correctAnswerText, fg="#fff", bg="#454545", font="Roboto 15")
        correctAnswerAI = Label(self, text=correctAnswerTextAI, fg="#fff", bg="#454545", font="Roboto 15", pady="7", padx='18')
        verbNextBTN = Button(self, text="►►►", font="20", bg="#cfcfcf", fg="#168a1c", activebackground="#454545", activeforeground="#168a1c", height="1", command=NextVerb)
        verbHelpBTN = Button(self, text='               ?               ', font="20", bg="#454545", fg="#525252", activebackground="#454545", activeforeground="#454545", height="1", command=helpButton)# command=helpButton)

        verbTitle.pack(pady="5")
        verbLabel.pack(pady="50")
        verbEntry.pack(pady="20")
        verbCheckBTN.pack(pady="17")
        correctAnswer.pack(pady='12')
        correctAnswerAI.pack(pady='1')
        verbNextBTN.pack(pady='20')
        verbHelpBTN.pack(side='bottom')

        self.bind('<Return>', NextVerbEnter)




if __name__ == "__main__":
    root = Tk()
    app = Main(root)
    app.pack()
    root.resizable(False, False)
    root.geometry('800x300')
    root.title('Deutsch Learning Helper')
    root[ 'bg' ] = '#454545'
    root.iconbitmap( 'icon.ico' )
    root.mainloop()

