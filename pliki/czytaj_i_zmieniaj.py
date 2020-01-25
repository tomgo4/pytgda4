F3 = 'plik3.txt'


def czytaj_i_zmieniaj(file):
    with open(file, 'a+') as f:
        print(f.tell())
        # f.write("moze cos dopisze")
        # f.seek(10)
        # f.write(" -- NA POCZATKU -- ")
        # f.seek(0)
        # print()
        # print(f.read())


if __name__ == "__main__":
    czytaj_i_zmieniaj(F3)
