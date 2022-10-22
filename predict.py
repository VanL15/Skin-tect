import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np

class_indicies = {0: 'akiec', 1: 'bcc', 2: 'bkl', 3: 'df', 4: 'mel', 5: 'nv', 6: 'vasc'}

def load_image(img_path, show=False):

    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(224, 224, 3))
    img_tensor = tf.keras.preprocessing.image.img_to_array(img)                         # create tensor of image with parameters (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)                                     # expand img_tensor to include batch parameter so it's correctly formatted
    img_tensor /= 255.                                                                  # divide by 255 to normalize

    # display image as graph
    if show:
        plt.imshow(img_tensor[0])
        plt.axis('off')
        plt.show()

    return img_tensor

if __name__ == "__main__":

    # load model
    model = load_model("hackgt9.h5")

    # image path
    FILE_NAME = "nv"
    img_path = '/Images/{FILE_NAME}.jpg'

    # load a single image
    new_image = load_image(img_path)

    # check prediction
    preds_classes = model.predict_step(new_image)
    cls = np.argmax(preds_classes)
    print(class_indicies[cls])