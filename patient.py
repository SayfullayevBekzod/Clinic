class Patient:
    def __init__(self, ismi, familyasi, ssn) -> None:
        self._ismi = ismi
        self._familyasi = familyasi
        self._ssn = ssn
        self._doctor = None

    @property
    def ssn(self):
        return self._ssn
    
    @property
    def ismi(self):
        return self._ismi
    
    @property
    def familyasi(self):
        return self._familyasi
    
    @property
    def doctor(self):
        return self._doctor
    
    def collectDoctor(self, doctor_id):
        self._doctor = doctor_id
        print('doctor biriktirildi !!.. ')

    
    def __str__(self) -> str:
        return f'{self.ismi}, {self.familyasi} ssn ---> {self.ssn}'