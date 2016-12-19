import folium
import pandas

df = pandas.read_csv("Volcanoes-USA.txt")
fg = folium.FeatureGroup(name = "Volcanoes display")
map = folium.Map(location = [df['LAT'].mean(), df['LON'].mean()], zoom_start =4, tiles = "openstreetmap")

min = min(df['ELEV'])
max = max(df['ELEV'])
step = (min+max)/3
def color(elev):
	if elev in range(int(min), int(min+step)):
		color = 'green'
	elif elev in range(int(min+step), int(min+step*2)):
		color =  'orange'
	else:
		color = 'red'
	return color
for lat, lon, name,elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):		
	marker = folium.Marker(location = [lat,lon], popup=name, icon = folium.Icon(color=color(elev)))
	fg.add_child(marker)
	
map.add_child(fg)
map.add_child(folium.GeoJson(data=open("World_population.json"), name = "World Population", style_function = lambda x: {'fillcolour' :'green' if x['properties']['POP2005']<=90000 else 'red'}))
map.add_child(folium.LayerControl())
map.save(outfile="test1.html")