#encoding=utf-8
import tensorflow as tf
import numpy as np
import input
import os

"""
使用vgg16修改的模型实现的猫狗大战神经网络
"""
learning_rate = 0.0005  # 模型的学习率
N_CLASSES = 2  # 分类的数量

class Vgg16:
    def __init__(self,vgg_npy_path = None):
        self.data_dict = np.load(vgg_npy_path,encoding="latin1").item()
        self.x = tf.placeholder(tf.float32,[None,224,224,3])
        self.y_ = tf.placeholder(tf.float32,[None,N_CLASSES])
        # pre-trained VGG layers are fixed in fine-tune
        conv1_1 = self.conv_layer(self.x, "conv1_1")
        conv1_2 = self.conv_layer(conv1_1, "conv1_2")
        pool1 = self.max_pool(conv1_2, 'pool1')

        conv2_1 = self.conv_layer(pool1, "conv2_1")
        conv2_2 = self.conv_layer(conv2_1, "conv2_2")
        pool2 = self.max_pool(conv2_2, 'pool2')

        conv3_1 = self.conv_layer(pool2, "conv3_1")
        conv3_2 = self.conv_layer(conv3_1, "conv3_2")
        conv3_3 = self.conv_layer(conv3_2, "conv3_3")
        pool3 = self.max_pool(conv3_3, 'pool3')

        conv4_1 = self.conv_layer(pool3, "conv4_1")
        conv4_2 = self.conv_layer(conv4_1, "conv4_2")
        conv4_3 = self.conv_layer(conv4_2, "conv4_3")
        pool4 = self.max_pool(conv4_3, 'pool4')

        conv5_1 = self.conv_layer(pool4, "conv5_1")
        conv5_2 = self.conv_layer(conv5_1, "conv5_2")
        conv5_3 = self.conv_layer(conv5_2, "conv5_3")
        pool5 = self.max_pool(conv5_3, 'pool5')

        self.flatten = tf.reshape(pool5,[-1,7*7*512])

        with tf.name_scope(name='fc6'):
            self.fc6 = tf.layers.dense(self.flatten,256,tf.nn.relu,name='fc6')

        with tf.name_scope(name='softmax'):
            softmax_W = self.weight_variable([256,N_CLASSES],name='softmax_W')
            softmax_b = self.biases_variable([N_CLASSES],name='softmax_b')
            tf.summary.histogram('softmax/W',softmax_W)
            tf.summary.histogram('softmax/b',softmax_b)

            self.softmax = tf.add(tf.matmul(self.fc6,softmax_W),softmax_b,name='softmax')

        with tf.name_scope(name='loss'):
            cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits=self.softmax,labels=self.y_)
            # self.loss = tf.reduce_mean(cross_entropy, name='loss')
            self.loss = tf.reduce_mean(cross_entropy,name='loss') + tf.contrib.layers.l2_regularizer(0.5)(softmax_W)
            tf.summary.scalar('loss',self.loss)

        with tf.name_scope(name='train_op'):
            self.train_op = tf.train.RMSPropOptimizer(learning_rate).minimize(self.loss)

        with tf.name_scope(name='acc'):
            correct = tf.equal(tf.argmax(self.softmax,axis=1),tf.argmax(self.y_,axis=1))
            correct = tf.cast(correct,tf.float32)
            self.acc = tf.reduce_mean(correct,name='acc')
            tf.summary.scalar('acc',self.acc)

        self.merged = tf.summary.merge_all()


    def conv_layer(self,bottom,name):
        with tf.name_scope(name=name):
            conv = tf.nn.conv2d(bottom,self.data_dict[name][0],[1,1,1,1],padding='SAME',name=name)
            return tf.nn.relu(tf.nn.bias_add(conv,self.data_dict[name][1]))

    def max_pool(self,bottom,name):
        return tf.nn.max_pool(bottom,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME',name=name)

    def weight_variable(self,shape,name="weight",stddev = 0.1):  #stddev  表示标准差
        initializer = tf.contrib.layers.xavier_initializer()

        return tf.Variable(initializer(shape),name=name)

    def biases_variable(self,shape, name="bias", value=0.1):
        initial = tf.constant(value, shape=shape, dtype=tf.float32)
        return tf.Variable(initial, name=name)

IMG_W = 224
IMG_H = 224
BATCH_SIZE = 32  # 每次取的batch数
CAPACITY = 2000
MAX_STEP = 500

npyPath = "/Users/aria/MyDocs/npy/vgg16.npy"  # vgg16的预训练模型
# npyPath = "D:\\train_data\\npy\\vgg16.npy"
def train():
    train, train_label, test_img, test_label = input.get_img_files()
    train_batch, train_label_batch = input.get_img_batch(train, train_label, w=IMG_W, h=IMG_H,
                                                              batch_size=BATCH_SIZE, capacity=CAPACITY)
    test_batch, test_label_batch = input.get_img_batch(test_img, test_label, w=IMG_W, h=IMG_H,
                                                            batch_size=BATCH_SIZE, capacity=CAPACITY)
    print("data loaded")
    vgg = Vgg16(npyPath)
    sess = tf.Session()
    saver = tf.train.Saver()
    writer = tf.summary.FileWriter('graph/', sess.graph)  #训练后的tensorboard保存目录
    sess.run(tf.global_variables_initializer())
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    try:
        for step in range(MAX_STEP):
            tra_images,tra_labels = sess.run([train_batch,train_label_batch])
            _,tra_loss,tra_acc = sess.run([vgg.train_op,vgg.loss,vgg.acc],feed_dict={vgg.x:tra_images,vgg.y_:tra_labels})
            if step % 50 == 0:
                print("step:%d , tra loss = %.2f, tra acc = %.2f%%"%(step,tra_loss,tra_acc * 100))
                merged = sess.run(vgg.merged,feed_dict={vgg.x:tra_images,vgg.y_:tra_labels})
                writer.add_summary(merged,step)
            if step % 100 == 0 or step + 1 == MAX_STEP:
                val_imgs_batch, val_label_batch = sess.run([test_batch,test_label_batch])
                val_loss,val_acc = sess.run([vgg.loss,vgg.acc],
                                                   feed_dict={vgg.x:val_imgs_batch,vgg.y_:val_label_batch})
                print("Step:%d, val loss = %.2f, val acc = %.2f%%" % (step,val_loss,val_acc * 100))

            if step + 1 == MAX_STEP:
                checkpoint_path = os.path.join("checkpoint_dir","model.ckpt")
                saver.save(sess, checkpoint_path, global_step=step)
    except Exception as e:
        print(e)
        coord.request_stop()
    finally:
        coord.request_stop()
    coord.join(threads)


# 这里用于测试，适当修改或者往predict_dir放入要测试的图片即可
def predict_in_files():
    img_path = "predict_dir"    # 用于测试的文件目录
    imgs,labels = input.get_predict_files(img_path)
    vgg = Vgg16(npyPath)
    saver = tf.train.Saver()
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    ckpt = tf.train.get_checkpoint_state("checkpoint_dir/")   # 训练好的模型存放位置。模型的话在百度盘上下载或者自己训练
    if ckpt and ckpt.model_checkpoint_path:
        print("start load model")
        global_step = ckpt.model_checkpoint_path.split('/')[-1].split('-')[-1]
        saver.restore(sess, ckpt.model_checkpoint_path)
        print('Loading success, global_step is %s' % global_step)
    predictions = sess.run(vgg.softmax,
                           feed_dict={vgg.x: imgs})

    for i in range(len(predictions)):
        if predictions[i][0] >= predictions[i][1]:
            print("fileName:%s    prediction:cat   value:%f   other value:%f"%(labels[i],predictions[i][0],predictions[i][1]))
        else:
            print("fileName:%s    prediction:dog   value:%f   other value:%f"%(labels[i],predictions[i][1],predictions[i][0]))


if __name__=='__main__':
    # train()
    predict_in_files()