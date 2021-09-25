"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
# 1.
from datetime import datetime, timedelta
dt_now = datetime.now()
print(datetime.now())
delta = timedelta(days=1)
dt_yest = dt_now - delta
print(dt_yest)
delta_2 = timedelta(days=30)
dt_ago = dt_now - delta_2
print(dt_ago)
print(datetime.now()-timedelta(days=1))   # - алтернативный метод
print(datetime.now()-timedelta(days=30))  # - алтернативный метод
print(dt_now.strftime('%d.%m.%Y %H:%m'))
print(dt_yest.strftime('%d.%m.%Y %H:%m'))
print(dt_ago.strftime('%d.%m.%Y %H:%m'))


# 2.
dt = '01/01/25 12:10:03.234567'
date_dt = datetime.strptime(dt, '%y/%m/%d %H:%M:%S.%f')
print(date_dt)