class Person:
    def __init__(self, lastName, firstName, middleInitial,streetAddress, city, state, zipCode, phoneNumber, eMail):
        self.__lastName = lastName
        self.__firstName = firstName
        self.__middleInitial = middleInitial
        self.__streetAddress = streetAddress
        self.__city = city
        self.__state = state
        self.__zipCode = zipCode
        self.__phoneNumber = phoneNumber
        self.__eMail = eMail

    def getLastName(self):
        return self.__lastName
    def getFirstName(self):
        return self.__firstName
    def getMiddleInitial(self):
        return self.__middleInitial
    def getStreetAddress(self):
        return self.__streetAddress
    def getCity(self):
        return self.__city
    def getState(self):
        return self.__state
    def getZipCode (self):
        return self.__zipCode
    def getPhoneNumber (self):
        return self.__phoneNumber
    def getEmail(self):
        return self.__eMail

    def setLastName(self, LastName):
        self.__lastName = lastName
    def setFirstname(self, firstName):
        self.__firstName = firstName
    def setMiddleInitial(self, middleInitial):
        self.__middleInitial = middleInitial
    def setStreetAddress(self, streetAddress):
        self.__streetAddress = selfAddress
    def setCity(self, city):
        self.__city = city
    def setZipCode(self, zipCode):
        self.__zip = zipCode
    def setPhoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber
    def setEmail(self, eMail):
        self.__eMail = eMail

    def getVerification(self):
        return "Name: " + self.__lastName + ", " + self.__firstName + " " + self.__middleInitial +  \
               "\nStreet Address: " + self.__streetAddress + \
               "\nCity, State Zip: " + self.__city + " " + self.__state + " " + self.__zipCode +   \
               "\nPhone Number: " + self.__phoneNumber +  \
               "\neMail: " + self.__eMail
 


'''
lastName = "Woodburn"
firstName = "Matthew"
middleInitial = "O"
address = "10 Circle Rock Drive"
city = "Ephrata"
state = "PA"
zipCode = "17522"
phoneNumber = "6074274393"
eMail = "mkwoodburn@gmail.com"
    
    
p1 = Person(lastName, firstName, middleInitial, address, city, state, zipCode, phoneNumber, eMail)
'''


    
    
