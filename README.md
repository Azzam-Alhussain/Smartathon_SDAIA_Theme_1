# Smartathon by SDAIA - Theme 1

![ezgif com-gif-maker](https://user-images.githubusercontent.com/74447207/213848226-47d96eea-90b4-42b4-831f-91e9ca6dccb9.gif)

## Description

Visual Pollution detection project in KSA by SDAIA dataset.

## Getting Started

1. Getting the dataset from the [Smartathon challange webiste](https://drive.google.com/file/d/1ULqYtd9yomeGz53WBhgRdPRFB37ppeDU/view) 
2. Train/test using YOLOv5 using our code with S,M,L,X models on [Google Colab](https://drive.google.com/file/d/1UfGKvBBxgrmcO-R7bTmRahWvwjPDle6m/view?usp=sharing).
4. Evaluate and visualize the trained model on the [test data](https://drive.google.com/file/d/1cycWWo6rUMJcIQbHC4m9rQdTLPZRoHN-/view?usp=sharing).
5. Measure the Mean Average Precision (mAP) and Intersection Over Union (IoU).
6. Inference/run the model/weights on new/unseen data.
7. Convert the best.pt model into ONNX format to be used later with OpenCV DNN for deployment (Currently, not needed in this project).
8. Export the best.onnx model into your local machine or mount it to your drive.


## Dependencies

* [Google Colab](https://colab.research.google.com/?utm_source=scs-index) for online training/testing
* Linux or Window 10 for local training/testing
* High GPU for faster training
* CUDA +11.0
* cuDNN +8.0
* Anaconda
* Python +3.8.0
* PyTorch +1.11.0 (Currently only & TBD)

## Dataset

- [The well prepared data for training with YOLOv5 format coordiantes](https://drive.google.com/file/d/1_PF_JeAngh0PlW2gkNDuXfvjm9RMVKRM/view?usp=sharing)
- [The test data for inference](https://drive.google.com/file/d/1cycWWo6rUMJcIQbHC4m9rQdTLPZRoHN-/view?usp=sharing)

## Program executing

* For training/testing, go to the [Source code](https://github.com/Azzam-Alhussain/Smartathon_SDAIA_Theme_1/blob/main/Unique_Team_YOLOv5_KSA_Visual_Pollution_Detection.ipynb) and download the file, then uplaod it into Google Colab.

## Result

You can download our [model](https://drive.google.com/file/d/1srn-uJHbiYDhz6bwpJpBC-iKkDb8SAE3/view?usp=sharing) from here and also the [labels result coordinates](https://github.com/Azzam-Alhussain/Smartathon_SDAIA_Theme_1/blob/main/labels.csv) from here. 


![vis1](https://user-images.githubusercontent.com/74447207/213851744-325c557e-d51c-447b-a662-00556567bca8.png)

![vis1](https://user-images.githubusercontent.com/74447207/213851766-39683b0c-539e-425c-8815-c4ae73a1591a.jpeg)

## Demo Video 

These [videos](https://drive.google.com/file/d/13B_f2DZa0Tq8de_ITXvuT6rXGt0NBuR5/view?usp=sharing) have been captured from real world streets in KSA, and we run our model on them to demonstrate how the model can be implemented in real world. Please clink on the videos to watch them


## Authors

Azzam Alhussain  
Abdulrahman Alghamdi  
Ahmed Kabli

## License

This project is licensed under the [MIT license] License - see the LICENSE.md file for details


## Acknowledgments

Inspiration, code snippets, etc.

- [YOLOv5 algorithm repository](https://github.com/ultralytics/yolov5)
- [Roboflow - YOLOv5 - Custom Dataset](https://blog.roboflow.com/how-to-train-yolov5-on-a-custom-dataset/)
- [Weights & Biases - YOLOv5 - Debug bounded box](https://wandb.ai/cayush/yoloV5/reports/Track-and-debug-your-YOLOv5-models--VmlldzozMDQ1OTg)
