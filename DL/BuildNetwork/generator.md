## Build the Neural Network
### The function generator is implemented correctly.

* Suggestion:
  * `activation function for hidden layers:`  To improve the performance of the model to generate realistic faces, you should use Leaky ReLU as the activation function for the convolution layers which avoids sparse gradients problems too.
  * You can implement it in the same way you have implemented for discriminator function.
  * Remember , it is recommended that there should not be any batch normalization on last layer.
  * I would also suggest you to go through [this paper](https://arxiv.org/abs/1606.03498) for improving GAN training.

* Required:
    * `activation function for hidden layers :` should use Leaky ReLU as the activation function for the convolution layers which avoids sparse gradients problems too.
       Hint- use a positive constant close to 0 for leaky ReLu.
    * `batch normalization:` to stabilizes GAN training `tf.layers.batch_normalization` should be used for all layers, provided no batch normalization on last layer.
    * The function should also return the generated 28 x 28 x out_channel_dim images
    * Suggestion: I would suggest you to go through [this paper](https://arxiv.org/abs/1606.03498) for improving GAN training.

* I would suggest you to go through [this paper](https://arxiv.org/abs/1606.03498) for improving GAN training.