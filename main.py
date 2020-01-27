from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox('C:/Users/egor/geckodriver')
browser.get('https://www.lacentrale.fr/cote-voitures-renault-megane--2006-.html')

cars = browser.find_elements_by_class_name('listingResultLine.auto')
count_of_cars = len(cars)
print(count_of_cars)
YOUR_NAME_OF_CAR = '307 2.0I 16V XS PREMIUM'
car_number = 0
car_name = ""
cheapest_car = ""
cheapest_car_money = 99999999
count_of_similar = 0
most_similar_count = 0
most_similar_name = ''
YOUR_NAME_OF_CAR = YOUR_NAME_OF_CAR.split()
print(YOUR_NAME_OF_CAR)


while car_number < count_of_cars:

        cars = browser.find_elements_by_class_name('listingResultLine.auto')
        link = cars[car_number].find_element_by_partial_link_text('')
        car_characteristic = link.text
        car_characteristic = car_characteristic.split()
        print(car_characteristic)
        for name1 in car_characteristic:
            for name2 in YOUR_NAME_OF_CAR:
                if name1.lower() == name2.lower():
                    count_of_similar += 1
        if count_of_similar > most_similar_count:
            most_similar_count = count_of_similar
            most_similar_name = link.text
        car_number += 1    

print(**********************)
print(most_similar_name)
print(**********************)

    

    
