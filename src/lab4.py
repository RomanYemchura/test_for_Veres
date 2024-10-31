class Hotel:
    def __init__(self,buget = 0 ,   name = " Unnamed Hotel", visitors_per_year = 0, number_of_rooms = 0 , owner_name = " Unknown owner " ,year_of_creation = 0 ):


        self.__visitors_per_year = visitors_per_year
        self.__number_of_rooms = number_of_rooms
        self.__name = name
        self.year_of_creation = year_of_creation
        self.owner_name = owner_name
        self.__buget = buget


    def get_buget(self):
        return self.__buget
    def set_buget(self, value):
        self.__buget -= value
        if self.__buget < value:
            print("Error")





    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name



    def get_visitors_per_year(self):
        return self.__visitors_per_year
    def set_visitors_per_year(self, visitors_per_year):
        self.__visitors_per_year = visitors_per_year


    def get_number_of_rooms(self):
        return self.__number_of_rooms
    def set_number_of_rooms(self , number_of_rooms):
        self.__number_of_rooms = number_of_rooms



    def ___str___(self):
        return f"name : {self.__name} , visitors per year : {self.__visitors_per_year} , number of rooms : {self.__number_of_rooms} , owner name : {self.owner_name} , year of creation : {self.year_of_creation}"


    def __del__(self):
        return f"Object {self.__name} is deleted"

    def main(self):

       hotel1 = Hotel(10000 ," Breath " , 5000  , 65 , "Cristiano", 2003 )
       hotel2 = Hotel(20000," Ocean " ,1200, 35, "Messi" , 1990 )
       hotel3 = Hotel(30000 , " Grant " , 7500 , 50 , "Rick" , 2010)
       print(hotel1.___str___())






hotel0 = Hotel()
hotel0.main()