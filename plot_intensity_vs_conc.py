import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import polyfit


def find_max_intensity(filename):
    max_y = -float('inf')

    with open(filename, 'r') as f:
        for i in range(18): # get rid of padding lines
            f.readline()
        
        for i in f.readlines():
            line = i.split()
            y = (float(line[1]) + float(line[2])) / 2
            max_y = max(max_y, y)
    

    return max_y

xpoints = np.array([0.2, 0.4, 0.6, 0.8, 1.0])
ypoints = np.array([
        find_max_intensity("G1-0.2mgml.txt"),
        find_max_intensity("G1-0.4mgml.txt"),
        find_max_intensity("G1-0.6mgml.txt"),
        find_max_intensity("G1-0.8mgml-em.txt"),
        find_max_intensity("G1-1mgml-em.txt")
    ])

unknown_max = find_max_intensity("G1-unknown.txt")

b, m = polyfit(xpoints[1:4], ypoints[1:4], 1)

unknown_conc = (unknown_max - b) / m

print(f"{unknown_conc=}")
print(f"{unknown_max=}")

colors = ['#ef476f', '#f78c6b', '#ffd166', '#06d6a0', '#118ab2', '#073b4c']


for i in range(5):
    plt.plot(xpoints[i], ypoints[i], 'ro', color=colors[i])
    plt.annotate(f'{round(ypoints[i], 2)}', xy=(xpoints[i], ypoints[i]))
plt.annotate(f'{round(unknown_max, 2)}', xy=(unknown_conc, unknown_max))
plt.plot(xpoints, b + m * xpoints, '-', label=f"y={round(m, 3)}x + {round(b, 3)}")
plt.plot(unknown_conc, unknown_max, 'ro', color=colors[5], label=f"Unknown Concentration")

plt.xlabel("Concentration")
plt.ylabel("Max Intensity")
plt.title("Intensity vs. Concentration")


plt.grid()
plt.legend()

plt.show()
