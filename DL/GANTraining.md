# Problems
1- dimension of image in D & G
2- Language
3- Format
4- alpha 

section -2

1- model_inputs - 
   passed - simple method signature with passing null or different data types as arguments

2- descriminator -

  Required: This is a good start however I have a few suggestions for improvement :
  `activation function for hidden layers :` should use Leaky ReLU as the activation function for the convolution layers which helps gradient to flow through entire architecture.
  `batch normalization:` should use batch normalization which stabilizes GAN training provided no batch normalization on `first layer`.

3- generator-

  Suggestion: I would suggest you to go through [this paper](https://arxiv.org/abs/1606.03498) for improving GAN training.
  Required:  :
  `activation function for hidden layers :` should use Leaky ReLU as the activation function for the convolution layers which helps to alleviate the problem of sparse gradients.
  `batch normalization:` should use batch normalization which stabilizes GAN training provided no batch normalization on `last layer`.


  4-model_loss

    Well Done !!! However, you could have used one-sided label smoothing as discussed in this paper[link].
  
  5- model_ops -
  
  6- training -
  
  7- hyperparameters -
  
  8- model output -
