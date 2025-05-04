class Bank:
    bank_name = "Mezan"
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def get_bank_name(self):
        print(f"{Bank.bank_name}")

first = Bank()
first.get_bank_name()
Bank.change_bank_name("ALfala")

sec = Bank()
sec.get_bank_name()

