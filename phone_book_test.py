import unittest
import phone_book

class phone_books(unittest.TestCase):

    def test_phone_book_can_exit(self):
        my_phonebook = phone_book.PhoneBook
        self.assertIsNotNone(my_phonebook)

    def test_phone_book_can_be_lock(self):
        my_phonebook = phone_book.PhoneBook("emmanuel", "12345")
        my_phonebook.is_locked()
        self.assertTrue(my_phonebook.is_locked())

    def test_phone_book_can_be_unlock(self):
        my_phonebook = phone_book.PhoneBook("emmanuel", "12344")
        my_phonebook.unlock("12344")
        self.assertFalse(my_phonebook.is_locked())

    def test_phone_book_cannot_be_unlock_with_wrong_password(self):
        my_phonebook = phone_book.PhoneBook("emmanuel", "12345")
        self.assertRaises(TypeError, my_phonebook.unlock, "2323")

    def test_phone_book_can_create_contact(self):
        my_phone_book = phone_book.PhoneBook("emmanuel", "12345")
        my_phone_book.create_contact("segun", "08141221934")
        my_phone_book.contact_size()
        self.assertEqual(1, my_phone_book.contact_size())

    def test_phone_book_can_add_more_than_two_contact(self):
        my_phone_book = phone_book.PhoneBook("emmanuel", "12345")
        my_phone_book.create_contact("segun", "08141221934")
        my_phone_book.create_contact("lol", "12345")
        self.assertEqual(2, my_phone_book.contact_size())

    def test_phone_book_can_search_for_contact(self):
        my_phone_book = phone_book.PhoneBook("emmanuel", "12345")
        my_phone_book.create_contact("segun", "09037375208")
        my_phone_book.create_contact("dele", "09141221934")
        contact = my_phone_book.search_for_contact("dele")
        self.assertEqual("NAME : dele PHONE NUMBER : 09141221934", contact.__str__())

    def test_phone_book_cannot_search_for_contact_that_doest_not_exist(self):
        my_phone_book = phone_book.PhoneBook("emmanuel", "12345")
        my_phone_book.create_contact("segun", "09037375208")
        my_phone_book.create_contact("dele", "09141221934")
        self.assertRaises(TypeError, my_phone_book.search_for_contact, "de5He")

    def test_phone_book_can_delete_contact(self):
        my_phone_book = phone_book.PhoneBook("emmanuel", "12345")
        my_phone_book.create_contact("segun", "09037375208")
        my_phone_book.create_contact("dele", "09141221934")
        my_phone_book.remove_contact("dele")
        self.assertEqual(1, my_phone_book.contact_size())

    def test_phone_book_cannot_delete_contact_that_name_doesnt_exit(self):
        my_phone_book = phone_book.PhoneBook("emmanuel", "12345")
        my_phone_book.create_contact("segun", "09037375208")
        my_phone_book.create_contact("dele", "09141221934")
        self.assertRaises(TypeError,  my_phone_book.remove_contact, "del45e" )