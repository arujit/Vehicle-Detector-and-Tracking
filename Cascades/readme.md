# CASCADES

## Haar like Cascades -
Haar-like features are digital image features used in object detection. They owe their name to their intuitive similarity with Haar wavelets and were used in the first real-time object detector.
They use sliding windows to get features and train upon them.Haar Cascades are comparetively slower with respect to LBP features and take a lot of time to train.But they are way more accurate than LBP features as they use floating numbers for all the calculations part.

## LBP Cascades - 
Local Binary Pattern (LBP) is a simple yet very efficient texture operator which labels the pixels of an image by thresholding the neighborhood of each pixel and considers the result as a binary number. Due to its discriminative power and computational simplicity, LBP texture operator has become a popular approach in various applications.

## Cascade Training
### Opencv Provides a simple traincascades modules that is used in our training of Haar and LBP Cascades.

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
