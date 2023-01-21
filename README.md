# Smartathon_SDAIA_Theme_1

![ezgif com-gif-maker](https://user-images.githubusercontent.com/74447207/213848226-47d96eea-90b4-42b4-831f-91e9ca6dccb9.gif)

## Description

Visual Pollution detection project in KSA by SDAIA dataset.

## Getting Started

1. Getting the dataset.
2. Start annotating using [CVAT](https://github.com/openvinotoolkit/cvat) or [Lebelimg](https://github.com/heartexlabs/labelImg).
3. Train/test using YOLOv5 with S,M,L,X models on [Google Colab](https://app.box.com/s/z2c6p4yntzbm0pvr67ra0pwsz0ffjvm0).
4. Evaluate and visualize the trained model on the test data.
5. Measure the Mean Average Precision (mAP) and Intersection Over Union (IoU).
6. Inference/run the model/weights on new/unseen data.
7. Convert the best.pt model into ONNX format to be used later with OpenCV DNN.
8. Export the best.onnx model into your local machine or mount it to your drive.
9. Pass the frames in Microsoft Visual Studio runtime to the ONNX model using OpenCV DNN in C++, and get back the coordinates of X,Y, Width, Height, and class name.


### Dependencies

* [Google Colab](https://colab.research.google.com/?utm_source=scs-index) for online training/testing
* Linux or Window 10 for local training/testing
* GPU RTX3080 for best FPS 
* CUDA +11.0
* cuDNN +8.0
* Anaconda
* Python +3.8.0
* PyTorch 1.11.0 (Currently only & TBD)
* OpenCV +4.5.5
* [ImageJ](https://imagej.nih.gov/ij/) to visualize medical images

### Program executing

* For training/testing, go to the [Complete_training_testing](https://github.com/Omega-Medical-Imaging/EclipseAI/tree/main/Complete_training_testing) folder.
* For running the model in Visual Studio with C++, go to [Run Inference - OpenCV](https://github.com/Omega-Medical-Imaging/EclipseAI/tree/main/Run%20Inference%20-%20OpenCV) folder.

## Dataset

- [Annotated dataset with a mix of raw and processed images - three classes of Catheter, Bolis, and Stent](https://app.box.com/s/1i0pjl0wm6x7ts50q2tb593fvz4ogqwr)
- [Un-annotated dataset - Three classes of Catheter, Bolis, and Stent](https://knightsucfedu39751-my.sharepoint.com/:u:/g/personal/mr_azzam_knights_ucf_edu/ETbmj436QqtJsawlTC2A-14BoZ_ZnPhIgV4tKpNpJLx72Q?e=p2HkM9)

## Authors

Azzam Alhussain  
Jiff Schmidt 

## License

This project is licensed under the [BSD-3-Clause license] License - see the LICENSE.md file for details

## Tutorial 

These are some documents and videos that will guide you through the whole process in sequence;

1. [Using LabelImg to annotate your dataset](https://app.box.com/s/vd1yy5umq6hiacza41vpbvmmsjtk9tg9)
2. [Steps in sequence: Training and testing 1,2,3. Running the inference with OpenCV, and All folder in PC](https://app.box.com/s/zen06o5y7ziif834c7g6zy446tzsiszp)

## Acknowledgments

Inspiration, code snippets, etc.

- [Deep Learning in Medical Imaging](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6945006/pdf/ns-1938396-198.pdf)
- [An overview of deep learning in medical imaging](https://reader.elsevier.com/reader/sd/pii/S2352914821002033?token=6367B8345B2D892431690DF52086FC1E932CFD7890E429A59644A4F45A09571895D948E3AC6D14C65820A9E058BCCAED&originRegion=us-east-1&originCreation=20220520201648)
- [Advances in Deep Learning-Based Medical Image Analysis](https://downloads.spj.sciencemag.org/hds/2021/8786793.pdf)
- [LabelImg repository for annotation](https://github.com/tzutalin/labelImg)
- [YOLOv5 algorithm repository](https://github.com/ultralytics/yolov5)
- [OpenCV DNN and YOLOv5 in C++](https://learnopencv.com/object-detection-using-yolov5-and-opencv-dnn-in-c-and-python/)
- [Roboflow - YOLOv5 - Custom Dataset](https://blog.roboflow.com/how-to-train-yolov5-on-a-custom-dataset/)
- [Weights & Biases - YOLOv5 - Debug bounded box](https://wandb.ai/cayush/yoloV5/reports/Track-and-debug-your-YOLOv5-models--VmlldzozMDQ1OTg)
