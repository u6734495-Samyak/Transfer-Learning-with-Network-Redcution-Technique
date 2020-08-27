CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Installation
 * Confugration
 * Author

INTRODUCTION
------------
The goal of this study was to  experiment with the network reduction technique based on distinctiveness. We implemented the technique on a simple feed-forward neural network that dealt with the summarized version of the images and extended our implementation to deep learning that dealt with actual images . Our findings showed us that using deep learning and transfer learning to detect faces-emotion had a higher performance measure than using the summarized version .In addition to this, we experimented with the number of hidden neurons and our research showed us that overall the pruning technique  was useful to an extent in removing undesirable and redundant neurons and increasing the performance of our model with a large number of hidden neurons.But on the other hand when the number of hidden neurons are small the pruning had a negative effect on the performance measure.


REQUIREMENTS
------------
MTCNN pyhton package
Torchvision
all other packages are imported in the code


INSTALLATION
------------

For installing MTCNN-
open Command prompt and type - 
	!pip3 install mtcnn(if python3 )
	!pip install mtcnn (for pyhton2)
For installing torchvision-
open Command prompt and type - 
	!pip3 install torchvision(if python3 )
	!pip install torchvision (for pyhton2)
CONFIGURATION
-------------
	1.First we have place the folder containing images namely "Subset For Assignment SFEW" in this folder.(Since the large amount of space the folder requires , we have to download the SFEW dataset that contains images which can be easy to find online.)
	2.Run the code Face_detector.py for creating a new folder"cropped_SFEW" that is the output of the face detector
	3.Run the code NN_2.py to seee the results.
 
Configurable parameters:
 * For generating results with different pre trained models, base_model has to be changed
   uncomment the code for which of the pre trained models u want to train. 
 * Change the number in the self.classifier (input number) to that of the convolved feature of the pre trained model.
 * For runing my own implementation of CNN model comment all the code for the pre-trained model and uncomment
   all the code below it for the NET class.

AUTHOR
-----------

 * Samyak Jain

Supporting organization:

 * AUSTRALIAN NATIONAL UNIVERSITY
