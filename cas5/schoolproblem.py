class Wagon:
    def __init__(self, code):
        self.code = code
        self.passengers = []

    def add_passenger(self, name, surname, telephone, email):
        self.passengers.append({
            "name": name,
            "surname": surname,
            "telephone": telephone,
            "email": email
        })

    def remove_passenger(self, telephone):
        for passenger in self.passengers:
            if passenger['telephone'] == telephone:
                self.passengers.remove(passenger)
                return True
        return False

    def is_passenger_in_wagon(self, telephone):
        for passenger in self.passengers:
            if passenger['telephone'] == telephone:
                return True
        return False

class Train:
    total_wagons = 0

    def __init__(self, departure_station, arrival_station, departure_time, arrival_time):
        self.departure_station = departure_station
        self.arrival_station = arrival_station
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.wagons = []

    def add_wagon(self, wagon):
        self.wagons.append(wagon)
        Train.total_wagons += 1

    def reserve_seat(self, wagon_code, name, surname, telephone, email):
        for wagon in self.wagons:
            if wagon.code == wagon_code:
                if not wagon.is_passenger_in_wagon(telephone):
                    wagon.add_passenger(name, surname, telephone, email)
                    return f"Reservation successful for {name} {surname} in wagon {wagon_code}."
                else:
                    return "Passenger already has a reservation in this wagon."
        return "Wagon not found."

    def cancel_reservation(self, wagon_code, telephone):
        for wagon in self.wagons:
            if wagon.code == wagon_code:
                if wagon.remove_passenger(telephone):
                    return f"Reservation canceled for telephone number {telephone} in wagon {wagon_code}."
                else:
                    return "Reservation not found."
        return "Wagon not found."

    def get_wagon_passengers(self, wagon_code):
        for wagon in self.wagons:
            if wagon.code == wagon_code:
                return wagon.passengers
        return "Wagon not found."


# Example usage:
if __name__ == "__main__":
    train = Train("New York", "Los Angeles", "08:00 AM", "08:00 PM")
    wagon1 = Wagon("W01")
    wagon2 = Wagon("W02")

    train.add_wagon(wagon1)
    train.add_wagon(wagon2)

    print(train.reserve_seat("W01", "John", "Doe", "1234567890", "john@example.com"))
    print(train.reserve_seat("W02", "Jane", "Doe", "0987654321", "jane@example.com"))

    print(train.get_wagon_passengers("W01"))

    print(train.cancel_reservation("W01", "1234567890"))
    print(train.get_wagon_passengers("W01"))

    print(f"Total wagons: {Train.total_wagons}")
