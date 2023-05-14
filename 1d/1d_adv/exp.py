from execute import run_1d
import time


begin = time.time()

dense = []

for i in range(10, 11):
    for j in range(60,  101, 10):
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
incre_1 = n6 + n7 + n8

for i in range(len(incre)):
    t = incre[i][::-1]
    decre.append(t)
decre_1 = decre[30:]
def dense_exp(dense):
    fh_dense = 'dense_r/'
    for i in range(len(dense)):
        loss, err_mean, l1, l2 = run_1d(dense[i])
        fn_d = fh_dense + 'dense_' + str(len(dense[i])).zfill(2) + '_{}.txt'.format(dense[i][0])
        text = str([loss]+[err_mean]+[l1]+[l2])
        with open(fn_d, 'w') as f:
            f.write(text)
    print('------------finished dense experiment--------------')

def incre_exp(incre):
    fh_incre = 'incre_r/'
    for i in range(len(incre)):
        loss, err_mean, l1, l2 = run_1d(incre[i])
        fn_i = fh_incre + 'incre_' + str(len(incre[i])).zfill(2) + '_{}.txt'.format(incre[i][0])
        text = str([loss]+[err_mean]+[l1]+[l2])
        with open(fn_i, 'w') as f:
            f.write(text)
    print('------------finished dense experiment--------------')


def decre_exp(decre):
    fh_decre = 'decre_r/'
    for i in range(len(decre)):
        loss, err_mean, l1, l2 = run_1d(decre[i])
        fn_dc = fh_decre + 'decre_' + str(len(decre[i])).zfill(2) + '_{}.txt'.format(decre[i][-1])
        text = str([loss]+[err_mean]+[l1]+[l2])
        with open(fn_dc, 'w') as f:
            f.write(text)
    print('------------finished dense experiment--------------')


# dense_exp(dense)
# incre_exp(incre_1)
decre_exp(decre_1)

end = time.time()

t_time = end - begin
print('Total time for exploration: {: .2f}'.format(t_time))