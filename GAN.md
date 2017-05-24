## Introduction
Used for Image to Image translation.
Simulated training set for other machine learning models.
Imitation learning.

## How GAN works
GANs are a kind of generative model.

## For a simple task to  generate 28*28 image MNIST

* For fully connected arch - metrics * wt metrics - no CONV no RNN
* Both generator and description have at least 1 hidden layer
* Hidden units - activation function - leaky reLu - the gradient can flow through entire architecture
* Avoid Sparse Gradients: ReLU, MaxPool
* Output - hyperbolic tangent activation function
* For other gan - output - probability - sigmoid
* Adom is recommended for optimizer - DC GAN arch - fb
* To regularize normal classifier levels to be 0.9 for 1 and 0 (GAN specific) to avoid extreme prediction
* Batch normalization is recommended to be used at every layer except output layer of generator and input layer of discriminator.


## For large Image to generate
* use CONV


##  Meets Specifications / Required changes 
>Well Done !!! Congratulations on completing the project.
In order to gain more intuition about GANs in general, I would suggest you take a look at this blog post. Also, if you want to gain intuition about the convolution and transpose convolution arithmetic, I would suggest referring to this paper.
All the best. Keep learning.


## Required Files and Tests

* ### The project submission contains the project notebook, called “dlnd_face_generation.ipynb”.
* ### All the unit tests in project have passed.


## Build the Neural Network

* ### The function model_inputs is implemented correctly.
>model_inputs has correctly defined the placeholder tensors for real input, z input and the learning rate.

* ### The function discriminator is implemented correctly.
>Well Done !!! The function discriminator is implemented correctly. Below are the good points of the architecture chosen:
You have used Leaky ReLU as the activation function for the convolution layers which helps with the gradient flow. It helps alleviate the problem of sparse gradients.
You are using same size filters across all the layers.
You have used batch normalization which stabilizes GAN training.
You have used Sigmoid as the activation function for the output layer which produces probability-like values between 0 and 1.
I would like you to think about one question. Why did you not use any pooling layer here as used in normal convolutional nets?

* ### The function generator is implemented correctly.
>Good Job implementing the generator. However, I would suggest not using batch normalization after the first fully connected layer.

* ### The function model_loss is implemented correctly.
>Well Done !!! However, you could have used one-sided label smoothing as discussed in this paper.

* ### The function model_opt is implemented correctly.
>Good Job !!!

## Neural Network Training

* ### The function train is implemented correctly.

>It should build the model using model_inputs, model_loss, and model_opt.
It should show output of the generator using the show_generator_output function
Well Done !!! The train function has been implemented correctly. However, I would suggest removing code that is not being used. eg. saver object is not being used anywhere. Similarly, The generated samples are neither shown nor are they saved to disk for later use. So, there is no point in generating them.

* ### The parameters are set reasonable numbers.
>The hyperparameters are optimal. Well Done !!!
* ### The project generates realistic faces. It should be obvious that images generated look like faces.
>The model generates faces. Good Job !!!
 