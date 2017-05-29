## Build the Neural Network
### The function discriminator is implemented correctly.

* Well Done !!! The function discriminator is implemented correctly. Following are the good points of the architecture chosen:
  `activation function for convolution layers :` the only way by which generator can learn is by receiving gradient from discriminator, hence gradient to flow through entire architecture , it is recommended to use Leaky ReLU as the activation function for the convolution layers and *you have implemented it correctly*.
  `filters:`  use of same size filters for all the layers.
  `normalization:` use of  batch normalization to stabilize GAN training.
  `activation function:` use of  Sigmoid  function for the output layer to produce values between 0 and 1 (probability values).


* Required: This is a good start however I have a few suggestions for improvement :
  * `activation function for hidden layers :` should use Leaky ReLU as the activation function for the convolution layers which helps gradient to flow through entire architecture.
  * `activation function for convolution layers :` the only way by which generator can learn is by receiving gradient from discriminator, hence gradient to flow through entire architecture , it is        recommended to use Leaky ReLU as the activation function for the convolution layers.
  Hint- use a positive constant close to 0 for leaky ReLu.
  * `batch normalization:` should use batch normalization which stabilizes GAN training provided no batch normalization on `first layer`.
