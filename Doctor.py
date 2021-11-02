# Question Link: https://www.computerdeveloper.in/2021/04/tcs-xplore-cpa-11-april-2021-python-coding-question-solution.html
class Doctor:
	def __init__(self,*args):
		self.doctorId = int(args[0])
		self.doctorName = args[1]
		self.deptName = args[2]
		self.consultFee = int(args[3])
		self.sundayAvailable = args[4]

class Hospital:
	def __init__(self,doctorList):
		self.dList = doctorList

	def getDoctorList(self,deptName):
		ans = []
		for obj in self.dList:
			if obj.deptName.lower() == deptName.lower() and obj.sundayAvailable == "available":
				ans.append(obj)

		if len(ans):
			return ans
		else:
			return None

	def selectDoctor(self,fee):
		temp = len(self.dList)
		for obj in self.dList:
			if obj.sundayAvailable == "not available" and obj.consultFee > fee:
				self.dList.remove(obj)

		if len(self.dList) < temp:
			return True
		else:
			return False

if __name__ == "__main__":
	doctorList = []
	for i in range(5):
		doctorId = input()
		doctorName = input()
		deptName = input()
		consultFee = input()
		sundayAvailable = input()

		D = Doctor(doctorId,doctorName,deptName,consultFee,sundayAvailable)
		doctorList.append(D)

	H = Hospital(doctorList)
	deptName = input()
	fee = int(input())

	doctors = H.getDoctorList(deptName)

	if len(doctors):
		for obj in doctors:
			print(f'Doctor Id:{obj.doctorId}')
			print(f'Doctor Name:{obj.doctorName}')
	else:
		print("Doctor not found!")

	val = H.selectDoctor(fee)

	if val:
		for Obj in doctorList:
			print(f'Doctor Id:{Obj.doctorId}')
			print(f'Doctor Name:{Obj.doctorName}')
			print(f'Doctor Fee:{Obj.consultFee}')
	else:
		print("Returning the original list:")
		for Obj in doctorList:
			print(f'Doctor Id:{Obj.doctorId}')
			print(f'Doctor Name:{Obj.doctorName}')