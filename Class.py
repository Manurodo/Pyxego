from datetime import datetime, date

class fecha:
    def __init__(self, age_cadena):

        self.age_cadena = age_cadena

    def valid (self, age_cadena):
        try:
            age = datetime.strptime(age_cadena, "%Y-%m-%d").date()
            self.age = age
        except ValueError:
            return None
        
        try:
            if self.age > date.today():
                return False  # La fecha es futura
            return True  # La fecha es válida y no es futura
        except ValueError:
            return None  # La fecha no es válida
        
    def underage(self):
        today = date.today()
        diff = today.year - self.age.year
        if diff > 18:
            return False
        else:
            return True



class Compañero: 

    aula = "A404"

    def __init__(self, name, age, sex, telf):
        self.name = name
        self.age = age
        self.sex = sex
        self.telf = telf
        self.hobbies = []
        self.notes = []
        self.friends = []
        self.date_birth = ()

    def intro(self):
        return f"Wenas gente, me llamo {self.name} y tengo {self.age} años."
    
    def add_hobby(self, hobby):
        self.hobbies.append(hobby)
        return f"{self.name} añadió {hobby} como un nuevo hobby"
    
    def show_hobby(self):
        if self.hobbies:
            return f"Los pasatiempos de {self.name} son: {','.join(self.hobbies)}"
        else:
            return f"{self.name} no tiene pasatiempos aún."
        
    def birthday(self):
        self.age += 1
        return f"{self.name} acaba de tener un cumpleaños, ahora tiene {self.age} años"
    
    def add_note(self, note):
        self.notes.append(note)
        return f"{self.name} añadio una nueva nota"
    
    def add_friend(self, friend):
        self.friends.append(friend)
        return f"{self.name} es ahora amigo de {friend}"
    
    def info(self):
        return print(f"{self.name}, {self.age}, {self.sex}, {self.telf}, {self.hobbies}, {self.friends}, {self.notes}") 
    
    def date_of_birth(self):

        return 

class BankAccount:
    def __init__(self, acc_num, name):
        self.acc_num = acc_num
        self.balance = 0
        self.name = name
        
    def depositar(self, ammount):
        ammount = float (ammount)
        self.balance = self.balance + ammount
        return (f"El nuevo balance es {self.balance}€")

    def retirar(self, ammount):
        ammount = float (ammount)
        if self.balance >= ammount:
            self.balance = self.balance - ammount
            return (f"El nuevo balance es {self.balance}€")

        else:
            return ("no existe suficiente dinero en la cuenta")
    
    def cantidad(self):
        return (f"El balance es: {self.balance}€")
    
class Pokemon:
    def __init__(self, name):
        self.hp = 0
        self.level = 0
        self.name = name

        





