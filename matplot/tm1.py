import numpy as np
import matplotlib.pyplot as plt

X = np.arange(0, 3 * np.pi, 0.1)
y_cos = np.cos(X)
y_sin = np.sin(X)

plt.subplot(2, 1, 1)
plt.plot(X, y_cos)
plt.title('cosine')

plt.subplot(2, 1, 2)
plt.plot(X, y_sin)
plt.title('sine')

plt.show()

