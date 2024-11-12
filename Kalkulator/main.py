print("Witam w kalkulatorze :-)")
while True:
    option = int(input("Wybierz opcję:\n1. Dodawanie\n2. Odejmowanie \n3. Mnożenie\n4. Dzielenie\n"
                       "5. Pierwiastkowanie\n6. Potęgowanie\n7. Procent z liczby\n8. Koniec\n>> "))

    if option == 8:
        print("Dziękujemy za skorzystanie z naszego kalkulatora :-)")
        break
    if option < 5:
        def calculator(optioncalc):
            number1 = int(input("Podaj pierwszą liczbę:\n>>  "))
            number2 = int(input("Podaj drugą liczbę\n>> "))
            if optioncalc == 1:
                answercalc = number1 + number2
            elif optioncalc == 2:
                answercalc = number1 - number2
            elif optioncalc == 3:
                answercalc = number1 * number2
            elif optioncalc == 4:
                answercalc = number1 / number2
            return answercalc

        answer = calculator(option)

    elif option == 5:
        number1 = int(input("Z jakiej liczby chcesz pierwiastek:\n>> "))
        number2 = int(input("Jakiego stopnia:\n>> "))
        answer = pow(number1, 1 / number2)

    elif option == 6:
        number1 = int(input("Podaj liczbę do zpotęgowania:\n>> "))
        number2 = int(input("Podaj stopień potęgi:\n>> "))
        answer = pow(number1, number2)

    elif option == 7:
        number1 = int(input("Podaj liczbę:\n>> "))
        number2 = int(input("Jaki procent chcesz z tej liczby:\n>> "))
        answer = number1*number2/100

    print("Wynik: ", answer)