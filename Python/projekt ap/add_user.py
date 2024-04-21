import json
def add_user(login):
    with open('user_data.json', 'r') as file:
        data = json.load(file)
    data['Persons'][login]={}
    data['Persons'][login]['login']=login
    data['Persons'][login]['Imie']=input("Podaj imie: ")
    data['Persons'][login]['Nazwisko']=input("Podaj Nazwisko: ")
    data['Persons'][login]['Email']=input("Podaj Email: ")
    password1=True
    password2=False
    while password1!=password2 or len(password1)<6:
        password1=input("Podaj Haslo: ")
        password2=input("Powtorz Haslo: ")
    data['Persons'][login]['Password']=password1
    data['Persons'][login]['Treningi']={}
    with open('user_data.json', 'w') as file:
        json.dump(data, file, indent=4)
    print("Uzytkownik dodany pomyslnie")
with open('user_data.json', 'r') as file:
    data = json.load(file)
login=input("Podaj swoj login ")
if not login in data['Persons']:
    add_user(login)