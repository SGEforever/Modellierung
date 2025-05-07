import matplotlib.pyplot as plt
import numpy as np

image = np.load('Abgabe_1/image.npy')
converted_image = np.transpose(image, (1, 2, 0))

plt.imshow(converted_image)
plt.show()