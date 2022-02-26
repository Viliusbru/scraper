from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from flight import Depart, Return, Flight
import time


url = 'https://www.fly540.com/flights/nairobi-to-mombasa?isoneway=0&depairportcode=NBO&arrvairportcode=MBA&date_from=Tue%2C+1+Mar+2022&date_to=Tue%2C+8+Mar+2022&adult_no=1&children_no=0&infant_no=0&currency=USD&searchFlight='
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options, service=Service(
    ChromeDriverManager().install()))
driver.get(url)

departing = driver.find_element(By.CLASS_NAME, "fly5-depart")
departing_flights = departing.find_elements(By.CLASS_NAME, "fly5-result")
inbound = driver.find_element(By.CLASS_NAME, "fly5-return")
inbound_flights = inbound.find_elements(By.CLASS_NAME, "fly5-result")


departing_objects = []
inbound_objects = []


# INSERT DEPARTING FLIGHT DATA
def create_departing_classes(departing):
    # for departing in departing_flights:
    # DEPARTING DATA
    ActionChains(driver).move_to_element(
        departing).click(departing).perform()
    departing.click()
    flight_cards = departing.find_element(By.CLASS_NAME, "comparetable")
    row = flight_cards.find_elements(By.CLASS_NAME, "row")[0]
    card_data = row.find_element(
        By.CLASS_NAME, "card")
    card_body = card_data.find_element(By.CLASS_NAME, "card-body")
    print(card_body.get_attribute('innerHTML'))
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    btn = card_body.find_element(By.TAG_NAME, "button")
    # print(btn.get_attribute('outerHTML'))
    btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(btn))
    ActionChains(driver).move_to_element(btn).click(btn).perform()

    # ARIVAL DATA
    # arival_data = departing.find_element(
    #     By.CSS_SELECTOR, '[data-title="Arrives"]')
    # inbound_departure = arival_data.find_element(
    #     By.CLASS_NAME, 'flfrom').text.rstrip()[-4:-1]
    # arival_departure_time = arival_data.find_element(
    #     By.CLASS_NAME, 'fltime').text
    # arival_date = arival_data.find_element(
    #     By.CLASS_NAME, 'fldate').text
    # arival_departure_time = arival_departure_time + arival_date
    # outbound_flight_key = departing.find_element(By.CLASS_NAME,
    #                                             "flight-classes").get_attribute('data-flight-key')
    # departing_objects.append(Depart(outbound_departure, inbound_departure,
    #                                 outbound_departure_time, arival_departure_time, outbound_flight_key))


# INSERT RETURNING FLIGHT DATA
def create_returning_classes(inbound):
    # for inbound in inbound_flights:
    # DEPARTING DATA
    ActionChains(driver).move_to_element(
        inbound).click(inbound).perform()
    inbound.click()
    flight_cards = inbound.find_element(By.CLASS_NAME, "comparetable")
    row = flight_cards.find_elements(By.CLASS_NAME, "row")[0]
    card_data = row.find_element(
        By.CLASS_NAME, "card")
    card_body = card_data.find_element(By.CLASS_NAME, "card-body")
    print(card_body.get_attribute('innerHTML'))
    print('bbbbbbbbbbbbbbbbbbbbbbbbbbbb')
    btn = card_body.find_element(By.TAG_NAME, "button")
    # print(btn.get_attribute('outerHTML'))
    btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(btn))
    ActionChains(driver).move_to_element(btn).click(btn).perform()

    # ARIVAL DATA
    # arival_data = outbound.find_element(
    #     By.CSS_SELECTOR, '[data-title="Arrives"]')
    # inbound_departure = arival_data.find_element(
    #     By.CLASS_NAME, 'flfrom').text.rstrip()[-4:-1]
    # arival_departure_time = arival_data.find_element(
    #     By.CLASS_NAME, 'fltime').text
    # arival_date = arival_data.find_element(
    #     By.CLASS_NAME, 'fldate').text
    # arival_departure_time = arival_departure_time + arival_date
    # outbound_flight_key = outbound.find_element(By.CLASS_NAME,
    #                                             "flight-classes").get_attribute('data-flight-key')
    # inbound_objects.append(Return(outbound_departure, inbound_departure,
    #                               outbound_departure_time, arival_departure_time, outbound_flight_key))


