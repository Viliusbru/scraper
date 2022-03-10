# scraper
Using the following website www.fly540.com you need to collect required data for ALL round trip flight 
combinations from NBO (Nairobi) to MBA (Mombasa) departing 10 and 20 days from the current date 
and returning 7 days after the departure date. The required data:
o departure airport, arrival airport - Outbound and inbound departure and arrival flight IATA airport 
code extracted from the source (it is a three-letter geocode designating many airports and 
metropolitan areas around the world)
o departure time, arrival time - Time including date in any human understandable format extracted 
from the source.
o cheapest fare price - final price which would be paid by the customer for the selected outbound 
and inbound flight.
2. After finishing the task above, please implement additional logic to extract taxes with the same flight 
combinations described above:
o taxes - There can be many different types of taxes included in the final price of a flight. This field 
should include all of the taxes for the selected flight combination.
