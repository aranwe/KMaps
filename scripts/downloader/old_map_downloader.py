#! /bin/python
import sys, urllib

#settings:
language = 'cs' #language used in googlemaps as the overlay text
defaultserver = 2 #default map server : for IDs check download_tile comment
defaultmaptype = 2 #default map type : for IDs check download_tile comment
folder = 'mapy' #folder where to save the maps

def reporthook(a,b,c): 
    # ',' at the end of the line is important!
    print "% 3.1f%% of %d bytes\r" % (min(100, float(a * b) / c * 100), c),
    #you can also use sys.stdout.write
    #sys.stdout.write("\r% 3.1f%% of %d bytes" 
    #                 % (min(100, float(a * b) / c * 100), c)
    sys.stdout.flush()

def download_tile(server_id,map_type,x,y,z):
          """
              ***server_id: name (map_type: desc)
              0: maps.google.com (1: satellite, 2: normal, 3: terrain)
              1: mapy.cz (1: normal, 2: turistic, 3: aircraft)
              2: openstreetmap.org (1: standard, 2: cyclo, 3: transport, 4: mapquest)
             
              x = horizontal id
              y = vertical id
              z = zoom
              ***URL_patterns
              ***googlemaps
              0:0 src = khms0.google.com/kh/v=115&src=app&x=1&y=6&z=4 + http://mts0.google.com/vt/src=app&x=3&y=5&z=4&hl=en&lyrs=h // first jpeg , second png
              0:1 src = http://mts0.google.com/vt/src=app&x=3&y=5&z=4&hl=en&lyrs=m // png
              0:2 src = http://mts0.google.com/vt/src=app&x=21&y=11&z=5&hl=cs&lyrs=t,r // jpeg
              ****mapy.cz
              1:0 src = m1.mapserver.mapy.cz/base-n/8_8000000_7f00000 -  posledni cisla z_x_y //gif
              1:1 src = m1.mapserver.mapy.cz/turist/8_8000000_7f00000 -  posledni cisla z_x_y // png
              1:2 src = m1.mapserver.mapy.cz/ophoto/8_8000000_7f00000 + m1.mapserver.mapy.cz/hybrid/8_8000000_7f00000 -  posledni cisla z_x_y // jpeg, second png
              ***openstreetmaps.org
              2:0 src = a.tile.openstreetmap.org/9/286/173.png - posledni tri cisla: z/x/y.png
              2:1 src = a.tile.opencyclemap.org/cycle/9/286/173.png - posledni tri cisla: z/x/y.png
              2:2 src = a.tile2.opencyclemap.org/transport/9/286/173.png - posledni tri cisla z/x/y.png
              2:3 src = otile1.mqcdn.com/tiles/1.0.0/osm/9/291/174.png - posledni tri cisla: z/x/y.png
          """
          url_struct = [
          [
          ['khms0.google.com/kh/v=115&src=app&x=%x&y=%y&z=%z', 'jpg', 'http://mts0.google.com/vt/src=app&x=%x&y=%y&z=%z&hl=en&lyrs=h', 'png'],
          ['http://mts0.google.com/vt/src=app&x=%x&y=%y&z=%z&hl=en&lyrs=m', 'png'],
          ['http://mts0.google.com/vt/src=app&x=%x&y=%y&z=%z&hl=cs&lyrs=t,r', 'jpg']
          ],
          [
          ['http://m1.mapserver.mapy.cz/base-n/%z_%x_%y', 'gif'],
          ['http://m1.mapserver.mapy.cz/turist/%z_%x_%y', 'png'],
          ['http://m1.mapserver.mapy.cz/ophoto/%z_%x_%y', 'jpg', 'http://m1.mapserver.mapy.cz/hybrid/%z_%x_%y', 'png']
          ],
          [
          ['http://a.tile.openstreetmap.org/%z/%x/%y.png', 'png'],
          ['http://a.tile.opencyclemap.org/cycle/%z/%x/%y.png', 'png'],
          ['http://a.tile2.opencyclemap.org/transport/%z/%x/%y.png', 'png'],
          ['http://otile1.mqcdn.com/tiles/1.0.0/osm/%z/%x/%y.png', 'png']
          ]
          ]
          edits = [('%x',x),('%y',y),('%z',z)]
          url1=url_struct[server_id][map_type][1]
          for search, replace in edits:
                    url1 = url1.replace(search, replace)

          if len(url_struct[server_id][map_type])>2:
                url2=url_struct[server_id][map_type][3]
                for search, replace in edits:
                        url1 = url1.replace(search, replace)
                
          filename=folder+'/tile_'+x+'_'+y+'_'+z+'.'+ext
          i = url.rfind('/')
          file = url[i+1:]
          print url, "->", file
          urllib.urlretrieve(url, file, reporthook)

"""
 my notes:
 
 ***snippet to combine the two layered gmaps map
 import Image

 background = Image.open("test1.png")
 foreground = Image.open("test2.png")

 background.paste(foreground, (0, 0), foreground)
 background.show()
 ***endsnippet
 
 ***
"""