tempCh = int(input('Введите температуру в Чуйской области:'))
tempT = int(input('Введите температуру в Таласской области:'))
tempN = int(input('Введите температуру в Нарынской  области:'))
tempDj = int(input('Введите температуру в Джалал-Абадской области:'))
tempO = int(input('Введите температуру в Ошской области:'))
tempB = int(input('Введите температуру в Баткенской области:'))
tempI = int(input('Введите температуру в Иссык-Кульской области:'))
print(f'Средний показатель температуры в КР сегодня {(tempCh+tempT+tempN+tempDj+tempO+tempB+tempI)/7} °C')
