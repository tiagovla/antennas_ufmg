clear; clc;

%Param
c = 299792458;
f = 840e6;
lambda = c/f;

%Eff
Rc  = 50;
Zin = 84.8 + 47.9j;
Rr  = real(Zin);
effr = 4*Rr*Rc/abs(Zin+Rc)^2;

distRT = [1 10 100]*lambda;
Imod  = [ 1.5082E-03, 1.5990E-04, 1.6006E-05];
Pr    = [ 4.4712E-03, 4.4678E-03, 4.4684E-03];

Dt = 10^(2.18/10);
Dr = Dt;

Pc_friis = Dt*effr*Dr.*Pr.*(lambda./(4*pi*distRT)).^2
Pc_4nec2 = Rc*Imod.*Imod/2

%Dipole rotation
Angle = [0 45 90];
Current = [1.6006E-05 1.1318E-05 9.8037E-22]
