import folium

map = folium.Map(location=(35.61,-82.44),zoom_start = 50)
map.save('map1.html')

import csv
fv = open("data/volcanoes.tsv", "r" )
dialect = csv.Sniffer().sniff(fv.read(10000))
fv.seek(0)
d = csv.DictReader(fv, dialect=dialect)
rows = []
for line in d:
    rows.append(line)
