# OpenCv Cascade Training


## How To Train

### Getting Dataset Right
First it is very important to get proper dataset for our traing purpose

#### Positive Images
Now we need to either take photos of the object we want to detect that is car sample images. We got around 16000 positive images of them which we got from either from scraping internet or from some pre-defined dataset. It’s also important that they should differ in lighting and background conditions.
Once we have the pictures, we need to crop them so that only our desired object is visible.Proper Background extraction,cropping and finding bounding regions also important. 

#### Negative Images
Now we need the negative images, the ones that shouldn't be detected. Negative images play crucial role in higher efficiency classifiers.Negative images should higher in number than the positive images.In our case we are able to gather around 29000 negative images.
Our Negative image dataset basically contain images of empty roads,road signs,trees,sky,pedestrians,houses and related places etc.Proper Positive and Negative ratio is also important. Most effective ratio would be like 1:2.

### Proper Processing Of Dataset

#### Per-Processing Task
For both LBP and Haar Classifiers it is also important to do the whole image processing tasks.As LBP and Haar both gradient based Classifiers it is crucial to convert all the images to Grayscale.For a faster Training all postive and negative images shoulb be resized to a default size. 
For our Cascades we are usining Grayscale positive images of size 100 to 70 pixels and negative samples of size 150 to 120 pixels.All the basic image processing tasks is done by positive.py and negative.py scripts.

```
posive.py/negative.py [Image dataset folder] [Processed Image destination folder]
```

#### Sample file generation
Opencv does not take images directly during training process. Rather than it takes some sample .dat type of file with images information in it.
For Positive images this is in the form of
```
~/[Path to a perticular image sample] [no of positive samples in the image] [Co-oirdinate of each samples]
```
And For Negative images 
```
~/[Path to a perticular image sample] 
```
Creation of both the sample files is also done by postive.py and negative.py scripts. Positive sample file is generated as cars.dat and negative back-ground samples as neg.dat

### Vector File Creation
After Positive samples generation we make a positive vector file which is provided directly during the opencv haar training procedure.It takes some parameters like width and height of sliding window,back ground file ,number of positives and deviations.
```
-vec <vec_file_name>

Name of the output file containing the positive samples for training.

-img <image_file_name>

Source object image 

-bg <background_file_name>

Background description file; contains a list of images which are used as a background for randomly distorted versions of the object.

-num <number_of_samples>

Number of positive samples to generate.

-w <sample_width>

Width (in pixels) of the output samples.

-h <sample_height>

Height (in pixels) of the output samples.

-pngoutput

With this option switched on opencv_createsamples tool generates a collection of PNG samples and a number of associated annotation files, instead of a single vec file.
```

### Final Training
Finally we progress to the final traing appropriate parameters

```
  opencv_traincascade 
  -data <cascade_dir_name> 
  -vec <vec_file_name> 
  -bg <background_file_name> 
  -numPos <number_of_positive_samples> =16000 
  -numNeg <number_of_negative_samples> =29000
  -numStages <number_of_stages > =20
  -precalcValBufSize <precalculated_vals_buffer_size_in_Mb > =8500 
  -precalcIdxBufSize <precalculated_idxs_buffer_size_in_Mb > =16500
  -featureType <{HAAR(default), LBP, HOG}>  =LBP
  -w <sampleWidth > =25
  -h <sampleHeight > =25
  -minHitRate <min_hit_rate> =0.999 
  -maxFalseAlarmRate <max_false_alarm_rate > =0.45 
  -maxDepth <max_depth_of_weak_tree > =1
```





