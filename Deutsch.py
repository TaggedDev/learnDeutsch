import random as rand
a = True
nexting = input("Press enter \n")
pronoun = ["я", "ты", "мы", "вы", "Вы", "он", "она", "оно", "они"]
verb = ["сделать", "танцевать", "играть", "сказать", "спросить", "любить", "работать", "слышать", "отвечать"]
pastVerb = ["сделал", "танцевал", "играл", "сказал", "спросил", "любил", "работал", "слышал", "отвечал"]
quest = ["Что", "Кто", "Где", "Когда", "Почему", "Как", "Кого"]
while a == True:
    if nexting == '':
        randomPr = rand.randint(0, 8)
        randomQu = rand.randint(0, 6)
        randomVe = rand.randint(0, 8)
        
        past = rand.randint(0, 1)
        nein = rand.randint(0, 1)
        que = rand.randint(0, 1)
        if past == 1: #past simple
            if que == 1 and nein == 1: #past + question + nein
                
               print(quest[randomQu] + " " + pronoun[randomPr] + " не " + pastVerb[randomVe]) 

            if que == 1 and nein == 0: #past + question
        
                print(quest[randomQu] + " " + pronoun[randomPr] + " " + pastVerb[randomVe]) 
               
            if que == 0 and nein == 1: #past + nein

                print(pronoun[randomPr] + " не " + pastVerb[randomVe]) 
                
            if que == 0 and nein == 0: #past + positive

                print(pronoun[randomPr] + " не " + pastVerb[randomVe]) 
        if past == 0:
                        
            if que == 1 and nein == 1: #past + question + nein
                
               print(quest[randomQu] + " " + pronoun[randomPr] + " не " + verb[randomVe]) 

            if que == 1 and nein == 0: #past + question
        
                print(quest[randomQu] + " " + pronoun[randomPr] + " " + verb[randomVe]) 
               
            if que == 0 and nein == 1: #past + nein

                print(pronoun[randomPr] + " не " + verb[randomVe]) 
                
            if que == 0 and nein == 0: #past + positive

                print(pronoun[randomPr] + " не " + verb[randomVe]) 
        a = input() == ''
