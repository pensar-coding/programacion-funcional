from data import API_KEY
import requests
import json
from func.flight import Flight
from datetime import datetime
from functools import reduce
from dataclasses import dataclass
        

class AirlabsAPI():
    def __init__(self,api_key):
        self.API_KEY = api_key
        self.URL = "https://airlabs.co/api/v9/"

    def get_airport(self,airport:str) -> list():
        url = f"{self.URL}schedules?dep_iata={airport}&api_key={API_KEY}"
        response = requests.get(url)
        
        response = response.json()
        response = self.responseToFlight(response["response"])
        return response


    def responseToFlight(self,response) -> list():
        final_response = []
        for f in response:
            if f["status"] == "active":
                final_response.append(Flight(f.get("flight_iata"),f.get("arr_time_utc"),f.get("status")))

        return final_response



if __name__ == "__main__":
    lista_aeropuertos = ["EZE","JFK"]
    api = AirlabsAPI(API_KEY)
    #for airport in lista_aeropuertos:
    #    lista_vuelos = api.get_airport(airport)
    listas_vuelos= map(api.get_airport,lista_aeropuertos)
    flights = reduce(lambda lista1,lista2: lista1+lista2,listas_vuelos)
    for flight in flights:
        flight.setTimeDifference()
        critic = flight.evaluateCriticality()
        if flight.getCriticality() == "ALTA":
            print(f"------ ALERT! Flight with IATA {flight.getFlightIATA()} is arriving: in {int(flight.getTimeDifference())} minutes")
        elif flight.getCriticality() == "MEDIA":
            print(f"Flight with IATA {flight.getFlightIATA()} is arriving soon: in {int(flight.getTimeDifference())} minutes")
        elif flight.getCriticality() == "BAJA":
            print(f"Chill ! :) Flight with IATA {flight.getFlightIATA()} is arriving in a while: in {int(flight.getTimeDifference())} minutes")
        else:
            print(f"¡¡¡¡ Flight with IATA {flight.getFlightIATA()} already LANDED !!!!")



