import numpy as np

def pos_generator(D, obstacles:list):
    generated = False
    choices = []
    # for j in range(101):
    #     for i in range(101):
    #         choices.append(np.array([i, j]))

    while not generated:
        q = np.array([np.random.randint(D[0][0], D[0][1]), np.random.randint(D[1][0], D[1][1])])
        checked = []
        for obs in obstacles:
            if np.linalg.norm(q - obs.center) < obs.radius:
                break
            checked.append(obs)
        if len(checked) == len(obstacles):
            generated = True
    return q
