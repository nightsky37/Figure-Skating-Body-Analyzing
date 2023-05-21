# Figure-Skating-Action-Analyzing
### This is our junior independent study in NCU CSIE 


![image](https://user-images.githubusercontent.com/38932681/167997038-ed6f6b3c-67bb-498a-a08b-73f4654551e1.png)

* Dataset  
  * Our dataset consists of 400 jump clips of 2018 and 2019 international figure skating competitions.  
  * There are 6 kinds of figure skating jumps such as Axel, Flip, Salchow, Lutz, Toeloop, Loop in our dataset.  

* Model  
  * We use LSTM architecture to analyze our dataset.
  * The LSTM code is referenced from : https://github.com/SBoyNumber1/LSTM-video-classification

* Body skeleton
  * OpenPose : https://github.com/CMU-Perceptual-Computing-Lab/openpose

* GUI 
  * We built our GUI by PyQt5.  
  * Uploading jump clips to analyze. 
  * Saving analyzed clips to related category.
  * We have audio guide(Mandarin) corresponding to each jump.
