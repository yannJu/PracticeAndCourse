class Box:
    def __init__(self, width = 0, length = 0, height = 0):
        self.__width = width
        self.__length = length
        self.__height = height

    def setWidth(self, width):
        self.__width = width

    def setLength(self, length):
        self.__length = length

    def setHeight(self, height):
        self.__height = height

    def getVolume(self):
        return self.__width * self.__height * self.__length

    def __str__(self):
        return "({}, {}, {})".format(self.__width, self.__length, self.__height)

b = Box()
b.setWidth(100)
b.setLength(100)
b.setHeight(100)
print(b)
print(b.getVolume())