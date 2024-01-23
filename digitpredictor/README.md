# Digit predictor
[Link to the youtube video](https://youtu.be/wK1MnMz35Xw)
## CS50 Final project
### Background
Computer vision is a rapidly growing and advancing field. Being a student of Data Science, this field holds great importance for me and I plan to pursue a career in it someday. As soon as I completed CS50 and understood the basics of programming, I started exploring this field. After going through some tutorials, I thought myself to be well equipped for a basic computer vision problem, the so called "Hello World" of computer vision students, Hand Written Digit Identifier
### Problem Statement
The problem statement for this project was quite simple. I planned to design a program which identifies handwritten digits.
### Approach
The problem falls under multiple categories. Machine Learning, Computer Vision, Data Science etc. In order for the successful completion of the project, there are some fundamental steps
*Create a machine learning model which can identify patterns in the images and train itself
*Train the model by feeding it data and allowing it to correct itself
*Ask the user for a picture and tell the trained model to predict that classify that picture
### Tools used
Although it might sound like a daunting task, basic digit recognisation has been made extremly easy thanks to the plethora of librarires and frameworks available. The following are the tools which were not mentioned in the course but are used in this project
*Tensorflow library in python
*Jupiter notebook
*OpenCV library in Python
### Making the computer learn
Machine learning has become a buzz word these days. It is basically a set of algorithms and instructions which allow the computer to detect certain patterns in data and based on those findings performs certain functions on it. There are hundreds of machine learning models each being suited for a particular task and having its pros and cons. In computer vision, the choice most often made is a neural network. That is exactly what I have used in my project
#### Model Selection
This project uses a specialized type of neural network, one specifically designed for classifying objects in images. It is called a convoutional neural network. This is a vast and well documented subject on which multiple papers have been written so I will not dwell on this much. 
#### Model Architecture
Having chosen which model I would use, the next task was to choose a model architecture i.e how many layers to use, which activation functions to use and so forth. The architecture I have used is perhaps the simplest CNN architecture with just one convolutional layer. Owing to the simplicity of the task, an extremely complex model was not required so I settled on this architecture. It goes without saying that models which perform more complex tasks use extremely intricate models with hundreds of layers but as explained earlier, in our case this was not required.
#### Training the model
Usually considered as the hardest part of any machine learning project, training the model is an umbrella term which consists of multiple sub problems which are descibed below
##### Data Selection
For a hand written digit classifier I had two choices. Either train on a simple dataset and perform more image processing on the user provided picture or train on a complex dataset and do minimal image pre processing. I chose the former because of the ease of obtaining such a dataset i.e the MNIST datatset
##### Data cleaning 
In most datasets, data cleaning is often regarded as the hardest part. We have to basically shape the data in such a way thet the computer can understand it. This is an entire field of its own and requires considerable expertise. In our case, we use the mnist dataset provided by the keras library. It requires no processing and is ready to be fed directly into the network. However I did some minimal processing just to normalize all the pixel values in the pictures 
##### Model training
With the data ready to be fed the model was ready to be trained. Python's tensorflow library makes this part extremely easy. If the model has been constructed properly and the data has been processed accordingly, training a model is as simple as clicking a button. We wait until the model has reached our requird accuracy and interrupt the process. Then the model is saved so that it can be used in other files
### Making predictions
With the model trained now it was time for the actual functionality of my project i.e to take an actual image from the user and classify it. For the purpose of image processing and handling we use the Opencv python library.
#### Taking and processing the user's image
As mentioned earlier, I opted to train my model on extremely standard and organized data however the image which the user provides will almost never be the same type of image on which the model has been trained. Thus it was important for me to preprocess the image and try to make it as simple as possible before feeding it to the model. This is reason i chose opencv because it makes working with images an easy task. In the code, I first ask the user for the image. The image is not taken by a specific file path because i thought it would be tedious for the user to ensure the correct path instead I use opencv to capture a video and when the button is pressed, the picture is captured. The user is then prompted to confirm whether they want to proceed with the picture. If the user does not like it the picture is deleted and program terminates
#### Displaying results
Finally when the picture has been processed, I pass it to the model to make a prediction and then after decoding the model's response, print it on the screen
### Constraints
Being a model of an extrmely simple nature, it goes without saying that it does make some wrong predictions. However I have provided some methods which might help to diagnose the problem. Mainly the code which I have commented out does exactly that. It allows us to preview the image which is being fed to the model. I it is anything but a white digit against a black background, it means that further image processing is required. In this case we can fine tune the parameters to correct it
#### Image type
The model is basically designed for black(or a dark color) against a white background. A simple black hand written digit on a plane white sheet of paper would yield the best results. 
### Bottom Line
Overall, the project was a thrilling experience. It put me out of my comfort zone more than once and forced me to explore resources, adapt to certain challenges, leverage the power of certain libraries and choose between certain tradeoffs. All credit goes to [Harvard's CS50](https://cs50.harvard.edu/x/2023/) for teaching me the invaluable skills of coding and more importantly, self learning
