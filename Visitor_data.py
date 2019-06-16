''' CREATING A DATABASE OF CUSTOMERS LOOKING FOR CARS AND PROVIDING THEM REVIEWS OF VARIOUS CARS BASED ON THEIR BUDGET'''

class Person:
	''' CONTAINS THE DETAILS OF THE CUSTOMER'''
	def __init__(self,name,age,mailid,mobile, price):
		self.name = name
		self.age = age
		self.mailid = mailid
		self.mobile = mobile
		self.price = price
		self.choice = Choice(price)				# Creating a object of choice class inside a 
	def m1(self):
		detailsdict = {}
		detailsdict['Age'] = self.age
		detailsdict['mailid'] = self.mailid
		detailsdict['Mobile'] = self.mobile
		detailsdict['Budget'] =  self.price
		cdict[self.name] = detailsdict
		self.choice.method1()

class Choice:
	''' CHECKING THE BUDGET OF THE PERSON'''
	def __init__(self,budget):
		self.budget = budget
		self.bugcars = bugcars()
	def method1(self):
		if self.budget <= 300000:
			self.bugcars.carslt3lac()			
		elif self.budget > 300000 and self.budget <= 600000:
			self.bugcars.carslt6lac()
		elif self.budget >600000 and self.budget  <= 1000000:
			self.bugcars.carslt10lac()
		elif self.budget  > 1000000:
			self.bugcars.carsgt10lac()
			
class bugcars:
	''' THIS CLASS SHOWS VARIOUS CARS IN VARIOUS BUDGET RANGE'''
	def __init__(self):
		self.carreviews = Reviews()
	def carslt3lac(self):
		print('These are the available options between 3 lacs to 6 lacs')
		print('Tata Nano\n''Reanult Kwid\n''Datsun Redigo\n')
		vehicle = input('Enter the vehicle whose review you want to look(Nano/Kwid/Redigo): ')
		ques = input('Do you want to see its reviews(yes/no): ')
		if ques.lower() == 'yes':
			if vehicle.lower() == 'nano':
				self.carreviews.Nano()
			elif vehicle.lower() == 'kwid':
				self.carreviews.Kwid()
			elif vehicle.lower() == 'redigo':
				self.carreviews.Redigo()
			else:
				print('You have entered a invalid Car')
		else:
				ques2 = input('Do you want to see vehicle in range 3 lacs to 6 lacs(yes/no): ')
				if ques2.lower() == 'yes':
					self.carslt6lac()
				else:
					print('Thankyou for visiting us')
	def carslt6lac(self):
		print('These are the available options between 3 lacs to 6 lacs')
		print('Maruti Wagon R\n''Maruti Alto\n''Tata Tiago\n''Hyundai Santro\n''Maruti Suzuki Celerio\n')
		vehicle = input('Enter the vehicle whose review you want to look(Wagonr/Alto/Tiago/Santro/Celerio): ')
		ques = input('Do you want to see its reviews(yes/no): ')
		if ques.lower() == 'yes':
			if vehicle.lower() == 'alto':
				self.carreviews.Alto()
			elif vehicle.lower() == 'wagonr':
				self.carreviews.Wagonr()
			elif vehicle.lower() == 'tiago':
				self.carreviews.Tiago()
			elif vehicle.lower() == 'santro':
				self.carreviews.Santro()
			elif vehicle.lower() == 'celerio':
				self.carreviews.Celerio()
			else:
				print('You have entered a invalid Car')
		else:
			ques2 = input('Do you want to see vehicle in range 6 lacs to 10 lacs(yes/no): ')
			if ques2.lower() == 'yes':
				self.carslt10lac()
			else:
				print('Thankyou for visiting us')
	def carslt10lac(self):
		print('These are the available options between 6 lacs to 10 lacs')
		print('Maruti Suzuki Baleno\n''Maruti Swift\n''Tata Nexon\n''Hyundai i20\n''Maruti Suzuki Vitara Brezza\n')
		vehicle = input('Enter the vehicle whose review you want to look(Baleno/Swift/Nexon/i20/Brezza): ')
		ques = input('Do you want to see its reviews(yes/no): ')
		if ques.lower() == 'yes':
			if vehicle.lower() == 'baleno':
				self.carreviews.Baleno()
			elif vehicle.lower() == 'swift':
				self.carreviews.Swift()
			elif vehicle.lower() == 'nexon':
				self.carreviews.Nexon()
			elif vehicle.lower() == 'i20':
				self.carreviews.i20()
			elif vehicle.lower() == 'brezza':
				self.carreviews.Brezza()
			else:
				print('You have entered a invalid Car')
		else:
			ques2 = input('Do you want to see vehicle in range greater than 10 lacs(yes/no): ')
			if ques2.lower() == 'yes':
				self.carsgt10lac()
			else:
				print('Thankyou for visiting us')
	def carsgt10lac(self):
		print('These are the available options above 10 lacs')
		print('Toyota Fortuner\n''Mahindra Alturas G4\n''Tata Harrier\n''Hyundai Creta\n''Mahindra Marazzo\n')
		vehicle = input('Enter the vehicle whose review you want to look(Fortuner/Alturas/Harrier/creta/Marazzo): ')
		ques = input('Do you want to see its reviews(yes/no): ')
		if ques.lower() == 'yes':
			if vehicle.lower() == 'fortuner':
				self.carreviews.Fortuner()
			elif vehicle.lower() == 'alturas':
				self.carreviews.Alturas()
			elif vehicle.lower() == 'harrier':
				self.carreviews.Harrier()
			elif vehicle.lower() == 'creta':
				self.carreviews.Creta()
			elif vehicle.lower() == 'marazzo':
				self.carreviews.Marazzo()
			else:
				print('You have entered a invalid Car')
		else:
			print('Thankyou for visiting us, We hope you found what you were look for')

