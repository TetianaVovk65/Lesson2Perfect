class Human:

    def __init__(self, name: str, surname: str, age: int, phone: str, address: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        print(f'Hello! {self.name}{self.surname}{self.age}{self.phone}{self.address}')

    def call(self, phone_number):
        print(f'{self.phone} вызывает абонента {phone_number}')


bob = Human('Bob', ' Yoy ', 25, '  +1 123412512412', ' Shevchenka')
tom = Human('Tom', ' Youtube', 32, ' +380 661234124', ' Puliya')
john = Human('John', ' Jually', 35, ' +380 55123124', ' Juraska')

bob.get_info()
tom.get_info()
john.get_info()
bob.call(phone_number = '+380 965665')

