eta = 120*pi;
d = 0.01;
z0 = 300;
f = 300e6;
c = 299792458;
lmbda = c/f;
k = 2*pi/lmbda;
Z_L = 300;


%%a)
a = d/cosh(z0*pi/eta)/2
Z_0 = (eta/pi)*acosh(0.5*d/a)

Z_lt = @(l) Z_0*(Z_L+j*Z_0*tan(k*l))./(Z_0+j*Z_L*tan(k*l));
l = linspace(0,1,100)*lmbda;
Z = Z_lt(l);


plot(l,abs(Z))




