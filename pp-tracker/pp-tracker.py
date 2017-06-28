#!/usr/bin/python3
#Importowanie bibliotek Zeep
from zeep import Client
from zeep import xsd
from zeep import helpers
from zeep.wsse.username import UsernameToken
#Importowanie biblioteki JSON
import json
#Importowanie biblioteki parsera oraz ustawienie parsera
import argparse
#Ustawianie argparser oraz dodanie argumentu potrzebnego
parser = argparse.ArgumentParser(description='Program do łączenia się z serwerami Poczty Polskiej - Pobieranie informacji na temat przesyłki')
parser.add_argument('kodprz', help='Wpisz kod przesyłki')
results = parser.parse_args()

#Ustawianie połączenia z serwerem api poczty polskiej przy użyciu domyślnego loginu i hasła
client = Client(
	'https://tt.poczta-polska.pl/Sledzenie/services/Sledzenie?wsdl',
	wsse=UsernameToken('sledzeniepp', 'PPSA'))
#Sprawdzanie numeru przesyłki
response = client.service.sprawdzPrzesylke(results.kodprz)
#Konwertowanie z listy wsdl na json (Tylko zdarzenie)
serialize = helpers.serialize_object(response.danePrzesylki.zdarzenia.zdarzenie)
#Ładowanie json
jsonzdarzenie = json.loads(json.dumps(serialize))
#Policzenie ilości elementów json
ilosc = len(jsonzdarzenie)
#Generowanie URL z numeru przesyłki
url = 'emonitoring.poczta-polska.pl/?numer=' + results.kodprz
#Wypisywanie informacji
print('Informacje o przesyłce:')
print('Data Nadania:',response.danePrzesylki.dataNadania)
print('Kraj Nadania:',response.danePrzesylki.krajNadania)
print('Kraj Przeznaczenia:',response.danePrzesylki.krajPrzezn)
print('Rodzaj Przesyłki:',response.danePrzesylki.rodzPrzes)
print('Numer Przesyłki:',response.danePrzesylki.numer,' |Link do poczty polskiej:',url)
print('Masa Przesyłki:',response.danePrzesylki.masa,'kg')
print('Status Przesyłki:')
for x in range(0,ilosc):
        print('------------------------------------------------------------------------------------------------------------')
        print('Stan:',jsonzdarzenie[x]['nazwa'],'|Czas:',jsonzdarzenie[x]['czas'],'|Lokalizacja:',jsonzdarzenie[x]['jednostka']['nazwa'])

