horoscope = {3: [20, "Овен"], 4: [20, "Телец"], 5: [20, "Близнаци"],
             6: [20, "Рак"], 7: [21, "Лъв"], 8: [22, "Дева"],
             9: [22, "Везни"], 10: [22, "Скорпион"], 11: [21, "Стрелец"],
             12: [21, "Козирог"], 1: [19, "Водолей"], 2: [18, "Риби"]}


def what_is_my_sign(day, month):
    if month == 1 and horoscope[1][0] >= day:
        return horoscope[12][1]

    elif horoscope[month][0] >= day:
        return horoscope[month-1][1]

    else:
        return horoscope[month][1]
