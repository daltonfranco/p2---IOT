import requests
import json
import time

readAPI = "QN0B1W3ZFF1FCF9E"

link = "https://api.thingspeak.com/channels/1580794/feeds.json?api_key="+readAPI

#with open("dados.json", "w", encoding="utf-8") as json_file:

while True:
    dadosBrutos = requests.get(link)
    #dadosJson = json.dumps(dadosBrutos.text, ensure_ascii=False, indent=4)
    time.sleep(10)

    json_file = open("dados.json", "w", encoding="utf-8")

    json_file.write(json.dumps(json.loads(dadosBrutos.text), ensure_ascii=False, indent=4))

    json_file.close()

    print("Dados foram salvos no CSV")
    print(dadosBrutos.text)