from PyNEC import *
import numpy as np
import matplotlib.pyplot as plt

frequency = 860             #frequency
c = 299792458               #speed of light
lmbda = c/frequency*1e-6    #wavelength

def z11_plus_z12(d_lmbda):
    context=nec_context()
    geo = context.get_geometry()
    geo.wire(1, 21, 0, 0, -lmbda/4, 0, 0, lmbda/4, 0.001*lmbda, 1.0, 1.0)
    geo.wire(2, 21, d_lmbda*lmbda, 0, -lmbda/4, d_lmbda*lmbda, 0, lmbda/4, 0.001*lmbda, 1.0, 1.0)
    geo.wire(9901, 1, -0.01, 0, 9901, 0.01, 0, 9901, 0.001, 1.0, 1.0)
    geo.wire(9902, 1, -0.01, 0, 9902, 0.01, 0, 9902, 0.001, 1.0, 1.0)
    context.geometry_complete(0)
    context.gn_card(-1, 0, 0, 0, 0, 0, 0, 0)
    context.ex_card(0, 9901, 1, 0, 1.0, 0, 0, 0, 0, 0)
    context.ex_card(0, 9902, 1, 0, 1.0, 0, 0, 0, 0, 0)
    context.nt_card(9901,1,1,11,0,0,1,0,0,0)
    context.nt_card(9902,1,2,11,0,0,1,0,0,0)
    context.fr_card(0, 1, frequency, 0)
    context.rp_card(0, 90, 1, 0,5,0,0, 0, 90, 1, 0, 0, 0)
    return -1/context.get_input_parameters(0).get_impedance()[0]

def z11(d_lmbda):
    context=nec_context()
    geo = context.get_geometry()
    geo.wire(1, 21, 0, 0, -lmbda/4, 0, 0, lmbda/4, 0.001*lmbda, 1.0, 1.0)
    geo.wire(2, 21, d_lmbda*lmbda, 0, -lmbda/4, d_lmbda*lmbda, 0, lmbda/4, 0.001*lmbda, 1.0, 1.0)
    geo.wire(9901, 1, -0.01, 0, 9901, 0.01, 0, 9901, 0.001, 1.0, 1.0)
    context.geometry_complete(0)
    context.gn_card(-1, 0, 0, 0, 0, 0, 0, 0)
    context.ex_card(0, 9901, 1, 0, 1.0, 0, 0, 0, 0, 0)
    context.ld_card(4, 2, 11, 11, 10**6, 0, 0)
    context.nt_card(9901,1,1,11,0,0,1,0,0,0)
    context.fr_card(0, 1, frequency, 0)
    context.rp_card(0, 90, 1, 0,5,0,0, 0, 90, 1, 0, 0, 0)
    return -1/context.get_input_parameters(0).get_impedance()[0]


z11 = np.vectorize(z11) #z11 impedance
z11_plus_z12 = np.vectorize(z11_plus_z12) #z11+z12 impedance
dist_lambda = np.linspace(0.1,10,200)
z12 = z11_plus_z12(dist_lambda)-z11(dist_lambda)

#plot the results
plt.plot(dist_lambda, np.real(z12),'b',label = 'R')
plt.plot(dist_lambda, np.imag(z12),'r',label = 'X')
plt.ylabel('Impedância ($\Omega$)')
plt.xlabel('Distância entre dipolos ($\lambda$)')
plt.legend()
plt.grid()
plt.show()

#save the results to an 'output.dat' file
# with open('output.dat','w') as f:
#     f.write("{}, {}, {}\n".format("d_lbmda", "real(z12)","imag(z12)"))
#     for dist, z in zip(dist_lambda, z12):
#         f.write("{}, {}, {}\n".format(dist, np.real(z),np.imag(z)))
