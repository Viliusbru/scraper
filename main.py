from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from flight import Flight
from datetime import datetime
from datetime import timedelta
import csv
import calendar


# INSERT DEPARTING FLIGHT DATA

ALL_FLIGHT_LIST = []


def create_departing_classes(departing):
    # DEPARTING DATA
    ActionChains(driver).move_to_element(
        departing).click(departing).perform()
    departing.click()
    flight_cards = departing.find_element(By.CLASS_NAME, "comparetable")
    row = flight_cards.find_elements(By.CLASS_NAME, "row")[0]
    card_data = row.find_element(
        By.CLASS_NAME, "card")
    card_body = card_data.find_element(By.CLASS_NAME, "card-body")
    btn = card_body.find_element(By.TAG_NAME, "button")
    btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(btn))
    ActionChains(driver).move_to_element(btn).click(btn).perform()


# INSERT RETURNING FLIGHT DATA
def create_returning_classes(inbound):
    # DEPARTING DATA
    ActionChains(driver).move_to_element(
        inbound).click(inbound).perform()
    inbound.click()
    flight_cards = inbound.find_element(By.CLASS_NAME, "comparetable")
    row = flight_cards.find_elements(By.CLASS_NAME, "row")[0]
    card_data = row.find_element(
        By.CLASS_NAME, "card")
    card_body = card_data.find_element(By.CLASS_NAME, "card-body")
    btn = card_body.find_element(By.TAG_NAME, "button")
    btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(btn))
    ActionChains(driver).move_to_element(btn).click(btn).perform()


def get_data():
    # DEPART DATA
    flight_summary = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.ID, "fsummary")))
    flight_out = flight_summary.find_element(By.CLASS_NAME, "fly5-fout")
    flight_time_data = flight_out.find_element(By.CLASS_NAME, "fly5-det")
    flight_out_time_data = flight_time_data.find_element(
        By.CLASS_NAME, "fly5-timeout")
    flight_out_time = flight_out_time_data.find_element(
        By.CLASS_NAME, "fly5-ftime").text
    flight_out_date = flight_out_time_data.find_element(
        By.CLASS_NAME, "fly5-fdate").text
    outbound_departure_time = flight_out_time + ' ' + flight_out_date
    flight_landing_data = flight_time_data.find_element(
        By.CLASS_NAME, "fly5-timein")
    flight_landing_time = flight_landing_data.find_element(
        By.CLASS_NAME, "fly5-ftime").text
    flight_landing_date = flight_landing_data.find_element(
        By.CLASS_NAME, "fly5-fdate").text
    outbound_arrival_time = flight_landing_time + ' ' + flight_landing_date
    flight_container = flight_out.find_element(By.CLASS_NAME, "fly5-liner")
    depart_from = flight_container.find_element(
        By.CLASS_NAME, "fly5-frshort").text
    depart_to = flight_container.find_element(
        By.CLASS_NAME, "fly5-toshort").text
    # RETURN DATA
    flight_return = flight_summary.find_element(By.CLASS_NAME, "fly5-fin")
    flight_container = flight_return.find_element(By.CLASS_NAME, "fly5-liner")
    return_from = flight_container.find_element(
        By.CLASS_NAME, "fly5-frshort").text
    return_to = flight_container.find_element(
        By.CLASS_NAME, "fly5-toshort").text
    flight_time_data = flight_return.find_element(By.CLASS_NAME, "fly5-det")
    flight_out_time_data = flight_time_data.find_element(
        By.CLASS_NAME, "fly5-timeout")
    flight_out_time = flight_out_time_data.find_element(
        By.CLASS_NAME, "fly5-ftime").text
    flight_out_date = flight_out_time_data.find_element(
        By.CLASS_NAME, "fly5-fdate").text
    inbound_departure_time = flight_out_time + ' ' + flight_out_date
    flight_landing_data = flight_time_data.find_element(
        By.CLASS_NAME, "fly5-timein")
    flight_landing_time = flight_landing_data.find_element(
        By.CLASS_NAME, "fly5-ftime").text
    flight_landing_date = flight_landing_data.find_element(
        By.CLASS_NAME, "fly5-fdate").text
    inbound_arrival_time = flight_landing_time + ' ' + flight_landing_date
    # PRICE DATA
    total_price_breakdown = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "fly5-totalprice")))
    total_price = total_price_breakdown.find_element(
        By.CLASS_NAME, "fly5-price").text
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

    # CREATE OBJECT LIST
    ALL_FLIGHT_LIST.append(
        Flight(depart_from, depart_to, outbound_departure_time, outbound_arrival_time, return_from, return_to, inbound_departure_time, inbound_arrival_time, float(total_price), total_tax))


