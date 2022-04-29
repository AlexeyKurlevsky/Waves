import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def H(t):
    n, m = t.shape
    for i in range(n):
        for j in range(m):
            if t[i][j] >= 0:
                t[i][j] = 1
            else:
                t[i][j] = 0

    return t


l = 1
E = 1
rho = 1
M = 1
sigma_0 = 1

C_0 = np.sqrt(E / rho)
alpha = rho * C_0 / M

print(C_0)

x = np.arange(0, l, 0.01)
t = np.arange(0, 3, 10 ** (-3))

xv, tv = np.meshgrid(x, t)
sigma = np.exp(-alpha * (tv - xv / C_0)) * H(tv - xv / C_0) - np.exp(-alpha * (tv - (2 * l - x) / C_0)) * H(
    tv - (2 * l - x) / C_0)

print(sigma)
fig, ax = plt.subplots()
ln, = plt.plot([], [], 'k')
plt.grid()

def init():
    ax.set_xlim(0, l)
    ax.set_ylim(-2, 2)
    plt.xlabel("х, метры")
    plt.ylabel("Sigma, Па")
    plt.title("Напряжение от координаты")
    return ln,

def update(frame):
    ln.set_data(x, sigma[frame,:])
    return ln,

anim = animation.FuncAnimation(fig, update, frames=np.arange(0, len(t), 100),
                    init_func=init, blit=True)
# writervideo = animation.FFMpegWriter(fps=60)
# anim.save(r'increasingStraightLine.mp4', writer=writervideo)
plt.show()