class Reviews():
	''' THIS CLASS CONTAINS THE REVIEWS OF VARIOUS CARS POSSIBLE IN DIFFERENT BUDGET RANGE'''
	def Nano(self):
		print('This is Tata Nano')
		print('It has NDTV rating of 6.6')
		print('It is a hatchback car with mileage of 21.9 kmpl')
	def Kwid(self):
		print('This is Renault Kwid')
		print('It has NDTV rating of 8.0')
		print('It is a hatchback car with mileage of 25.2 kmpl')
	def Redigo(self):
		print('This is Datsun Redi Go')
		print('It has NDTV rating of 7.6')
		print('It is a hatchback car with mileage of 22.7 kmpl')
	def Wagonr(self):
		print('This is Maruti Wagon R')
		print('It has NDTV rating of 6.1')
		print('It is a hatchback car with mileage range from 21.5-33.4 kmpl')
	def Alto(self):
		print('This is Maruti Suzuki Alto 800')
		print('It has NDTV rating of 6.6')
		print('It is a hatchback car with mileage of 24.7 kmpl')
	def Tiago(self):
		print('This is Tata Tiago')
		print('It has NDTV rating of 8.2')
		print('It is a hatchback car with mileage range from 23.8-27.2 kmpl')
	def Santro(self):
		print('This is Hyundai Santro')
		print('It has NDTV rating of 8.5')
		print('It is a hatchback car with mileage range from 20.3-30.5 kmpl')
	def Celerio(self):
		print('This is Maruti Suzuki Celerio')
		print('It has NDTV rating of 6.5')
		print('It is a hatchback car with mileage range from 23.1-31.8 kmpl')
	def Baleno(self):
		print('This is Maruti Suzuki Baleno')
		print('It has NDTV rating of 8.2')
		print('It is a hatchback car with mileage range from 21.4-27.4 kmpl')
	def Swift(self):
		print('This is Maruti Suzuki Swift')
		print('It has NDTV rating of 8.0')
		print('It is a hatchback car with mileage range from 22-28.4 kmpl')
	def Nexon(self):
		print('This is Tata Nexon')
		print('It has NDTV rating of 7.8')
		print('It is a SUV car with mileage range from 17-21.5 kmpl')		
	def i20(self):
		print('This is Hyundai i20')
		print('It has NDTV rating of 8.2')
		print('It is a hatchback car with mileage range from 18.6-22.5 kmpl')
	def Brezza(self):
		print('This is Maruti Suzuki Vitara Brezza')
		print('It has NDTV rating of 7.9')
		print('It is a SUV car with mileage of 24.3 kmpl')
	def Fortuner(self):
		print('This is Toyota Fortuner')
		print('It has NDTV rating of 8.3')
		print('It is a SUV car with mileage of 14.2 kmpl')
	def Alturas(self):
		print('This is Mahindra Alturas G4')
		print('It has NDTV rating of 8.0')
		print('It is a SUV car with mileage of 12.4 kmpl')
	def Harrier(self):
		print('This is Tata Harrier')
		print('It has NDTV rating of 6.5')
		print('It is a SUV car with mileage of 15.0 kmpl')
	def Creta(self):
		print('This is Hyundai Creta')
		print('It has NDTV rating of 8.0')
		print('It is a SUV car with mileage range from 15.3-21.4 kmpl')
	def Marazzo(self):
		print('This is Mahindra Marazzo')
		print('It has NDTV rating of 8.0')
		print('It is a SUV car with mileage of 17.6 kmpl')

import re, csv	
cdict = {}
try:
	with open('data.csv','r',newline = '') as f:
		w = csv.reader(f)		# Creating a CSV writer object pointing to the file.
		
except FileNotFoundError:
	with open('data.csv','w',newline = '') as f:
		w = csv.writer(f)	
		print('CREATING FILE')
		w.writerow(['NAME','AGE','MOBILE#','MAILID','PRICE_RANGE'])
		
finally:		
	while True:
		with open('data.csv','a', newline = '') as f:
			w = csv.writer(f)
			name = input('Enter you Full Name: ')
			age = int(input('Enter you age: '))
			while True:
				s = input('Mobile#: ')
				m = re.fullmatch('[6-9]\d{9}',s)	# Creating a match object to discard the invalid mobile number.
				if m != None:
					mobilenum = s
					print('Mobile No. you entered is {}'.format(s))
					break
				else:
					print('you have entered a invalid mobile number. Please try again')
				continue
			mobile = mobilenum
			while True:
				s = input('Emailid: ')
				m = re.fullmatch('\w[a-zA-Z0-9_.]*@[a-zA-Z0-9]+[.][a-z]+',s)	# Creating a match object to discard the invalid Email id.
				if m != None:
					emailid = s
					print('Entered Emailid is {}'.format(s))
					break
				else:
					print('you have entered a invalid Email number. Please try again')
				continue
			mailid = emailid
			price_range = int(input('Enter the price range in which you are looking for car: '))
			w.writerow([name,age,mobile,mailid,price_range])
			p = Person(name,age,mailid,mobile,price_range)
			p.m1()
			option = input('Do you want to insert one more record [Yes/No]: ')
			if option.lower() == 'no':
				break
	
