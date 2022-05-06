import datetime

today_date = datetime.date.today()
print(today_date)

my_brithday = datetime.date(2001,9,1) #-> Formato de fecha
print(my_brithday)

dias_birth = (today_date - my_brithday).days
print("-> Days:", dias_birth)

sumar_dias =  datetime.timedelta(days=21)  # -> Suma los días que le pase
print(today_date + sumar_dias)

tiempo = datetime.time(7,55,56) #Formato de hora (hora, minutos,segundo,mlsegundos)
print(tiempo)

hour_delta = datetime.timedelta(hours=10) # -> Suma la cantidad de horas y puede modificar la fecha si es el caso
tiempo_fecha_actual = datetime.datetime.now()
print(tiempo_fecha_actual + hour_delta)