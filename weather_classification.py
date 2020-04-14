import keras
from keras.layers import Conv2D
from keras.models import Sequential
from keras.layers import MaxPool2D
from keras.layers import Flatten
from keras.layers import Dense

#Initialize CNN
Classifier=Sequential()


# Step 1 - Convolution
#Conv2D(Convolution 2Dimension)32- Filter(any number can be given),Filter size(3x3),(64,64=>x and y axis), 3 -RGB image
Classifier.add(Conv2D(32,(3,3),input_shape=(64,64,3),activation='relu'))


# Step 2 - Pooling
Classifier.add(MaxPool2D(pool_size=(2, 2)))

# Adding a second convolutional layer. No need of giving input shape as system will automatically understand 64,64
Classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
Classifier.add(MaxPool2D(pool_size = (2, 2)))


# Step 3 - Flattening  - we are trying make it as one array
Classifier.add(Flatten())

# Step 4 - Full connection(Feed forward network) - Dense layer, 128- nuerons , nuerons can be changeable
Classifier.add(Dense(units = 128, activation = 'relu'))

Classifier.add(Dense(units = 1, activation = 'sigmoid'))

# Compiling the CNN
Classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])


# Part 2 - Fitting the CNN to the images

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,shear_range = 0.2,zoom_range = 0.2,horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('C:\\Users\\z014413\\Desktop\\Ramesh\\Project\\Image_classification\\weather_dataset',
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')

test_set = test_datagen.flow_from_directory('C:\\Users\\z014413\\Desktop\\Ramesh\\Project\\Image_classification\\weather_dataset',
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = None)

Classifier.fit_generator(training_set,
                         steps_per_epoch = 8000,
                         epochs = 2,
                         validation_data = test_set,
                         validation_steps = 2000)

import numpy as np
from keras.preprocessing import image
test_image = image.load_img('C:\\Users\\z014413\\Desktop\\pexels-photo-414659.jpg', target_size = (64, 64))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = Classifier.predict(test_image)
training_set.class_indices
if result[0][0] == 1:
    prediction = 'cloudy'
    print(prediction)
elif result[0][0]== 2:
    prediction = 'Rainy'
    print(prediction)
elif result[0][0] == 3:
    prediction = 'Shiny'
    print(prediction)
else:
    prediction = 'Sunrise'
    print(prediction)

