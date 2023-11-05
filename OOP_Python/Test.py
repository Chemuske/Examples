from __init__ import creature, player, attack

#Пример работы
Zombie = creature('Zombie', 20, 4, '3-4', 1)
Player = player('Player', 20, 4, '4-5', 1)
for i in range(10):
    attack(Zombie,Player)
    attack(Zombie,Player)
    if Player._isDead == True:
        print('{} - {}, оно имело {} атаки, {} урона, {} защиты'.format(Player.get_Name(), Player.get_Health(), Player.get_Attack(), Player.get_Damage(), Player.get_Defence()))
        break
    if Player.get_Health() <= 10:
        Player.healing()
    attack(Player,Zombie)
    if Zombie._isDead == True:
        print('{} - {}, оно имело {} атаки, {} урона, {} защиты'.format(Zombie.get_Name(), Zombie.get_Health(), Zombie.get_Attack(), Zombie.get_Damage(), Zombie.get_Defence()))
        break 

if not Zombie._isDead:
    print('Существо {} имеет {} здоровья, {} атаки, {} урона, {} защиты'.format(Zombie.get_Name(), Zombie.get_Health(), Zombie.get_Attack(), Zombie.get_Damage(), Zombie.get_Defence()))
if not Player._isDead:    
    print('Существо {} имеет {} здоровья, {} атаки, {} урона, {} защиты'.format(Player.get_Name(), Player.get_Health(), Player.get_Attack(), Player.get_Damage(), Player.get_Defence()))

#Проверка атаки
#attack(Player, Player)

#Проверка всех Set - методов
"""
Player.set_Attack(2.1)
Player.set_Damage('4-6.2')
Player.set_Defence('2')
Player.set_Health(-1)
Player.set_Name(2)
"""

#Общая проверка + пример вывода информации
#print('Существо {} имеет {} здоровья, {} атаки, {} урона, {} защиты'.format(Player.get_Name(), Player.get_Health(), Player.get_Attack(), Player.get_Damage(), Player.get_Defence()))

#Отдельная проверка всех Get - Методов
"""
print(Player.get_Name())
print(Player.get_Health())
print(Player.get_Attack())
print(Player.get_Damage())
print(Player.get_Defence())
"""

#Проверка на неправильные входные данные
#Player2 = player(1, 0, 31, -1, 's')

#Проверка на попытку вывода таких данных
"""
print(Player2.get_Name())
print(Player2.get_Health())
print(Player2.get_Attack())
print(Player2.get_Damage())
print(Player2.get_Defence())
"""
'''
#Проверка лечения
Player.set_Health(1)
Player.healing()
Player.healing()
Player.healing()
Player.healing()
Player.healing()
'''