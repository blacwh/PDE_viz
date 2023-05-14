from exp1 import exp1
from exp2 import exp2

layers = [
    [30, 30, 30, 30, 30, 30, 30, 30], 
    # 'loss': 0.0005173106328584254, 'error': 0.0009600000000000719, 
    [10, 20, 30, 40], 
    # 'loss': 0.00032473623286932707, 'error': 0.0016750000000000376,
    [20, 30, 40, 50, 60], 
    # 'loss': 0.0003366930177435279, 'error': 0.0019700000000000273,
    [30, 40, 50, 60, 70, 80], 
    # 'loss': 0.0005334117449820042, 'error': 0.0020599999999999508,
    [20, 30, 40, 50, 60, 70, 80], 
    # 'loss': 0.0006077102152630687, 'error': 0.0027349999999999874,
    [40, 40, 40, 40], 
    # 'loss': 0.0004039407067466527, 'error': 0.0034000000000000696,
    [20, 20, 20, 20, 20, 20, 20, 20], 
    # 'loss': 0.00042097660480067134, 'error': 0.0037299999999999,
    [10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 
    # 'loss': 0.0005014578346163034, 'error': 0.0038400000000,
    [60, 70], 
    # 'loss': 0.00038408051477745175, 'error': 0.003994999999999971,
    [10, 10, 10, 10, 10, 10, 10, 10]
    # 'loss': 0.00023611006326973438, 'error': 0.004064999999999985,
]

for i in range(len(layers)):
    exp1(layers[i], i)
    exp2(layers[i], i)
    print('================')
    print('finish layer{} experiment'.format(i))
    print('================')