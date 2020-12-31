import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Activation, Dense, Flatten

def get_dataset(training=True):

    mnist = tf.keras.datasets.mnist
    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

    if(training == False):
        return (test_images, test_labels)
    else:
        return (train_images, train_labels)

def print_stats(train_images, train_labels):
    class_names = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

    i = 0
    num_im = 0
    while i < len(train_images):
        num_im += 1
        i += 1
    print(num_im)
    size, x,y = train_images.shape
    print(x,"x",y, sep="")
    zero = 0;
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    i = 0
    while i < len(train_images):
        if(train_labels[i] == 0):
           zero += 1
        if (train_labels[i] == 1):
            one += 1
        if (train_labels[i] == 2):
            two += 1
        if (train_labels[i] == 3):
            three += 1
        if (train_labels[i] == 4):
            four += 1
        if (train_labels[i] == 5):
            five += 1
        if (train_labels[i] == 6):
            six += 1
        if (train_labels[i] == 7):
            seven += 1
        if (train_labels[i] == 8):
            eight += 1
        if (train_labels[i] == 9):
            nine += 1

        i += 1

    print('0. Zero - ', zero)
    print('1. One - ', one)
    print('2. Two - ', two)
    print('3. Three - ', three)
    print('4. Four - ', four)
    print('5. Five - ', five)
    print('6. Six - ', six)
    print('7. Seven - ', seven)
    print('8. Eight - ', eight)
    print('9. Nine - ', nine)


def build_model():
    loss = tf.keras.losses.SparseCategoricalCrossentropy(True)
    optimizer = tf.keras.optimizers.SGD(learning_rate=0.001)
    metrics = ['accuracy']

    model = Sequential()

    layer1 = Flatten()
    model.add(layer1)
    layer2 = Dense(128, input_shape=(28, 28), activation="relu")
    model.add(layer2)
    layer3 = Dense(64, input_shape=(28, 28), activation="relu")
    model.add(layer3)
    layer4 = Dense(10, input_shape=(28, 28))
    model.add(layer4)
    model.build(input_shape=(None, 28, 28))
    model.compile(optimizer=optimizer, loss=loss, metrics=metrics)
    return model

def train_model(model, train_images, train_labels, T):

    return  model.fit(train_images, train_labels, T)



def evaluate_model(model, test_images, test_labels, show_loss=True):
    # accuracy = model.evaluate(test_images, test_labels)
    loss_metric, accuracy = model.evaluate(test_images, test_labels)
    accuracy_percent = "{:.2%}".format(accuracy)
    # loss_metric = model.evaluate(test_images, test_labels)
    loss_f = '{0:.4f}'.format(loss_metric)
    if (show_loss==False):
        print("Accuracy:", accuracy_percent)

    else:
        print("Loss:", loss_f)
        print("Accuracy:", accuracy_percent, end="")

def predict_label(model, test_images, index):
    class_names = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    i = 0

    # tf.keras.activations.softmax(model, axis=-1)

    proba = model.predict(test_images)
    ind = proba[index]
    print(ind)
    # idxs = np.argsort(ind)[::-1]
    idxs = ind

    while( i < 10):
        if(idxs[i]==0):
            print("Zero:", "{:.2%}".format(ind[0]))
        if (idxs[i] == 1):
            print("One:", "{:.2%}".format(ind[1]))
        if (idxs[i] == 2):
            print("Two:", "{:.2%}".format(ind[2]))
        if (idxs[i] == 3):
            print("Three:", "{:.2%}".format(ind[3]))
        if (idxs[i] == 4):
            print("Four:", "{:.2%}".format(ind[4]))
        if (idxs[i] == 5):
            print("Five:", "{:.2%}".format(ind[5]))
        if (idxs[i] == 6):
            print("Six:", "{:.2%}".format(ind[6]))
        if (idxs[i] == 7):
            print("Seven:", "{:.2%}".format(ind[7]))
        if (idxs[i] == 8):
            print("Eight:", "{:.2%}".format(ind[8]))
        if (idxs[i] == 9):
            print("Nine:", "{:.2%}".format(ind[9]))

        i += 1

