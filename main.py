jahr = int(input("Wann ist ihr Geburtsjahr?"))
import time
aktuelles_jahr = time.localtime().tm_year
alter = aktuelles_jahr - jahr
print(f"Sie sind {alter} Jahre alt.")

if alter < 18:
    print("Sie sind minderjährig.")
elif alter >= 18 and alter < 65:
    print("Sie sind volljährig.")
else:
    print("Sie sind im Rentenalter.")

alter_in_10_jahren = alter + 10
print(f"In 10 Jahren werden Sie {alter_in_10_jahren} Jahre alt sein.")

next_year = aktuelles_jahr + 1
alter_nächstes_jahr = alter + 1
print(f"Nächstes Jahr ({next_year}) werden Sie {alter_nächstes_jahr} Jahre alt sein.")  

ihr_name = input("Wie heißen Sie?")
print(f"Hallo {ihr_name}, schön Sie kennenzulernen!")

print("Vielen Dank für die Nutzung dieses Programms. Auf Wiedersehen!")
      