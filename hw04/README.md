# Homework 4: DL 101
2. ConvnetJS MNIST Demo

In this lab, we will look at the processing of the MNIST data set using ConvnetJS. This demo uses this page: http://cs.stanford.edu/people/karpathy/convnetjs/demo/mnist.html The MNIST data set consists of 28x28 black and white images of hand written digits and the goal is to correctly classify them. Once you load the page, the network starts running and you can see the loss and predictions change in real time. Try the following:

- Name all the layers in the network, make sure you understand what they do.

**Layer 1:** Input Layer - The first layer of a neural network, the input layer declares the size of the input volume. In this case, the input volumes are images of 24x24x1 dimensions, corresponding to the out_sx, out_sy, and out_depth parameters respectively.

**Layer 2:** 1st Convolutional Layer - Convolutional layers map the features of an input image using a specified filter size (sx:5); number of filters (filters:8); amount by which the filter is applied to the input (stride:1); and padding to maintain spacial dimensions (pad:2). This layer also applies an nonlinear activation layer (in this case, ReLU) to avoid the vanishing gradient problem which can affect training of the model.

**Layer 3:** 1st Pooling Layer - The pooling layer generally follows the nonlinear activation layer. It down samples the feature maps output by the convolutional layers by taking either an average or a max of a grouping of features defined by size (sx) and stride (stride) parameters. to highlight the most important features. This has the effect of highlighting the most important features, thus reducing the feature space and making it more computationally effecient, and helping control for overfitting. In the given example, this layer also applies size (sx:2) and stride (stride:2) parameters.

**Layer 4:** 2nd Convolutional Layer - This layer performs the same general functionality as the first convolutional layer instance but, in this case, increases the number of filters to 16.

**Layer 5:** 2nd Pooling Layer - This layer performs the same general functionality as the first pooling layer instance but, in this case, increases the size and stride of the pooling "filter" to 3.

**Layer 6:** Loss Layer - The last layer of a neural network, the loss layer outputs probabilities that sum to 1 for a defined number of classes (num_classes). 

- Experiment with the number and size of filters in each layer. Does it improve the accuracy?



- Remove the pooling layers. Does it impact the accuracy?



- Add one more conv layer. Does it help with accuracy?



- Increase the batch size. What impact does it have?



- What is the best accuracy you can achieve? Are you over 99%? 99.5%
