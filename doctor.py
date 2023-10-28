from patient import Patient


class Doctor(Patient):
    def __init__(self, ismi, familyasi, ssn, id, mutaxasislik) -> None:
        self._id = id
        self._mutaxasislik = mutaxasislik
        self._bemor_list: list[Patient] = [] 
        super().__init__(ismi, familyasi, ssn)
        
    @property
    def bemorlar(self):
        return self._bemor_list
    @property
    def id(self):
        return self._id
    
    @property
    def mutaxasislik(self):
        return self._mutaxasislik
    
    def collentPatient(self, patiend_id):
        self._bemor_list.append(patiend_id)
        print('doctorga bemor biriktirildi !!.. ')

    def getPatients(self):
        return self._bemor_list

    def __str__(self) -> str:
        return f'{self.ismi}, {self.familyasi} id ---> {self.id}, mutaxasislik --> {self.mutaxasislik}'