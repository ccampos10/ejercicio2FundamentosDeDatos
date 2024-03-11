ingresos = int(input("Ingrese sus ingresos mensuales: "))
valorCasa = int(input("Ingrese el valor de la casa: "))
if 80000 <= ingresos:
    pie = valorCasa*0.15
    pie = round(pie)
    resto = valorCasa-pie
    pagoMensual = round(resto/120)
    print(f"El pie a pagar es de ${pie} correspondiente al 15% del valor de la casa")
    print(f"El valor de cada pago mensual es de ${pagoMensual} por un periodo de 10 años")
else:
    pie = valorCasa*0.3
    pie = round(pie)
    resto = valorCasa-pie
    pagoMensual = round(resto/84)
    print(f"El pie a pagar es de ${pie} correspondiente al 30% del valor de la casa")
    print(f"El valor de cada pago mensual es de ${pagoMensual} por un periodo de 7 años")

