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
#for line in rows:
    #icon_lightblue = folium.Icon(color='lightblue')
    #marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon=icon_cadetblue)
    #map.add_child(marker)

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
        #add_marker_to_map(map, location=(line['Latitude'], line['Longitude'], popup=(line['Volcano Name'], color='red')
        icon_red = folium.Icon(color='red')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_red)
        map.add_child(marker)
        stratovolcano += 1
    elif line['Type'] == 'Stratovolcanoes':
        icon_red = folium.Icon(color='red')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_red)
        map.add_child(marker)
        stratovolcano += 1
    elif line['Type'] == 'Stratovolcano(es)':
        icon_red = folium.Icon(color='red')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_red)
        map.add_child(marker)
        stratovolcano += 1
    elif line['Type'] == 'Lava dome':
        icon_orange = folium.Icon(color='orange')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_orange)
        map.add_child(marker)
        lava_dome += 1
    elif line['Type'] == 'Lava domes':
        icon_orange = folium.Icon(color='orange')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_orange)
        map.add_child(marker)
        lava_dome += 1
    elif line['Type'] == 'Lava cone':
        icon_orange = folium.Icon(color='orange')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_orange)
        map.add_child(marker)
        lava_dome += 1
    elif line['Type'] == 'Submarine volcano':
        icon_blue = folium.Icon(color='blue')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_blue)
        map.add_child(marker)
        submarine_volcano += 1
    elif line['Type'] == 'Submarine volcanoes':
        icon_blue = folium.Icon(color='blue')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_blue)
        map.add_child(marker)
        submarine_volcano += 1
    elif line['Type'] == 'Submarine':
        icon_blue = folium.Icon(color='blue')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_blue)
        map.add_child(marker)
        submarine_volcano += 1
    elif line['Type'] == 'Submarine volcano?':
        icon_blue = folium.Icon(color='blue')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_blue)
        map.add_child(marker)
        submarine_volcano += 1
    elif line['Type'] == 'Subglacial volcano':
        icon_blue = folium.Icon(color='blue')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_blue)
        map.add_child(marker)
        submarine_volcano += 1
    elif line['Type'] == 'Caldera':
        icon_pink = folium.Icon(color='pink')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_pink)
        map.add_child(marker)
        caldera += 1
    elif line['Type'] == 'Volcanic field':
        icon_green = folium.Icon(color='green')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_green)
        map.add_child(marker)
        volcanic_field += 1
    elif line['Type'] == 'Shield volcano':
        icon_darkpurple = folium.Icon(color='darkpurple')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_darkpurple)
        map.add_child(marker)
        shield_volcano += 1
    elif line['Type'] == 'Shield':
        icon_darkpurple = folium.Icon(color='darkpurple')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_darkpurple)
        map.add_child(marker)
        shield_volcano += 1
    elif line['Type'] == 'Shield volcanoes':
        icon_darkpurple = folium.Icon(color='darkpurple')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_darkpurple)
        map.add_child(marker)
        shield_volcano += 1
    elif line['Type'] == 'Cinder cone':
        icon_purple = folium.Icon(color='purple')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_purple)
        map.add_child(marker)
        cinder_cone += 1
    elif line['Type'] == 'Cinder cones':
        icon_purple = folium.Icon(color='purple')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_purple)
        map.add_child(marker)
        cinder_cone += 1
    elif line['Type'] == 'Complex volcano':
        icon_black = folium.Icon(color='black')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_black)
        map.add_child(marker)
        complex_volcano += 1
    elif line['Type'] == 'Compound volcano':
        icon_black = folium.Icon(color='black')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_black)
        map.add_child(marker)
        complex_volcano += 1
    elif line['Type'] == 'Volcanic complex':
        icon_black = folium.Icon(color='black')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_black)
        map.add_child(marker)
        complex_volcano += 1
    elif line['Type'] == 'Maar':
        icon_gray = folium.Icon(color='gray')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_gray)
        map.add_child(marker)
        maar += 1
    elif line['Type'] == 'Maars':
        icon_gray = folium.Icon(color='gray')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_gray)
        map.add_child(marker)
        maar += 1
    elif line['Type'] == 'Fumarole field':
        icon_lightgreen = folium.Icon(color='lightgreen')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_lightgreen)
        map.add_child(marker)
        fumarole_field += 1
    elif line['Type'] == 'Explosion crater':
        icon_cadetblue = folium.Icon(color='cadetblue')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_cadetblue)
        map.add_child(marker)
        explosion_crater += 1
    elif line['Type'] == 'Tuff cone':
        icon_purple = folium.Icon(color='purple')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_purple)
        map.add_child(marker)
        tuff_cone += 1
    elif line['Type'] == 'Tuff rings':
        icon_purple = folium.Icon(color='purple')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_purple)
        map.add_child(marker)
        tuff_cone += 1
    elif line['Type'] == 'Pyroclastic cone':
        icon_purple = folium.Icon(color='purple')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_purple)
        map.add_child(marker)
        pyroclastic_cone += 1
    elif line['Type'] == 'Pyroclastic cones':
        icon_purple = folium.Icon(color='purple')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_purple)
        map.add_child(marker)
        pyroclastic_cone += 1
    elif line['Type'] == 'Pyroclastic shield':
        icon_purple = folium.Icon(color='purple')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_purple)
        map.add_child(marker)
        pyroclastic_cone += 1
    elif line['Type'] == 'Pumice cone':
        icon_purple = folium.Icon(color='purple')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_purple)
        map.add_child(marker)
        pumice_cone += 1
    elif line['Type'] == 'Scoria cone':
        icon_purple = folium.Icon(color='purple')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_purple)
        map.add_child(marker)
        scoria_cone += 1
    elif line['Type'] == 'Scoria cones':
        icon_purple = folium.Icon(color='purple')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_purple)
        map.add_child(marker)
        scoria_cone += 1
    elif line['Type'] == 'Fissure vent':
        icon_darkred = folium.Icon(color='darkred')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_darkred)
        map.add_child(marker)
        fissure_vent += 1
    elif line['Type'] == 'Fissure vents':
        icon_darkred = folium.Icon(color='darkred')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_darkred)
        map.add_child(marker)
        fissure_vent += 1
    elif line['Type'] == 'Crater rows':
        icon_cadetblue = folium.Icon(color='cadetblue')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_cadetblue)
        map.add_child(marker)
        crater_rows += 1
    elif line['Type'] == 'Somma volcano':
        icon_lightblue = folium.Icon(color='lightblue')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_lightblue)
        map.add_child(marker)
        somma_volcano += 1
    elif line['Type'] == 'Hydrothermal field':
        icon_darkgreen = folium.Icon(color='darkgreen')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_darkgreen)
        map.add_child(marker)
        hydrothermal_field += 1
    elif line['Type'] == 'Unknown':
        icon_white = folium.Icon(color='white')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_white)
        map.add_child(marker)
        unknown += 1
    elif line['Type'] == 'Cone':
        icon_purple = folium.Icon(color='purple')
        marker = folium.Marker(location=(line['Latitude'], line['Longitude']), popup=(line['Volcano Name'], line['Type']), icon = icon_purple)
        map.add_child(marker)
        unknown += 1
    else:
        print(line['Type'])

map.save('map1.html')