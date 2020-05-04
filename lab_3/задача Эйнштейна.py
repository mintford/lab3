from logpy import *
from logpy.core import lall

people = var()
rules = lall(
	(eq,		(var(), var(), var(), var(), var()), people),
	(membero, 	('Англичанин', var(), var(), var(), 'красный'), people),
	(membero, 	('Швед', var(), var(), 'собака', var()), people),
	(membero, 	('Датчанин', var(), 'чай', var(), var()), people),
	(membero, 	(var(), var(), 'кофе', var(), 'зеленый'), people),
	(membero, 	(var(), 'Pall Mall', var(), 'птицы', var()), people),
	(membero, 	(var(), 'Dunhill', var(), var(), 'желтый'), people),
	(membero, 	(var(), 'Rothmans', var(), var(), var()), people),
	(membero, 	(var(), var(), 'молоко', var(), var()), people),
	(membero, 	(var(), 'Philip Morris', 'пиво', var(), var()), people),
	(membero, 	(var(), var(), 'вода', var(), var()), people),
	(membero, 	(var(), var(), var(), 'лошади', 'синий'), people),
	(membero, 	(var(), var(), var(), 'кошки', var()), people),
	(membero, 	('Немец', 'Marlboro', var(), var(), var()), people),
	(membero, 	(var(), var(), var(), 'рыбки', var()), people)
)

solution = run(0, people, rules)

for item in solution[0]:
	print(item)


