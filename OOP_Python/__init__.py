import random
#Описание всех классов
class creature:
    
    def __init__(self, name, health, attack, damage, defence):
        
        if not(isinstance(name, str)):
            print('Введено неправильное значение имени для {}'.format(name))
            print('Введите имя в формате "Имя"')
            self._name = None
        else:
            self._name = name

        if not(isinstance(health, int)) or health < 1:
            print('Введено неправильное значение здоровья для {}'.format(name))
            print('Значение здоровья должно быть натуральным числом')
            self._health = None
        else:
            self._isDead = False
            self._health = health
        
        if not(isinstance(attack, int)) or (attack < 1) or (attack > 30):
            print('Введено неправильное значение атаки для {}'.format(name))
            print('Значение атаки должно быть целым числом от 1 до 30')
            self._attack = None       
        else:
            self._attack = attack
        
        if not(isinstance(damage, str)):
            print('Введено неправильное значение урона для {}'.format(name))
            print('Введите урон в формате "MinDamage-MaxDamage"')
            self._damage = None
        else:
            minDamage = float(damage.replace('-', ' ').split()[0])
            maxDamage = float(damage.replace('-', ' ').split()[1])
            if (not float.is_integer(minDamage)) or (not float.is_integer(maxDamage)):
                print('Диапазон значений урона - натуральные числа')
                self._damage = None
            else:
                self._damage = damage
                self._minDamage = int(minDamage)
                self._maxDamage = int(maxDamage)

        if not(isinstance(defence, int)) or (defence < 1) or (defence > 30): 
            print('Введено неправильное значение защиты для {}'.format(name))
            print('Значение защиты должно быть целым числом от 1 до 30')
            self._defence = None
        else:
            self._defence = defence
    
    def death(self):
        self._health = 0
        self._isDead = True
        print('{} умирает..'.format(self._name))
        
    #Set    
    def set_Name(self, name):
        if not(isinstance(name, str)):
            print('Введено неправильное значение имени для {}'.format(self._name))
            print('Введите имя в формате "Имя"')
            return        
        oldname = self._name
        self._name = name
        print('Имя {} изменено на {}'.format(oldname, self._name))
        
    def set_Health(self, health):
        if not(isinstance(health, int)) or (health < 1):
            print('Введено неправильное значение здоровья для {}'.format(self._name))
            print('Значение здоровья должно быть натуральным числом')
            return
        self._health = health
        print('Здоровье {} изменено на {}'.format(self._name, self._health))

    def set_Attack(self, attack):
        if not(isinstance(attack, int)) or (attack < 1) or (attack > 30):
            print('Введено неправильное значение атаки для {}'.format(self._name))
            print('Значение атаки должно быть целым числом от 1 до 30')
            return
        self._attack = attack
        print('Атака {} изменена на {}'.format(self._name, self._attack))
        
    def set_Damage(self, damage):
        if not(isinstance(damage, str)):
            print('Введено неправильное значение урона для {}'.format(self._name))
            print('Введите урон в формате "MinDamage-MaxDamage"')
            return        
        minDamage = float(damage.replace('-', ' ').split()[0])
        maxDamage = float(damage.replace('-', ' ').split()[1])
        if (not float.is_integer(minDamage)) or (not float.is_integer(maxDamage)):
            print('Диапазон значений урона - натуральные числа')
            return        
        self._damage = damage
        self._minDamage = int(minDamage)
        self._maxDamage = int(maxDamage)
        print('Урон {} изменена на {}'.format(self._name, damage))
    
    def set_Defence(self, defence):
        if not(isinstance(defence, int)) or (defence < 1) or (defence > 30): 
            print('Введено неправильное значение защиты для {}'.format(self._name))
            print('Значение защиты должно быть целым числом от 1 до 30')
            return
        self._defence = defence
        print('Защита {} изменена на {}'.format(self._name, self._defence))
        
    #Get
    def get_Name(self):
        if not self._name:
            return ("У данного существа нет имени")
        return self._name
    
    def get_Health(self):
        if self._isDead:
            return ("Существо мертво")
        if not self._health:
            return ("У данного существа нет параметра здоровья")
        return self._health
    
    def get_Attack(self):
        if not self._attack:
            return ("У данного существа нет параметра атаки")
        return self._attack
    
    def get_Damage(self):
        if not self._damage:
            return ("У данного существа нет параметра урона")
        return self._damage
    
    def get_Defence(self):
        if not self._defence:
            return ("У данного существа нет параметра защиты")
        return self._defence    
        
class player(creature):
    
    def __init__(self, name, health, attack, damage, defence):
        super().__init__(name, health, attack, damage, defence)
        self._fullHealth = health
        self.__healingNum = 0
        
    def set_Health(self, health):
        if health > self._health:
            self._fullHealth = health
        return super().set_Health(health)
    
    def healing(self): #Лечение на 30% от maxHp с округлением
        if self.__healingNum >= 4:
            print('Лечение недоступно')
            return
        if not isinstance(self.get_Health(), int):
            return
        self.__healingNum += 1
        self._health = self._health + round(0.3 * self._fullHealth)
        if self._health > self._fullHealth:
            self._health = self._fullHealth
        print('Игрок {} исцелился на {}, теперь его здоровье равно {}'.format(self._name, round(self._fullHealth * 0.3), self._health))
        print(f'Кол-во доступных исцелений {4 - self.__healingNum}')

def attack(attacker, defender):
    if not isinstance(attacker, creature):
        print("Выбрано несуществующее существо")
        return
    elif not isinstance(defender, creature):
        print("Выбран несуществующий противник")
        return
    attackMod = attacker.get_Attack() - (defender.get_Defence() + 1)
    damage = False
    if attackMod <= 0:
        attackMod = 1
    while attackMod:
        if random.randint(1, 6) >= 5:
            if not isinstance(defender.get_Health(), int):
                break
            damage = random.randint(attacker._minDamage, attacker._maxDamage)
            print("{} потерял {} здоровья от атаки {}".format(defender.get_Name(), damage, attacker.get_Name()))
            if damage >= defender.get_Health():
                defender.death()
            else:
                defender.set_Health(defender.get_Health() - damage)
        attackMod -= 1
    if not damage:
        print("{} не получил урона от {}".format(defender.get_Name(), attacker.get_Name()))