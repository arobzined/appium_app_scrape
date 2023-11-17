from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
import time

capabilities = {
    "automationName":"UiAutomator2",
    "platformName":"Android",
    "deviceName":"192.168.56.101:5555",
    "appPackage": "com.sahibinden",
    "appActivity": "com.sahibinden.ui.supplementary.UrlForwardingActivity",
}

# I used UiAutomator for testing my application , i created my android device with the help of Genymotion , I haven't mentioned here
# but i used Android version 9.0 . I also mentioned my app's package and activity sources for opening app automatically.

capabilities_ = UiAutomator2Options().load_capabilities(capabilities)

appium_server_url = 'http://192.168.56.1:4723' #local_server

class Scraper():
    def __init__(self, input_):
        self.driver = webdriver.Remote(appium_server_url, options=capabilities_)        #webdriver
        self.data = dict()                                                              #data that is stored from the app i used
        self.car_ids = set()                                                            #page's spesific car id's
        self.input_ = input_                                                            #input i got from console (Input.py)
    
    def wait_parameter(self,xpath_):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((AppiumBy.XPATH, xpath_)))
    def click_parameter(self,xpath_):
        element = self.driver.find_element(AppiumBy.XPATH, xpath_)
        element.click()
    def send_text_to_textbox(self, text_box_XPATH, text_to_send):
        self.wait_parameter(text_box_XPATH)
        text_box = self.driver.find_element(AppiumBy.XPATH, text_box_XPATH)
        text_box.send_keys(text_to_send)

    # Helper functions : 
    # wait_parameter -> waits until the element presents
    # click_parameter -> click the parameter
    # send_text_to_textbox -> send the input we got to textboxes
    def go_to_result_page(self):
        
        #CLICK "VASITA" ON THE HOME PAGE
        self.wait_parameter('//android.widget.TextView[@text="Vasıta"]')
        self.click_parameter('//android.widget.TextView[@text="Vasıta"]')

        #CLICK THE POP-UP ON THE UPPER-LEFT SIDE
        self.wait_parameter('//android.widget.TextView[@text="Otomobil"]')
        self.click_parameter('//android.widget.TextView[@text="Otomobil"]')

        #CLICK "Otomobil" BUTTON
        self.wait_parameter('//android.widget.TextView[@text="Otomobil"]')
        self.click_parameter('//android.widget.TextView[@text="Otomobil"]')

        #In here , i choose the brand and model inputs before going to the "Filtre" page , because in this way it works
        #faster and make more sence since we already can choose the brand and model.

        self.wait_parameter('(//android.widget.TextView[@resource-id="com.sahibinden:id/util_primary_text"])[1]')
        if(self.input_["marka"]):
            self.scroll_to_element('//android.widget.TextView[@text="{}"]'.format(self.input_["marka"]))
            self.wait_parameter('(//android.widget.TextView[@resource-id="com.sahibinden:id/util_primary_text"])[1]')
            if(self.input_['model']):
                self.scroll_to_element('//android.widget.TextView[@text="{}"]'.format(self.input_['model']))
        
        #CLICK THE SERCH BUTTON ON UPPER SIDE.
        
        self.wait_parameter('(//android.widget.TextView[@resource-id="com.sahibinden:id/util_primary_text"])[1]')
        self.click_parameter('(//android.widget.TextView[@resource-id="com.sahibinden:id/util_primary_text"])[1]')

        self.wait_parameter('//android.widget.Button[@text="İzin Verme"]')
        self.click_parameter('//android.widget.Button[@text="İzin Verme"]')

        self.filter_car() #-> FILTER_PAGE
        # WE HAVE THE CARS PAGE !!!!!!!
    
    #Another helper function , which i used for finding the brand and model names. this code basically
    #looking for the input we search in the app page and swipes the screen until we can see the input.
    #Mobile Apps do not let us to choose the input we want if it is not on the screen , even if we can see in the app source. 
    def scroll_to_element(self, desired_element_XPATH):
        max_attempts = 10 
        current_attempt = 0
        element_found = False

        while current_attempt < max_attempts and not element_found:
            try:
                element = self.driver.find_element(AppiumBy.XPATH, desired_element_XPATH)
                if element.is_displayed():
                    element_found = True
                    self.click_parameter(desired_element_XPATH)
                    break
            except:
                pass 

            self.driver.swipe(350, 1150, 350, 650, 1000)

        if not element_found:
            print("Element not found after scrolling.")
    #Helper -> Swipe the screen vertically
    def scroll_to_element_(self):
       self.driver.swipe(350, 1200, 350, 450, 1000)

    def filter_car(self):

        self.wait_parameter('//android.widget.TextView[@resource-id="com.sahibinden:id/tvFilter"]')
        self.click_parameter('//android.widget.TextView[@resource-id="com.sahibinden:id/tvFilter"]')        #press Filter Button
        
        #I checked the input if they are exist or not , if they are i basically press the spesific filter attribute and send the input
        #i have.
        if(self.input_["fiyat"]):
            self.wait_parameter('//android.widget.TextView[@text="Fiyat"]')
            self.click_parameter('//android.widget.TextView[@text="Fiyat"]')
            if(self.input_["fiyat"][0]):
                self.send_text_to_textbox('//android.widget.EditText[@resource-id="com.sahibinden:id/minAmountEditText"]',self.input_["fiyat"][0])
            if(self.input_["fiyat"][1]):
                self.send_text_to_textbox('//android.widget.EditText[@resource-id="com.sahibinden:id/maxAmountEditText"]',self.input_["fiyat"][1])
            
            self.wait_parameter('//android.widget.Button[@resource-id="android:id/button1"]')
            self.click_parameter('//android.widget.Button[@resource-id="android:id/button1"]')

        if(self.input_["yil"]):
            self.wait_parameter('//android.widget.TextView[@text="Yıl"]')
            self.click_parameter('//android.widget.TextView[@text="Yıl"]')

            self.wait_parameter('//android.widget.EditText[@resource-id="com.sahibinden:id/minValueEditText"]')
            if(self.input_["yil"][0]):
                self.send_text_to_textbox('//android.widget.EditText[@resource-id="com.sahibinden:id/minValueEditText"]',self.input_["yil"][0])
            if(self.input_["yil"][1]):
                self.send_text_to_textbox('//android.widget.EditText[@resource-id="com.sahibinden:id/maxValueEditText"]',self.input_["yil"][1])

            self.wait_parameter('//android.widget.Button[@resource-id="android:id/button1"]')
            self.click_parameter('//android.widget.Button[@resource-id="android:id/button1"]')
            
        if(self.input_["vites"]):
            self.wait_parameter('//android.widget.TextView[@text="Vites"]')
            self.click_parameter('//android.widget.TextView[@text="Vites"]')

            if(self.input_["vites"] == "Manuel"):
                self.click_parameter('//android.widget.CheckedTextView[@text="Manuel"]')
            else:
                self.click_parameter('//android.widget.CheckedTextView[@text="Otomatik"]')

            self.wait_parameter('//android.widget.Button[@resource-id="android:id/button1"]')
            self.click_parameter('//android.widget.Button[@resource-id="android:id/button1"]')

        if(self.input_["km"]):
            self.wait_parameter('//android.widget.TextView[@text="KM"]')
            self.click_parameter('//android.widget.TextView[@text="KM"]')

            self.wait_parameter('//android.widget.EditText[@resource-id="com.sahibinden:id/minValueEditText"]')
            if(self.input_["yil"][0]):
                self.send_text_to_textbox('//android.widget.EditText[@resource-id="com.sahibinden:id/minValueEditText"]',self.input_["km"][0])
            if(self.input_["yil"][1]):
                self.send_text_to_textbox('//android.widget.EditText[@resource-id="com.sahibinden:id/maxValueEditText"]',self.input_["km"][1])

            self.wait_parameter('//android.widget.Button[@resource-id="android:id/button1"]')
            self.click_parameter('//android.widget.Button[@resource-id="android:id/button1"]')
        #After all the filters we want are selected , we can start getting data.
        self.wait_parameter('//android.widget.Button[@resource-id="com.sahibinden:id/search_button"]')
        self.click_parameter('//android.widget.Button[@resource-id="com.sahibinden:id/search_button"]')

        self.get_data() # -> get_data

    #Helper -> find the elements we have currently in our app page
    def xpath_define(self, iter_):
        return '(//android.view.ViewGroup[@resource-id="com.sahibinden:id/browsing_category_search_result_item_linear_layout"])[{}]'.format(iter_)
    def title(self, xpath_):
        return xpath_ + '/android.widget.TextView[@resource-id="com.sahibinden:id/title"]'
    def get_data(self):
        # The scraping part , it basically selects the elements and get the attributes of the elements.

        self.wait_parameter('//android.view.ViewGroup[@resource-id="com.sahibinden:id/sahibinden_toolbar"]/android.widget.TextView')
        
        #Defining element size in the page. 
        elm = (self.driver.find_elements(AppiumBy.XPATH, '//android.view.ViewGroup[@resource-id="com.sahibinden:id/sahibinden_toolbar"]/android.widget.TextView'))[1].text
        elm = elm.replace(" sonuç bulundu","")
        print(elm)
        max_len = int(elm)  #-> element size.

        self.driver.swipe(350, 230, 350, 140, 1000) # the first swape just for once , there is a blank in the page at the beginning i just want to put more element
                                                    # one time.

        while len(self.car_ids) < max_len:
            n = 12                                              #the avg of the element size at one time , the page can screen 10 min , 11 at avg and 12 at max elements.
            if n > max_len:
                n = max_len                                     # if we have less than defined size , just resizing the n , for not getting any error.
            for i in range(1,n):                                # in every for loop , we choose every element from top to bottom and click it, after we       
                                                                # got to last index , we swipe the page and do the same steps again until we become max_len.

                self.wait_parameter(self.xpath_define(i))       #click element
                self.click_parameter(self.xpath_define(i))

                self.wait_parameter('//android.widget.ListView[@resource-id="com.sahibinden:id/detailsListView"]/android.view.ViewGroup[3]/android.widget.TextView[@resource-id="com.sahibinden:id/value"]')
                element = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ListView[@resource-id="com.sahibinden:id/detailsListView"]/android.view.ViewGroup[3]/android.widget.TextView[@resource-id="com.sahibinden:id/value"]').text

                # element -> id of the car. we use this information to check if we saw this car before or we haven't saw it yet.

                print(element)
                if(element in self.car_ids):
                    #if we saw , we just can go back to elements page and looking for other elements.
                    print("DUPLICATE !!")
                    self.driver.back()
                    continue

                # if we haven't , i added the id to id set (every attr can appeared here only once) so i say we saw this car , do not get this cars data again.
                self.car_ids.add(element)

                that_dict = self.get_attr()  #-> data we keep that we got from cars attribute page.

                self.data[element] = that_dict # append the attributes to data dict with key of id and value of attributes.

                self.driver.back()
            time.sleep(1)
            self.scroll_to_element_()

    def get_attr(self):
        dict_ = dict()  # data we are going to keep of our car.
        self.driver.swipe(350, 1100, 350, 700, 1000)  # swiping so we can get every attribute in the info list.

        self.wait_parameter('//android.widget.ListView[@resource-id="com.sahibinden:id/detailsListView"]/android.widget.LinearLayout[4]')
        # just for pricing
        price_key = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ListView[@resource-id="com.sahibinden:id/detailsListView"]/android.widget.LinearLayout[4]/android.view.ViewGroup/android.widget.TextView[@resource-id="com.sahibinden:id/label"]').text
        price_attr = self.driver.find_element(AppiumBy.XPATH,'//android.widget.ListView[@resource-id="com.sahibinden:id/detailsListView"]/android.widget.LinearLayout[4]/android.view.ViewGroup/android.widget.TextView[@resource-id="com.sahibinden:id/value"]').text
        #pricing has a different app view so i used a different xpath here , others have the same xpath
        dict_[price_key]=price_attr

        for idx in range(2,23):
            #for every element in info page , i get the key and value of that element , and put it into our info dict .

            key_xpath = '//android.widget.ListView[@resource-id="com.sahibinden:id/detailsListView"]/android.view.ViewGroup[{}]/android.widget.TextView[@resource-id="com.sahibinden:id/label"]'.format(idx)
            val_xpath = '//android.widget.ListView[@resource-id="com.sahibinden:id/detailsListView"]/android.view.ViewGroup[{}]/android.widget.TextView[@resource-id="com.sahibinden:id/value"]'.format(idx)

            key_elm = self.driver.find_element(AppiumBy.XPATH, key_xpath)
            val_elm = self.driver.find_element(AppiumBy.XPATH, val_xpath)

            key_ = key_elm.text
            val_ = val_elm.text

            dict_[key_] = val_
        # we got all the data , lets go other cars!
        return  dict_