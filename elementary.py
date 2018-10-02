import scipy as sp
class Particle(object):
    """ class """

    mass = 0.00
    position = (0.0, 0.0, 0.0)
    momentum = (0.0,0.0,0.0)
    
'''
    def __init__(self):
        self.momentum =(px, py, pz)

    def __init__(self):
        self.position =(x, y, z)


    def __init__(self):
        self.mass =
'''

    def __init__(self, x, y, z):
        self.momentum = (0.0,0.0,0.0)
        self.mass = 1.0
        self.position = (x,y,z)
        
    def impulse(self,px,py,pz):
        momentum[0] = momentum[0] + px
        momentum[1] = momentum[1] + px
        momentum[2] = momentum[2] + px
        
    def move(self, dt):
        #p = mv
        #v = d/t
        #p = (d/t)*m
        #p = (d*m)/t
        #p*t = d*m
        #(p*t)/m = d
        position[0] = position[0] + (momentum[0]*dt)/mass
        position[1] = position[1] + (momentum[1]*dt)/mass
        position[2] = position[2] + (momentum[2]*dt)/mass

def ChargedParticle(Particle):
    
    charge = 0
        
def Electron(ChargedParticle):
    
    def __init__(self, x,y,z):
        super(Electron,self).__init__(x,y,z)
        self.charge = sp.e*(-1)
        self.mass = sp.electron_mass
        
def Proton(ChargedParticle):
    
    def __init__(self, x,y,z):
        super(Proton,self).__init__(x,y,z)
        self.charge = sp.e
        self.mass = sp.proton_mass
        
        
        