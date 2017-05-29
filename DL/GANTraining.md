# Problems
1- Dimension of image in D & G
2- Language
3- Format
4- Alpha

## Review Note

  This is a good start. :thumbsup: You submission shows that you have a good understanding of GAN. Please check my comments on how to further improve your project and the performance of your model to generate realistic faces. To get some more intuition about GANs check this blog post . All the best for your next submission.


## Required Files and Tests
  1- The project submission contains the project notebook, called “dlnd_face_generation.ipynb”.
  2- All the unit tests in project have passed.

## Build the Neural Network

  1- The function model_inputs is implemented correctly.
   Good job !!!, function model_inputs has correctly defined the placeholder tensors for real input,z input and the learning rate.
   Perfect !!!, function `model_inputs` has perfectly implemented the placeholder tensors for `real input`,`z input `and the `learning rate`.


  2- The function discriminator is implemented correctly.

  Required: This is a good start however I have a few suggestions for improvement :

  activation function for convolution layers : the only way by which generator can learn is by receiving gradient from discriminator, hence gradient to flow through entire architecture , it is recommended to use Leaky ReLU as the activation function for the convolution layers.
  Hint- use a positive constant close to 0 for leaky ReLu.

  batch normalization: to stabilizes GAN training tf.layers.batch_normalization should be used for all layers, provided no batch normalization on first layer.

  Required: This is a good start however I have a few suggestions for improvement :
  `activation function for hidden layers :` should use Leaky ReLU as the activation function for the convolution layers which helps gradient to flow through entire architecture.
  `batch normalization:` should use batch normalization which stabilizes GAN training provided no batch normalization on `first layer`.

  Well Done !!! The function discriminator is implemented correctly. Following are the good points of the architecture chosen:
`activation function for convolution layers :` the only way by which generator can learn is by receiving gradient from discriminator, hence gradient to flow through entire architecture , it is recommended to use Leaky ReLU as the activation function for the convolution layers and you have implemented it correctly.
`filters:`  use of same size filters for all the layers.
`normalization:` use of  batch normalization which stabilizes GANs training.
`activation function:` use of  Sigmoid  function for the output layer to produce values between 0 and 1 (probability values).

  3- The function generator is implemented correctly.

  Required:
  activation function for hidden layers : should use Leaky ReLU as the activation function for the convolution layers which avoids sparse gradients problems too.
  Hint- use a positive constant close to 0 for leaky ReLu.
  batch normalization: to stabilizes GAN training tf.layers.batch_normalization should be used for all layers, provided no batch normalization on last layer.
  The function should also return the generated 28 x 28 x out_channel_dim images

  Suggestion: I would suggest you to go through [this paper](https://arxiv.org/abs/1606.03498) for improving GAN training.
  Required:  :
  `activation function for hidden layers :` should use Leaky ReLU as the activation function for the convolution layers which helps to alleviate the problem of sparse gradients.
  `batch normalization:` should use batch normalization which stabilizes GAN training provided no batch normalization on `last layer`.


  4- The function model_loss is implemented correctly.
    Well Done !!! Check out this openAI paper for details on One-sided label smoothing.
    Well Done !!! However, you could have used one-sided label smoothing as discussed in this paper[link].

  5- The function model_opt is implemented correctly.
    Awesome !! AdamOptimizer is recommended optimizer which was also used in DC GAN arch project, additionally you can make sure that all generator updates are computed before running optimizer by control_dependencies

## Neural Network Training    

  6- The function train is implemented correctly.

    It should build the model using model_inputs, model_loss, and model_opt.
    It should show output of the generator using the show_generator_output function
    Required: Most parts of the function is implemented perfectly however to improve training of the model I would suggest -
    batch_images : Increasing batch_images can improve in optimizing d_opt.
    I would suggest you to think about tnumpy.random.random and numpy.random.uniform for using it as z_input.

  7- The parameters are set reasonable numbers.
    Required: Choosing reasonable parameters is always tough for model. Try adjusting following parameters to produce realistic results -
    batch_size : Increase it to a range of 64 to 128.
    learning_rate : Decrease it to a range of 0.0003 to 0.0002
    beta1 : Slightly decrease the value around 0.4 to 0.5

  8- The project generates realistic faces. It should be obvious that images generated look like faces.
