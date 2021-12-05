import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
fg = folium.FeatureGroup(name="My Map")

map = folium.Map(location=[42.1354, 24.7453], zoom_start=6, tiles="Stamen Terrain")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=el, zoom_start=6, tiles="Stamen Terrain"))

map.add_child(fg)
map.save("Map1.html")

# tiles = "Stamen Terrain"
print("map loaded")
