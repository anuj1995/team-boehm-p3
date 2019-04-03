# team-boehm-p3
## neuron finding 
## Member 
* Anuj Panchmia  
* Lei Xian  
* Mohammadreza Iman   
## Outline  
We did a NMF(non-negative matrix factorization) cluster algorithm to detect neurons in each sample in the test dataset. Each input sample in our model has thounds of images. The output is a json file contains coordinates of neurons. 

## Data
Below are the dimentions for 9 test dataset.  
  
(3000, 512, 512)  
(3000, 512, 512)  
(2250, 512, 512)  
(5000, 512, 512)  
(8000, 512, 512)  
(8000, 512, 512)  
(2250, 498, 467)  
(3000, 512, 512)  
(3000, 512, 512)  
  

## Evaluation
To evaluate our results we use five methods: 1. Recall, 2. Precision, 3. Combined (2 ∗ (recall ∗ precision)/(recall + precision)), 4. Inclusion (Number of intersecting pixels divided by the number of total pixels in the ground-truth regions) 5. Exclusion(Number of intersecting pixels divided by the number of total pixels in your regions).   
After trying different parameters, the highest accuracy we got is 2.99994 from NMF for overall test dataset.
 
## NMF 
1. Use thunder library and import that in your code.
2. Load the testing dataset.
3. Create the algorithm with various parameters.
4. Fit the model in our algorithm.
5. Transform and merge the overlapping coordinates.
6. Save the output in desired json format.


## Complie  
In GCP:
  * python3.5 remove_outlier.py --test 'test dataset dir' --save_path 'output dir'
  * python3.5 nmf.py -d 'test dataset dir' -o 'output dir'  
  
## Built with
* GCP
* python 3.5

## Reffernece

* [Freeman-lab](https://gist.github.com/freeman-lab/330183fdb0ea7f4103deddc9fae18113).
* [Opencv](https://docs.opencv.org)


