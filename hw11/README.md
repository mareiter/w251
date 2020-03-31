# Homework 11 -- More fun with OpenAI Gym!

## Configuration 1

For the first attempt I used the "base" configuration provided in the assignment. In all, Configuration 1 took an estimated 12 hours to complete, and yielded the following results:

At step  50000  
reward:  -3.5618822310845246  
total rewards  211.26489119530189  
loss: 169.1214 - accuracy: 0.0000e+00
Total successes are:  73  

Note: Running the docker build and docker run scripts provided executes properly, however, after 3,000 steps I started to experience low memory issues on the Jetson Tx2 and the training process was very slow.

## Configuration 2

After conducting some research, for the second configuration I chose to apply Nadam as the optimizer as a variation of adam. Nadam applies a Nesterov momentum term to the stochastic gradient descent (SGD) model. The result is a more 'efficient' adjustment to the learning rate that has shown to be more accurate than Adam alone (https://towardsdatascience.com/adam-latest-trends-in-deep-learning-optimization-6be9a291375c). Interestingly, this model seemed to improve upon Configuration 1 in terms of loss, however it did not result in more successful landings overall with just 46.

At step  50000  
reward:  -3.9854708528737985  
total rewards  -147.0776759120238  
loss: 133.8880 - accuracy: 0.0000e+00  
Total successes are:  46  

## Configuration 3

