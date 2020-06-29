import tensorflow as tf
import numpy as np

class DenseSnakeModel(tf.keras.Model):
  def __init__(self, width, height):
    super(DenseSnakeModel, self).__init__()
    self.dense1 = tf.keras.layers.Dense(width*height*2, activation=tf.nn.sigmoid)
    self.dense2 = tf.keras.layers.Dense(width*height, activation=tf.nn.sigmoid)
    self.dense3 = tf.keras.layers.Dense(4, activation=tf.nn.sigmoid)
    self.dropout = tf.keras.layers.Dropout(0.5)

  def call(self, inputs, training=False):
    x = self.dense1(inputs)
    x = self.dense2(x)
    if training:
      x = self.dropout(x, training=training)
    return self.dense3(x)

model = DenseSnakeModel(10,10)
model.compile(loss=tf.keras.losses.MeanSquaredError(),
              optimizer=tf.keras.optimizers.Adadelta(),
              metrics=['mean_squared_error'])

model.fit(x=np.ones((100000,400), int), 
          y=np.ones((100000,4), int), 
          epochs=3,
          batch_size=64,
          verbose=1,
          validation_split=0.0,
          validation_data=None,
          shuffle=True,
          class_weight=None)

model.summary()
model.save('models')
print("made it")