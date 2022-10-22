from keras.models import load_model
from keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
import os


def load_image(img_path, show=False):

    img = image.load_img(img_path, target_size=(150, 150))
    img_tensor = image.img_to_array(img)                    # create tensor of image with parameters (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # expand img_tensor to include batch parameter so it's correctly formatted
    img_tensor /= 255.                                      # divide by 255 to get values in range of [0, 1]

    # display image as graph
    if show:
        plt.imshow(img_tensor[0])
        plt.axis('off')
        plt.show()

    return img_tensor


if __name__ == "__main__":

    # load model
    model = load_model("model_aug.h5")

    # image path
    img_path = '/media/data/dogscats/test1/3867.jpg'    # dog
    #img_path = '/media/data/dogscats/test1/19.jpg'      # cat

    # load a single image
    new_image = load_image(img_path)

    # check prediction
    pred = model.predict(new_image)