import numpy as np
import matplotlib.pyplot as plt
#from scipy.io.wavfile import read
#from scipy.io.wavfile import write

# DFT
N = 4
k0 = 2
#x = np.exp(1j * 2 * np.pi * k0 / N * np.arange(N))
x = np.cos(2 * np.pi * k0 / N * np.arange(N))

X = np.array([])
nv = np.arange(-N/2, N/2)

for k in nv: # DFT
    #s = np.exp(1j * 2 * np.pi * k / N * np.arange(N))
    s = np.exp(1j * 2 * np.pi * k / N * nv)
    X = np.append(X, sum(x*np.conjugate(s)))
  
# IDFT
y = np.array([])
for n in nv:
    s = np.exp(1j * 2 * np.pi * n / N * nv)
    y = np.append(y, 1.0/N * sum(X*s))

#plt.plot(np.arange(N), abs(X))
plt.plot(nv, abs(X))
plt.plot(nv, y)
#plt.axis([0, N-1, 0, N])
plt.axis([-N/2, N/2-1, -1, 1])
plt.show()

# complex sinusoid
'''
N = 32
k = 5
n = np.arange(-N/2,N/2)
s = np.exp(1j * 2 * np.pi * k * n /N)

plt.plot(n, np.real(s))
plt.plot(n, np.imag(s))
plt.axis([-N/2,N/2, -1, 1])
plt.xlabel('n')
plt.ylabel('amplitude')
plt.show()
'''

# Sinusoid
'''
A = .8
f0 = 1000
phi = np.pi/2
fs = 44100
t = np.arange(-0.002,.002, 1.0/fs)
x = A * np.cos(2 * np.pi * f0 * t + phi)
#x = A * np.cos(2 * np.pi * f0 * t + phi)

plt.plot(t,x)
plt.axis([-.002,.002, -.8, .8])
plt.xlabel('time')
plt.ylabel('amplitude')

plt.show()
'''

