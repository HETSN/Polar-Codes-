%#ok<*GVMIS>
%#ok<*NASGU>
global seq
global index

N=1024;
k=512;
n=log2(N);
d=0;

seq=zeros(1,N);
index=1;

R = k/N;
EbN0dB=5;
EbN0=10.^(EbN0dB./10);
sigma_square=1/(R*2*EbN0);

erasure_prob=0.5;

temp=reli(erasure_prob,d,n);
plot(1:N,seq,'LineStyle','none','Marker','.');
xlabel('Channel Index');
ylabel('Bhattacharya Parameter Z(W)');
title('Bhattacharya Parameter for BEC channel after Channel Polarization');
ylim([0 1]);
xlim([1 N]);

function r=reli(x,d,n)
    global seq
    global index

    if d==n
        seq(index)=x;
        index=index+1;
        r=0;
    else 
        left=reli(2*x-x^2,d+1,n);
        right=reli(x^2,d+1,n);
        r=0;
    end
end
