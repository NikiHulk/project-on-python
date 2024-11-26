import requests
from bs4 import BeautifulSoup

class checkWeather:

    def checkWeatherNow(city):

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 YaBrowser/24.10.0.0 Safari/537.36"
        }

        url = f"https://www.google.com/search?q=погода+в+{city}"
        response = requests.get(url,headers=headers)

        getHtmlPage = BeautifulSoup(response.text,"html.parser")

        title = getHtmlPage.select("#wob_dc")[0].getText()
        temperature = getHtmlPage.select("#wob_tm")[0].getText()
        humidity = getHtmlPage.select("#wob_hm")[0].getText()
        time = getHtmlPage.select("#wob_dts")[0].getText()
        wind = getHtmlPage.select("#wob_ws")[0].getText()

        print(f"В городе {city} сейчас {title.lower()}: \n"
              f"Температура составляет: {temperature}℃ \n"
              f"Влажность составляет: {humidity} \n"
              f"Настоящее время: {time[:1].upper() + time[1:]} \n"
              f"Ветер: {wind}")

    if __name__ == "__main__":
        city = str(input("Город: "))
        checkWeatherNow(city=city)

    #Написан фрагмент кода только для погоды в настоящее время
    #TODO -> сделать оставшийся фрагмент кода с прогнозом на неделю~