from address_book import AddressBook, Contact


def test_add_person():
    """
    testing the add_person method
    :return:
    """
    address_book = AddressBook()
    contact_dict = {"first_name":"sunanda", "last_name":"shil", "age":25, "mobile_no":7578061886, "email":"ssunanda02@gmail.com", "state":"Assam", "pin_no":784115}
    contact = Contact(contact_dict)
    address_book.add_person(contact)
    assert len(address_book.address_list) > 0