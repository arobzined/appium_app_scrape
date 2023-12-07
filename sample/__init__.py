from core import Scraper
from get_input import Input_
import json
if __name__== "__main__":
    
    inputs = Input_()
    inputs = {"marka":"Ford",
              "model":"Focus",
              "fiyat":[150000,600000],
              "yil":[2010,2014],
              "vites":"Otomatik",
              "km":[0,150000]} # EXAMPLE INPUT , CHANGE THE VARIABLE WITH "inputs.get_input()" METHOD
    scr = Scraper(input_=inputs)
    scr.go_to_result_page()

    data_ = scr.data  # the all data we got.

    #save the data
    path = "output//sahibinden.json"
    with open(path,"w", encoding="utf-8") as f:
        json.dump(data_, f, ensure_ascii=False, indent=4)
    
    # THATS IT! WE FINISHED YEEEEY!