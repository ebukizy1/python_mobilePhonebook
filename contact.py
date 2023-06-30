class Contact:

    def __init__(self, name, phone_number):
        self.__name = name
        self.__phone_number = phone_number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self.__phone_number = phone_number

    def __str__(self):
        return f"NAME : {self.__name} "\
               f"PHONE NUMBER : {self.__phone_number}"

