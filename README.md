# upgrade-the-skill
torturing the python
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада'))

old = 0
for keys in per_cent:
  max_number = per_cent[keys]
  if max_number > old:
    old = max_number
    summ = max_number * money / 100

print("Максимальная сумма, которую вы можете заработать", summ)
