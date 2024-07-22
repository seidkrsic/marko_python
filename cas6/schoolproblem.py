

class Wagon: 
    wagons = 0
    def __init__(self, code):
        self.code = code
        self.passengers = []
        Wagon.wagons += 1
    
    def add_passenger(self, name, surname, telephone, email):
        self.passengers.append({"name" : name, "surname" : surname, "telephone" : telephone, "email" : email}) 
        print("Successfuly added passenger!") 

    def is_passenger_in_wagon(self, telephone):
        for passenger in self.passengers:
            if passenger["telephone"] == telephone:
                return True
        return False 
    
    def remove_passenger(self, telephone):
        for passenger in self.passengers:
            if passenger["telephone"] == telephone:
                self.passengers.remove(passenger)
                return True 
        return False 

              

class Train: 
    def __init__(self, departure_station, arrival_station, departure_time, arrival_time):
        self.departure_station = departure_station
        self.arrival_station = arrival_station
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.wagons = []

    def add_wagon(self, wagon):
        self.wagons.append(wagon)
        print(f"{wagon.code} added successfully")

    def reserve_seat(self, wagon_code, name, surname, telephone, email):
        for wagon in self.wagons: 
            if wagon.code == wagon_code:
                if not wagon.is_passenger_in_wagon(telephone):
                    wagon.add_passenger(name, surname, telephone, email)
                else: 
                    print("Passenger already in this wagon.") 

    def cancel_reservation(self, telephone, wagon_code):
        for wagon in self.wagons:
            if wagon.code == wagon_code:
                if wagon.remove_passenger(telephone) == True: 
                    wagon.remove_passenger(telephone)
                    return True 
                else: 
                    return False 

    def get_passengers(self, wagone_code): 
        for wagon in self.wagons: 
            if wagon.code == wagone_code: 
                return wagon.passengers
            
        return "No such wagon" 

if __name__ == "__main__" : 
    train  = Train("Milano", "Bologna", "8AM", "10AM")  
    wagon1 = Wagon("w01")
    wagon2 = Wagon("w02")
    wagon3 = Wagon("w03")

    train.add_wagon(wagon1)
    train.add_wagon(wagon2) 
    train.add_wagon(wagon3) 
    train.reserve_seat("w01", "John", "Doe", "123456", "john@gmail.com")
    train.reserve_seat("w01", "John", "Doe", "123", "john@gmail.com")
    x = train.cancel_reservation("123", "w01") 
    print(x) 
    print(train.get_passengers("w03"))

    print(f"Total number of Wagons: {Wagon.wagons}") 