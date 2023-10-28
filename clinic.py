from patient import Patient
from exeptions import NoSuchPatient, NoSuchDoctor
from doctor import Doctor

class Clinic:
    def __init__(self) -> None:
        self._patient_list: list[Patient] = []
        self._doctor_list: list[Doctor] = []

    def checkPatient(self, ssn):
        for patient in self._patient_list:
            if patient.ssn == ssn:
                return True
        return False

    def checkDoctor(self, ssn):
        for doctor in self._doctor_list:
            if doctor.ssn == ssn:
                return True
        return False

    def addPatient(self, patient: Patient):
        if self.checkPatient(patient.ssn) == False:
            self._patient_list.append(patient)
            return 'bemor ro\'yhatga olindi'
        return 'bemor ro\'yhatda mavjud'

    def getPatient(self, ssn):
        for patient in self._patient_list:
            if patient.ssn == ssn:
                return patient
        raise NoSuchPatient(ssn)

    def addDoctor(self, doctor: Doctor):
        if self.checkDoctor(doctor.ssn) == False:
            self._doctor_list.append(doctor)
            return 'shifokor ro\'yhatga olindi'
        return 'shifokor ro\'yhatda mavjud'

    def getDoctor(self, id):
        for doctor in self._doctor_list:
            if doctor.id == id:
                return doctor
        raise NoSuchDoctor(id, 'doctor')

    def assignPatientToDoctor(self, patient_ssn, doctor_id):
        if self.getPatient(patient_ssn) and self.getDoctor(doctor_id):
            bemor = self.getPatient(patient_ssn)
            doctor = self.getDoctor(doctor_id)
        bemor.collectDoctor(doctor_id)
        doctor.collentPatient(patient_ssn)


    def idleDoctors(self):
        idle_doctors = {}
        for doctor in self._doctor_list:
            if len(doctor.bemorlar) == 0:
                idle_doctors[doctor.familyasi] = doctor.ismi
        idle_doctors = sorted(idle_doctors.items() ,key=lambda x:x[1])
        return idle_doctors
    
    def busyDoctors(self):
        idle_doctors = {}
        count = 0
        for doctor in self._doctor_list:
            count += len(doctor.bemorlar)
        ort = count // len(self._doctor_list)
        for doctor in self._doctor_list:
            if len(doctor.bemorlar) >= ort:
                idle_doctors[doctor.familyasi] = doctor.ismi
        idle_doctors = sorted(idle_doctors.items() ,key=lambda x:x[1])
        return idle_doctors
    
    def doctorsByNumPatients(self):
        idle_doctors = []
        for doctor in self._doctor_list:
            if len(doctor.bemorlar) != 0:
                idle_doctors.append(f'{len(doctor.bemorlar)} -- {doctor.id}, {doctor.ismi}, {doctor.familyasi}')
        idle_doctors = sorted(idle_doctors, reverse=True)
        return idle_doctors
    
    def countPatientPerSpecialization(self):
        res = {}
        for doctor in self._doctor_list:
                if doctor.mutaxasislik not in res.keys():
                    res[doctor.mutaxasislik] = len(doctor.bemorlar)
                else:
                    res[doctor.mutaxasislik] += len(doctor.bemorlar)
        res = sorted(res.items(),key=lambda x:x[1], reverse=True)
        return res