print("Witam w kalkulatorze :-)")
while True:
    try:
        option = int(input("Wybierz opcję:\n1. Dodawanie\n2. Odejmowanie \n3. Mnożenie\n4. Dzielenie\n"
                           "5. Pierwiastkowanie\n6. Potęgowanie\n7. Procent z liczby\n8. Koniec\n>> "))

        # Sprawdzenie, czy użytkownik chce zakończyć działanie kalkulatora
        if option == 8:
            print("Dziękujemy za skorzystanie z naszego kalkulatora :-)")
            break

        # Funkcja pomocnicza do pobierania liczby
        def get_number(prompt):
            return float(input(prompt))

        # Podstawowe operacje arytmetyczne
        if option in [1, 2, 3, 4]:
            number1 = get_number("Podaj pierwszą liczbę:\n>>  ")
            number2 = get_number("Podaj drugą liczbę\n>> ")

            if option == 1:
                answer = number1 + number2
            elif option == 2:
                answer = number1 - number2
            elif option == 3:
                answer = number1 * number2
            elif option == 4:
                if number2 == 0:
                    print("Błąd: Nie można dzielić przez zero!")
                    continue
                answer = number1 / number2

        # Pierwiastkowanie
        elif option == 5:
            number1 = int(input("Z jakiej liczby chcesz pierwiastek:\n>> "))
            number2 = int(input("Jakiego stopnia:\n>> "))
            answer = pow(number1, 1 / number2)

        # Potęgowanie
        elif option == 6:
            number1 = int(input("Podaj liczbę do zpotęgowania:\n>> "))
            number2 = int(input("Podaj stopień potęgi:\n>> "))
            answer = pow(number1, number2)

        # Obliczanie procentu z liczby
        elif option == 7:
            number1 = int(input("Podaj liczbę:\n>> "))
            number2 = int(input("Jaki procent chcesz z tej liczby:\n>> "))
            answer = number1*number2/100

        else:
            print("Nieprawidłowa opcja, wybierz ponownie.")
            continue

        print("Wynik: ", answer)

    except ValueError:
        print("Błąd: Wprowadzono nieprawidłową wartość. Spróboj ponownie")
