
import random
print ("*" * 30 ,"Угадай число", "*" *30)

print("Наша реклама:")
print("Добро пожаловать в казино! Правила таковы : Компьютер выбирает число случайным образом от 1 до 10.Попробуй угадать и ты получишь 100 рублей!В случае неправильного числа ты отдаешь 100 рублей в банк!")
print("Для выхода нажми 0")
answer = 1
score = 0
i = 0
while answer :
    i=i + 1
    rand = random.randint (1,5) + random.randint (1,10)
    answer = int(input ("Введите число:"))
    if answer == 0 :
        break
    if answer == rand :
        score = score + 1
        print("Правильно!ты выйграл 100 рублей ! Ваш счет :",score,"из",i)
        print("Вот мои поздравления:")
        print("https://www.youtube.com/watch?v=_ubucL5znyM")
    else:
            print("Ты проиграл 100 рублей!Попробуй снова и фартуна будет на твоей стороне!Вот мои соболезнования:")
            print("https://www.youtube.com/watch?v=O85nbEpGzuA")
            print("До встречи!")
            
