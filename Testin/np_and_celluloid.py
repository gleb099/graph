import numpy as np
from matplotlib import pyplot as plt
from celluloid import Camera

fig, axes = plt.subplots(1)
camera = Camera(fig)
t = np.linspace(0, 2 * np.pi, 128, endpoint=False)
for i in t:
    axes[0].plot(t, np.sin(t + i), color='blue')
    axes[0].plot(t, np.sin(t - i), color='red')
    camera.snap()
    
animation = camera.animate()  
#animation.save('celluloid_subplots.gif', writer = 'imagemagick')
animation.show()