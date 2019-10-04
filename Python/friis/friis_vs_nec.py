from PyNEC import *
from math import pi
import numpy as np
import matplotlib.pyplot as plt

frequency = 860                         #frequency
c = 299792458                           #speed of light
lmbda = c/frequency*1e-6                #wavelength
radius = 0.001*lmbda                    #radius of the wire
segs = 21                               #number of segments
mid_seg = 11;                           #number of the middle segment
zr = 50                                 #loading resistence
Zin = np.array([84.8 + 47.9j])          #input impedance 1 dipole
Prad = 0.5*np.real(1**2/np.conj(Zin))   #power radiated
D = 10**(2.18/10)                       #directivity


def power_on_load_nec(dist_RT):
    #creation of a nec context
    context=nec_context()
    #get the associated geometry
    geo = context.get_geometry()
    #add wires to the geometry
    geo.wire(1, segs, 0, 0, -lmbda/4, 0, 0, lmbda/4, radius, 1.0, 1.0)
    geo.wire(2, segs, dist_RT, 0, -lmbda/4, dist_RT, 0, lmbda/4, radius, 1.0, 1.0)
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

def power_on_load_friis(dist_RT):
    effr = 4*np.real(Zin)*zr/np.power(np.absolute(Zin+zr),2)
    PR = D*effr*D*Prad*(lmbda/(4*pi*dist_RT))**2
    return PR[0]

distances = [dd for dd in np.linspace(1,100,1000)]
Pr_nec   = list(map(power_on_load_nec,[dd*lmbda for dd in distances]))
Pr_friis = list(map(power_on_load_friis,[dd*lmbda for dd in distances]))

plt.plot(distances, Pr_nec, color = 'b', label = 'NEC')
plt.plot(distances, Pr_friis, color = 'r', label = 'Friis')
plt.xscale('log')
plt.xlabel('Distance ($\lambda_0$)')
plt.ylabel('Power received (W)')
plt.tight_layout()
plt.legend()
plt.show()

#Comparison between the friis equation and the NEC solution using 2 dipole antennas
