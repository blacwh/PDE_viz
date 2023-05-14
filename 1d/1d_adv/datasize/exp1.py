import tensorflow as tf
import numpy as np
import os
import time
import pandas as pd

def exp1(layer, i):
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

            # self.hy = hy
            
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
            self.lam = 10**-5
            # self.reg_l1 = self.lam * tf.reduce_mean(tf.math.abs(self.lambda_1))
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
                                                'ftol' : 0.001 * np.finfo(float).eps
                                                })
                                                # 'ftol' : 0.001 * np.finfo(float).eps                                                             
            
            self.optimizer_Adam = tf.train.AdamOptimizer(learning_rate=0.01)
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
            # u = self.neural_net(tf.concat([x, y, z, t], 1), self.weights, self.biases, self.activation)
            

            u = self.neural_net(tf.concat([x, t], 1), self.weights, self.biases, self.activation)

            # hy = self.neural_net(tf.concat([x, y, z, t], 1), self.weights, self.biases, self.activation)

            lambda_1 = self.lambda_1
            lambda_2 = self.lambda_2



            # time derivatives
            u_t = tf.gradients(u, t)[0]


            # first derivatives
            u_x = tf.gradients(u, x)[0]
            # second derivatives
            u_xx = tf.gradients(u_x, x)[0]


            # third derivatives


            f = u_t + lambda_1 * u_x - lambda_2 * u_xx

            return u, f
            # return u, u_t, u_x, u_y, u_z, u_xx, u_yy, u_zz, f

        def callback(self, loss, lambda_1, lambda_2):
            # print('Loss: %.3e, l1: %.5f l2: %.5f' % (loss, lambda_1, lambda_2))
            
            self.l1 = '%.5f'%lambda_1
            self.l2 = '%.5f'%lambda_2


        def train(self, nIter):
            
            tf_dict = {self.x_tf: self.x, self.t_tf: self.t,
                    self.u_tf: self.u
                    }

            epoch_time = start_time = time.time()
            loss = []
            # print('!!!!!', len(new_df), '!!!!!')
            # print('model_temp/' + model_name)
            # if len(new_df) != 100:
            # saver = tf.train.Saver()
            # saver.restore(self.sess, 'model_temp/' + model_name)

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

                    # print('It: %d, Loss: %.3e, loss1: %.3e, loss2: %.3e, l1: %.3f l2: %.3f Time: %.2f' % 
                    #     (it, loss_value, loss1, loss2, lambda_1_value, lambda_2_value, elapsed))

                    epoch_time = time.time()
                if it % 100 == 0:
                    loss.append(loss_value.item())

            self.optimizer.minimize(self.sess,
                        feed_dict = tf_dict,
                        fetches = [self.loss, self.lambda_1, self.lambda_2],
                        loss_callback = self.callback)
                        
            saver = tf.train.Saver()
            saver.save(self.sess, model_name, write_meta_graph=False)
            # end_time = time.time()
            # total_time = end_time - start_time
            # print('The total time for training: {: .2f}'.format(total_time))

            return loss, self.l1, self.l2


        # def predict(self, x_star, y_star, z_star, t_star):
        #     tf_dict = {self.x_tf: x_star, self.y_tf: y_star, self.z_tf: z_star, self.t_tf: t_star}

        #     ex_star = tf.sess.run(self.ex_pred, tf_dict)
        #     ey_star = tf.sess.run(self.ey_pred, tf_dict)
        #     ez_star = tf.sess.run(self.ez_pred, tf_dict)

        #     hx_star = tf.sess.run(self.hx_pred, tf_dict)
        #     hy_star = tf.sess.run(self.hy_pred, tf_dict)
        #     hz_star = tf.sess.run(self.hz_pred, tf_dict)
        #     return ex_star, ey_star, ez_star, hx_star, hy_star, hz_star

    def model_execution(neurons, df):
        # shape of dataset
        (row, col) = df.shape
        # split dataset to traning(70%) and validation(30%) then training
        u = df['u'].values


        t = df['t'].values
        x = df['x'].values


        N_train = row // 10 * 7
        idx = np.random.choice(x.shape[0], N_train, replace=False)
        x_train = x[idx].reshape(N_train,1)
        t_train = t[idx].reshape(N_train,1)

        u_train = u[idx].reshape(N_train,1)

        # hy_train = hy[idx].reshape(N_train,1)


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

    def fit(model, epochs):
        history, l1, l2 = model.train(epochs)
        loss = history[-1]
        # print('history: ', history)
        # print('loss: ', loss)
        return loss, float(l1), float(l2)


    df = pd.read_csv('../adv_1d.csv')
    # df = new_df
    def random_sample(st):
        new_df = df.loc[0:0]
        for i in st:
            n1 = df.loc[i:i]
            new_df = pd.concat([n1, new_df])
        new_df = new_df[:-1]

        return new_df


    layer = layer
    tf.reset_default_graph()
    s = np.random.choice(20000, size=20000, replace=False)
    new_df = random_sample(s)
    epochs = 800

    model = model_execution(layer, new_df)

    print('~~~~~start the model: {}~~~~~~~~'.format(layer))
    loss, l1, l2 = fit(model, epochs)
    err = abs(np.array([(1 -  l1), (1 - l2)]))
    err_mean = err.mean()


    # return loss, err_mean, l1, l2