import matplotlib.pyplot as plt
import numpy as np

xpoints = []
ypoints = []


def plot(filename, color, label):
    xpoints = []
    ypoints = []

    with open(filename, 'r') as f:
        for i in range(18): # get rid of padding lines
            f.readline()
        
        for i in f.readlines():
            line = i.split()
            x = int(line[0])
            y = (float(line[1]) + float(line[2])) / 2
            xpoints.append(x)
            ypoints.append(y)
    
    xpoints = np.array(xpoints)
    ypoints = np.array(ypoints)

    plt.plot(xpoints, ypoints, color=color, label=label)


plot("G1-0.2mgml.txt", '#ef476f', '0.2 mg/ml')
plot("G1-0.4mgml.txt", '#f78c6b', '0.4 mg/ml')
plot("G1-0.6mgml.txt", '#ffd166', '0.6 mg/ml')
plot("G1-0.8mgml-em.txt", '#06d6a0', '0.8 mg/ml')
plot("G1-1mgml-em.txt", '#118ab2', '1 mg/ml')
plot("G1-unknown.txt", '#073b4c', 'unknown')

plt.xlabel("Wavelength (nm)")
plt.ylabel("Intensity")
plt.title("Emission Spectra")

plt.legend()
plt.grid()

plt.show()
