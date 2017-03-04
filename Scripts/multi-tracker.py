import cv2
import sys


def track():
    print "teacker initialization"
    return cv2.MultiTracker("MIL")


if __name__ == '__main__' :

    carCascade = cv2.CascadeClassifier("Cascades/LBP_cascade.xml")
    
    # Set up tracker.
    # Instead of MIL, you can also use
    # BOOSTING, KCF, TLD, MEDIANFLOW or GOTURN
     
    #tracker = cv2.Tracker_create("MIL")

    #tracker = cv2.MultiTracker("KCF")
    # Read video
    video = cv2.VideoCapture("videos/road.mp4")
 
    # Exit if video not opened.
    if not video.isOpened():
        print "Could not open video"
        sys.exit()
 
    # Read first frame.
    ok, frame = video.read()
    if not ok:
        print 'Cannot read video file'
        sys.exit()

    frames = 0
        
        
    
    # Uncomment the line below to select a different bounding box
    #bbox = cv2.selectROI(frame, False)
 
    # Initialize tracker with first frame and bounding box
    #ok = tracker.init(frame, bbox)
    #ok = True
    #cars = []
    while True:
        # Read a new frame
        ok, frame = video.read()
        if not ok:
            break


        #print bbox
        if (frames % 3 == 0):
            cars = carCascade.detectMultiScale(
                frame,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            #bbox = cars
            """
            p1 = (int(bbox[0]),int(bbox[1]))
            p2 =  (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1,p2,(255,0,0))
            # Update tracker
            """
            for (x, y, w, h) in cars:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            bbox = tuple(tuple(car) for car in cars)

            print bbox
            #bbox = tuple(cars[0])
            #ok = tracker.init(frame,bbox)

            print "I am detecting"
            print len(bbox)
            #tracker = cv2.MultiTracker("KCF")
            tracker = track()
            print type(bbox)
            k =((311, 178, 67, 67), (56, 207, 66, 66))

            print k
            print type(k)
            if len(bbox) == 1:
                ok = tracker.add(frame, bbox[0] )
                print bbox[0]
            elif len(bbox) > 1:

                
                print "good to come"
                ok = tracker.add(frame,bbox)

                
                #print bbox
            elif len(cars) == 0:
                print "no frames here..."
                continue
              
        else :
            print "hello to else"
            #print cars
            """
            for car in cars:
                print tuple(car)
                ok, bbox = tracker.update(frame)
               
                #print bbox
            # Draw bounding box
            """
            ok,boxes = tracker.update(frame)

            for box in boxes:
                if ok:
                    p1 = (int(box[0]), int(box[1]))
                    p2 = (int(box[0] + box[2]), int(box[1] + box[3]))
                    cv2.rectangle(frame, p1, p2, (0,0,255),2)
                    print "I am tracking"

                    """
            if ok:
                p1 = (int(bbox[0]), int(bbox[1]))
                p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
                cv2.rectangle(frame, p1, p2, (0,0,255))
                print "I am tracking" """
        # Display result
        #print cars
        cv2.imshow("Tracking", frame)
 
        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27 : break
        frames = frames+1
Contact GitHub API Training Shop Blog About
© 2017 GitHub, Inc. Terms Privacy Security Status Help
