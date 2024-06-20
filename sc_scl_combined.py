import matplotlib.pyplot as plt
from montecarlo_sc import EbN0dB ,Ber_sc,blker_sc,success_sc,Nsim, Rate,N
from montecarlo_scl import EbN0dB,Ber_scl,blker_scl,success_scl,Nsim,Rate,K
# ------------------------------------------------------------------------------------------
#If you wnt to run this you hv to comment the plots of montecarloe_scl and montecarloe_sc and put Nsim , N, K same in both the code
# --------------------------------------------------------------------------------------------------------------------

plt.figure(figsize=(10, 6))
plt.figure(1)
plt.yscale('log')
plt.plot(EbN0dB,Ber_sc,label='simulated SC', marker='o', linestyle='-', color='blue', linewidth=2)
plt.plot(EbN0dB,Ber_scl,label='simulated SCL', marker='s', linestyle='-', color='red', linewidth=2)
plt.xlabel('Eb/N0 (dB)')  # Label x-axis
plt.ylabel('Bit Error Rate ')  # Label y-axis
plt.title(f'Bit Error Rate vs. Eb/N0 (N={N}, K={K}, Rate={Rate}, Nsim={Nsim})')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # Add gridlines
plt.legend(loc='upper right')  # Move legend to upper right corner
# plt.plot(EbN0dB,theoritical``,label='Theoritical')
plt.xlim(0,10)

plt.legend()


plt.figure(2)
plt.yscale('log')
plt.plot(EbN0dB,blker_sc,label = 'Block error rate simulated SC', marker='o', linestyle='-', color='blue',linewidth=2)
plt.plot(EbN0dB,blker_scl,label = 'Block error rate simulated SCL', marker='s', linestyle='-', color='red',  linewidth=2)
plt.xlabel('Eb/N0 (dB)')  # Label x-axis
plt.ylabel('Block Error Rate')  # Label y-axis
plt.title(f'Block Error Rate vs. Eb/N0 (N={N}, K={K}, Rate={Rate}, Nsim={Nsim})')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # Add gridlines
plt.legend(loc='upper right')  # Move legend to upper right corner
plt.xlim(0,10)

plt.legend()

plt.figure(3)
plt.yscale('log')
plt.plot(EbN0dB,success_sc,label = 'Success rate simulated SC ', marker='o', linestyle='-', color='blue', linewidth=2)
plt.plot(EbN0dB,success_scl,label = 'Success rate simulated SCL', marker='s', linestyle='-', color='red', linewidth=2)
plt.xlabel('Eb/N0 (dB)')  # Label x-axis
plt.ylabel('Success Rate ')  # Label y-axis
plt.title(f'Success Rate vs. Eb/N0 (N={N}, K={K}, Rate={Rate}, Nsim={Nsim})')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)  # Add gridlines
plt.legend(loc='lower right')  # Move legend to lower right corner
plt.legend()
plt.xlim(0,10)
plt.ylim(0,1.01)

plt.show()
