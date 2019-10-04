from PyNEC import *
from math import pi, cos, sin
import numpy as np
import matplotlib.pyplot as plt

frequency = 860                         #frequency
c = 299792458                           #speed of light
lmbda = c/frequency*1e-6                #wavelength
radius = 0.001*lmbda                    #radius of the wire
segs = 21                               #number of segments
mid_seg = 11;                           #number of the middle segment
zr = 50                                 #loading impedance
Zin = np.array([84.8 + 47.9j])          #input impedance 1 dipole
Prad = 0.5*np.real(1**2/np.conj(Zin))   #power radiated
D = 10**(2.18/10)                       #directivity


def power_on_load_nec(theta):
    #creation of a nec context
    context=nec_context()
    #get the associated geometry
    geo = context.get_geometry()
    #add wires to the geometry
    geo.wire(1, segs, 0, 0, -lmbda/4, 0, 0, lmbda/4, radius, 1.0, 1.0)
    geo.wire(2, segs, 100*lmbda, -lmbda*sin(theta)/4, -lmbda*cos(theta)/4,
                      100*lmbda, lmbda*sin(theta)/4, lmbda*cos(theta)/4, radius, 1.0, 1.0)
    context.geometry_complete(0)
    #add a "gn" card to specify the ground
    context.gn_card(-1, 0, 0, 0, 0, 0, 0, 0)
    #add a "ex" card to specify an excitation
    context.ex_card(0, 1, mid_seg, 0, 1.0, 0, 0, 0, 0, 0)
    #add a "fr" card to specify the frequency
    context.fr_card(0, 1, frequency, 0)
    #add a "ld" card to specify the loading
    context.ld_card(4, 2, mid_seg, mid_seg, zr, 0, 0)
    #add a "rp" card to specify radiation pattern sampling parameters and to cause program execution
    context.rp_card(0, 90, 1, 0,5,0,0, 0, 90, 1, 0, 0, 0)
    #calculate the power on the load
    ir = context.get_structure_currents(0).get_current()[mid_seg + segs]
    #return the power on the load
    return 0.5*zr*np.absolute(ir)**2


thetas = [tt for tt in np.linspace(0,2*pi,100)]
Pr_nec   = list(map(power_on_load_nec,[tt for tt in thetas]))

plt.plot(np.rad2deg(thetas), Pr_nec, color = 'b', label = 'NEC')
plt.xlabel('Theta (degrees)')
plt.ylabel('Power received (W)')
plt.tight_layout()
plt.show()

# polarization loss of 2 dipole antennas (TX/RX) by an angle theta
