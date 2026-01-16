temperatura = 0
aQueVaAConvertir = input('¿Deseas convertir a (F)ahrenheit o (C)elcius?: ').upper()


if(aQueVaAConvertir == 'F'):
    fahrenheit = int(input('Ingresa la temperatura en grados Fahrenheit: '))
    celcius = (fahrenheit - 32) * 5/9
    print(f'La temperatura en Celcius es: {celcius}°C')
elif(aQueVaAConvertir == 'C'):
    celcius = int(input('Ingresa la temperatura en grados Celcius: '))
    fahrenheit = (celcius * 9/5) + 32
    print(f'La temperatura en Fahrenheit es: {fahrenheit}°F')
else: 
    print('Opción no válida. Por favor ingresa "F" o "C".')