# for departing in departing_flights:
#     departing.click()
#     first_card = departing.find_element(
#         By.ID, "flt0417-0")
#     card = first_card.find_element(
#         By.CLASS_NAME, "card")
#     card_body = card.find_element(By.CLASS_NAME, "card-body")
#     button = first_card.find_element(By.TAG_NAME, "button").click()


def input_flight_key(depart_flight_key, inbound_flight_key):
    driver.execute_script(
        f"document.getElementById('outbound-solution-id').setAttribute('value', '{depart_flight_key}')")
    driver.execute_script(
        "document.getElementById('outbound-cabin-class').setAttribute('value', '0')")
    driver.execute_script(
        f"document.getElementById('inbound-solution-id').setAttribute('value', '{inbound_flight_key}')")
    driver.execute_script(
        "document.getElementById('inbound-cabin-class').setAttribute('value', '0')")


def all_requests(departing, inbound):
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "outbound-solution-id")))
    input_flight_key(departing.depart_flight_key,
                     inbound.depart_flight_key)
    print(departing.depart_flight_key)
    print(inbound.depart_flight_key)
    continue_btn = driver.find_element(By.ID, "continue-btn")
    driver.execute_script(
        "return arguments[0].scrollIntoView(true);", continue_btn)
    continue_btn.click()
    total_price_breakdown = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "fly5-totalprice")))
    total_price = total_price_breakdown.find_element(
        By.CLASS_NAME, "fly5-price")

    breakdown = driver.find_element(By.CLASS_NAME, "fly5-breakdown")
    breakdown_outgoing_div_tax = breakdown.find_elements(
        By.CLASS_NAME, "fly5-bkdown")[0]
    breakdown_outgoing_div_tax = breakdown_outgoing_div_tax.find_elements(
        By.CSS_SELECTOR, "div")[1]
    out_tax = breakdown_outgoing_div_tax.find_element(
        By.CLASS_NAME, "num").get_attribute('innerHTML')

    breakdown_return_div_tax = breakdown.find_elements(
        By.CLASS_NAME, "fly5-bkdown")[1]
    breakdown_return_div_tax = breakdown_return_div_tax.find_elements(
        By.CSS_SELECTOR, "div")[1]
    return_tax = breakdown_return_div_tax.find_element(
        By.CLASS_NAME, "num").get_attribute('innerHTML')

    total_tax = float(out_tax) + float(return_tax)
    print(total_tax)


def click_continue():
    # continue_btn = driver.find_element(By.ID, "continue-btn")
    driver.execute_script("arguments[0].click();", WebDriverWait(
        driver, 20).until(EC.element_to_be_clickable((By.ID, "continue-btn"))))
    # driver.execute_script(
    #     "return arguments[0].scrollIntoView(true);", continue_btn)
    # continue_btn.click()


# for count, departing in enumerate(departing_objects):
#     for count1, inbound in enumerate(inbound_objects):
#         print(count, count1)
#         all_requests(departing, inbound)
#         driver.back()
#         driver.implicitly_wait(3)

for count1, depart in enumerate(departing_flights):
    departing = driver.find_element(By.CLASS_NAME, "fly5-depart")
    depart = departing.find_elements(By.CLASS_NAME, "fly5-result")
    inbound = driver.find_element(By.CLASS_NAME, "fly5-return")
    for count2, returning in enumerate(inbound_flights):
        departing = driver.find_element(By.CLASS_NAME, "fly5-depart")
        depart = departing.find_elements(By.CLASS_NAME, "fly5-result")
        inbound = driver.find_element(By.CLASS_NAME, "fly5-return")
        returning = inbound.find_elements(By.CLASS_NAME, "fly5-result")
        create_departing_classes(depart[count1])
        print(count1, count2)
        create_returning_classes(returning[count2])
        click_continue()
        driver.back()
        WebDriverWait(
            driver, 20).until(EC.element_to_be_clickable((By.TAG_NAME, "body"))).send_keys(Keys.HOME)
