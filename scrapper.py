from selenium import webdriver
import time
import pandas as pd

file = pd.read_csv()

driver = webdriver.Chrome(executable_path=r'C:\path\to\ChromeDriver.exe')
driver.get('https://www.carvana.com/cars?page=1')
time.sleep(0.2)

Make = driver.find_elements_by_class_name("vehicle-make.MakeModelTrimstyles__VehicleMake-sc-1fjrpe9-2.holwOb")

for pls in Make:
    print(pls.text)
    time.sleep(0.2)

Model = driver.find.elements_by_class_name("vehicle-model MakeModelTrimstyles__VehicleModel-sc-1fjrpe9-1.byvBlP")
for gimme in Model:
    print(gimme.text)
    time.sleep(0.2)

Miles = driver.find_elements_by_class_name("vehicle-mileage.VehicleMileagestyles__VehicleMileageWrapper-uui7q8-0.btouIQ")

for idk in Miles:
    print(idk.text)
    time.sleep(0.2)

Price = driver.find_elements_by_class_name("vehicle-price.VehiclePricestyles__VehiclePriceWrapper-sc-5x47dg-2.kbkrNn")

for whoknows in Price:
    print(whoknows.text)
    time.sleep(0.2)
