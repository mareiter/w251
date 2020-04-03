# Homework 11 -- More fun with OpenAI Gym!

## Configuration 1

For the first attempt I used the "base" configuration provided in the assignment. After the training threshold of 3,000 steps there was a significant reduction in performance of the model, generating low-memory warnings. Furthermore, the model performed progressively slower throughout the process as after each 1,000 steps the model was retrained. In all, Configuration 1 took an estimated 12 hours to complete, yielding the following results:

At step  50000  
loss: 169.121  
accuracy: 0.0000e+00  
Total successes are:  73

## Configuration 2

For the second attempt, I wanted to see if I could speed up the process to evaluate the model quicker. Since the model seemed to slow down significantly after the training threshold was met, I increased the threshold to 5,000 and reduced the total iterations by half to 25,000. I also changed the optimizer from adam to adamax and increased the batch size from 20 to 30. While the changes had the desired result, finishing in a fraction of the time, the model resulted in just 29 successful landings.

At step  25000  
loss: 238.6118  
accuracy: 0.0000e+00  
Total successes are:  29

## Configuration 3

After conducting some research, for the third configuration I chose to apply Nadam as the optimizer as a variation of adam. Nadam applies a Nesterov momentum term to the stochastic gradient descent (SGD) model. The result is a more 'efficient' adjustment to the learning rate that has shown to be more accurate than Adam alone (https://towardsdatascience.com/adam-latest-trends-in-deep-learning-optimization-6be9a291375c). Interestingly, this model seemed to improve upon Configuration 1 in terms of loss, however it did not result in more successful landings overall with just 46.

At step  50000  
loss: 133.8880  
accuracy: 0.0000e+00  
Total successes are:  46

## Configuration 4

For the fourth and final attempt, I decided to increase to 75,000 iterations implementing adamax for the optimizer.

At step 65000  
loss: 137.7095  
accuracy: 0.0000e+00  
Total successes are:  47

## Conclusions

Due to time limitations in running the model, I was not able to attempt a wider variety of configurations, especially given the number of parameters and potential adjustments. However, I would have explored more combinations of loss, metrics, and the number of layers.

## Cloud Object Storage

https://s3.us-south.cloud-object-storage.appdomain.cloud/mareiter-cos-hw11/frame48000.mp4  
https://s3.us-south.cloud-object-storage.appdomain.cloud/mareiter-cos-hw11/frame49000.mp4  
https://s3.us-south.cloud-object-storage.appdomain.cloud/mareiter-cos-hw11/frame50000.mp4
