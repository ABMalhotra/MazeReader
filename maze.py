data_storage = "./data/"

im = imageio.imread(data_storage+"input.png") # values from 0 to 255
im = im.astype(np.float) / 255. # 0 to 1
plt.imshow(im)

traveller = MazeSolver(im)
traveller.findShortestPath()
traveller.printSolvedMaze()
