import requests  # pip install requests (python 2.7)
import csv
import time

value = 1
aantal = 14
som = 0
vorigePrice = 0.87
change = 0.00

def schrijfKolomNamen():
    with open('price.csv', mode='a') as f:
            fieldnames = ['timestamp', 'price']
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()

schrijfKolomNamen()

for x in range(14):
    ################################### haal prijs en datum van API ##################################
    r = requests.get('https://freeforexapi.com/api/live?pairs=EURGBP')

    print("Rauwe Data: " + r.text)

    value = value + 1

    rate = r.text[27:35]
    timestamp = r.text[48:58]

    change = float(rate) - float(vorigePrice)
    '{:.20f}'.format(change)

    som = som + float(rate)
    avg = som / aantal

    vorigePrice = rate

    print("Rate: " + str(rate))
    print("Timestamp: " + str(timestamp))
    print("Change: " + str(change))
    print("som: " + str(som))
    print("avg: " + str(avg))
################################### bereken change ##################################

    
    with open('price.csv', mode='a') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, rate, change, avg])
    
    time.sleep(5)
    print(value)

