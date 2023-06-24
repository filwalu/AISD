def zbuduj_graf():
    print("Witaj! Zbudujmy graf.")

    # Wybór rodzaju grafu
    rodzaj_grafu = input("Wybierz rodzaj grafu (skierowany/nieskierowany/ważony): ")

    # Pobranie liczby wierzchołków
    liczba_wierzcholkow = int(input("Podaj liczbę wierzchołków: "))

    # Inicjalizacja macierzy sąsiedztwa
    macierz_sasiedztwa = [[0] * liczba_wierzcholkow for _ in range(liczba_wierzcholkow)]

    # Inicjalizacja listy sąsiedztwa
    lista_sasiedztwa = [[] for _ in range(liczba_wierzcholkow)]

    # Pobranie połączeń pomiędzy wierzchołkami
    liczba_polaczen = int(input("Podaj liczbę połączeń: "))

    for _ in range(liczba_polaczen):
        zrodlo = int(input("Podaj wierzchołek źródłowy: "))
        cel = int(input("Podaj wierzchołek docelowy: "))

        if rodzaj_grafu == "ważony":
            waga = float(input("Podaj wagę połączenia: "))
            macierz_sasiedztwa[zrodlo][cel] = waga

        else:
            macierz_sasiedztwa[zrodlo][cel] = 1

        if rodzaj_grafu == "nieskierowany":
            if rodzaj_grafu == "ważony":
                macierz_sasiedztwa[cel][zrodlo] = waga
            else:
                macierz_sasiedztwa[cel][zrodlo] = 1

        lista_sasiedztwa[zrodlo].append(cel)

        if rodzaj_grafu == "nieskierowany":
            lista_sasiedztwa[cel].append(zrodlo)

    print("\nMacierz sąsiedztwa:")
    for wiersz in macierz_sasiedztwa:
        print(wiersz)

    print("\nLista sąsiedztwa:")
    for wierzcholek, sasiedzi in enumerate(lista_sasiedztwa):
        print(f"{wierzcholek}: {sasiedzi}")

    print("\nInterpretacja graficzna:")
    for wierzcholek in range(liczba_wierzcholkow):
        sasiedzi = lista_sasiedztwa[wierzcholek]
        print(f"{wierzcholek} -> {sasiedzi}")

    print("\nDziękujemy za skorzystanie z programu!")


zbuduj_graf()
