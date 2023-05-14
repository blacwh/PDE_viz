import numpy as np
import pandas as pd
# from exp_datasize import run_1d_datasize
from exp1 import exp1
from exp2 import exp2


# random sampling 
# s = []
# df = pd.read_csv('../adv_1d.csv')
# # print(df)
# for i in range(100, 1000, 100):
#     temp = np.random.choice(20000, size=(i), replace=False)
#     s.append(temp)

# for i in range(1000, 10001, 1000):
#     temp = np.random.choice(20000, size=(i), replace=False)
#     s.append(temp)



# def random_sample(st):
#     new_df = df.loc[0:0]
#     for i in st:
#       n1 = df.loc[i:i]
#       new_df = pd.concat([n1, new_df])
#     new_df = new_df[:-1]

#     return new_df


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


    
# fh = 'result/'

# for i in range(len(layers)):
#     err_list = []
#     loss_list = []
#     for st in s:
#         new_df = random_sample(st)
#         # lg = len(new_df)
#         loss, error, l1, l2 = run_1d_datasize(layers[i], new_df, i)
#         err_list.append(error)
#         loss_list.append(loss)
#     # write 100 to 19000 results in one text file
#     with open(fh + str(layers[i]) + '.txt', 'w') as f:
#         f.write('error: ' + str(err_list))
#         f.write('loss: ' + str(loss_list))

#     print('-----finished Model {}-----'.format(layers[i]))

    