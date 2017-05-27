## Introduction
Used for Image to Image translation.
Used for simulating training set for other machine learning models.
Imitation learning.

## How GAN works
GANs are a kind of generative model.
GANs are different as they run 2 optimization algorithms at a time (G & D).

## For a simple task to  generate 28*28 px image on MNIST data

* For fully connected arch - all interaction b/w layers consist of  metrics multiplication by  weight metrics - no CONV no RNN required
* Both generator and description should have at least 1 hidden layer so that they can represent any probability distribution
* for Hidden units - recommended activation function is leaky reLu, so that the gradient can flow through entire architecture (imp)
  the only way by which generator can learn is by receiving gradient from descriminator
* Avoid Sparse Gradients: ReLU, MaxPool
* Output - hyperbolic tangent activation function (-1 to 1)
* For other gan - output - probability - sigmoid
* we define loss for G & D and then we run optimizer for both G & D to minimize the loss
* AdamOptimizer is recommended for optimizer - used DC GAN arch project developed by fb

* Batch normalization is recommended to be used at every layer except output layer of generator and input layer of discriminator.
* For generator loss we use another cross entropy loss with labels flipped -to  minimize cross entropy

## Mistakes people do in GAN game
* Own implementation of loss functions
* people forget to use Numerically stable version of cross entropy where loss is computed using logits
  levels to be 0.9 for 1 and 0 for 0. (This is GAN specific approach to avoid extreme prediction and label smoothing strategy used to regularize normal classifier)
	this helps discriminator to generalized better and avoid making extreme predictions.

## scaling up GAN for large image
* we use convolutional Networks , they replace some of the matrix multipliers in normal nural networks with convolutions
* we can replace matrix multiplier in GAN with convolutions

* for inputs to generator we use random vector z, mini batch of this vector form matrix, convolution expects many batch to be 4d tensors for input z (axis for feature maps and width and height axis) to get the random input in this format we use reshape op near the start of generator.

* usually convolution net change the shape of feature map as we move through the Network, the input to convolution net is very tall and wide image with just 3 feature maps (the red blue and green) , after applying pooling several times, we end up with very short and narrow feature maps, thats all happens when we use classifier convolutional net

* when we use a convolutional net as generator net, most researchers think that we need to do opposite, we want to start of with small feature map and expand it to wide and tall image
 to do this we need to have an op that can increase the width and height of feature maps at every layer, so by using convolution transpose ops with stride >1 (this means when we move by 1 px in input map , we move by >1 px in output map)

 * Batch normalization is recommended to be used at every layer except output layer of generator and input layer of discriminator
   Normalization strategy - improved technique for training GAN - openAI paper - []




* Metrics multiplying with normal metrics multiplier with convolution
* CONV expects many batch to be 4d tensors for input z
* To get random input, we have to reshape ops for start of generator
* CONV as generator - need ops - that can improve height and width - CONV transpose ops with stride >1
* CONV transpose, batch normalization, AdamOptimizer, cross entropy with label smoothing works really well in practice


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

	* Real input images placeholder with rank 4 using image_width, image_height, and image_channels.
	* Z input placeholder with rank 2 using z_dim.
	* Learning rate placeholder with rank 0.
	* Return the placeholders in the following the tuple (tensor of real input images, tensor of z data)

* ### The function discriminator is implemented correctly.
>Well Done !!! The function discriminator is implemented correctly. Below are the good points of the architecture chosen:
You have used Leaky ReLU as the activation function for the convolution layers which helps with the gradient flow. It helps alleviate the problem of sparse gradients.
You are using same size filters across all the layers.
You have used batch normalization which stabilizes GAN training.
You have used Sigmoid as the activation function for the output layer which produces probability-like values between 0 and 1.
I would like you to think about one question. Why did you not use any pooling layer here as used in normal convolutional nets?

	* tf.variable_scope with a scope name of "discriminator" to allow the variables to be reused.
	* No batch normalization on first layer.
	* stride > 1
	* padding to be 'same'
	* activation function to be sigmoid for output
	* The function should return a tuple of (tensor output of the generator, tensor logits of the generator).


* ### The function generator is implemented correctly.
>Good Job implementing the generator. However, I would suggest not using batch normalization after the first fully connected layer.

	* tf.variable_scope with a scope name of "generator" to allow the variables to be reused.
	* stride >=1
	* padding === ('same' || 'valid')
	* No batch normalization in last layer.
	* recommended activation function to be tanh for output.
	* The function should return the generated 28 x 28 x out_channel_dim images.

* ### The function model_loss is implemented correctly.
>Well Done !!! However, you could have used one-sided label smoothing as discussed in this paper.

	* Use of functions:discriminator(images, reuse=False), generator(z, out_channel_dim, is_train=True)
	* The function should return a tuple of (discriminator loss, generator loss).

* ### The function model_opt is implemented correctly.
>Good Job !!!

	*  tf.trainable_variables to get all the trainable variables.
	*  Filter the variables with names that are in the discriminator and generator scope names.
	*  optimize loss using tf.GraphKeys.UPDATE_OPS .
	*  recommended AdamOptimizer for optimizing loss.
	*  The function should return a tuple of (discriminator training operation, generator training operation).

## Neural Network Training

* ### The function train is implemented correctly.
>It should build the model using model_inputs, model_loss, and model_opt.
It should show output of the generator using the show_generator_output function
Well Done !!! The train function has been implemented correctly. However, I would suggest removing code that is not being used. eg. saver object is not being used anywhere. Similarly, The generated samples are neither shown nor are they saved to disk for later use. So, there is no point in generating them.

	* Use of following functions : model_inputs(image_width, image_height, image_channels, z_dim),
		model_loss(input_real, input_z, out_channel_dim) , model_opt(d_loss, g_loss, learning_rate, beta1)
	* running optimizer and after each epoch printing loss values
	* Use of show_generator_output to show generator output while training after every 100 batches.


* ### The parameters are set reasonable numbers.
>The hyperparameters are optimal. Well Done !!!
64-100 - 0.0002- 0.4 && 128-100-0.002- 0.0001

* ### The project generates realistic faces. It should be obvious that images generated look like faces.
>The model generates faces. Good Job !!!
