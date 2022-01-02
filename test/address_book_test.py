from address_book import AddressBook, Contact


def test_add_person():
    """
    testing the add_person method
    """
    address_book = AddressBook("ss")
    contact_dict = {"first_name": "sunanda", "last_name": "shil", "age": 25, "mobile_no": 7578061886,
                    "email": "ssunanda02@gmail.com", "state": "Assam", "pin_no": 784115}
    contact = Contact(contact_dict)
    address_book.add_person(contact)
    assert len(address_book.contact_list) > 0


def test_edit_details():
    """
    testing the edit details method
    """
    address_book = AddressBook("ss")
    contact_dict = {"first_name": "sunanda", "last_name": "shil", "age": 25, "mobile_no": 7578061886,
                    "email": "ssunanda02@gmail.com", "state": "Assam", "pin_no": 784115}
    contact = Contact(contact_dict)
    address_book.add_person(contact)
    address_book.edit_contact("sunanda",1,"rahul")
    assert address_book.contact_list[0].first_name == "rahul"


def test_delete_contact():
    """
    test delete contact method
    """
    address_book = AddressBook("ss")
    contact_dict = {"first_name": "sunanda", "last_name": "shil", "age": 25, "mobile_no": 7578061886,
                    "email": "ssunanda02@gmail.com", "state": "Assam", "pin_no": 784115}
    contact = Contact(contact_dict)
    address_book.add_person(contact)
    address_book.delete_contact("sunanda")
    assert len(address_book.contact_list) == 0


def test_get_adress_book():
    """
    testing the get address book method
    """
    address_book = AddressBook("ss")
    assert isinstance(address_book, AddressBook) == True
