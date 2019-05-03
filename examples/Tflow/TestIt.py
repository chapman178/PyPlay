import tensorflow as tf
# a = tf.constant(5.0)
# b = tf.constant(6.0)
# c = a * b                # c represents an operation
# sess = tf.Session()
# output_c = sess.run(c)        # causes the operation to be executed
# print(output_c)     # outputs 30.0
# sess.close()
#
# # line model
# W = tf.Variable([.3],tf.float32)
# b = tf.Variable([-.3],tf.float32)
# x = tf.placeholder(tf.float32)
# linear_model = W * x + b
# y = tf.placeholder(tf.float32)
# squared_deltas = tf.square(linear_model - y) # least squares method
# loss = tf.reduce_sum(squared_deltas) # residual
#
# optimizer = tf.train.GradientDescentOptimizer(0.01) # create optimizer
# train = optimizer.minimize(loss) # add optimizer to minimize loss
#
# init = tf.global_variables_initializer()
# sess = tf.Session()
# sess.run(init) # initialize variables
# print( sess.run([W, b]))
#
# for i in range(1000):
# 	sess.run( train, {x : [1,2,3,4], y : [0,-1,-2,-3]}) # train line model
# print( sess.run([W, b]))

c1 = tf.constant(4)
c2 = tf.constant(5)
c3 = tf.constant(6)
x = tf.placeholder(tf.float32)
x2 = tf.pow(x,2)
op = c1*x2 + c2*x + c3

y = tf.placeholder(tf.float32)
squared_deltas = tf.square(op - y) # least squares method
loss = tf.reduce_sum(squared_deltas)

optimizer = tf.train.GradientDescentOptimizer(0.001) # create optimizer
train = optimizer.minimize(loss) # add optimizer to minimize loss

init = tf.global_variables_initializer()
ses = tf.Session()
ses.run(init)
for i in range(1000)

print(result)









