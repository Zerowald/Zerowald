print("Привет! Калькулятор «продвинутый»! Могу выполнять арифметические действия, переводить из одной системы измерения в другую, считать доход от вклада.")
print("Выберай, какой калькулятор ты хочешь открыть? :обычный, доход от вклада, длина  и масса,") ##рассказываю что этот калькулятор может
MainUser = input()##одна из самых главных строк по моему мнению, смысл этой строки в том что мы пишим любую из 3 модификаций и нас переносит именно туда 
if MainUser == "доход от вклада":##если мы пишим "доход от вклада" то нас сюда перебрасывает благодаря if и переменой  мол если MainUser такой то такой то ,то сюда и перебрасывает
    while True:
        print("Вы выбрали модификацию `доход от вклада`")
        print("Напишите сумму вклада")
        Deposit = float(input())##просто выбераю переменые 
        print("напишите процентовую ставку")
        per = float(input())
        print("Для получения ответа, нужно указать на какой период вы будете вкладывать деньги в банк: '31 день' '28 дней' '30 дней' '365 дней' '90 дней' '270 дней'")
        print("Так же вы можете написать 'стоп' и программа закончится!")
        user2 = input()
        if user2 == "31 день":##больше всего я провел за этим заданием, я не знаю правильно ли я решил но это работает, я перепробывал вариантов 3-4.
            print((Deposit * per * 31 / 365)/100 , "a полная сумма = ", ((Deposit * per * 31 / 365)/100) + Deposit)##если переменая такая то такая то то запускается print в котором находится формула нахождения дохода от вклада
            a31 = ((Deposit * per * 31 / 365)/100) + Deposit
        elif user2 == "28 дней":
            print((Deposit * per * 28 / 365)/100, "а полная сумма = ", ((Deposit * per * 28 / 365)/100) + Deposit )
            a28 = ((Deposit * per * 28 / 365)/100) + Deposit
        elif user2 == "30 дней":
            print((Deposit * per * 30 / 365)/100, "а полная сумма = ", ((Deposit * per * 30 / 365)/100) + Deposit)
            a30 = ((Deposit * per * 30 / 365)/100) + Deposit
        elif user2 == "365 дней":
            print(Deposit * per * 365 / 365 / 100, "а полная сумма = ", ((Deposit * per * 365 / 365)/100) + Deposit )
            a365 = ((Deposit * per * 365 / 365)/100) + Deposit
        elif user2 == "90 дней":
            print(Deposit * per * 90 / 365 / 100, "а полная сумма = ", ((Deposit * per * 90 / 365)/100) + Deposit )
            a90 = ((Deposit * per * 90 / 365)/100) + Deposit
        elif user2 == "270 дней":
            print(Deposit * per * 270 / 365 / 100, "а полная сумма = ", ((Deposit * per * 270 / 365)/100) + Deposit )
            a270 = ((Deposit * per * 270 / 365)/100) + Deposit
        
        else: 
            if user2 == "стоп": ##теперь если мы напишем слово "стоп" весь "кусочек" прогрмаммы будет остановлен и условие пока True становиться False
                False
                break
        print("есть желание узнать вашу прибыль в другой валюте?(Да/Нет)")
        answer = input()
        if answer == "Да":
            print("В какой валюте есть желание узнать вашу прибыль?(Доллары)")
            mon_answer = input()
            if mon_answer == "Доллары":
                print("Т.к калькулятор не абсолютен, он не может знать в настоящем времяни во сколько русс рубль меньше доллара")
                print("Напишите на сколько 1 рубль в доллорах(например, сейчас 1 рубль = 0.01177 доллара)")
                how_much = float(input())
                awe = 1 // how_much
                if user2 == "31 день":
                    print(a31 // awe, "Это ваш заработак в ДОЛЛАРАХ")
                elif user2 == "28 дней":
                    print(a28 // awe, "Это ваш заработак в ДОЛЛАРАХ")
                elif user2 == "30 дней":
                    print(a30 // awe, "Это ваш заработак в ДОЛЛАРАХ")
                elif user2 == "365 дней":
                    print(a365 // awe, "Это ваш заработак в ДОЛЛАРАХ")
                elif user2 == "90 дней":
                    print(a90 // awe, "Это ваш заработак в ДОЛЛАРАХ")
                elif user2 == "270 дней":
                    print(a270 // awe, "Это ваш заработак в ДОЛЛАРАХ")
                else:
                    break
        else:
            if answer == "Нет":
                False
                break
            






if MainUser == "обычный":     ##обычный калькулятор, кстати опять возвращаюсь к  переменой MainUser я пишу что хочу перейти к обычному калькулятору и меня сюда перебрасывает
    while(True): ## создаем цикл который будет без остановки проигрывать кусочек кода(этот калькулятор)
        print("Вы выбрал модификацию `обычный`")
        print("Напишите первое число")
        a = int(input("Если вы хотите вычислить факториал числа, введите его в поле. Второе число не учитывается."))
        print("Напишите второе число")
        b = int(input())
        print("Выберите операцию: +, -, *, /, //, **, %, n!")
        user0 = input("вы так же можете написать 'стоп', и прогрмамма остановится: ")  ##такую идею я взял из видео которое было прикреплено в LMS, но я взял только идею, не сам код!
        if user0 == "+": ##если пользователь пишет например + то через if и переменую это отображается и запускается print
            print("Ответ", a + b)
        if user0 == "-": 
            print("Ответ", a - b)
        if user0 == "*": 
            print("Ответ", a * b)
        if (user0 == "/") and (b != 0):
            print("Ответ", a / b)
        else:
            if (b == 0) and user0 == "/":
                print("Так нельзя")
        if (user0 == "//") and (b != 0):
            print("Ответ", a // b)
        else:
            if (b == 0) and (user0 == "//"):
                print("На 0 делить нельзя!")
        if user0 == "**":
            print("Ответ (b ввиде степени)", a ** b)
            print("Ответ (a ввиде степени)", b ** a)
        elif user0 == "%":
            print("Ответ", a % b)
        
        elif user0 == "n!":
            cq = 1
            for i in range(1, a + 1):     ## факториал числа где как раз и используется цикл for
                cq = i * cq
            print("Ответ",cq, sep=" ")

        if user0 == "стоп": ##теперь если мы напишем слово "стоп" весь "кусочек" прогрмаммы будет остановлен и условие пока True становиться False
            break
            False

        

 
                

MainUser = input()
if MainUser == "длина  и масса":##самое интересное  опять приравниваю переменую MainUser
    while True: ## создаем цикл который будет без остановки проигрывать кусочек кода(длина  и масса)
        print("Вы выбрали модификацию `длина  и масса` ")
        print("Выбери что будем считать: массу или длинну?")
        user1 = input("вы так же можете написать 'стоп', и прогрмамма остановится: ")## как и MainUser приравниваю массу и длинну
        if user1 == "массу":
            print("Вы выбрали `массу`") 
            print("Напишите любое число")
            massa = int(input())
            print("Напишите единицу измерения: грамм, килограмм, центнер, тонна")
            while True:
                
                unit = input()##просто переменые
                                       

                print("напишите в какую ед. вы хотите перевести: грамм, килограмм, центнер, тонна")
                workunit = input()
                if unit == "грамм" and workunit == "килограмм":##обычная закономерность ,если одно больше другого во столько то раз и т.п , и так повторяется до конца.
                    print("Ответ", massa / 1000,"гр", sep=" ")
                elif unit == "грамм" and workunit == "центнер":       ##грамм
                    print("Ответ", massa / 100000,"гр", sep=" ")
                elif unit == "грамм" and workunit == "тонна":
                    print("Ответ", massa / 1000000,"гр", sep=" ")



                if unit == "килограмм" and workunit == "грамм":
                    print("Ответ", massa * 1000,"кг", sep=" ")
                elif unit == "килограмм" and workunit == "центнер":    ##кг
                    print("Ответ", massa / 100,"кг", sep=" ")
                elif unit == "килограмм" and workunit == "тонна":
                    print("Ответ", massa / 1000,"кг", sep=" ")
  


                if unit == "центнер" and workunit == "грамм":
                    print("Ответ", massa * 100000,"ц", sep=" ")
                elif unit == "центнер" and workunit == "килограмм":  ##центр
                    print("Ответ", massa * 100,"ц", sep=" ")
                elif unit == "центнер" and workunit == "тонна":
                    print("Ответ", massa / 10,"ц", sep=" ")


                if unit == "тонна" and workunit == "грамм":
                    print("Ответ", massa * 1000000,"т", sep=" ")
                elif unit == "тонна" and workunit == "килограмм":  ##тонна
                    print("Ответ", massa * 1000,"т", sep=" ")
                elif unit == "тонна" and workunit == "центнер":
                    print("Ответ", massa * 10,"т", sep=" ")
                
        else:
            if user1 == "стоп":
                break
                False
            


                                        ##вторая часть(мера)


        if user1 == "длина":
            print("вы выбрали `длина`")
        else:
            if user1 == "стоп":
                break
        print("напишите любое число")
        value = int(input())
        print("Напишите единицу измерения: миллиметр, сантиметр, дециметр, метр, километр")
        NameValue = input()
        print("В какую единицу измерения переводим?: миллиметр, сантиметр, дециметр, метр, километр")
        changed_value = input()



        if NameValue == "миллиметр" and changed_value == "сантиметр":
            print("Ответ", value / 10,"мм", sep=" ")
        elif NameValue == "миллиметр" and changed_value == "дециметр":     ##мм
            print("Ответ", value / 100,"мм", sep=" ")
        elif NameValue == "миллиметр" and changed_value == "метр":
            print("Ответ", value / 1000,"мм", sep=" ")
        elif NameValue == "миллиметр" and changed_value == "километр":
            print("Ответ", value / 1000000,"мм", sep=" ")



        if NameValue == "сантиметр" and changed_value == "миллиметр":
            print("Ответ", value * 10,"см", sep=" ")
        elif NameValue == "сантиметр" and changed_value == "дециметр":    ##см
            print("Ответ", value / 10,"см", sep=" ")
        elif NameValue == "сантиметр" and changed_value == "метр":
            print("Ответ", value / 100,"см", sep=" ")
        elif NameValue == "сантиметр" and changed_value == "километр":
            print("Ответ", value / 100000,"см", sep=" ")



        if NameValue == "дециметр" and changed_value == "миллиметр":
            print("Ответ", value * 100,"дм", sep=" ")
        elif NameValue == "дециметр" and changed_value == "сантиметр":    ##дм
            print("Ответ", value * 10,"дм", sep=" ")
        elif NameValue == "дециметр" and changed_value == "метр":
            print("Ответ", value / 10,"дм", sep=" ")
        elif NameValue == "дециметр" and changed_value == "километр":
            print("Ответ", value / 10000,"дм", sep=" ")




        if NameValue == "метр" and changed_value == "миллиметр":
            print("Ответ", value * 1000,"м", sep=" ")
        elif NameValue == "метр" and changed_value == "сантиметр":     ##м
            print("Ответ", value * 100,"м", sep=" ")
        elif NameValue == "метр" and changed_value == "дециметр":
            print("Ответ", value * 10,"м", sep=" ")
        elif NameValue == "метр" and changed_value == "километр":
            print("Ответ", value / 1000,"м", sep=" ")



        if NameValue == "километр" and changed_value == "миллиметр":
            print("Ответ", value * 1000000,"км", sep=" ")
        elif NameValue == "километр" and changed_value == "сантиметр":    ##км
            print("Ответ", value * 100000,"км", sep=" ")
        elif NameValue == "километр" and changed_value == "дециметр":
            print("Ответ", value * 10000,"км", sep=" ")
        elif NameValue == "километр" and changed_value == "метр":
            print("Ответ", value * 1000,"км", sep=" ")


else:
    if not (MainUser == "длина  и масса") or not MainUser == "обычный" or not MainUser == "доход от вклада" :
        StopAsyncIteration
        print("Программа остановлена") ## изначально я хотел сделать так что бы можно было  отменить программу в самом начале, сразу я хотел использовать оператор break но ничего не получилось - 
        StopIteration            ## тогда я решил написать просто слово Stop  что означает стоп, остановка  и на мое удевление  VSC показал эти 2 слова я решил попробывать, и оно как то работает. :)


        

























##калькулятор эмодзи



#if MainUser == "эмодзи":##призываю переменую MainUser если MainUser = эмодзи то запускается этот код.
 #       print("Вы выбрали модификацию `Эмодзи`")
  #      print("Это не песочница! ")
   #     print("выберите операцию : +, -, *, /, //, **, %")
    #    sing = input()
     #   if sing == "+" or sing == "-":
      #      print("выберите 1 из Эмодзи:😀 💫 😇 💀 🦴 ☠ 😠 💢 🤬 😈 😄 💤 😴 ☕")
       #     emojik = input()
        #    print("Выбери 2 Эмодзи: 😀 💫 😇 💀 🦴 ☠ 😠 💢 🤬 😈 😄 💤 😴 ☕")
         #   emojik2 = input()
          #  user3 = input()
           # if emojik == "😀" and emojik2 == "💫":##принцип работы как калькулятор с цифрами только здесь эмодзи и условия по больше.
            #    print("\U0001F600 + \U0001F4AB = \U0001F607")
            #elif emojik == "😇" and emojik2 == "💫":
            #    print("\U0001F607 - \U0001F4AB = \U0001F600 ")
            #elif emojik == "💀" and emojik2 == "🦴":
            #    print("\U0001F480 + \U0001F9B4 = \U00002620 ")
            #elif emojik == "☠" and emojik2 == "🦴" :
            #    print("\U00002620 - \U0001F9B4 = \U0001F480 ")
            #elif emojik == "😠" and emojik2 == "💢":
            #    print("\U0001F620 + \U0001F4A2 = \U0001F621 ")
            #elif emojik == "🤬" and emojik2 == "😈":
            #    print("\U0001F92C - \U0001F608 = \U0001F620 ")
            #elif emojik == "😄" and emojik2 == "💤" :
            #    print("\U0001F604 + \U0001F4A4 = \U0001F634 ")
            #elif emojik == "😴" and emojik2 == "☕" :
             #   print("\U0001F634 - \U00002615 = \U0001F92A ")


        #if sing == "*" or "**":  
         #   print("выберите 1 из Эмодзи:")
          #  emojik = input()
#            print("Выбери 2 Эмодзи: ")
#            emojik2 = input()
#            user3 = input()
#            print("напиши 2 числа для возведения в степень")
#            num = int(input())
#            num1 = int(input())
#            if emojik == "😇" and emojik2 == "😇":##времени у меня было много вот я и решил разбить арифметические операции по 2 и сделать такие вот отдельные группки.
#                print("\U0001F607 * \U0001F607 = \U0001F47C ")
#            elif emojik == "👍" and emojik2 == "👍" :
#                print("\U0001F44D", *num ,"=")
#            elif emojik == "❤" and emojik2 == "❤" :
#                print(" \U00002764 * \U00002764 = \U0001F49E ")
#            elif emojik == "🖖" and emojik2 == "🖖" :
#                print("\U0001F596 ", * num1 , "=  ")
#            elif emojik == "🏔" and emojik2 == "🏖" :                         ##до делать + вернуть выбор знака
#                print(" \U0001F3D4 * \U0001F3D6  = \U0001F30D ")
#            elif emojik == "🧊" and emojik2 == "🧊":
#                print(" \U0001F9CA", * num ,"= ")
#            elif emojik == "🚂" and emojik2 == "🚂":
#                print("\U0001F682 * \U0001F682 = \U0001F684 ")
#            elif emojik == "" and emojik2 == "":
#                print(" * = ")



        