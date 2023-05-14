import json

base = [i * 100 for i in range(1, 10)] + [i * 1000 for i in range(1, 11)]
sample = [

    {'loss': 0.0005173106328584254, 'error': 0.0009600000000000719}, 
 
    {'loss': 0.00032473623286932707, 'error': 0.0016750000000000376},

    {'loss': 0.0003366930177435279, 'error': 0.0019700000000000273},

    {'loss': 0.0005334117449820042, 'error': 0.0020599999999999508},
 
    {'loss': 0.0006077102152630687, 'error': 0.0027349999999999874},

    {'loss': 0.0004039407067466527, 'error': 0.0034000000000000696},

    {'loss': 0.00042097660480067134, 'error': 0.0037299999999999},

    {'loss': 0.0005014578346163034, 'error': 0.0038400000000},

    {'loss': 0.00038408051477745175, 'error': 0.003994999999999971},

    {'loss': 0.00023611006326973438, 'error': 0.004064999999999985},
]
err = {}
loss = {}
for i in range(10):
    d1 = []
    d2 = []
    with open('error_r_' + str(i) + '.txt') as f1:
        t1 = f1.readlines()[0].strip('[').strip(']').split(',')
        t1 = [float(i) for i in t1]
        # print(len(t1))
    with open('loss_r_' + str(i) + '.txt') as f2:
        t2 = f2.readlines()[0].strip('[').strip(']').split(',')
        t2 = [float(i) for i in t2]
    for j in range(len(base)):
        d1.append([base[j], t1[j]])
        d2.append([base[j], t2[j]])
    d1.append([20000,sample[i]['error']])
    d2.append([20000,sample[i]['loss']])
    err[str(i)] = d1
    loss[str(i)] = d2


j_e = json.dumps(err)
j_l = json.dumps(loss)
with open('1d_dz_e.json', 'w') as f:
    f.write(j_e)
with open('1d_dz_l.json', 'w') as f:
    f.write(j_l)
# print(len(base))
# print(len(err['1']))
# print(err)
# print(loss)