class Depart:
    def __init__(self, outbound_departure: str, outbound_arrival: str, outbound_departure_time: str, outbound_arrival_time: str, depart_flight_key: str) -> None:
        self.outbound_departure = outbound_departure
        self.outbound_arrival = outbound_arrival
        self.outbound_departure_time = outbound_departure_time
        self.outbound_arrival_time = outbound_arrival_time
        self.depart_flight_key = depart_flight_key


class Return:
    def __init__(self, inbound_departure: str, inbound_arrival: str, inbound_departure_time: str, inbound_arrival_time: str, depart_flight_key: str) -> None:
        self.inbound_departure = inbound_departure
        self.inbound_arrival = inbound_arrival
        self.inbound_departure_time = inbound_departure_time
        self.inbound_arrival_time = inbound_arrival_time
        self.depart_flight_key = depart_flight_key


class Flight:
    def __init__(self, outbound_departure: str, outbound_arrival: str, outbound_departure_time: str, outbound_arrival_time: str, inbound_departure: str, inbound_arrival: str, inbound_departure_time: str, inbound_arrival_time: str, price: int, taxes: int) -> None:
        self.outbound_departure = outbound_departure
        self.outbound_arrival = outbound_arrival
        self.outbound_departure_time = outbound_departure_time
        self.outbound_arrival_time = outbound_arrival_time
        self.inbound_departure = inbound_departure
        self.inbound_arrival = inbound_arrival
        self.inbound_departure_time = inbound_departure_time
        self.inbound_arrival_time = inbound_arrival_time
        self.price = price
        self.taxes = taxes

    def __iter__(self):
        return iter([self.outbound_departure, self.outbound_arrival, self.outbound_departure_time, self.outbound_arrival_time, self.inbound_departure, self.inbound_arrival, self.inbound_departure_time, self.inbound_arrival_time, self.price])

    # def to_csv(flight):
    #     headers = ['outbound_departure_airport', 'outbound_arrival_airport', 'outbound_departure_time', 'outbound_arrival_time',
    #                'inbound_departure_airport', 'inbound_arrival_airport', 'inbound_departure_time', 'inbound_arrival_time', 'inbound_arrival_time', 'price', 'taxes']
    #     with open('data.csv', 'w', newline='', encoding='UTF8') as f:
    #         writer = csv.writer(f)
    #         writer.writerow(headers)
    #         writer.writerow(flight)
