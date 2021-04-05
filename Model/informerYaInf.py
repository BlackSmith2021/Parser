import requests
from bs4 import BeautifulSoup

class Pars_inf():
    def __init__(self, url='https://export.yandex.ru/bar/reginfo.xml?region=194'):
        self.xml = requests.get(url)

    def getInf_level(self):
        xmlka = self.xml
        if xmlka.status_code == 200:
            soup = BeautifulSoup(xmlka.text, "html.parser")
            try:
                inform = soup.find('level')
                result = f"Пробки {inform.text}"
            except AttributeError:
                pass
        return result

    def getInf_time(self):
        xmlka = self.xml
        if xmlka.status_code == 200:
            soup = BeautifulSoup(xmlka.text, "html.parser")
            try:
                inform = soup.find('time')
                result = inform.text
            except AttributeError:
                pass
        return result

    def getInf_temperature(self):
        xmlka = self.xml
        if xmlka.status_code == 200:
            soup = BeautifulSoup(xmlka.text, "html.parser")
            try:
                inform = soup.find('temperature')
                result = str(inform.text)
            except AttributeError:
                pass
        return result

    def getInf_day(self):
        xmlka = self.xml
        if xmlka.status_code == 200:
            soup = BeautifulSoup(xmlka.text, "html.parser")
            try:
                inform = soup.find('date').find('day').text + " " + soup.find('date').find(
                    'month').attrs["name"] + " " + soup.find('date').find('year').text
                result = f"Дата {inform}"
            except AttributeError:
                pass
        return result

    def getInf_wind(self):
        xmlka = self.xml
        if xmlka.status_code == 200:
            soup = BeautifulSoup(xmlka.text, "html.parser")
            try:
                inform = soup.find('wind_speed')
                result = f"Скорость ветра {inform.text}"
            except AttributeError:
                pass
            return result
