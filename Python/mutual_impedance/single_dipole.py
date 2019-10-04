from PyNEC import *
import numpy as np

frequency = 860             #frequency
c = 299792458               #speed of light
lmbda = c/frequency*1e-6    #wavelength

context=nec_context()
geo = context.get_geometry()
geo.wire(1, 21, 0, 0, -lmbda/4, 0, 0, lmbda/4, 0.001*lmbda, 1.0, 1.0)
geo.wire(99, 1, -99, 0, -0.01, -99, 0, 0.01, 0.001, 1.0, 1.0)
context.geometry_complete(0)
context.gn_card(-1, 0, 0, 0, 0, 0, 0, 0)
context.ex_card(0, 99, 1, 0, 1, 0, 0, 0, 0, 0)
context.nt_card(99,1,1,11,0,0,-1,0,0,0)
context.fr_card(0, 1, frequency, 0)
context.rp_card(0, 90, 1, 0,5,0,0, 0, 90, 1, 0, 0, 0)
z = -1/context.get_input_parameters(0).get_impedance()

print ("Impedance \t(%6.3f,%+6.3fI) Ohms" % (np.real(z), np.imag(z)))

# impedance of 1/2 wavelength dipole using a current source
