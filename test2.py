# coding: utf-8
import matplotlib.pyplot  as plt
from astropy import units as u
plt.ion()
b = [23, 45, 88] * u.second
c = [3, 7 ,10] * u.meter
plt.plot(b, c, 'og', ls='')
plt.xlabel("seconds", fontsize=14)
plt.ylabel("distance", fontsize=14)
plt.savefig("test.png")
print("Done")
