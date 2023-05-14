import numpy as np


fh_dense = 'dense_r/'
fh_incre = 'incre_r/'
fh_decre = 'decre_r/'


total_res = []

for i in range(1,11):
    for j in range(10,101,10):
        res_d = {}
        fn_d = fh_dense + 'dense_'+ str(i).zfill(2) + '_{}.txt'.format(j)
        with open(fn_d, 'r') as f:
            a = f.readlines()[0]
            a = a.strip('[').strip(']').split(',')

            a = [float(i) for i in a]

            res_d['structure'] = 'dense_'+ str(i).zfill(2) + '_{}.txt'.format(j)
            res_d['loss'] = a[0]
            res_d['error'] = a[1]
            res_d['l1'] = a[2]
            res_d['l2'] = a[3]
            total_res.append(res_d)

for i in range(2,11):
    for j in range(10,(111-i*10),10):
        res_i = {}
        fn_i = fh_incre + 'incre_'+ str(i).zfill(2) + '_{}.txt'.format(j)
        with open(fn_i, 'r') as f:
            a = f.readlines()[0]
            a = a.strip('[').strip(']').split(',')

            a = [float(i) for i in a]

            res_i['structure'] = 'incre_'+ str(i).zfill(2) + '_{}.txt'.format(j)
            res_i['loss'] = a[0]
            res_i['error'] = a[1]
            res_i['l1'] = a[2]
            res_i['l2'] = a[3]
            total_res.append(res_i)

for i in range(2,11):
    for j in range(10,(111-i*10),10):
        res_dc = {}
        fn_dc = fh_decre + 'decre_'+ str(i).zfill(2) + '_{}.txt'.format(j)
        with open(fn_dc, 'r') as f:
            a = f.readlines()[0]
            a = a.strip('[').strip(']').split(',')

            a = [float(i) for i in a]

            res_dc['structure'] = 'decre_'+ str(i).zfill(2) + '_{}.txt'.format(j)
            res_dc['loss'] = a[0]
            res_dc['error'] = a[1]
            res_dc['l1'] = a[2]
            res_dc['l2'] = a[3]
            total_res.append(res_dc)

# print(total_res)
# print(len(total_res))

f_res = sorted(total_res, key=lambda i:i['error'])

print(f_res)
print(len(f_res))
# print(f_res[:10])

# with open('top10.txt', 'w') as f:
#     f.write(str(f_res[:10]))