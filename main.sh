#!/bin/bash
while read perfil; do
        cd /home/LAMPIAO/tubo/ && python3 ./tubo.py -type c -channel "$perfil"  -t h --hours 6 -index youtube_bolsonarismo -u twint -p NiDJlptp57kg1KCkZgWH &
        sleep 1
done < "/home/LAMPIAO/tubo/canais.txt"