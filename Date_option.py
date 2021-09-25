"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
# 1.
def print_days():
    from datetime import datetime, timedelta
    dt_now = datetime.now()
    print(datetime.now())
    delta = timedelta(days=1)
    dt_yest = dt_now - delta
    print(dt_yest)
    delta_2 = timedelta(days=30)
    dt_ago = dt_now - delta_2
    print(dt_ago)
    print(datetime.now())                     # - алтернативный метод
    print(datetime.now()-timedelta(days=1))   # - алтернативный метод
    print(datetime.now()-timedelta(days=30))  # - алтернативный метод
print_days()


# 2.
from datetime import datetime
dt = "01/01/20 12:10:03.234567"
def str_2_datetime():
    date_dt = datetime.strptime(dt, '%y/%m/%d %H:%M:%S.%f')
    print(date_dt)
if __name__ == "__main__":
    str_2_datetime()

