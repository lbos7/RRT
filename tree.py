import numpy as np
import math
import matplotlib as plt
import imageio

class Tree:

    def __init__(self, q_init:np.array, K:int, delta:int, D):
        self.q_init = q_init
        self.K = K
        self.delta = delta
        self.D = D
        self.nodes = [q_init]
        self.nodes_x = [q_init[0]]
        self.nodes_y = [q_init[1]]
        self.edges = []


    def random_config(self, D):
        return np.array([np.random.randint(D[0][0], D[0][1]), np.random.randint(D[1][0], D[1][1])])
        

    def nearest_vertex(self, q_rand:np.array):
        smallest_dist = []
        smallest_ind = 0
        for i in range(len(self.nodes)):
            dist = np.linalg.norm(q_rand - self.nodes[i])
            if smallest_dist == [] or dist < smallest_dist:
                smallest_dist = dist
                smallest_ind = i
        return self.nodes[smallest_ind]


    def new_config(self, q_near:np.array, q_rand:np.array, delta:int):
        dif = q_rand - q_near
        unit_vec = dif/np.linalg.norm(dif)
        q_new = q_near + unit_vec*delta
        self.nodes.append(q_new)
        self.nodes_x.append(q_new[0])
        self.nodes_y.append(q_new[1])
        self.edges.append([(q_near[0], q_near[1]), (q_new[0], q_new[1])])
        return q_new

