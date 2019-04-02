## Member 
* Anuj   
* Lei Xian  
* Mohammadreza Iman   
## Outline  
We did a NMF(non-negative matrix factorization) cluster algorithm to detect neurons in each sample in the test dataset. Each input sample in our model has thounds of images. The output is a json file contains coordinates of neurons. Below are the dimentions for our test samples.  
  
(3000, 512, 512)  
(3000, 512, 512)  
(2250, 512, 512)  
(5000, 512, 512)  
(8000, 512, 512)  
(8000, 512, 512)  
(2250, 498, 467)  
(3000, 512, 512)  
(3000, 512, 512)  
  
To evaluate our results we use five methods: 1. Recall, 2. Precision, 3. Combined (2 ∗ (recall ∗ precision)/(recall + precision)), 4. Inclusion (Number of intersecting pixels divided by the number of total pixels in the ground-truth regions) 5. Exclusion(Number of intersecting pixels divided by the number of total pixels in your regions).   
After trying different parameters, the highest accuracy we got is 2.99994 from NMF for overall test dataset.
 
## Prerequisites
python 3.5 or higher
anaconda
pip install thunder-extraction  

## complie  
We setup everything in GCP.     
python3.5 nmf.py -d 'test dataset dir' -o 'output dir'  

