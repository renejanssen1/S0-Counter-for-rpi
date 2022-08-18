# s0 Counter for the raspberry
uitlezen kWh meter 1 fase

Eenvoudig python scriptje om je kWh metertje uit te lezen.

Benodigheden 
1. Een Pi zero of een ander formaat.
2. https://www.raspberrypi.com/software/operating-systems/ De OS-lite versie geinstalleerd
3. installeer rpi.gpio
4. installeer indien nodig MySqldb
4. upload dit script naar je home directory

## Aansluiten rpi op de kwh meter
1. verbind een 3.3v pin met de + van de meter.
2. verbind op gpio22 pin met de  - van de meter.