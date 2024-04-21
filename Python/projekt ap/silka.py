import json

# Otwórz plik JSON do odczytu
with open('user_data.json', 'r') as file:
    data = json.load(file)

# Odczytaj konkretne informacje i przypisz je do zmiennych
imie = data['osoba']['imie']
nazwisko = data['osoba']['nazwisko']
wiek = data['osoba']['wiek']
ulica = data['osoba']['adres']['ulica']
miasto = data['osoba']['adres']['miasto']
kod_pocztowy = data['osoba']['adres']['kod_pocztowy']
email = data['osoba']['email']
telefon = data['osoba']['telefon']

# Wyświetl odczytane dane
print(f"Imię: {imie}")
print(f"Nazwisko: {nazwisko}")
print(f"Wiek: {wiek}")
print(f"Adres: {ulica}, {kod_pocztowy}, {miasto}")
print(f"Email: {email}")
print(f"Telefon: {telefon}")
with open('user_data.json', 'r') as file:
    data = json.load(file)

# Dodaj dodatkowe informacje
data['osoba']['drugie_imie'] = 'Tomasz'

# Zapisz zaktualizowany obiekt JSON do pliku
with open('user_data.json', 'w') as file:
    json.dump(data, file, indent=4)

