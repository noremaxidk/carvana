from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'C:\path\to\chromedriver.exe')
time.sleep(0.2)

for i in range(1, 500):
    url = 'https://www.carvana.com/cars?page=' + str(i)
    driver.get(url)
    time.sleep(0.2)
    getthismug = driver.find_elements_by_class_name("ShowroomResultTile__ShowroomTileWrapper-n5q2qt-0.fobSgr.styles__ResultTileWrapper-sc-1algal3-0.gUbYju")
    time.sleep(0.3)
    for what in getthismug:
        Make = what.find_element_by_class_name("vehicle-make.MakeModelTrimstyles__VehicleMake-sc-1fjrpe9-2.holwOb")
        Model = what.find_element_by_class_name("vehicle-model.MakeModelTrimstyles__VehicleModel-sc-1fjrpe9-1.byvBlP")
        Miles = what.find_element_by_class_name("vehicle-mileage.VehicleMileagestyles__VehicleMileageWrapper-uui7q8-0.btouIQ")
        time.sleep(0.2)
        Price = what.find_element_by_class_name("vehicle-price.VehiclePricestyles__VehiclePriceWrapper-sc-5x47dg-2.kbkrNn")
        print(Make.text,'/',Model.text,'%',Miles.text,'/',Price.text)
        time.sleep(0.1)