def click_continue():
    driver.execute_script("arguments[0].click();", WebDriverWait(
        driver, 20).until(EC.element_to_be_clickable((By.ID, "continue-btn"))))


def loop_for_data():
    departing = driver.find_element(By.CLASS_NAME, "fly5-depart")
    departing_flights = departing.find_elements(By.CLASS_NAME, "fly5-result")
    inbound = driver.find_element(By.CLASS_NAME, "fly5-return")
    inbound_flights = inbound.find_elements(By.CLASS_NAME, "fly5-result")
    for index1, depart in enumerate(departing_flights):
        departing = driver.find_element(By.CLASS_NAME, "fly5-depart")
        depart = departing.find_elements(By.CLASS_NAME, "fly5-result")
        inbound = driver.find_element(By.CLASS_NAME, "fly5-return")
        for index2, returning in enumerate(inbound_flights):
            departing = driver.find_element(By.CLASS_NAME, "fly5-depart")
            depart = departing.find_elements(By.CLASS_NAME, "fly5-result")
            inbound = driver.find_element(By.CLASS_NAME, "fly5-return")
            returning = inbound.find_elements(By.CLASS_NAME, "fly5-result")
            create_departing_classes(depart[index1])
            create_returning_classes(returning[index2])
            click_continue()
            get_data()
            driver.back()
            WebDriverWait(
                driver, 20).until(EC.element_to_be_clickable((By.TAG_NAME, "body"))).send_keys(Keys.HOME)


def write_to_csv(flight_list):
    headers = ['outbound_departure_airport', 'outbound_arrival_airport', 'outbound_departure_time', 'outbound_arrival_time',
               'inbound_departure_airport', 'inbound_arrival_airport', 'inbound_departure_time', 'inbound_arrival_time', 'price', 'taxes']
    with open('data.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for obj in flight_list:
            writer.writerow([obj.outbound_departure, obj.outbound_arrival, obj.outbound_departure_time, obj.outbound_arrival_time,
                            obj.inbound_departure, obj.inbound_arrival, obj.inbound_departure_time, obj.inbound_arrival_time, obj.price, obj.taxes])


def create_urls():
    # DEPART +10 days
    date_now = datetime.now()
    add_ten_days = date_now + timedelta(days=10)
    day_from = calendar.day_name[add_ten_days.weekday()][0:3]
    date_number_from = add_ten_days.day
    month_name_from = add_ten_days.strftime("%b")
    year_from = add_ten_days.year

    # RETURN DATE
    add_seven_days = add_ten_days + timedelta(days=7)
    day_to = calendar.day_name[add_seven_days.weekday()][0:3]
    date_number_to = add_seven_days.day
    month_name_to = add_seven_days.strftime("%b")
    year_to = add_seven_days.year

    # DEPART +20 days
    add_twenty_days = date_now + timedelta(days=20)
    day_from2 = calendar.day_name[add_twenty_days.weekday()][0:3]
    date_number_from2 = add_twenty_days.day
    month_name_from2 = add_twenty_days.strftime("%b")
    year_from2 = add_twenty_days.year

    # RETURN DATE
    add_seven_days2 = add_twenty_days + timedelta(days=7)
    day_to2 = calendar.day_name[add_seven_days2.weekday()][0:3]
    date_number_to2 = add_seven_days2.day
    month_name_to2 = add_seven_days2.strftime("%b")
    year_to2 = add_seven_days2.year

    urls = [f'https://www.fly540.com/flights/nairobi-to-mombasa?isoneway=0&depairportcode=NBO&arrvairportcode=MBA&date_from={day_from}%2C+{date_number_from}+{month_name_from}+{year_from}&date_to={day_to}%2C+{date_number_to}+{month_name_to}+{year_to}&adult_no=1&children_no=0&infant_no=0&currency=USD&searchFlight=',
            f'https://www.fly540.com/flights/nairobi-to-mombasa?isoneway=0&depairportcode=NBO&arrvairportcode=MBA&date_from={day_from2}%2C+{date_number_from2}+{month_name_from2}+{year_from2}&date_to={day_to2}%2C+{date_number_to2}+{month_name_to2}+{year_to2}&adult_no=1&children_no=0&infant_no=0&currency=USD&searchFlight=']

    return urls


for url in create_urls():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options, service=Service(
        ChromeDriverManager().install()))
    driver.get(url)
    driver.maximize_window()
    loop_for_data()


write_to_csv(ALL_FLIGHT_LIST)
driver.quit()
