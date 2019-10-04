from PyNEC import *
import numpy as np

frequency = 860             #frequency
c = 299792458               #speed of light
lmbda = c/frequency*1e-6    #wavelength


#creation of a nec context
context=nec_context()
#get the associated geometry
geo = context.get_geometry()
#add wires to the geometry
geo.wire(1, 21, 0, 0, -lmbda/4, 0, 0, lmbda/4, 0.0001*lmbda, 1.0, 1.0)
context.geometry_complete(0)
#add a "gn" card to specify the ground
context.gn_card(-1, 0, 0, 0, 0, 0, 0, 0)
#add a "ex" card to specify an excitation
context.ex_card(0, 1, 11, 0, 1.0, 0, 0, 0, 0, 0)
#add a "fr" card to specify the frequency
context.fr_card(0, 1, frequency, 0)
#add a "rp" card to specify radiation pattern sampling parameters and to cause program execution
context.rp_card(0, 90, 1, 0,5,0,0, 0, 90, 1, 0, 0, 0)

z = context.get_input_parameters(0).get_impedance()

print ("Impedance \t(%6.3f,%+6.3fI) Ohms" % (np.real(z), np.imag(z)))

#Input impedance of a 1/2 wavelength dipole using:
# number of segments = 21
# radius = 0.0001*lambda
# voltage source = 1V
# frequency 860Mhz
