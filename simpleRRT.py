from tree import Tree
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np

q_init = np.array([50, 50])
K = 1000
delta = 1
D = [[0, 100], [0, 100]]
G = Tree(q_init, K, delta, D)
q_rand = G.random_config(D)
lines = []

for i in range(K):
    q_rand = G.random_config(G.D)
    q_near = G.nearest_vertex(q_rand)
    q_new = G.new_config(q_near, q_rand, G.delta)

fig, ax = plt.subplots()
# ax.set_xlim(0, 100)
# ax.set_ylim(0, 100)
ax.set_aspect("equal")
plt.scatter(G.nodes_x, G.nodes_y)
ax.add_collection(LineCollection(G.edges))
plt.show()