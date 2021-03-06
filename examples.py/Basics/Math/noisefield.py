"""
  noisefield.py - demonstrate Perlin noise
  Jonathan Feinberg
"""
srcSize = 50
destSize = 400
g = None

def setup():
    global g
    size(destSize, destSize)
    g = createGraphics(srcSize, srcSize)
    
def draw():
    t = .0005 * millis()
    g.beginDraw()
    for y in range(srcSize):
        for x in range(srcSize):
            blue = noise(t + .1*x, t + .05*y, .1 * t)
            g.set(x, y, color(0, 0, 255 * blue))
    g.endDraw()
    image(g, 0, 0, destSize, destSize)
