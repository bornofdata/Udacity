# Dog Breed Image Classification Project

## Overview

This project uses a pre-trained image classifier to identify dog breeds from pet images and to determine whether each image is of a dog or not a dog. The main goal is not to build a new deep learning model, but to apply Python programming skills to evaluate how well existing convolutional neural network (CNN) architectures perform on this task.

The project compares three different CNN model architectures:

- AlexNet
- VGG
- ResNet

Using these models, the program classifies pet images, compares the classifier output with expected labels, and reports performance results. In addition to classification accuracy, the project also considers runtime so that model quality can be evaluated alongside computational cost.

---

## Project Objectives

The project is designed around the following objectives:

1. Correctly identify which pet images are of dogs and which are not dogs
2. Correctly classify the breed of dog for images that are of dogs
3. Compare the performance of different CNN architectures
4. Evaluate the trade-off between classification accuracy and execution time

---

## Project Description

A citywide dog show requires participants to register their dogs using pet images. Since some submitted images may not actually be dogs, the registration system needs a way to verify the images automatically.

In this project, a pre-trained classifier is used as the image recognition engine. The Python program built around it performs the following tasks:

- reads pet image filenames
- creates labels from filenames
- classifies images using a provided classifier function
- compares classifier labels with expected pet labels
- determines whether labels correspond to dogs or not dogs
- calculates summary statistics
- prints final results for analysis

This project focuses on using Python to organize and evaluate the classification workflow rather than creating or training the classifier itself.

---

## Key Features

- Uses a pre-trained image classifier
- Processes pet image filenames into readable labels
- Compares expected labels with classifier predictions
- Identifies whether images are dogs or not dogs
- Computes classification statistics
- Measures runtime for each model architecture
- Compares AlexNet, VGG, and ResNet performance

---

## Technologies and Tools

This project uses:

- Python
- Pre-trained CNN architectures
- Command line arguments
- Dictionaries and lists for structured results
- File-based label lookup using `dognames.txt`

---

## Program Workflow

The program follows a multi-step workflow:

1. Measure the start time of the program
2. Get user input from command line arguments
3. Extract pet image labels from image filenames
4. Store labels in a dictionary data structure
5. Run the provided classifier on each image
6. Compare classifier labels with pet image labels
7. Determine whether both labels represent dogs
8. Calculate summary statistics
9. Print formatted results
10. Measure total runtime

This workflow is repeated for each of the provided CNN architectures.

---

## Data Handling

A central part of the project is organizing results in a compound data structure. The program stores information such as:

- pet image label
- classifier label
- whether the labels match
- whether the pet image is a dog
- whether the classifier label is a dog

This structure makes it possible to compute statistics efficiently and compare model performance across all images.

---

## Model Comparison

The project evaluates three CNN architectures:

### AlexNet
A classic CNN architecture that is relatively lightweight and fast.

### VGG
A deeper architecture known for strong image classification performance.

### ResNet
A more advanced architecture that uses residual connections and often performs well on image tasks.

The goal is to determine which model best satisfies the project objectives while also considering how long each model takes to run.

---

## Expected Results

The project evaluates model performance in two main areas:

- dog vs not-dog identification
- correct dog breed classification

According to the project materials, both VGG and AlexNet can correctly identify dogs and not-dogs at a very high level, while VGG performs best on breed classification, achieving over 90% accuracy for that objective.

---

## Learning Outcomes

By completing this project, the learner strengthens skills in:

- Python scripting
- string processing
- dictionary-based data organization
- command line input handling
- working with pre-built AI tools
- evaluating model outputs
- comparing accuracy and runtime trade-offs

This project also reinforces the idea that practical AI work often involves integrating, testing, and analyzing models rather than always building them from scratch.

---

## Files and Components

The project typically works with the following kinds of files:

- pet image files
- a provided classifier function
- a test file demonstrating classifier usage
- `dognames.txt` for identifying valid dog breeds
- the main project script and helper functions

Each file plays a role in the overall classification and evaluation pipeline.

---

## Conclusion

This project demonstrates how Python can be used to build a complete evaluation workflow around a pre-trained image classifier. Rather than focusing on model creation, it emphasizes the practical programming tasks required to make AI systems useful: preparing inputs, organizing outputs, validating predictions, calculating statistics, and comparing performance.

By comparing AlexNet, VGG, and ResNet, the project highlights an important real-world lesson in AI development: the best solution is not only about accuracy, but also about efficiency and suitability for the task.
