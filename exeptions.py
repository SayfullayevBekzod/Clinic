class NoSuchPatient(Exception):
    def __init__(self, ssn, shaxs = 'bemor') -> None:
        self.message = str(ssn) + f' nomerli {shaxs} mavjud emas'
        super().__init__(self.message)

class NoSuchDoctor(NoSuchPatient):
    def __init__(self, ssn, shaxs) -> None:
        super().__init__(ssn, shaxs)
