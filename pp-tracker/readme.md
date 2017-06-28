# PP-Tracker (Pobieranie informacji na temat przesyłki porzez API Poczty Polskiej)

## Licencja
>    PP-Tracker pobiera informacje na temat przesyłki z serwera poczty polskiej
    Copyright (C) 2017  Mateusz Pieła

>    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

 >   You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
 ## Informacje
 Ten program program pobiera informacje na temat przesyłki z serwera poczty polskiej poprzez udostępnione api  które można znależć na [Poczta Polska WebServices](https://www.poczta-polska.pl/webservices/)
 oraz wyświetla je w konsoli
 
 ## Wymagania
 Python w wersji większej lub równej python3.0 oraz zeep
 
 ## Instalacja
Dla windows

pip install git+https://github.com/mateuszpiela/tracker.git#subdirectory=pp-tracker

Alt:

C:\Python34\python.exe -m pip install git+https://github.com/mateuszpiela/tracker.git#subdirectory=pp-tracker

Dla linux

sudo apt install python3-dev libxslt-dev libxml2-dev

sudo pip3 install git+https://github.com/mateuszpiela/tracker.git#subdirectory=pp-tracker

## Jak uruchromić ?
Dla linux

pp-tracker.py twój_numer_przesyłki

Alt:

python3 -m pp-tracker twój_numer_przesyłki

Dla windows (Python 3.4)

pp-tracker.py twój_numer_przesyłki

Alt:

C:\Python34\python.exe -m pp-tracker twój_numer_przesyłki

## Użyte biblioteki python w programie
[Zeep](http://docs.python-zeep.org/en/master/)

Json

Argparse
