import os
import itertools
from keras.callbacks import EarlyStopping
from sklearn.metrics import f1_score
import tools_split as tools
import tensorflow as tf

training_data, training_label, validation_data, validation_label, validation_cate_label = tools.get_data()

kernel_size = [3, 5, 7]
num_layers = [8, 9, 10, 11, 12]
batch_size = [30, 50, 70, 90, 120]
learning_rate = [0.00005, 0.0001, 0.0005, 0.001, 0.005]
overflow_model = 0

def run(bs, path, lr, ks, num_layer):   
    with tf.device('/cpu:0'):
        model = tools.create_model(lr, bs, ks, num_layer)
    early_stop = EarlyStopping(patience=20)
    with tf.device("/device:GPU:0"):
        history = model.fit(x = training_data, 
                            y = training_label,
                            epochs=80,
                            validation_data=(validation_data, validation_label),
                            callbacks=[early_stop],
                            batch_size=bs, 
                            verbose=0)
    evaluation = model.evaluate(x = validation_data, y = validation_label)
    validation_prediction = model.predict_classes(validation_data, batch_size=bs)
    score = f1_score(validation_cate_label, validation_prediction, average=None)

    tools.show_plot(path, history)
    tools.write_file(path+"/readme.txt", evaluation, score, model)
    del model

## main()
base_path = "train_test_split/"
if not os.path.exists(base_path):
    os.makedirs(base_path)

index=1
with open(base_path+"Cartesian_product.txt", "w+") as writer:
    for ks, num_layer, bs, lr in itertools.product(kernel_size, num_layers, batch_size, learning_rate):
        writer.write(str(index)+":"+"\n")
        writer.write('ks={}, num_layer={}, bs={}, lr={}'.format(ks, num_layer, bs, lr)+"\n")
        index = index + 1
    del index

index=1
for ks, num_layer, bs, lr in itertools.product(kernel_size, num_layers, batch_size, learning_rate):
    print("Index "+str(index))
    path = base_path+str(index)
    if not os.path.exists(path):
        os.makedirs(path)
    
    with tf.device('/cpu:0'):
        model = tools.create_model(lr, bs, ks, num_layer)
    if model:
        run(bs, path, lr, ks, num_layer)
    else:
        overflow_model = overflow_model + 1
    del model
    index = index + 1

print("Training finished! Overflow model: ", overflow_model)