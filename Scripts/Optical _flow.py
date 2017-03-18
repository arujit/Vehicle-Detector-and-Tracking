import numpy as np
import cv2
import itertools

cap = cv2.VideoCapture('videos/road.mp4')

# params for ShiTomasi corner detection
feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )

# Parameters for lucas kanade optical flow
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
color = np.random.randint(0,255,(100,3))
# Take first frame and find corners in it
ret, old_frame = cap.read()
oldg = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

def __predictBB( bb0, pt0, pt1):
    if not pt0:
        pt0 = pt1
    dx = []
    dy = []
    for p1, p2 in itertools.izip(pt0, pt1):
        dx.append(p2[0] - p1[0])
        dy.append(p2[1] - p1[1])
    if not dx or not dy:
        return bb0
    cen_dx = round(sum(dx) / len(dx)) / 2
    cen_dy = round(sum(dy) / len(dy)) / 2
    bb = [int(bb0[0] + cen_dx), int(bb0[1] + cen_dy), bb0[2], bb0[3]]
    if bb[0] <= 0:
        bb[0] = 10
    if bb[1] <= 0:
        bb[1] = 10
    return bb

carCascade = cv2.CascadeClassifier("Cascades/LBP_cascade.xml")
cars =  carCascade.detectMultiScale(
                old_frame,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
)
old_pts = None
print len(cars)
bb =None
if len(cars) >0:
    bb = cars[0]
    print bb
frame_conter = 0
while True:
    _,img = cap.read()

    if (frame_conter % 5 == 0):
        oldg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cars =  carCascade.detectMultiScale(
                img,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
)
        old_pts = None
        bb = None
        if len(cars)>0:
            bb = cars[0]
        print bb
        for (x, y, w, h) in cars:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        print cars
        # Display the resulting frame
        #cv2.imshow('Video', img)
    
        
    else :
        if (bb ==None):
            print "No Cars to be detected !!!"
            #continue
        else:
            img1 = img[bb[1]:bb[1] + bb[3], bb[0]:bb[0] + bb[2]]
            g = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            pt = cv2.goodFeaturesToTrack(g, **feature_params)
            print pt
            print "hello bro"
        
            if (frame_conter == 900):
                break
            if pt is None:
                print "Cann't track any features bro!!!"

            else:
                for i in xrange(len(pt)):
                    pt[i][0][0] = pt[i][0][0] + bb[0]
                    pt[i][0][1] = pt[i][0][1] + bb[1]
                newg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                p0 = np.float32(pt).reshape(-1, 1, 2)

                p1, st, err = cv2.calcOpticalFlowPyrLK(oldg, newg, p0, None, **lk_params)
                p0r, st, err = cv2.calcOpticalFlowPyrLK(newg, oldg, p1, None,
                                                    **lk_params)
                d = abs(p0 - p0r).reshape(-1, 2).max(-1)
                good = d < 1
                new_pts = []
                for pts, val in itertools.izip(p1, good):
                    if val:
                        new_pts.append([pts[0][0], pts[0][1]])
                        cv2.circle(img, (pts[0][0], pts[0][1]), 2, thickness=2,
                                   color=(255, 255, 0))

                bb = __predictBB(bb, old_pts, new_pts)
                print bb
                if bb[0] + bb[2] >= img.shape[1]:
                    bb[0] = img.shape[1] - bb[2] - 10
                if bb[1] + bb[3] >= img.shape[0]:
                    bb[1] = img.shape[0] - bb[3] - 10
                old_pts = new_pts
                oldg = newg
                cv2.rectangle(img, (bb[0], bb[1]),
                          (bb[0] + bb[2], bb[1] + bb[3]),
                              color=(255, 0, 0))
            #cv2.imshow("img", img)
            k = cv2.waitKey(30)
            if k == 27:
                cv2.destroyAllWindows()
                break

    cv2.imshow("img", img)
    frame_conter = frame_conter + 1
