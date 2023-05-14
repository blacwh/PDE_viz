dic = [{'structure': 'dense_08_30.txt', 'loss': 0.0005173106328584254, 'error': 0.0009600000000000719, 'l1': 1.00045, 'l2': 1.00147}, {'structure': 'incre_04_10.txt', 'loss': 0.00032473623286932707, 'error': 0.0016750000000000376, 'l1': 0.9994, 'l2': 1.00275}, {'structure': 'incre_05_20.txt', 'loss': 0.0003366930177435279, 'error': 0.0019700000000000273, 'l1': 0.99827, 'l2': 1.00221}, {'structure': 'incre_06_30.txt', 'loss': 0.0005334117449820042, 'error': 0.0020599999999999508, 'l1': 0.99638, 'l2': 1.0005}, {'structure': 'incre_07_20.txt', 'loss': 0.0006077102152630687, 'error': 0.0027349999999999874, 'l1': 1.00538, 'l2': 0.99991}, {'structure': 'dense_04_40.txt', 'loss': 0.0004039407067466527, 'error': 0.0034000000000000696, 'l1': 1.00364, 'l2': 1.00316}, {'structure': 'dense_08_20.txt', 'loss': 0.00042097660480067134, 'error': 0.0037299999999999, 'l1': 1.00368, 'l2': 1.00378}, {'structure': 'incre_10_10.txt', 'loss': 0.0005014578346163034, 'error': 0.0038400000000000656, 'l1': 1.00502, 'l2': 1.00266}, {'structure': 'incre_02_60.txt', 'loss': 0.00038408051477745175, 'error': 0.003994999999999971, 'l1': 1.00389, 'l2': 0.9959}, {'structure': 'dense_08_10.txt', 'loss': 0.00023611006326973438, 'error': 0.004064999999999985, 'l1': 0.99222, 'l2': 0.99965}]



def dense_c(l,n):
    return [n for i in range(l)]

def incre_c(l,n):
    s = []
    for i in range(l):
        s.append(n)
        n += 10
    return s

# print(dense_c)
res = []
for d in dic:
    s = d['structure']
    s = s.strip('.txt')
    data = {}
    l = int(s[6:8])
    n = int(s[-2:])
    print(l, n)
    if s[:5] == 'dense':
        
        data['layers'] = dense_c(l,n)
        # print('1')
    elif s[:5] == 'incre':
        data['layers'] = incre_c(l,n)
    print(data)
    data['loss'] = d['loss']
    data['error'] = d['error']
    data['l1'] = d['l1']
    data['l2'] = d['l2']
    res.append(data)

with open('top10_1.txt', 'w') as f:
    f.write(str(res))