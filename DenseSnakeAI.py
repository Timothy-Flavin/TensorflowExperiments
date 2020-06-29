import tensorflow as tf

class DenseSnakeModel(tf.keras.Model):
  def __init__(self, width, height):
    super(DenseSnakeModel, self).__init__()
    self.dense1 = tf.keras.layers.Dense(width*height, activation=tf.nn.relu)
    self.dense2 = tf.keras.layers.Dense(int(width*height/2), activation=tf.nn.sigmoid)
    self.dense3 = tf.keras.layers.Dense(4, activation=tf.nn.softmax)
  
  def call(self, inputs, training=False):
    x = self.dense1(inputs)
    x = self.dense2(x)
    if training:
      x = self.dropout(x, training=training)
    return self.dense3(x)

model = DenseSnakeModel(10,10)

print("made it")