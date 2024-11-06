class Hotel:
    def init(self, budget=0, name="Unnamed Hotel", visitors_per_year=0, number_of_rooms=0, owner_name="Unknown owner", year_of_creation=0):
        self.budget = budget
        self.__name = name
        self.__visitors_per_year = visitors_per_year
        self.__number_of_rooms = number_of_rooms
        self.owner_name = owner_name
        self.year_of_creation = year_of_creation

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value > self.__budget:
            print("Error: Insufficient funds!")
        else:
            self.__budget -= value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def visitors_per_year(self):
        return self.__visitors_per_year

    @visitors_per_year.setter
    def visitors_per_year(self, value):
        self.__visitors_per_year = value

    @property
    def number_of_rooms(self):
        return self.__number_of_rooms

    @number_of_rooms.setter
    def number_of_rooms(self, value):
        self.__number_of_rooms = value



    def str(self):
        return f"Name: {self.__name}, Visitors per year: {self.__visitors_per_year}, Rooms: {self.__number_of_rooms}, Owner: {self.owner_name}, Year of creation: {self.year_of_creation}"

    def __del__(self):
        return f"Object {self.__name} is deleted"

    def main(self):

       hotel1 = Hotel(10000 ," Breath " , 5000  , 65 , "Cristiano", 2003 )
       hotel2 = Hotel(20000," Ocean " ,1200, 35, "Messi" , 1990 )
       hotel3 = Hotel(30000 , " Grant " , 7500 , 50 , "Rick" , 2010)
       print(hotel1.___str___())






hotel0 = Hotel()
hotel0.main()