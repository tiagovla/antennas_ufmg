%NEC
data_nec = readmatrix("output.dat");
d_nec = data_nec(:,1);
z12_nec = data_nec(:,2) + data_nec(:,3)*j;

%%FEI
d_fei = linspace(0.1,10,300);
z12_fei = Z21_half_dipole(d_fei);

plot(d_fei, real(z12_fei),'-b','linewidth', 1); hold on; grid on;
plot(d_fei, imag(z12_fei),'-r','linewidth', 1);
plot(d_nec, real(z12_nec),'--b','linewidth', 1); hold on; grid on;
plot(d_nec, imag(z12_nec),'--r','linewidth', 1);
ylabel('Impedância (\Omega)')
xlabel('Distância entre dipolos (\lambda)')
legend('R - FEI','X - FEI','R - NEC','X - NEC')
set(gca,'box','off')
axis([0 3 -60 100])


function Zm = Z21_half_dipole(d_lmbda)
    eta = 120*pi;
    length = 0.5;
    u0 = d_lmbda*2*pi;
    u1 = 2*pi*(sqrt(length^2+d_lmbda.^2)+length);
    u2 = 2*pi*(sqrt(length^2+d_lmbda.^2)-length);
    R = +eta*(2*cosint(u0)-cosint(u1)-cosint(u2))/(4*pi);
    X = -eta*(2*sinint(u0)-sinint(u1)-sinint(u2))/(4*pi);
    Zm = R+X*j;
end
