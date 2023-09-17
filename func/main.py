from data import API_KEY
import requests
import json
from flight import Flight
from datetime import datetime
from functools import reduce


def get_airport(airport:str) -> list():
    url = f"https://airlabs.co/api/v9/schedules?dep_iata={airport}&api_key={API_KEY}"
    response = requests.get(url)
    response = response.json()
    response = responseToFlight(response["response"])
    return response


def responseToFlight(response) -> list():
    final_response = []
    for f in response:
        if f["status"] == "active":
            final_response.append(Flight(f.get("flight_iata"),f.get("arr_time_utc"),f.get("status")))

    return final_response



def getCriticality(flight: Flight) -> None:
    flight.setTimeDifference()
    flight.evaluateCriticality()
    if flight.getCriticality() == "ALTA":
        print(f"------ ALERT! Flight with IATA {flight.getFlightIATA()} is arriving: in {int(flight.getTimeDifference())} minutes")
    elif flight.getCriticality() == "MEDIA":
        print(f"Flight with IATA {flight.getFlightIATA()} is arriving soon: in {int(flight.getTimeDifference())} minutes")
    elif flight.getCriticality() == "BAJA":
        print(f"Chill ! :) Flight with IATA {flight.getFlightIATA()} is arriving in a while: in {int(flight.getTimeDifference())} minutes")
    else:
        print(f"¡¡¡¡ Flight with IATA {flight.getFlightIATA()} already LANDED !!!!")

def main():
    lista_aeropuertos = ["EZE","JFK"]
    listas_vuelos= map(get_airport,lista_aeropuertos)
    flights = reduce(lambda lista1,lista2: lista1+lista2,listas_vuelos)
    list(map(getCriticality,flights))


main()