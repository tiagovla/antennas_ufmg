%Experimental
dist_lambda = [0.10; 0.20; 0.50; 0.75; 1.00; 1.50; 10.00];
Z11_plus_Z12 = [166+43.7j;
                139+16.6j;
                66.5+16.3j;
                59.6+58.9j;
                92.6+68j;
                80.7+34.2j;
                85.2+50.1j];
            
Z11 =  [86.2+43.2j;
        82.5+45.8j;
        85.8+48.5j;
        84.3+47.5j;
        85+48.2j;
        84.9+48.1j;
        84.8+47.9j];
    
Z12 = Z11_plus_Z12 - Z11;

dist_lambda_cont = linspace(0.1,10,300);
Zm = Z21_half_dipole(dist_lambda_cont);

plot(dist_lambda_cont, real(Zm),'-b','linewidth', 1); hold on; grid on;
plot(dist_lambda_cont, imag(Zm),'-r','linewidth', 1);
ylabel('Impedância (\Omega)')
xlabel('Distância entre dipolos (\lambda)')
scatter(dist_lambda,real(Z12), 'b+','LineWidth',2)
scatter(dist_lambda,imag(Z12), 'rx','LineWidth',2)
legend('R - FEI','X - FEI','R - 4NEC2','X - 4NEC2')

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
