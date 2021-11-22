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
        if line['Status'] != 'Historical' and line['Latitude'] != '' and line['Longitude'] != '':
            rows.append(line)

icon_cadetblue = folium.Icon(color='cadetblue')

map = folium.Map(location=(35.61,-82.44),zoom_start = 5)
for line in rows:
    icon_cadetblue = folium.Icon(color='cadetblue')
    marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'], icon=icon_cadetblue)
    map.add_child(marker)

map.save('map1.html')