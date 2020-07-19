import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.io.wavfile import write

#a = np.array([0,2,1,4,5,6,3])
#plt.plot(a)
#plt.show()


(fs, x) = read('../sounds/flute-A4.wav')
print (fs) # sample rate
print (x)  # samples
print (x.size/float(fs)) # length in seconds

''' Plot with correct time axis
t = np.arange(x.size)/float(fs)
plt.plot(t,x)
plt.show()
'''

y = x[44100:45100]
print(np.max(y))
print(np.max(abs(y)))
print(np.sum(y))
print(np.sum(abs(y)))

plt.plot(y)
plt.show()

write('../sounds/output.wav', fs, y)


