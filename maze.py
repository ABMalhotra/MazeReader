import imageio
import numpy as np
import matplotlib.pyplot as plt

from lib.solver import MazeSolver

data_storage = "./data/"

im = imageio.imread(data_storage+"input.png") # values from 0 to 255
im = im.astype(np.float64) / 255. # 0 to 1
plt.imshow(im)

puzzle = MazeSolver(im)
plt.imshow(puzzle.solution)
imageio.imsave(data_storage+"output.png",puzzle.solution)
