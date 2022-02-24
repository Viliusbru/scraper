from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from flight import Depart, Return, Flight

PATH = 'C:\Program Files (x86)\chromedriver.exe'
op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome(PATH, options=op)
# driver = webdriver.Chrome(PATH)
url = 'https://www.fly540.com/flights/nairobi-to-mombasa?isoneway=0&depairportcode=NBO&arrvairportcode=MBA&date_from=Tue%2C+1+Mar+2022&date_to=Tue%2C+8+Mar+2022&adult_no=1&children_no=0&infant_no=0&currency=USD&searchFlight='
driver.get(url)

departing = driver.find_element(By.CLASS_NAME, "fly5-depart")
departing_flights = departing.find_elements(By.CLASS_NAME, "fly5-result")
inbound = driver.find_element(By.CLASS_NAME, "fly5-return")
inbound_flights = inbound.find_elements(By.CLASS_NAME, "fly5-result")


departing_objects = []
inbound_objects = []
# INSERT DEPARTING FLIGHT DATA


def create_departing_classes(departing_flights):
    for departing in departing_flights:
        # DEPARTING DATA
        depart_data = departing.find_element(
            By.CSS_SELECTOR, '[data-title="Departs"]')
        outbound_departure = depart_data.find_element(
            By.CLASS_NAME, 'flfrom').text
        outbound_departure = outbound_departure.rstrip()[-4:-1]
        outbound_departure_time = depart_data.find_element(
            By.CLASS_NAME, 'fltime').text
        depart_date = depart_data.find_element(
            By.CLASS_NAME, 'fldate').text
        outbound_departure_time = outbound_departure_time + depart_date

        # ARIVAL DATA
        arival_data = departing.find_element(
            By.CSS_SELECTOR, '[data-title="Arrives"]')
        inbound_departure = arival_data.find_element(
            By.CLASS_NAME, 'flfrom').text.rstrip()[-4:-1]
        arival_departure_time = arival_data.find_element(
            By.CLASS_NAME, 'fltime').text
        arival_date = arival_data.find_element(
            By.CLASS_NAME, 'fldate').text
        arival_departure_time = arival_departure_time + arival_date
        outbound_flight_key = departing.find_element(By.CLASS_NAME,
                                                     "flight-classes").get_attribute('data-flight-key')
        departing_objects.append(Depart(outbound_departure, inbound_departure,
                                        outbound_departure_time, arival_departure_time, outbound_flight_key))


def create_returning_classes(inbound_flights):
    for outbound in inbound_flights:
        # DEPARTING DATA
        outbound_data = outbound.find_element(
            By.CSS_SELECTOR, '[data-title="Departs"]')
        outbound_departure = outbound_data.find_element(
            By.CLASS_NAME, 'flfrom').text
        outbound_departure = outbound_departure.rstrip()[-4:-1]
        outbound_departure_time = outbound_data.find_element(
            By.CLASS_NAME, 'fltime').text
        depart_date = outbound_data.find_element(
            By.CLASS_NAME, 'fldate').text
        outbound_departure_time = outbound_departure_time + depart_date

        # ARIVAL DATA
        arival_data = outbound.find_element(
            By.CSS_SELECTOR, '[data-title="Arrives"]')
        inbound_departure = arival_data.find_element(
            By.CLASS_NAME, 'flfrom').text.rstrip()[-4:-1]
        arival_departure_time = arival_data.find_element(
            By.CLASS_NAME, 'fltime').text
        arival_date = arival_data.find_element(
            By.CLASS_NAME, 'fldate').text
        arival_departure_time = arival_departure_time + arival_date
        outbound_flight_key = outbound.find_element(By.CLASS_NAME,
                                                    "flight-classes").get_attribute('data-flight-key')
        inbound_objects.append(Return(outbound_departure, inbound_departure,
                                      outbound_departure_time, arival_departure_time, outbound_flight_key))


def input_flight_key(depart_flight_key, inbound_flight_key):
    driver.execute_script(
        f"document.getElementById('outbound-solution-id').setAttribute('value', '{depart_flight_key}')")
    driver.execute_script(
        "document.getElementById('outbound-cabin-class').setAttribute('value', '0')")
    driver.execute_script(
        f"document.getElementById('inbound-solution-id').setAttribute('value', '{inbound_flight_key}')")
    driver.execute_script(
        "document.getElementById('inbound-cabin-class').setAttribute('value', '0')")

    # driver.close()


create_departing_classes(departing_flights)
create_returning_classes(inbound_flights)
for departing in departing_objects:
    for inbound in inbound_objects:
        input_flight_key(departing.depart_flight_key,
                         inbound.depart_flight_key)
        continue_btn = driver.find_element(By.ID, "continue-btn").click()
        total_price_breakdown = driver.find_element(
            By.CLASS_NAME, "fly5-totalprice")
        total_price = total_price_breakdown.find_element(
            By.CLASS_NAME, "fly5-price")
        breakdown = driver.find_element(By.CLASS_NAME, "fly5-breakdown")
        out_tax = breakdown.find_elements(
            By.CSS_SELECTOR, "div")[2]
        out_tax = out_tax.find_element(By.CLASS_NAME, "num")
        print('asdasdasdasd', out_tax)

        # both = breakdown.find_elements(
        #     By.CLASS_NAME, "fly5-bkdown")
        # for i in both:
        #     tax = i.find_elements(By.CSS_SELECTOR, "div")[1]
        #     print('aaaaaaa', tax.get_attribute('outerHTML'))
