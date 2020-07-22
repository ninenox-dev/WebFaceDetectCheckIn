
## Web Flask Face Detection Check In.


![Alt Text](https://i.ibb.co/swWT9y8/Screen-Shot-2563-07-22-at-12-11-52.png)


### Description

1. Insert your model in project.
2. Change your model : file camera.py line 33 -> demo_clf = load('ann-age-gender-v1.ml')  # Your model for detect your face.

### Credits
Most of the code credits to Miguel Grinberg, except that I made a small tweak. Thanks!
http://blog.miguelgrinberg.com/post/video-streaming-with-flask

### Usage
1. Install Python dependencies: cv2, flask. (wish that pip install works like a charm)
2. Run "python main.py".
3. Navigate the browser to the local webpage.
