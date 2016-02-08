s = "P3 512 512 255 "
for y in range(1,512):
    for x in range(1,512):
        r = int((x**2+y**2)%256)
        g = int((x+y-r**.5)%256)
        b = int((x**3+y**3-r**.25-g**.25)%256)
        s += "%d %d %d "%(r,g,b) 

        
f = open("intro.ppm", "w")
f.write(s)
f.close()
