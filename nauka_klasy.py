class DataLoad:
    """Klasa z danymi"""

    def __init__(self, name, surname, place, typ):
        self.name = name
        self.surname = surname
        self.place = place
        self.typ = typ

    def read(self, lista):
        for a in range(0, len(lista)):
            print("\nObiekt", a,
                  "\nImie: ", lista[a].name,
                  "\nNazwisko: ", lista[a].surname,
                  "\nMiejsce: ", lista[a].place,
                  "\nTyp: ", lista[a].typ)


def load(file):
    f = open(file, "r")
    data = f.read()
    return data


# utworzenie obiektu
var_object = DataLoad(None, None, None, None)

# wczytanie danych z pliku
database = "user_base.txt"
dane = load(database).split(";")
# print(dane)

# stworzenie listy i objectów oraz zapisanie ich do listy
object_list = []

for i in range(0, len(dane), 4):
    var_object = DataLoad(dane[i], dane[i + 1], dane[i + 2], dane[i + 3])
    object_list.append(var_object)

# odczyt objektów z listy objektów
var_object.read(object_list)
