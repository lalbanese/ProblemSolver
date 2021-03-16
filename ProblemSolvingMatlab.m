tic
mass = linspace(0.01,1,10000);
coeff_fric = linspace(0.01,5,500);
length_leg = 8;
g = 9.81;

weight = mass*g;
f_friction = weight/4;

f_norm = zeros(length(coeff_fric),length(mass));
for fric_ind = 1:length(f_friction)
    f_norm(:,fric_ind) = f_friction(fric_ind)./coeff_fric;

end
torque_val = f_norm * length_leg;

toc

figure(1)
hold on
for coeff_val = 1:length(coeff_fric)
    plot(mass,torque_val(coeff_val,:))
end

