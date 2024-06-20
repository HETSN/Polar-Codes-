function r=f(x)
    alpha=-0.4527;
    beta=0.0218;
    gamma=0.86;
    r=(x<=10)*exp(alpha*(x^gamma)+beta) + (x>10)*(sqrt(pi/x)*exp(-x/4)*(2-20/(7*x)))/2;
end