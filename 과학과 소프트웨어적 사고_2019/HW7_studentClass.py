class Student:
    studentCnt = 0
    def getStudentCnt():
        return Student.getStudentCnt
    def setStudentCnt(self,number):
        Student.studentCnt = number
        return Student.studentCnt
    def __init__(self, name=None, age=0, phone = 0, id = 0, group = None, major = None):
        Student.studentCnt += 1
        self.__name = name
        self.__age = age
        self.__phone = phone
        self.__id = id
        self.__group = group
        self.__major = major
        self.__number = Student.studentCnt
    #getter
    def getAge(self):
        return self.__age
    def getName(self):
        return self.__name
    def getPhone(self):
        return self.__phone
    def getId(self):
        return self.__id
    def getGroup(self):
        return self.__group
    def getMajor(self):
        return self.__major
    #setter
    def setAge(self, age):
        self.__age = age
    def setName(self, name):
        self.__name = name
    def setPhone(self, phone):
        self.__phone = phone
    def setID(self, id):
        self.__id = id
    def setGroup(self, group):
        self.__group = group
    def setMajor(self, major):
        self.__major = major
    #오버로딩 _add_
    def __add__(self, other):
        return self.__age + other.getAge()

