"""
Multiple Particle Systems
by Daniel Shiffman.

Click the mouse to generate a burst of particles
at mouse location.

Each burst is one instance of a particle system
with Particles and CrazyParticles (a subclass of(object): Particle)
Note use of Inheritance and Polymorphism here.
"""
ArrayList<ParticleSystem> systems
def setup(): 
    size(640, 360)
    systems = ArrayList<ParticleSystem>()
def draw(): 
    background(0)
    for (ParticleSystem ps: systems) 
        ps.run()
        ps.addParticle()
    
    if systems.isEmpty():
        fill(255)
        textAlign(CENTER)
        text("click mouse to add particle systems", width/2, height/2)
    
def mousePressed(): 
    systems.add(ParticleSystem(1, PVector(mouseX, mouseY)))
