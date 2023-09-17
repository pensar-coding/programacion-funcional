from datetime import datetime


class Flight():
    def __init__(self, flight_iata:str, arr_time_utc:str, status:str, time_diff:int=-1):
        self.flight_iata = flight_iata
        self.arr_time_utc = arr_time_utc
        self.status = status
        self.time_diff = time_diff if time_diff != -1 else None
        self.criticality = None

    def __str__(self) -> str:
        return f"Flight IATA: {self.flight_iata},Arrival Time UTC: {self.arr_time_utc}, Status: {self.status}"
    
    def getFlightIATA(self) -> str:
        return self.flight_iata
    
    def getArrivalTimeUTC(self) -> str:
        return self.arr_time_utc
    
    def getStatus(self) -> str:
        return self.status
    
    def getTimeDifference(self) -> str:
        return self.time_diff
    
    def setTimeDifference(self) -> None:
        """Returns the difference between arrival time and current time in minutes"""
        if self.getArrivalTimeUTC():
            current_time = datetime.utcnow()
            try:
                arr_time = datetime.strptime(self.getArrivalTimeUTC(), "%Y-%m-%d %H:%M")
                diff = arr_time - current_time
                self.time_diff = int(diff.total_seconds()/60)
            except:
                self.time_diff

    def setCriticality(self, criticality) -> None:
        self.criticality = criticality if criticality.upper() in ("ALTA","MEDIA","BAJA") else None

    def getCriticality(self)-> str:
        return self.criticality
 
    def evaluateCriticality(self) -> str:
        if self.time_diff:
            if 0 < self.time_diff <= 15:
                self.setCriticality("ALTA")
            elif 15 < self.time_diff <= 30:
                self.setCriticality("MEDIA")
            elif self.time_diff > 30:
                self.setCriticality("BAJA")
