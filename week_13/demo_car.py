###################################################
# Instructional  Python file to outline inheritance 
# author: Cyndy Ishida
####################################################

##
# Car base/parent class, no error checking
##
class Car( object ):
    def __init__( self, model, company , name = ""):
        self.__model = model
        self.__name = name
        self.__company = company


    def __repr__(self):
        return "This car is: {} model, and is made from : {}".format(self.__model, self.__company)

    def __str__(self):
        if self.__name != "":
            car_output = "This car was named: {} by it's owner\nIt was made by the company: {}\nIt is an: {} model.\n".format(self.__name,self.__company , self.__model)
        else: 
            car_output = "This car was made by the company: {}\nIt is an: {} model.\n".format(self.__company, self.__model)

        return car_output

##
# Tesla Car, no error checking =
##
class Tesla( Car ):
    def __init__( self, model, voltage , name = "" ):
        Car.__init__(self, model , "Tesla", name)   # REALLY IMPORTANT LINE 
        self.__volt = voltage 
    
    def __str__(self):
        tesla_output = Car.__str__(self)
        tesla_output += "It has {} volt power.".format(self.__volt)
        return tesla_output




##
# Ford car 
##
class Ford( Car ):
    def __init__(self,model, year = 0, name = "" ):
        Car.__init__(self,model, "Ford", name )
        self.__year = year

    
    def __str__(self):
        ford_output = Car.__str__(self)
        if self.__year != 0:
            ford_output += "This car was made in year: {}".format(self.__year)
            if self.__year < 1980:
                ford_output  += "Wow, Whata classic!"

        return ford_output


