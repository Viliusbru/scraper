class Flight:
    def __init__(self, outbound_departure: str, outbound_arrival: str, outbound_departure_time: str, outbound_arrival_time: str, inbound_departure: str, inbound_arrival: str, inbound_departure_time: str, inbound_arrival_time: str, price: float, taxes: float) -> None:
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
