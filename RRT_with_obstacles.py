from tree import Tree
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection, PatchCollection
import matplotlib
import numpy as np
from pos_generator import pos_generator

K = 1000
delta = 1
D = [[0, 100], [0, 100]]
distinct_start_and_goal = False

num_obstacles = 15
obstacles = []
for i in range(num_obstacles):
    obstacles.append(matplotlib.patches.Circle([np.random.randint(D[0][0], D[0][1]), np.random.randint(D[1][0], D[1][1])],
                                               np.random.randint(5, 10), color = 'k'))
    

plt.show()

q_init = pos_generator(D, obstacles)
while not distinct_start_and_goal:
    q_goal = pos_generator(D, obstacles)
    if not (q_init == q_goal).all():
        distinct_start_and_goal = True

G = Tree(q_init, K, delta, D, obstacles)
q_rand = G.random_config(D)
lines = []

for i in range(K):
    q_rand = G.random_config(G.D)
    q_near = G.nearest_vertex(q_rand)
    q_new = G.new_config(q_near, q_rand, G.delta)
    if not q_new.all() == None:
        checked = []
        for obs in obstacles:
            u = np.dot(obs.center - q_new, q_goal - q_new)/(np.linalg.norm(q_goal - q_new)**2)
            if (u >= 0 and u <= 1):
                p = q_new + u*(q_goal - q_new)
                if np.linalg.norm(p - obs.center) < obs.radius:
                    break
            checked.append(obs)
        if len(checked) == len(obstacles):
            G.add_node(q_goal)
            break
                    

fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_aspect("equal")
plt.plot(G.nodes_x, G.nodes_y, 'bo', markersize=2)
plt.plot(G.nodes_x[0], G.nodes_y[0], 'gs')
plt.plot(G.nodes_x[-1], G.nodes_y[-1], 'r*')
lc = LineCollection(G.edges, color='b')
pc = PatchCollection(obstacles, color='k')
ax.add_collection(lc)
ax.add_collection(pc)

plt.show()