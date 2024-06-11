import random
import time
health = 100
exp = 0
food_suply = 50
energy = 50
enemy_health = 100
notes = []
def hunting():
        global exp, food_suply, energy
        if energy <= 20:
          print ("Я бы хотел продолжить охоту нооооо..... МНЕ ЛЕНЬ")
          return
        exp += 50
        food_suply += 25
        energy -= 20
        print ("Здоровье - "+ str(health))
        print ("Опыт - "+ str(exp))
        print ("Еда - "+ str(food_suply))
        print ("Энергия - "+ str(energy))
        print ("Прекрасно поохотился!")
def sleep():
        global exp, health, energy
        if energy == 100:
             print("Я ВПЕРВЫЕ НЕ ХОЧУ СПАТЬ")
        energy = 100
        exp += 10
        health = 100
        Abobus = random.randint (1,2)
        if Abobus == 2:
            print ("Ты не спал так долго что тебе померещелся ОГРОМНЫЙ и добрый великан который отвёл тебя в лес.")
            energy -= 30
            walk()
            return
        for zzz in range(5):
            print ("zzz"*3 )
            time.sleep (0.5)
        print ("Опыт - "+ str(exp))
        print ("Еда - "+ str(food_suply))
        print ("Энергия - "+ str(energy))
        print ("Я очень хорошо поспал!")
def food():
        global exp, energy, food_suply
        if food_suply <= 30:
          print ("НАШИ ЗАПАСЫ ГРЕЧКИ ПЕЛЬМЕНЕЙ ЗАКОНЧИЛИСЬ!!!!!!!!!!!")
          return
        elif energy > 99:
             print ("Я НЕ ХОЧУ БЫТЬ АВОКАДО")
        energy += 30
        exp += 10
        food_suply -= 30
        print ("Здоровье - "+ str(health))
        print ("Опыт - "+ str(exp))
        print ("Еда - "+ str(food_suply))
        print ("Энергия - "+ str(energy))
        print ("Я очень вкусно поел!")
def write():
      global exp
      exp += 15
      print("Что ты хочешь написать?")
      KAKAYA_TO_SHTYKA = input("Ответ:")
      notes.append(KAKAYA_TO_SHTYKA)
      print("Я написал - "+ str(KAKAYA_TO_SHTYKA))
def read():
      print ("Я написал: ")
      for sus in notes:
            print (sus)
def walk():
    global exp,energy,food_suply,health,pit,Effect
    if energy <= 30:
          print ("Хотел пойти погулять но понял что у меня стёрты ноги в порошок и мне надо отдохнуть.")
          return
    napadaem = random.randint(1,5)
    exp += 10

    if napadaem == 1:
            print ("НА МЕНЯ НАПАЛА ПОПУЗЬЯНАААААААА!!!!!!!!!!")
            energy -= 10
            health -=20
            food_suply += 20
    elif napadaem == 2:
          print ("Я нашёл бутылку с малым неизвестным зельем! Пить или нет? 1 = пить 2 = нет")
          pit = input ("Ответ:")
          if pit == 1:
                Effect = random.randint (1,3)
                if Effect == 1:
                      print ("Мммм... зелье здоровья")
                      health += 10
                elif Effect == 2:
                    print ("ТЬФУ ТЫ! ЗЕЛЬЕ ОПЫТА!")
                    exp += 100
                elif Effect == 3:
                      print ("Мммммммм... Зелье отравления...")
                      health -= 50
    elif napadaem == 3:
          print ("Я НАШЁЛ ОГРОМНОЕ НЕИЗВЕСНОЕ ЗЕЛЬЕ. ПИТЬ ИЛИ НЕТ 1 = Пить 2 = нет")
          pit = input ("Ответ:")
          if pit == 1:
                Effect = random.randint (1,3)
                if Effect == 1:
                      print ("Мммм... зелье здоровья")
                      health += 50
                elif Effect == 2:
                    print ("ТЬФУ ТЫ! ЗЕЛЬЕ ОПЫТА!")
                    exp += 100
                elif Effect == 3:
                      print ("Мммммммм...мммммММММММММММААААААМММММММММММАААААААААААААА ЗЕЛЬЕ ОТРАВЛЕНИЯЯЯЯЯЯЯЯЯ!!!!!!!")
                      print ("Вы умерли от зелья отравления...")
                      health == 100
                      exp = 0
                      food_suply = 50
                      energy = 50
    elif napadaem == 5:
         print ("На меня напали бандиты!")
         print ("Ох... я их победил...")
         health -= 10
         energy -=20
         food_suply += 30
         print ("Здоровье - "+ str(health))
         print ("Опыт - "+ str(exp))
         print ("Еда - "+ str(food_suply))
         print ("Энергия - "+ str(energy))
    else:
            print ("Я нашёл еду!!!!")
            food_suply += 10
def fight(name):
    global health , exp , enemy_health
    enemy_health = 100
    name = str(name)
    fight = True
    print ("Вы встретили :" + name)
    while fight:
         print ("Your turn")
         print ("1. Хедшот")
         print ("2. Бодишот")
         AAAAAAAAAAA_TRAAAAKTOR = int(input) ("Что делать?")
         if AAAAAAAAAAA_TRAAAAKTOR == 1:
              Strelyat = random.randint (1,5)
              if Strelyat == 1:
               print ("ЕС! Минус 50")
               enemy_health -= 50
              else:
                   print ("Не попал")
while True:
    print ("-----Список действий-----")
    print ("1: Охота")
    print ("2: Сон")
    print ("3: Есть")
    print ("4: Записать что-то в блокнот")
    print ("5: Прочитать записи из блокнота")
    print ("6: Прогулка")
    action = input("Напиши номер действия:")
    action = int(action)
    if action == 1:
        hunting()
    elif action == 2:
        sleep()
    elif action == 3:
        food()
    elif action == 4:
        write()
    elif action == 5:
        read()
    elif action == 6:
          walk()
    elif action == 7:
        fight()
    print ("Здоровье - "+ str(health))
    print ("Опыт - "+ str(exp))
    print ("Еда - "+ str(food_suply))
    print ("Энергия - "+ str(energy))

    if health <= 0:
          print ("Я увидел видео А4. ААААААААААААААААААААААААААААААА")
          print ("Вы здохли!")
          break