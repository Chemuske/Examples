Условия:
1) В игре есть Существа. К ним относятся Игрок и Монстры.
2) У Существа есть параметры Атака и Защита. Это целые числа от 1 до 30.
3) У Существа есть Здоровье. Это натуральное число от 0 до N. Если Здоровье становится равным 0, то Существо умирает. Игрок может себя исцелить до 4-х раз на 30% от максимального Здоровья.
4) У Существа есть параметр Урон. Это диапазон натуральных чисел M - N. Например, 1-6.
5) Одно Существо может ударить другое по такому алгоритму:
  - Рассчитываем Модификатор атаки. Он равен разности Атаки атакующего и Защиты защищающегося плюс 1
  - Успех определяется броском N кубиков с цифрами от 1 до 6, где N - это Модификатор атаки. Всегда бросается хотя бы один кубик.
  - Удар считается успешным, если хотя бы на одном из кубиков выпадает 5 или 6
  - Если удар успешен, то берется произвольное значение из параметра Урон атакующего и вычитается из Здоровья защищающегося.

Conditions:
1) There are creatures in the game. These include a player and monsters.
2) The creature has parameters of attack and protection. These are whole numbers from 1 to 30.
3) The creature has health. This is a natural number from 0 to n. If health becomes equal to 0, then the creature dies. The player can heal himself up to 4 times by 30% of maximum health.
4) The creature has a damage parameter. This is the range of natural numbers M - N. For example, 1-6.
5) One creature can hit another by this algorithm:
   - We calculate the attack modifier. It is equal to the attack difference of the attacking and defense of the defending plus 1
   - Success is determined by a throw of n cubes with numbers from 1 to 6, where n is a modifier of attack. At least one cube is always rushing.
     - the blow is considered successful if at least one of the cubes falls 5 or 6
   - If the blow is successful, then arbitrary value from the parameter is taken from the attacker and is deducted from the health of the defending.
