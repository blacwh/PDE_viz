import tensorflow as tf

import numpy as np
import pandas as pd
import time

def exp2(layer, i):
    model_name = 'params{}'.format(i)
    class PhysicsinformedNN:
        def __init__(self, x, t, u, layers, activation):
            X = np.concatenate([x, t], 1)
            
            self.lb = X.min(0)    #uniform
            self.ub = X.max(0)

            self.X = X 

            self.x = X[:,0:1]

            self.t = X[:,1:2]

            self.u = u
            
            # Initialize NNs
            self.layers = layers
            self.weights, self.biases = self.initialize_NN(layers)
            self.activation = activation
            
            # tf Placeholders        
            self.x_tf = tf.placeholder(tf.float32, shape=[None, self.x.shape[1]])

            self.t_tf = tf.placeholder(tf.float32, shape=[None, self.t.shape[1]])
            self.u_tf = tf.placeholder(tf.float32, shape=[None, self.u.shape[1]])


            # Initialize parameters
            self.lambda_1 = tf.Variable([0.0], dtype=tf.float32)
            self.lambda_2 = tf.Variable([0.0], dtype=tf.float32)



            # tf Graphs
            self.u_pred, self.f_pred = self.net_pde(
                self.x_tf, self.t_tf)

            # Loss
            lam = 10**-5
            self.loss_1 = tf.reduce_mean(tf.square(self.u_tf - self.u_pred))
            self.loss_2 = tf.reduce_mean(tf.square(self.f_pred))
            self.loss = self.loss_1 + self.loss_2 
            # Optimizers     

            self.optimizer = tf.contrib.opt.ScipyOptimizerInterface(self.loss, 
                                        method = 'L-BFGS-B', 
                                        options = {'maxiter': 50000,
                                                'maxfun': 50000,
                                                'maxcor': 50,
                                                'maxls': 50,
                                                'ftol' : 1.0 * np.finfo(float).eps})                                                             
            
            self.optimizer_Adam = tf.train.AdamOptimizer()
            self.train_op_Adam = self.optimizer_Adam.minimize(self.loss)
                    
            # tf session
            self.sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True,
                                    log_device_placement=False))
            # tf.debugging.set_log_device_placement(True)
            
            init = tf.global_variables_initializer()
            
            self.sess.run(init)

        def initialize_NN(self, layers):        
            weights = []        
            biases = []        
            num_layers = len(layers)
            for l in range(0, num_layers - 1):            
                W = self.xavier_init(size=[layers[l], layers[l + 1]])            
                b = tf.Variable(tf.zeros([1, layers[l + 1]], dtype=tf.float32), dtype=tf.float32)            
                weights.append(W)            
                biases.append(b)
            return weights, biases
            
        def xavier_init(self, size):        
            in_dim = size[0]        
            out_dim = size[1]        
            xavier_stddev = np.sqrt(2 / (in_dim + out_dim)) 
            return tf.Variable(tf.truncated_normal([in_dim, out_dim], stddev=xavier_stddev),dtype=tf.float32)

        def neural_net(self, X, weights, biases, activation):        
            num_layers = len(weights) + 1

            H = 2.0 * (X - self.lb) / (self.ub - self.lb) - 1.0  # uniform
            for l in range(0, num_layers - 2):            
                W = weights[l]            
                b = biases[l]
                H = tf.tanh(tf.add(tf.matmul(tf.cast(H, tf.float32), W), b))

            W = weights[-1]        
            b = biases[-1]        
            Y = tf.add(tf.matmul(H, W), b)
            return Y


        def net_pde(self, x, t):        
            u = self.neural_net(tf.concat([x, t], 1), self.weights, self.biases, self.activation)
            
            lambda_1 = self.lambda_1
            lambda_2 = self.lambda_2




            # time derivatives
            u_t = tf.gradients(u, t)[0]
            # first derivatives
            u_x = tf.gradients(u, x)[0]

            u_xx = tf.gradients(u_x, x)[0]

    
            f = u_t + lambda_1 * u_x - lambda_2 * u_xx


            return u, f


        def callback(self, loss, lambda_1, lambda_2):
            self.l1 = '%.5f'%lambda_1
            self.l2 = '%.5f'%lambda_2

        
        
        def change_data(self, x, t, u):
            X = np.concatenate([x, t], 1)

            self.lb = X.min(0)    #uniform
            self.ub = X.max(0)

            self.X = X 

            self.x = X[:,0:1]

            self.t = X[:,1:2]

            self.u = u

            self.x_tf = tf.placeholder(tf.float32, shape=[None, self.x.shape[1]])

            self.t_tf = tf.placeholder(tf.float32, shape=[None, self.t.shape[1]])
            self.u_tf = tf.placeholder(tf.float32, shape=[None, self.u.shape[1]])

            self.u_pred, self.f_pred = self.net_pde(
                self.x_tf, self.t_tf)
            
            self.loss_1 = tf.reduce_mean(tf.square(self.u_tf - self.u_pred))
            self.loss_2 = tf.reduce_mean(tf.square(self.f_pred))
            self.loss = self.loss_1 + self.loss_2 

            self.optimizer = tf.contrib.opt.ScipyOptimizerInterface(self.loss, 
                                        method = 'L-BFGS-B', 
                                        options = {'maxiter': 50000,
                                                'maxfun': 50000,
                                                'maxcor': 50,
                                                'maxls': 50,
                                                'ftol' : 1.0 * np.finfo(float).eps})                                                             
            
            self.optimizer_Adam = tf.train.AdamOptimizer()
            self.train_op_Adam = self.optimizer_Adam.minimize(self.loss)
                    
            # tf session
            self.sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True,
                                    log_device_placement=False))
            # tf.debugging.set_log_device_placement(True)
            
            init = tf.global_variables_initializer()
            
            self.sess.run(init)

        def train(self, nIter):
            
            tf_dict = {self.x_tf: self.x, 
                self.t_tf: self.t, self.u_tf: self.u}

            
            epoch_time = start_time = time.time()
            loss = []

            saver = tf.train.Saver()
            saver.restore(self.sess, model_name)
            # print('l1: %.3e, l2: %.3e, l3: %.3e, l4: %.3e, l5: %.3e, l6: %.3e' % 
            #         (lambda_1_value, lambda_2_value, lambda_3_value, lambda_4_value, lambda_5_value, lambda_6_value))
            # b = self.sess.run(self.biases[0])
            # w = self.sess.run(self.weights[0])
            # l_1 = self.sess.run(self.lambda_1)
            # print(b)
            # print(w)
            # print(l_1)
            lambda_1_value = self.sess.run(self.lambda_1)
            lambda_2_value = self.sess.run(self.lambda_2)

            # print('l1: %.3e, l2: %.3e, l3: %.3e, l4: %.3e, l5: %.3e, l6: %.3e' % 
            #       (lambda_1_value, lambda_2_value, lambda_3_value, lambda_4_value, lambda_5_value, lambda_6_value))
            for it in range(nIter):

                self.sess.run(self.train_op_Adam, tf_dict)
                
                # Print
                if it % 10 == 0:                
                    elapsed = time.time() - epoch_time               
                    loss_value = self.sess.run(self.loss, tf_dict)
                    loss1 = self.sess.run(self.loss_1, tf_dict)
                    loss2 = self.sess.run(self.loss_2, tf_dict)
                    # reg = self.sess.run(self.reg_l1, tf_dict)
                    lambda_1_value = self.sess.run(self.lambda_1)
                    lambda_2_value = self.sess.run(self.lambda_2)


                    # w = self.sess.run(self.weights[1].eval())
                    # print('It: %d, Loss: %.3e,  loss_1: %.3e, loss_2: %.3e, l1: %.3e, l2: %.3e, l3: %.3e, l4: %.3e, l5: %.3e, l6: %.3e Time: %.2f' % 
                    #       (it, loss_value, loss1, loss2, lambda_1_value, lambda_2_value, lambda_3_value, lambda_4_value, lambda_5_value, lambda_6_value, elapsed))
                    # print('It: %d, Loss: %.3e,  loss_1: %.3e, loss_2: %.3e, l1: %.3e, l2: %.3e, l3: %.3e, l4: %.3e Time: %.2f' % 
                        # (it, loss_value, loss1, loss2, lambda_1_value, lambda_2_value, lambda_3_value, lambda_4_value, elapsed))
                    epoch_time = time.time()
                    
                if it % 100 == 0:
                    loss.append(loss_value.item())
            
            # b = self.sess.run(self.biases[0])
            # print(b)
            
            # saver = tf.train.Saver()
            # saver.save(self.sess, 'params', write_meta_graph=False)
            # bias = self.sess.run(self.b)
            # with self.sess as sess:
            # print(self.biases[0].eval())
            self.optimizer.minimize(self.sess,
                        feed_dict = tf_dict,
                        fetches = [self.loss, self.lambda_1, self.lambda_2],
                        loss_callback = self.callback
                        )  
            # print('`````````````````')
            # print('l1: %.3e, l2: %.3e, l3: %.3e, l4: %.3e, l5: %.3e, l6: %.3e' % 
            #     (lambda_1_value, lambda_2_value, lambda_3_value, lambda_4_value, lambda_5_value, lambda_6_value))
            # print('`````````````````')
            print('loss: ', loss)
            saver = tf.train.Saver()
            saver.save(self.sess, model_name, write_meta_graph=False)

            return loss, self.l1, self.l2


    def model_execution(neurons, data):
        # shape of dataset
        (row, col) = data.shape
        # split dataset to traning(70%) and validation(30%) then training
        u = data['u'].values
        t = data['t'].values
        x = data['x'].values

        N_train = row // 10 * 7
        idx = np.random.choice(x.shape[0], N_train, replace=False)
        x_train = x[idx].reshape(N_train,1)

        t_train = t[idx].reshape(N_train,1)
        u_train = u[idx].reshape(N_train,1)
        N_val = row - N_train
        idx2 = np.random.choice(x.shape[0], N_val, replace=False)
        x_val = x[idx2].reshape(N_val,1)

        t_val = t[idx2].reshape(N_val,1)

        # input layers and neurons
        layers = [2] # input layer neuron number
        n = neurons
        for each in n:
            layers.append(int(each))
        layers.append(1) # output layer

        act_func = ['sigmoid', 'tanh', 'sin']
        model = PhysicsinformedNN(x_train, t_train, u_train, layers, activation=act_func[1])

        return model

    def new_model(model, new_data):
        # shape of dataset
        (row, col) = new_data.shape
        # split dataset to traning(70%) and validation(30%) then training
        u = new_data['u'].values
        t = new_data['t'].values
        x = new_data['x'].values


        N_train = row // 10 * 7
        idx = np.random.choice(x.shape[0], N_train, replace=False)
        x_train = x[idx].reshape(N_train,1)

        t_train = t[idx].reshape(N_train,1)
        u_train = u[idx].reshape(N_train,1)
        N_val = row - N_train
        idx2 = np.random.choice(x.shape[0], N_val, replace=False)
        x_val = x[idx2].reshape(N_val,1)

        t_val = t[idx2].reshape(N_val,1)

        model.change_data(x_train, t_train, u_train)

        # return model


    def fit(model, epochs):
        history, l1, l2 = model.train(epochs)
        loss = history[-1]

        # print('history: ', history)
        # print('loss: ', loss)
        return loss, float(l1), float(l2)


    df = pd.read_csv('adv_1d.csv')
    def random_sample(st):
        new_df = df.loc[0:0]
        for i in st:
            n1 = df.loc[i:i]
            new_df = pd.concat([n1, new_df])
        new_df = new_df[:-1]

        return new_df


    layer = layer
    # tf.reset_default_graph()
    # s = np.random.choice(20000, size=20000, replace=False)
    # new_df = random_sample(s)
    # epochs = 800

    # model = model_execution(layer, new_df)
    # loss, l1, l2, l3, l4, l5, l6 = fit(model, epochs)
    # err = abs(np.array([(1 -  l1), (1 - l4), (1 - l3), (1 - l5), (1 - l6), (2 - l2)]))
    # err_mean = err.mean()


    r1 = []
    r2 = []
    # load model and execute
    size = np.array([i * 100 for i in range(1, 10)] + [i * 1000 for i in range(1, 10)] + [10000]).flatten()
    for j in size:
        tf.reset_default_graph()
        s1 = np.random.choice(20000, size=j, replace=False)
        new_df = random_sample(s1)
        epochs = 2000
        model = model_execution(layer, new_df)
        loss, l1, l2 = fit(model, epochs)
        err = abs(np.array([(1 -  l1), (1 - l2)]))
        err_mean = err.mean()
        print(len(new_df))
        print('loss: ', loss)
        print('error: ', err_mean)
        r1.append(loss)
        r2.append(err_mean)

    with open('loss_r_{}.txt'.format(i), 'w') as f1:
        f1.write(str(r1))

    with open('error_r_{}.txt'.format(i), 'w') as f2:
        f2.write(str(r2))

