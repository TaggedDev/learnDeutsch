import googletrans as gt 
import random as rnd
from googletrans import Translator

# ===START===

translator = Translator()
themes = ['Знакомство, прощание, приветствие', 'Семья, родственники', 'Продукты, покупки', 'В ресторане', 'Квартира, мебель', 'Распорядок дня', 'Досуг, хобби, развлечения', 'Работа и профессия', 'Дорога, путешествие', 'Здоровье и самочувствие', 'Одежда', 'Праздники', 'Погода', 'Планы и желания']

wordsMeeting = ['Привет!', 'Доброе утро', 'Добрый день', 'Добрый вечер', 'Доброй ночи', 'Добро пожаловать', 'До свидания', 'Пока!', 'До завтра', 'Меня зовут', 'Я приехал из России', 'Простите', 'Пожалуйста', 'Спасибо', 'Удачи!', 'Взаимно']
wordsFamily = ['Семья', 'Родители', 'Мама', 'Папа', 'Сестра', 'Брат', 'Сын', 'Дочь', 'Отец', 'Мать', 'Мальчик', 'Девочка', 'Бабушка', 'Дедушка']
wordsProducts = []
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
    userChoose = int(input("Введите номер темы: "))
    print("\n")
    
    def question():
        while True:
            words = wordsDict[userChoose]
            length = len(words) - 1
            number = rnd.randint(0, length) # рандомим слово из списка
            
            print(f'Переведи на немецкий слово: {words[number]}')
            print()
            userAnswer = input("Перевод: ")
            print()
                
            result = translator.translate(f'{words[number]}', src='ru', dest='de')
            aiAnswer = result.text.casefold()
            userAnswer = userAnswer.casefold()
            
            if userAnswer == aiAnswer:
                print("Ответ верен!")
                print("\n")
            elif userAnswer == 'back':
                start()
            else:
                print(f"Неверно! Правильный ответ: {aiAnswer}")
                print("\n")
    question()

start()