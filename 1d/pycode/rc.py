import numpy as np
from sklearn.manifold import TSNE

# example = [i for i in range(10, 101, 10)]
dense = []

for i in range(1, 11):
    for j in range(10,  101, 10):
        dense.append([j] * i)

decre = []
incre = []

n = [[i, i+10] for i in range(10, 100, 10)]
n1 = [[i, i+10, i+20] for i in range(10, 90, 10)]
n2 = [[i, i+10, i+20, i+30] for i in range(10, 80, 10)]
n3 = [[i, i+10, i+20, i+30, i+40] for i in range(10, 70, 10)]
n4 = [[i, i+10, i+20, i+30, i+40, i+50] for i in range(10, 60, 10)]
n5 = [[i, i+10, i+20, i+30, i+40, i+50, i+60] for i in range(10, 50, 10)]
n6 = [[i, i+10, i+20, i+30, i+40, i+50, i+60, i+70] for i in range(10, 40, 10)]
n7 = [[i, i+10, i+20, i+30, i+40, i+50, i+60, i+70, i+80] for i in range(10, 30, 10)]
n8 = [[i, i+10, i+20, i+30, i+40, i+50, i+60, i+70, i+80, i+90] for i in range(10, 11, 10)]
incre = n + n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8
# print(len(incre))
for i in range(len(incre)):
    t = incre[i][::-1]
    decre.append(t)
# print(len(decre))
# print(incre)

# layers = dense + incre + decre


# dense error
e_d = []
file_head = ""
dense_head = "../1d_adv/dense_r/dense_"
for i in range(1, 11):
    for j in range(10, 101, 10):
        with open(file_head + dense_head + str(i).zfill(2) + "_" + str(j) + ".txt", "r") as f:
            t = f.readlines()[0].strip('[').strip(']').split(',')
            t = [float(i) for i in t]
            # print(t)
            t1 = t[1]
            e_d.append(t1)

e_dd = []
decre_head = "../1d_adv/decre_r/decre_"
c = 0
for i in range(2, 11):
    # print('``````````````')
    for j in range(10, (111-i*10), 10):
        # print(j)
        with open(file_head + decre_head + str(i).zfill(2) + "_" + str(j) + ".txt", "r") as f:
            t = f.readlines()[0].strip('[').strip(']').split(',')
            t = [float(i) for i in t]
            t1 = t[1]
            e_dd.append(t1)

# print(len(e_dd))
e_i = []
incre_head = "../1d_adv/incre_r/incre_"
for i in range(2, 11):
    for j in range(10, (111-i*10), 10):
        with open(file_head + incre_head + str(i).zfill(2) + "_" + str(j) + ".txt", "r") as f:
            t = f.readlines()[0].strip('[').strip(']').split(',')
            t = [float(i) for i in t]
            t1 = t[1]
            e_i.append(t1)
# print(len(e_i))
# print(e_i)

for i in range(len(dense)):
    while len(dense[i]) < 10:
        dense[i].insert(0, 0)
        
for i in range(len(decre)):
    while len(decre[i]) < 10:
        decre[i].insert(0, 0)

for i in range(len(incre)):
    while len(incre[i]) < 10:
        incre[i].insert(0, 0)

# for i in range(len(layers)):
#     layers[i].append(e[i])
for i in range(len(dense)):
    # print(sum(dense[i]))
    
    dense[i].append(sum(dense[i]))
    # print(dense[i])

        
for i in range(len(decre)):
    decre[i].append(sum(decre[i]))

for i in range(len(incre)):
    incre[i].append(sum(incre[i]))

for i in range(len(dense)):
    dense[i].append(e_d[i])
        
for i in range(len(decre)):
    decre[i].append(e_dd[i])

for i in range(len(incre)):
    incre[i].append(e_i[i])


layers = dense + decre + incre
# print(layers)
sorted_layers = sorted(layers, key=lambda x: x[-1])
# print(sorted_layers)
# X = np.array(layers)

X = np.array(sorted_layers)
# print(X)
X_embedded = TSNE(n_components=2, learning_rate='auto', init='random').fit_transform(X)

# print(X_embedded.tolist())
# # print(len(X_embedded))
with open('190_reduction.txt', 'w') as f:
    f.write(str(X_embedded.tolist()))

# layers = [[20, 30, 40, 50, 60, 70, 80, 90, 100],

# [30, 40, 50, 60, 70, 80, 90, 100],

# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],

# [20, 30, 40, 50],

# [60, 70, 80, 90],

# [40, 40, 40, 40, 40, 40, 40, 40, 40, 40],

# [80, 80],

# [20, 20, 20, 20, 20, 20, 20, 20, 20, 20],

# [30, 30, 30, 30, 30, 30, 30, 30, 30],

# [20, 20, 20, 20, 20, 20, 20, 20]]
# e = [0.010969999999999952,
# 0.018572500000000047,
# 0.023682500000000023,
# 0.027650000000000063,
# 0.02812500000000001,
# 0.028822500000000056,
# 0.02901999999999999,
# 0.03334249999999994,
# 0.0336225,
# 0.03429499999999994]

# r = []
# for i in range(len(layers)):
#     while len(layers[i]) < 10:
#         layers[i].insert(0, 0)

# for i in range(len(layers)):
#     layers[i].append(e[i])
    # print(len(layers[i]))
    # print(layers[i])
# print(layers)

# X = np.array([20, 20, 20, 20, 20, 20, 20, 20]).reshape(-1, 1)
# X = np.array(layers)
# # for i in range(len(layers)):
# X_embedded = TSNE(n_components=2, learning_rate='auto', init='random').fit_transform(X)

# print(X_embedded)
# with open('structure_reduction_e.txt', 'w') as f:
#     f.write(str(X_embedded))