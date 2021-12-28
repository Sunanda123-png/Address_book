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
    address_list = []

    def add_person(self, person_address):
        """
        Creating this method for adding person in list
        :param person_address:
        :return:
        """
        self.address_list.append(person_address)

    def show_details(self):
        """
        for display the inputted value created show details method
        :return:
        """
        for address in self.address_list:
            print("The firstname is :-", address.first_name)
            print("The lastname is :- ", address.last_name)
            print("Age of this person is :- ", address.age)
            print("Mobile number is :- ", address.mobile_no)
            print("Email id is :- ", address.email)
            print("The state of this person is :- ", address.state)
            print("Pin number is :- ", address.pin_no)

    def edit_details(self):
        """
        for editing the existing details created edit_details method
        :return:
        """
        try:
            contact_name = input("Enter the Firstname of person which you want to edit information:- ")
            for contact in self.address_list:
                if contact.first_name == contact_name:
                    print("""Your choice:-
                                    1.First name
                                    2.Last name
                                    3.Age
                                    4.Mobile number
                                    5.Email
                                    6.State
                                    7.Pin number
                                    """)
                    choices = int(input("Enter your choice:- "))
                    if choices == 1:
                        firstname = input("Enter the new first name:- ")
                        contact.first_name = firstname
                    elif choices == 2:
                        lastname = input("Enter new last name:- ")
                        contact.last_name = lastname
                    elif choices == 3:
                        ages = int(input("Enter new age:- "))
                        contact.age = ages
                    elif choices == 4:
                        mobile_number = int(input("Enter new mobile number:- "))
                        contact.mobile_no = mobile_number
                    elif choices == 5:
                        email_id = input("Enter new email id:-")
                        contact.email = email_id
                    elif choices == 6:
                        state_person = input("Enter new state:- ")
                        contact.state = state_person
                    elif choices == 7:
                        pin_number = int(input("Enter new pin number:- "))
                        contact.pin_no = pin_number
                    else:
                        print("Wrong choice!!!")
                        break
        except Exception:
            logging.exception("Type proper value!!!")

    def delete_contact(self):
        """
        Delete the contact details as per user choice
        :return:
        """
        try:
            delete_contact = input("Enter the first name you want to delete:- ")
            for contact in self.address_list:
                if contact.first_name == delete_contact:
                    self.address_list.remove(contact)
                else:
                    print("Name not found")
        except Exception:
            logging.exception("Type string value!!!")


if __name__ == "__main__":
    address_book = AddressBook()
    try:
        while True:
            print("""
                Choose as per your wish:-
                1.Add person
                2.Show details
                3.Edit details
                4.Delete contact
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
            elif choice == 3:
                address_book.edit_details()
            elif choice == 4:
                address_book.delete_contact()

    except Exception:
        logging.exception("Enter proper value!!!")
