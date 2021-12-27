import logging

"""
Author:- Sunanda Shil
Date:- 27-12-21
"""
logging.basicConfig(filename="address_book.log", filemode="w")


class Contact:
    """
    created class for person address
    """

    def __init__(self, contact_dict):
        """
        created constructor for initialize the variable
        :param contact_dict:
        """
        self.first_name = contact_dict.get("first_name")
        self.last_name = contact_dict.get("last_name")
        self.age = contact_dict.get("age")
        self.mobile_no = contact_dict.get("mobile_no")
        self.email = contact_dict.get("email")
        self.state = contact_dict.get("state")
        self.pin_no = contact_dict.get("pin_no")


class AddressBook:
    """
    created address book class for making require method
    """

    def __init__(self):
        """
        initializing the constructor
        """
        self.address_list = []

    def add_person(self, person_address):
        """
        Creating this method for adding person in list
        :param person_address:
        :return:
        """
        self.address_list.append(person_address)

    def show_details(self):
        for address in self.address_list:
            print("The firstname is :-", address.first_name)
            print("The lastname is :- ", address.last_name)
            print("Age of this person is :- ", address.age)
            print("Mobile number is :- ", address.mobile_no)
            print("Email id is :- ", address.email)
            print("The state of this person is :- ", address.state)
            print("Pin number is :- ", address.pin_no)


if __name__ == "__main__":
    address_book = AddressBook()
    try:
        while True:
            print("""
                Choose as per your wish:-
                1.Add person
                2.Show details
                """)
            choice = int(input("Enter your choice:- "))
            if choice == 1:
                first_name = input("Enter first name:- ")
                last_name = input("Enter last name:- ")
                age = int(input("Enter ages:- "))
                mobile_no = int(input("Enter the mobile number:- "))
                email = input("Enter the email id:- ")
                state = input("Enter the state :-")
                pin_no = int(input("Enter the pin number:- "))
                contact_dict = {"first_name": first_name, "last_name": last_name, "age": age,
                                "mobile_no": mobile_no, "email": email, "state": state, "pin_no": pin_no}
                contact = Contact(contact_dict)
                address_book.add_person(contact)
            elif choice == 2:
                address_book.show_details()

    except Exception:
        logging.exception("Enter proper value!!!")
