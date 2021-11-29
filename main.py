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

icon_cadetblue = folium.Icon(color='cadetblue') #Explosion crater, crater rows
icon_red = folium.Icon(color='red') #Stratovolcano
icon_orange = folium.Icon(color='orange') #Lava dome
icon_pink = folium.Icon(color='pink') #Caldera
icon_green = folium.Icon(color='green') #Volcanic field
icon_purple = folium.Icon(color='purple')#Cinder cone, Tuff cone, Pyroclastic cone, Pumice cone, Scoria cone
icon_blue = folium.Icon(color='blue') #Submarine volcano
icon_darkgreen = folium.Icon(color='darkgreen') #Hydrothermal field
icon_lightblue = folium.Icon(color='lightblue') #Somma volcano
icon_lightgreen = folium.Icon(color='lightgreen') #Fumarole field
icon_gray = folium.Icon(color='gray') #Maar
icon_black = folium.Icon(color='black') #Complex volcano
icon_white = folium.Icon(color='white') #Unknown
icon_darkpurple = folium.Icon(color='darkpurple') #Shield volcano
icon_darkred = folium.Icon(color='darkred') #Fissure vent

map = folium.Map(location=(35.61,-82.44),zoom_start = 5)
for line in rows:
    icon_cadetblue = folium.Icon(color='cadetblue')
    marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'], popup=line['Type'], icon=icon_cadetblue)
    map.add_child(marker)

map.save('map1.html')

stratovolcano = 0
lava_dome = 0
submarine_volcano = 0
caldera = 0
volcanic_field = 0
shield_volcano = 0
cinder_cone = 0
complex_volcano = 0
maar = 0
fumarole_field = 0
explosion_crater = 0
tuff_cone = 0
pyroclastic_cone = 0
pumice_cone = 0
scoria_cone = 0
fissure_vent = 0
crater_rows = 0
somma_volcano = 0
hydrothermal_field = 0
unknown = 0
for line in rows:
    if line['Type'] == 'Stratovolcano':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_red)
        map.add_child(marker)
        stratovolcano += 1
    elif line['Type'] == 'Stratovolcanoes':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_red)
        map.add_child(marker)
        stratovolcano += 1
    elif line['Type'] == 'Stratovolcano(es)':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_red)
        map.add_child(marker)
        stratovolcano += 1
    elif line['Type'] == 'Lava dome':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_orange)
        map.add_child(marker)
        lava_dome += 1
    elif line['Type'] == 'Lava domes':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_orange)
        map.add_child(marker)
        lava_dome += 1
    elif line['Type'] == 'Lava cone':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_orange)
        map.add_child(marker)
        lava_dome += 1
    elif line['Type'] == 'Submarine volcano':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_blue)
        map.add_child(marker)
        submarine_volcano += 1
    elif line['Type'] == 'Submarine volcanoes':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_blue)
        map.add_child(marker)
        submarine_volcano += 1
    elif line['Type'] == 'Submarine':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_blue)
        map.add_child(marker)
        submarine_volcano += 1
    elif line['Type'] == 'Submarine volcano?':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_blue)
        map.add_child(marker)
        submarine_volcano += 1
    elif line['Type'] == 'Subglacial volcano':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_blue)
        map.add_child(marker)
        submarine_volcano += 1
    elif line['Type'] == 'Caldera':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_pink)
        map.add_child(marker)
        caldera += 1
    elif line['Type'] == 'Volcanic field':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_green)
        map.add_child(marker)
        volcanic_field += 1
    elif line['Type'] == 'Shield volcano':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_darkpurple)
        map.add_child(marker)
        shield_volcano += 1
    elif line['Type'] == 'Shield':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_darkpurple)
        map.add_child(marker)
        shield_volcano += 1
    elif line['Type'] == 'Shield volcanoes':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_darkpurple)
        map.add_child(marker)
        shield_volcano += 1
    elif line['Type'] == 'Cinder cone':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_purple)
        map.add_child(marker)
        cinder_cone += 1
    elif line['Type'] == 'Cinder cones':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_purple)
        map.add_child(marker)
        cinder_cone += 1
    elif line['Type'] == 'Complex volcano':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_black)
        map.add_child(marker)
        complex_volcano += 1
    elif line['Type'] == 'Compound volcano':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_black)
        map.add_child(marker)
        complex_volcano += 1
    elif line['Type'] == 'Volcanic complex':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_black)
        map.add_child(marker)
        complex_volcano += 1
    elif line['Type'] == 'Maar':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_gray)
        map.add_child(marker)
        maar += 1
    elif line['Type'] == 'Maars':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_gray)
        map.add_child(marker)
        maar += 1
    elif line['Type'] == 'Fumarole field':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_lightgreen)
        map.add_child(marker)
        fumarole_field += 1
    elif line['Type'] == 'Explosion crater':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_cadetblue)
        map.add_child(marker)
        explosion_crater += 1
    elif line['Type'] == 'Tuff cone':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_purple)
        map.add_child(marker)
        tuff_cone += 1
    elif line['Type'] == 'Tuff rings':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_purple)
        map.add_child(marker)
        tuff_cone += 1
    elif line['Type'] == 'Pyroclastic cone':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_purple)
        map.add_child(marker)
        pyroclastic_cone += 1
    elif line['Type'] == 'Pyroclastic cones':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_purple)
        map.add_child(marker)
        pyroclastic_cone += 1
    elif line['Type'] == 'Pyroclastic shield':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_purple)
        map.add_child(marker)
        pyroclastic_cone += 1
    elif line['Type'] == 'Pumice cone':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_purple)
        map.add_child(marker)
        pumice_cone += 1
    elif line['Type'] == 'Scoria cone':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_purple)
        map.add_child(marker)
        scoria_cone += 1
    elif line['Type'] == 'Scoria cones':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_purple)
        map.add_child(marker)
        scoria_cone += 1
    elif line['Type'] == 'Fissure vent':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_darkred)
        map.add_child(marker)
        fissure_vent += 1
    elif line['Type'] == 'Fissure vents':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_darkred)
        map.add_child(marker)
        fissure_vent += 1
    elif line['Type'] == 'Crater rows':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_cadetblue)
        map.add_child(marker)
        crater_rows += 1
    elif line['Type'] == 'Somma volcano':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_lightblue)
        map.add_child(marker)
        somma_volcano += 1
    elif line['Type'] == 'Hydrothermal field':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_darkgreen)
        map.add_child(marker)
        hydrothermal_field += 1
    elif line['Type'] == 'Unknown':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_white)
        map.add_child(marker)
        unknown += 1
    elif line['Type'] == 'Cone':
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=line['Volcano Name'],
                               popup=line['Type'], icon = icon_purple)
        map.add_child(marker)
        unknown += 1
    else:
        print(line['Type'])

map.save('map1.html')