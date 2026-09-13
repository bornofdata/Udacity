#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER:
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:

#            Z: n_images - number of images
#            B: n_dogs_img - number of dog images
#            D: n_notdogs_img - number of NON-dog images
#            Y: n_match - number of matches between pet & classifier labels
#            A: n_correct_dogs - number of correctly classified dog images i.e both labels are a dog
#            C: n_correct_notdogs - number of correctly classified NON-dog images i.e both labels are NOT a dog
#            E: n_correct_breed - number of correctly classified dog breeds i.e pet label is a dog, and both labels match (if classifier label is not a dog, this could still be correct it does not make the actual breed wrong, it just means the classifier did not recognize it as a dog)
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """        
    # Replace None with the results_stats_dic dictionary that you created with 
    # this function 

    results_stats_dic = {
        'n_images': 0,
        'n_dogs_img': 0,
        'n_notdogs_img': 0,
        'n_match': 0,
        'n_correct_dogs': 0,
        'n_correct_notdogs': 0,
        'n_correct_breed': 0
    }

    # Calculate the number of images
    results_stats_dic['n_images'] = len(results_dic)

    for key, value in results_dic.items():
        # Check if the pet image label is a dog
        if value[3] == 1:
            results_stats_dic['n_dogs_img'] = results_stats_dic['n_dogs_img'] + 1

            # Check if the classifier label is also a dog i.e pet image is a dog and classifier label is also a dog
            if value[4] == 1:
                results_stats_dic['n_correct_dogs'] = results_stats_dic['n_correct_dogs'] + 1

                # Check if the breed is also correct
                if value[2] == 1:
                    results_stats_dic['n_correct_breed'] = results_stats_dic['n_correct_breed'] + 1

        elif value[3] == 0: # meaning the pet image label is NOT a dog
            results_stats_dic['n_notdogs_img'] = results_stats_dic['n_notdogs_img'] + 1

            # Check if the classifier label is also not a dog
            if value[4] == 0:
                results_stats_dic['n_correct_notdogs'] = results_stats_dic['n_correct_notdogs'] + 1

        elif value[2] == 1: # meaning the pet image label and classifier label match
            results_stats_dic['n_match'] = results_stats_dic['n_match'] + 1

#     # Calculate the number of dog images
#     results_stats_dic['n_dogs_img'] = sum([1 for v in results_dic.values() if v[3] == 1])

#     # Calculate the number of NON-dog images
#     results_stats_dic['n_notdogs_img'] = results_stats_dic['n_images'] - results_stats_dic['n_dogs_img']

#     # Calculate the number of matches
#     results_stats_dic['n_match'] = sum([1 for v in results_dic.values() if v[2] == 1])

#     # Calculate the number of correctly classified dog images
#     results_stats_dic['n_correct_dogs'] = sum([1 for v in results_dic.values() if v[3] == 1 and v[4] == 1])

#     # Calculate the number of correctly classified NON-dog images
#     results_stats_dic['n_correct_notdogs'] = sum([1 for v in results_dic.values() if v[3] == 0 and v[4] == 0])

#     # Calculate the number of correctly classified dog breeds
#     results_stats_dic['n_correct_breed'] = sum([1 for v in results_dic.values() if v[3] == 1 and v[2] == 1])

    # Calculate the percentages

    results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img'] * 100) if results_stats_dic.get('n_dogs_img', 0) > 0 else 0
    results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img'] * 100) if results_stats_dic.get('n_notdogs_img', 0) > 0 else 0
    results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img'] * 100) if results_stats_dic.get('n_dogs_img', 0) > 0 else 0
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / results_stats_dic['n_images'] * 100) if results_stats_dic.get('n_images', 0) > 0 else 0

    print("End of calculates_results_stats function.")
    print("Results Statistics Dictionary:\n", results_stats_dic)

    return results_stats_dic
