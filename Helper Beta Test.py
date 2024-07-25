
import random
from datetime import datetime
from datetime import date

inf_cal = 0
inf_ore = 0
inf_mood = 0
inf_film = 0
inf_data = 0
inf_spe = 0
inf_pict = 0
inf_gad = 0
inf_ran = 0
inf_list = 0


stop_words = ['стоп','Стоп','хватит','Хватит','выключить','Выключить']
stop_words2 = ' '.join(stop_words)

print("Привет, я твой помощник!")
print("Вы можете задавать мне различные вопросы а я постараюсь на них ответить")
print("Для начала работы советую написать команду 'help' что бы ознакомиться с моими умениями")

while True:
    MainUser = input()
    if MainUser == "help":
        print("Что ж, я могу запускать следующие модификации:")
        can_do1 = ['1)калькулятор','2)орел и решка','3)спроси какое у меня настроение?','4)посоветовать фильм','5)какое сегодня число?']
        can_do2 = ['5)мотивирующая речь','6)рандомная картинка','7)рандомное слово','8)инф-лист','9)гадалка', ]
        can_do3 = can_do1 + can_do2
        print(can_do3)
    if MainUser == "калькулятор":
        print()
        cal_funny_words = ['Запускаю калькулятор...', 'Почти...Почти...Почти... Готово, калькулятор запущен!', 'Запус... Ошибка, шутка, калькулятор включен!']
        cal_random_num = random.randint(0, 2)
        while True:
            inf_cal += 1
            print(cal_funny_words[cal_random_num])
            print()
            print("Вы включили 'калькулятор'")
            print("Напишите первое число:")
            cal_num1 = int(input())
            print("Напишите второе число:")
            cal_num2 = int(input())
            print("Выберети знак:  +, -, *, /, //, **, %, n!")
            cal_thing = input("если хочешь выключить помошника,посмотри 'стоп - слова' просто напиши покажи стоп - слова ")
            if cal_thing == "+":
                print(cal_num1,cal_thing,cal_num2, "=",cal_num1 + cal_num2)

            if cal_thing == "-":
                print(cal_num1,cal_thing,cal_num2, "=",cal_num1 - cal_num2)

            if cal_thing == "*":
                print(cal_num1,cal_thing,cal_num2, "=",cal_num1 * cal_num2)

            if (cal_thing == "/") and (cal_num2 != 0):
                print(cal_num1,cal_thing,cal_num2, "=",cal_num1 / cal_num2)
            else:
                if (cal_num2 == 0) and (cal_thing == "/"):
                    print("Нельзя делить на 0!")
                    print("Выберай следующую программу, для помощи введи команду help")
                    False
                    break

            if (cal_thing == "//") and (cal_num2 != 0):
                print(cal_num1,cal_thing,cal_num2, "=",cal_num1 // cal_num2)
            else:
                if (cal_num2 == 0) and (cal_thing == "/"):
                    print("Нельзя делить на 0!")
                    print("Выберай следующую программу, для помощи введи команду help")
                    False
                    break
            if cal_thing == "**":
                print(cal_num1,cal_thing,cal_num2, "=",cal_num1 ** cal_num2)

            if cal_thing == "%":
                print(cal_num1,cal_thing,cal_num2, "=",cal_num1 % cal_num2)

            if cal_thing == "n!":
                cq = 1
                for i in range(1, cal_num1 + 1):
                    cq = i * cq
                print("Ответ",cq, sep=" ")
            if cal_thing == "покажи стоп - слова":
                print("1)",stop_words)
                print("2)",stop_words2)
                print()
                print()
            
            else: 
                if (cal_thing == stop_words[0]) or (cal_thing == stop_words[1]) or (cal_thing == stop_words[2]) or (cal_thing == stop_words[3]) or  (cal_thing == stop_words[4]) or (cal_thing == stop_words[5]): 
                    print("Вы выключили калькулятор")
                    print("Выберай следующую программу, для помощи введи команду help")
                    False
                    break
    if MainUser == "орел и решка":
        
        while True:
            inf_ore += 1
            ore_funny_words = ['Выделяю память для включения "орел и решка"', '...98 99 100%! Готово!', 'Думаю сейчас вам выпадет Орел', 'Думаю уже сейчас вам выпадет Решка']
            ore_random_num = random.randint(0,3)
            print(ore_funny_words[ore_random_num])
            print()
            print("Вы включили 'орел и решка'")
            print()
            print("вы будете ставить ставку что выпадет?")
            print()
            ore_thing = input("Пиши орел или решка в зависимости на что вы поставили, если вы не хотите ставить напишите '-' ")
            print("так же не забывай про список стоп - слов, напоминаю, для просмотра его пиши 'покажи стоп - слова'  ")
            if ore_thing == "покажи стоп - слова":
                print("1)",stop_words)
                print("2)",stop_words2)
            ore_random_reshkaorel = random.randint(1,2)
            if ore_thing == "решка":
                if ore_random_reshkaorel == 1:
                    print("Ура! Вы выиграли!")
                else:
                    if ore_random_reshkaorel == 2:
                        print("Эх.. Вы проиграли!")
            if ore_thing == "орел":
                if ore_random_reshkaorel == 1:
                    print("К сожалению или к счастью... Вы проиграли!")
                else:
                    if ore_random_reshkaorel == 2:
                        print("Да!! Вы выиграли!")
            if ore_thing == "-":
                if ore_random_reshkaorel == 1:
                    print("Выпала решка")
                else:
                    if ore_random_reshkaorel == 2:
                        
                        print("выпал орел")
            else:
                if (ore_thing == stop_words[0]) or (ore_thing == stop_words[1]) or (ore_thing == stop_words[2]) or (ore_thing == stop_words[3]) or  (ore_thing == stop_words[4]) or (ore_thing == stop_words[5]):
                    print("Вы выключили орел и решка")
                    print("Выберай следующую программу, для помощи введи команду help")
                    False
                    break
    

    if (MainUser == "какое у тебя настроение?") or (MainUser == "Как у тебя дела?") or (MainUser == "как у тебя дела?") or (MainUser == "как дела?"):
        while True:
            inf_mood += 1
            print()
            mood_thing = ['Лучше всех!', 'Сегодня съел тортик поэтому настроение отличное','Восхитительное!', 'Учу пайтон поэтому настроение ХОРОШОЕ!']
            mood_random_num = random.randint(0,3)
            print(mood_thing[mood_random_num])
            False
            break
            

            


    if MainUser == "Посоветуй фильм":
        while True:
            inf_film += 1
            film_thing = ['1)Крепкий орешек', '2)Назад в будущее', '3)Таксист', '4)Леон', '5)Богемская рапсодия', '6)Город грехов', '7)Мементо', '8)Отступники', '9)Деревня','10)Звёздные войны.']
            film_thing2 = ['11)Тёмный рыцарь','12)Начало','13)Звёздные войны.']
            film_thing3 = film_thing + film_thing2
            print("напиши сколько фильмов ты хочешь увидеть?(максимум 12)")
            film_num = input()
            for i in range(film_num):
                print(film_thing3[i])
                False
                break

    if MainUser == "какое сегодня число?":
        while True:
            inf_data += 1
            print()
            print("Вы включили Календарь")
            print()
            print("Что вы хотите знать? (какой сегодня день/число/год/время/")
            data_thing = input()
            data_main = datetime.now()
            if data_thing == "день":
                data_day = (data_main.strftime("%A"))
                if data_day == "Monday":
                    data_day = "Понедельник!"
                    print(data_day)
                    print()
                if data_day == "Tuesday":
                    data_day = "Вторник!"
                    print(data_day)
                    print()
                if data_day == "Wednesday":
                    data_day = "Cреда!"
                    print(data_day)
                    print()
                if data_day == "Thursday":
                    data_day = "четверг"
                    print(data_day)
                    print()
                if data_day == "Friday":
                    data_day = "Пятница"
                    print(data_day)
                    print()
                if data_day == "Saturday":
                    data_day = "Суббота"
                    print(data_day)
                    print()
                if data_day == "Sunday":
                    data_day = "Воскресенье"
                    print(data_day)
                    print()

            if data_thing == "время":
                data_main2 = datetime.now()
                data_time = data_main2.strftime("%H:%M:%S")
                print(data_time)
                print()


            if data_thing == "число":
                data_num = datetime.now()
                data_num = data_num.day
                print(data_num)
                print()


            if data_thing == "год":
                data_year = datetime.now()
                print(data_year.year)
                print()

            else:
                if (data_thing == stop_words[0]) or (data_thing == stop_words[1]) or (data_thing == stop_words[2]) or (data_thing == stop_words[3]) or  (data_thing == stop_words[4]) or (data_thing == stop_words[5]):
                    print("Вы выключили календарь")
                    print("Выберай следующую программу, для помощи введи команду help")
                    False
                    break

    if MainUser == "мотивирующая речь":
        while True:
            inf_spe += 1
            spe_random_num = random.randint(0,6)
            print()
            print("Вы включили 'мотивирующую речь' ")
            print()
            print("Напиши что вас беспокоит а я выслушаю вас")
            spe_thing = input("так же не забывай про список стоп - слов, напоминаю, для просмотра его пиши 'покажи стоп - слова' ")
            spe_word = ['Я верю в тебя. Ты все сможешь','Понятно...', 'Я знаю что все будет ОК!!','Вы добьётесь успеха.','Понятно..','Ага','Я знаю у тебя все получиться!']
                        
            if (spe_thing == stop_words[0]) or (spe_thing == stop_words[1]) or (spe_thing == stop_words[2]) or (spe_thing == stop_words[3]) or  (spe_thing == stop_words[4]) or (spe_thing == stop_words[5]):
                    print("Вы выключили 'мотивирующую речь!'")
                    print("Выберай следующую программу, для помощи введи команду help")
                    False
                    break
            print(spe_word[spe_random_num])  


    
        

    if MainUser == "рандомная картинка":
        while True:
            print()
            print("Вы включили 'генератор картинок'")
            print()
            print("Выберай какую конкретно хочешь картинку и получи ее!")
            print("пиши 'tutorial' и увидишь все что надо")
            print()
            pict_thing = input()
            if pict_thing == "tutorial":
                while True:
                    inf_pict += 1
                    print("Вам будет писаться по порядку что вам нужно нажать, выбрать а вы все это делайте :)")
                    print("вот пример выбора!")
                    print("(Цифры/знаки)")
                    pict_tutorial = input()
                    if pict_tutorial != "Цифры" and pict_tutorial != "знак":
                        print("Нужно писать так как вас попросили, с большой буквы так с большой буквы, с ошибкой так с ошибкой :)")
                        True
                    else:
                        print("думаю теперь вы все поняли, пиши 'return', и начинай создавать, для запуска пиши 'start'")
                    pict_tutorial2 = input()
                    if pict_tutorial2 == "return":
                        False
                        break
                    else:
                        if pict_tutorial2 != "return":
                            True
            if  pict_thing == "start":
                print("Запускаем!") ## сюда можно добавить рофл слова
                print("Для начала мне нужно понять какую картинку ты хочеш из (цифра/знак) пример:  123... или !№;%...")
                pict_thing_num_sign = input()
                if pict_thing_num_sign == "цифра":
                    print("так и запишим!") ## сюда можно добавить рофл слова
                    print("теперь нужно знать (треугольник/квадрат)")
                    pict_thing_treyg_cvad = input()
                    if pict_thing_treyg_cvad == "треугольник":
                        print("ок!")
                        print("последние тоннкости!")
                        print("цифры в треугольнике должны быть(кастомный/зеркальный/статичный)")
                        pict_thing_num = input()
                        if pict_thing_num == "кастомный":
                            pict_thing_inputnum = int(input("пиши число и получай свою картинку!"))
                            for i in range(1,pict_thing_inputnum + 1): 
                                print(str(i)*i)
                            pict_paused = input()
                        
                        if pict_thing_num == "статичный":
                            print("отлично!")
                            print("Ну значит пиши цифру")
                            pict_num_2 = int(input("из какой цифры будем делать треугольник? "))
                            for i in range(1,pict_thing_inputnum + 1): 
                                print(str(pict_num_2)*i)
                            pict_paused = input()
                        if pict_thing_num == "зеркальный":
                            pict_num = int(input()) 
                            for i in range(1, pict_num + 1): 
                                for j in range(1, i + 1): 
                                    print(j, end="") 
                                for j in range(i - 1, 0, -1): 
                                    print(j, end="") 
                            pict_paused = input()



                    if pict_thing_treyg_cvad == "квадрат":
                        print("хорошо!")
                        print("цифры в квадрате должны быть (кастомный//статичный)")
                        pint_thing_kvad_input = input()
                        if pint_thing_kvad_input == "кастомный":
                            print("отлично, осталось уточнить пару нюансов и готов!")
                            pict_thing_kvad_shir = int(input("пиши ширину "))
                            pict_thing_kvad_dlin = int(input("пиши длинну "))
                            pict_thing_sing = int(input("пиши цифру "))  
                            for i in range(pict_thing_kvad_shir):
                                print(str(pict_thing_sing) * pict_thing_kvad_dlin)
                            pict_paused = input()
                        if pint_thing_kvad_input == "статичный":
                            pict_thing_kvad_shir2 = int(input("пиши ширину "))
                            pict_thing_kvad_dlin2 = int(input("пиши длинну "))
                            for i in range(1 ,pict_thing_kvad_shir2 + 1):
                                print(str(i) * pict_thing_kvad_dlin2)
                            pict_paused = input()
                if pict_thing_num_sign == "знак":
                    print("так и запишим!") ## сюда можно добавить рофл слова
                    print("теперь нужно знать (треугольник/квадрат)")
                    pict_thing_treyg_cvad = input()
                    if pict_thing_treyg_cvad == "треугольник":
                        print("ок!")
                        print("последние тоннкости!")
                        print("Знаки в треугольнике должны быть(кастомный/зеркальный/статичный)")
                        pict_thing_num = input()
                        if pict_thing_num == "кастомный":
                            pict_thing_custom_rannum = random.randint(0,5)
                            pict_thing_custom_ranlist = ["!",";","%",":","?","*"]
                            print("и так перерд тобой список знаков из которых может быть создан треугольник")
                            print(pict_thing_custom_ranlist)
                            print("пиши цифру (1-6) и получи свою картинку")
                            print("Если хочешь создать рандомный треугольник там и пиши 'рандом' если не хочешь то так и напиши! ")
                            pict_thing_custom_inputword = input()
                            if pict_thing_custom_inputword == "рандом":
                                pict_thing_custom_inputnum = int(input("пиши высоту треугольника!"))
                                print("Генерирую!")
                                for i in range(1,pict_thing_custom_inputnum + 1):
                                    print(pict_thing_custom_ranlist[pict_thing_custom_rannum] * i)
                                pict_paused = input()
                            else:
                                if pict_thing_custom_inputword != "рандом":
                                    print(pict_thing_custom_ranlist)
                                    print("пиши цифру (1-6) и получи свою картинку")
                                    pict_thing_custom_usernum = int(input())
                                    pict_thing_custom_usernum -= 1
                                    for i in range(int(input("Пиши высоту треугольник!"))):
                                        print(pict_thing_custom_ranlist[pict_thing_custom_usernum] * i)
                                    pict_paused = input()
                            

                        if pict_thing_num == "статичный":
                            print("Приступим!")
                            pict_thing_inputsing = input("Пиши какой знак хочешь увидеть? ")
                            pict_thing_inputnum = int(input("пиши высоту треугольника и получай свою картинку! "))
                            for i in range(1,pict_thing_inputnum + 1): 
                                print(pict_thing_inputsing * i)
                            pict_paused = input()
                        if pict_thing_num == "зеркальный":
                            pict_num = int(input("Ок! Пиши высоту треугольника"))
                            pict_sing = input("пиши первый знак!")
                            pict_sing2 = input("пиши второй знак!")
                            for i in range(1, pict_num + 1): 
                                for j in range(1, i + 1): 
                                    print(pict_sing, end="") 
                                for j in range(i - 1, 0, -1): 
                                    print(pict_sing2, end="") 
                                pict_paused = input()


                    if pict_thing_treyg_cvad == "квадрат":
                        print("хорошо!")
                        print("знаки в квадрате должны быть (кастомный/статичный)")
                        pint_thing_kvad_input = input()
                        if pint_thing_kvad_input == "кастомный":
                            print("Существует 2 уровня кастомизации квадрата ")
                            print()
                            print("Первый уровень - Выбераеться, настраивается знак из которого состоит квадрат")
                            print("Второй уровень - Выбераеться, настраивается знак из которого состоит квадрат а так же ширина и длинна ")
                            print("!Это все настраивается рандомно!")
                            pict_kvad_custom_lvlnum = int(input())
                            if pict_kvad_custom_lvlnum == 1:
                                
                                pict_thing_custom_rannum2 = random.randint(0,5)
                                print("отлично, осталось уточнить пару нюансов и готов!")
                                pict_thing_kvad_shir = int(input("пиши ширину "))
                                pict_thing_kvad_dlin = int(input("пиши длинну "))
                                pict_thing_sing = ["!","@","#","$","%","^"]
                                for i in range(pict_thing_kvad_shir):
                                    print(pict_thing_sing[pict_thing_custom_rannum2] * pict_thing_kvad_dlin)
                            if pict_kvad_custom_lvlnum == 2:
                                
                                pict_thing_custom_rannum3 = random.randint(0,5)
                                pict_thing_kvad_shir = random.randint(1,15)
                                pict_thing_kvad_dlin = random.randint(1,15)

                                pict_thing_sing = ["!","@","#","$","%","^"]
                                for i in range(pict_thing_kvad_shir):
                                    print(pict_thing_sing[pict_thing_custom_rannum3] * pict_thing_kvad_dlin)
                                
                        if pint_thing_kvad_input == "статичный":
                            print("И так у нас есть список, выберай пиши номер знака начиная с 1 и все!")
                            pict_thing_sing = ["!","@","#","$","%","^"]
                            pict_kvad_static_inputnum = int(input())
                            pict_kvad_static_inputnum -= 1

                            pict_thing_kvad_shir2 = int(input("пиши ширину "))
                            pict_thing_kvad_dlin2 = int(input("пиши длинну "))
                            for i in range(1 ,pict_thing_kvad_shir2 + 1):
                                print(pict_thing_sing[pict_kvad_static_inputnum] * pict_thing_kvad_dlin2)
## сделать рандом, полный радом и частичный для кастомного куба и блять слава богу все... :))))) (ггыгыыгыг еще рофл фразы писать...)
            if pict_thing == "стоп":
                print("программа выключена!")
                False
                break



    if MainUser == "рандомное слово":
       
            print("Вы включили модификацию 'рандомное слово'")
            print("Вы хотите получить слово или предложеие? если вы хотите получить слово пиши 'слово' а если ты хочешь получить предложение, так и пиши!")
            while True:
                inf_ran += 1
                ran_thing_input = input("Так же ты можешь написать Стоп ")
                if ran_thing_input == "слово":
                    ran_thing_rannum = random.randint(0,13)
                    print("Выбор сделан, и так вы получаете:")
                    ran_list_word = ["Python", "Rust", "Lua", "Гавань","Кнопка", "sql - инъекция","Программа","будующее","Время","Монитор","Наушники","Коктель","Сон","пицца"]
                    print(ran_list_word[ran_thing_rannum])
                if ran_thing_input != "слово" and ran_thing_input != "стоп" and ran_thing_input != "Стоп":
                    ran_list_1 = ["Я","Ты","Он"]
                    ran_list_2 = ["был"]
                    ran_list_3 = ["грустным","веселым","скучным","интересным"]
                    ran_thing_ran1 = random.randint(0,2)
                    ran_thing_ran2 = random.randint(0,3)
                    print("хорошо!")
                    print()
                    print(ran_list_1[ran_thing_ran1],ran_list_2[0], ran_list_3[ran_thing_ran2])
                    print()
                    ran_pause = input()
                    if ran_pause == "стоп" or ran_pause == "Стоп":
                        print("Выключено!")
                        False
                        break
                else:
                    if ran_thing_input == "Стоп" or ran_thing_input == "стоп":
                        ("Выключено! 2x")
                        False 
                        break
                        
    if MainUser == "гадалка":
            print("Вы включили 'Гадалка'")
            print("Пишии что ты хочешь узнать а я напишу тебе")
            print("Не повезло, возможно, повезло, 100% произойдет.")

            while True:
                inf_gad += 1
                gad_thing_rannum = random.randint(1,100)
                gad_thing_input = input("Что ты хочешь узнать?")
                if gad_thing_rannum < 25:
                    print("Вам не повезло :(")
                    gad_pause = input("Пиши стоп если хочешь выключить программу")
                    if gad_pause == "стоп" or gad_pause == "Стоп":
                        print("Вы выключили программу")
                        False
                        break
                    else:
                        True
                if gad_thing_rannum > 25 and gad_thing_rannum < 50:
                    print("Нейтрально, возможно повезет возможно нет")
                    gad_pause = input()
                    if gad_pause == "стоп" or gad_pause == "Стоп":
                        print("Вы выключили программу")
                        False
                        break
                    else:
                        True
                if gad_thing_rannum > 50 and gad_thing_rannum < 75:
                    print("повезло")
                    gad_pause = input()
                    if gad_pause == "стоп" or gad_pause == "Стоп":
                        print("Вы выключили программу")
                        False
                        break
                    else:
                        True
                if gad_thing_rannum > 75:
                    print("100% повезет")
                    gad_pause = input()
                    if gad_pause == "стоп" or gad_pause == "Стоп":
                        print("Вы выключили программу")
                        False
                        break
                    else:
                        True

    if MainUser == "инф - лист":
        inf_list += 1
        print("Вы включили 'Инф лист'")
        print("----------")
        print("За данный Тикет было использовано 'калькулятор' -",inf_cal)
        print("За данный Тикет было использовано 'орел и решка' -",inf_ore)
        print("За данный Тикет было использовано 'спроси какое у меня настроение?' -",inf_mood)
        print("За данный Тикет было использовано 'посоветовать фильм' -",inf_film)
        print("За данный Тикет было использовано 'какое сегодня число?' -",inf_data)
        print("За данный Тикет было использовано 'мотивирующая речь' -",inf_spe)
        print("За данный Тикет было использовано 'рандомная картинка' -",inf_pict)
        print("За данный Тикет было использовано 'рандомное слово' -",inf_ran)
        print("За данный Тикет было использовано 'гадалка' -",inf_gad)
        print("За данный Тикет было использовано 'инф-лист' -",inf_list)
        print("----------")

        # can_do1 = ['1)калькулятор','2)орел и решка','3)спроси какое у меня настроение?','4)посоветовать фильм','5)какое сегодня число?']
        # can_do2 = ['5)мотивирующая речь','6)рандомная картинка','7)рандомное слово','8)инф-лист','9)гадалка', ]

    else:
        if (MainUser == stop_words[0]) or (MainUser == stop_words[1]) or (MainUser == stop_words[2]) or (MainUser == stop_words[3]) or  (MainUser == stop_words[4]) or (MainUser == stop_words[5]):
            print("Вы выключили помощника :(")
            print("!Тикет закрыт! вся собраная информация удалена!")
            False
            break
