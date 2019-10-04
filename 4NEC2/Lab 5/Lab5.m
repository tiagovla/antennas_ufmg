eta0 = 120*pi;
f = 299.8e6;
c = 299792458;
lambda = c/f;
k = 2*pi/lambda;

l = 0.01*lambda;
b = lambda*10e-6;

Rin = pi*eta0/6*(l/lambda)^2
Xin = eta0/pi*(1-log(0.5*l/b))/(k*l/2)
D = 10^(1.75/10)

a = 0.01*lambda
Rr = (pi*eta0/6)*(k*a)^4


I2 = l/(2*pi*k*a*a)