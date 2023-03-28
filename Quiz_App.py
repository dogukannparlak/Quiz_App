def Quiz_app():
    import time
    Questiions = ("Shakespeare'in Othello isimli oyununda bulunan rakip karakterin adı nedir?",
                  "Matt Reeves'in yönetmenliğini üstlendiği yeni The Batman filminde Batman rolünü hangi İngiliz aktör üstlendi ?",
                  "Mustafa Kemal Atatürk’ün Nüfusa Kayıtlı Olduğu İl Hangisidir?",
                  "Dünyanın en uzun sahiline sahip ülkesi hangisidir?",
                  "Dünya'nın 2.büyük kanyonu olan Ulubey Kanyonu hangi şehrimizde bulunmaktadır?",
                  "Türkiye'de klonlanan ilk koyununun adı nedir?",
                  "İnci Küpeli Kız eseri kime aittir?",
                  "Hangi alkollü içki en yüksek alkol oranına sahiptir?",
                  "Türkiye'nin hapis cezası alan ilk bilgisayar korsanı kimdir?",
                  "On kıtadan oluşan İstiklal Marşı'nın tamamında, bu kelimelerden hangisi \ndiğerlerinden daha az geçer?")


    Options = (("A.Lago","B.Romeo","C.Desdemona","D.Bianca"),
               ("A.Christian Bale ","B.Ben Affleck ","C.Robert Pattinson","D.Benedick Cumberbatch"),
               ("A.İstanbul ","B.Gaziantep","C.İzmir","D.Ankara"),
               ("A.Şili ","B.Arjantin ","C.Endonezya","D.Kanada"),
               ("A.Uşak","B.Erzurum","C.Muğla","D.Adana"),
               ("A.Kınalı","B.Pamuk","C.Oyalı","D.Hediye"),
               ("A.Michelangelo","B.Pablo Picasso","C.Johannes Vermeer","D.Sandro Botticelli"),
               ("A.Küba Romu","B.Absvent","C.Cin","D.Rakı"),
               ("A.Burak Çağlar","B.Tamer Şahin","C.Mahir Arabul","D.Tolga Bilge"),
               ("A.Toprak", "B.Kan", "C.Yurt", "D.Vatan"))

    Correct_Answers = ("A","C","B","D","A","C","C","B","B","A")

    Guesses = []

    score = 0

    index = 0

    for Questiion in Questiions:
        print()
        print("---------------------------------------")
        print(f"{index + 1}.", Questiion)
        for Option in Options[index]:
            print(Option)
        print()
        Guess = input("Please enter your answer(A,B,C,D) : ").upper()
        Guesses.append(Guess)
        if(Guess == Correct_Answers[index]):
            print("Corect")
            score += 1
            print("Your Score : ", score)
        else:
            print("WRONG")
            print(f'Corect answer is {Correct_Answers[index]}')
            print("Your Score : ", score)
        index += 1

    print()
    print("---------------------------------------")
    print("-                                     -")
    print("-             RESULTS                 -")
    print("-                                     -")
    print("---------------------------------------")
    print()

    time.sleep(2)
    print("Answeres:", end=" |")
    for answer in Correct_Answers:
        print(answer, end= " |")
    print()

    print("Guesses:", end=" |")
    for Guess in Guesses:
        print(Guess, end=" |")
    print()
    time.sleep(2)
    Final_score = int((score/len(Correct_Answers))*100)
    print()
    print(f"Your correct answer percentage : {Final_score} % ")

Quiz_app()