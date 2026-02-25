class Contact:
    print("===Contact Directory===")

    phone_directory = []

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        Contact.phone_directory.append(self.phone)

    def show_contact(self):
        return f"Name: {self.name}, Phone: {self.phone}"

    @classmethod
    def show_all_phone(cls):
        if not cls.phone_directory:
            print("There is no contact!")
        else:
            for phone in cls.phone_directory:
                print(phone)


c1 = Contact("Yash", 9759521722)
c2 = Contact("Bharat", 96238238232)
c3 = Contact("Ram", 8929722922)

Contact.show_all_phone()
