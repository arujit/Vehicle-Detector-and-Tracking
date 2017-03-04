# CASCADES

## Haar like Cascades -
Haar-like features are digital image features used in object detection. They owe their name to their intuitive similarity with Haar wavelets and were used in the first real-time object detector.
They use sliding windows to get features and train upon them.Haar Cascades are comparetively slower with respect to LBP features and take a lot of time to train.But they are way more accurate than LBP features as they use floating numbers for all the calculations part.

## LBP Cascades - 
Local Binary Pattern (LBP) is a simple yet very efficient texture operator which labels the pixels of an image by thresholding the neighborhood of each pixel and considers the result as a binary number. Due to its discriminative power and computational simplicity, LBP texture operator has become a popular approach in various applications.

## Cascade Training
### Opencv Provides a simple traincascade modules that is used in our training of Haar and LBP Cascades.

```
  opencv_traincascade 
  -data <cascade_dir_name> 
  -vec <vec_file_name> 
  -bg <background_file_name> 
  -numPos <number_of_positive_samples> 
  -numNeg <number_of_negative_samples>  
  -numStages <number_of_stages > 
  -precalcValBufSize <precalculated_vals_buffer_size_in_Mb > 
  -precalcIdxBufSize <precalculated_idxs_buffer_size_in_Mb > 
  -featureType <{HAAR(default), LBP, HOG}> 
  -w <sampleWidth > 
  -h <sampleHeight > 
  -minHitRate <min_hit_rate> > 
  -maxFalseAlarmRate <max_false_alarm_rate > 
  -maxDepth <max_depth_of_weak_tree >
 
```
## Our Cascades
### 1.Haar 1000 - 
Trained Haar Cascades for 1000 p and 1000 n images.
  #### Positive & Negative images - 
  1000 cropped car images of from our dataset and 1000 empty road images from our negative image dataset
  size of sliding window is 50*35
  #### issue - 
  Not so good detection rate and poor false alarm performance.
### 2.Haar 2000 - 
Trained Haar Cascades for 2000 p and 3800 n images.
  #### Positive & Negative images - 
  2000 cropped car images of from our dataset and 2500 empty road images and 1000 trees,sky images from imagenet       dataset.
  size of sliding window is 40*30
  #### issue - 
  good detection rate and improved false alarm performance but problems detecting smaller cars .
  
### 3.LBP 2000 - 
Trained LBP Cascades for 1000 p and 3800 n images.
  #### Positive & Negative images - 
  2000 cropped car images of from our dataset and 2500 empty road images and 1300 trees,sky images from imagenet       dataset.
  size of sliding window is 40*30
  #### issue - 
  worse detection rate and false alarm performance than Haar. Problems in detecting smaller cars .
  
### 4.LBP 12000 - 
Trained LBP Cascades for 12000 p and 26000 n images.
  #### Positive & Negative images - 
  2000 cropped car images and 10000 other car images from our dataset . 14000 empty road images and 12000 trees,sky images,Padestrian,buildings,traffic images from imagenet and google images dataset.
  size of sliding window is 25*25
  #### issue - 
  best detection rate and false alarm performance.

### 5.Haar 14000 - 
Trained Haar Cascades for 14000 p and 26000 n images.
  #### Positive & Negative images - 
  2000 cropped car images and 12000 other car images from our dataset . 14000 empty road images and 12000 trees,sky images,Padestrian,buildings,traffic images from imagenet and google images dataset.
  size of sliding window is 25*25
  #### issue - 
  worst performance and we have find out a way to improve the performance of this detection.
