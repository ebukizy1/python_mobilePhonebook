from phonebook.contact import Contact


class PhoneBook:

    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__is_locked = True
        self.__contacts = []

    def is_locked(self):
        return self.__is_locked

    def unlock(self, password):
        if self.__password == password:
            self.__is_locked = False
        else:
            raise TypeError("wrong password enter")

    def create_contact(self, name, phone_number):
         my_contact = Contact(name, phone_number) 
         self.__contacts.append(my_contact)

    def contact_size(self):
        return len(self.__contacts)

    def search_for_contact(self, name):
        for contact in self.__contacts:
            if name == contact.name:
                return contact

        raise TypeError("name enter not found in the list")

    def remove_contact(self, name):
        for contact in self.__contacts:
            if name == contact.name:
                self.__contacts.remove(contact)
                break
        else:
            raise TypeError("name enter not found in the list")



    
