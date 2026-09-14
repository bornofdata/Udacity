#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Kehinde Fagbamigbe
# DATE CREATED: sep 13, 2026                             
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
import os

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
  """
  Creates a dictionary of pet labels (results_dic) based upon the filenames 
  of the image files. These pet image labels are used to check the accuracy 
  of the labels that are returned by the classifier function, since the 
  filenames of the images contain the true identity of the pet in the image.
  Be sure to format the pet labels so that they are in all lower case letters
  and with leading and trailing whitespace characters stripped from them.
  (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
  Parameters:
    image_dir - The (full) path to the folder of images that are to be
                classified by the classifier function (string)
  Returns:
    results_dic - Dictionary with 'key' as image filename and 'value' as a 
    List. The list contains for following item:
        index 0 = pet image label (string)
  """
  filename_list = listdir(image_dir)

  # Print 10 of the filenames from folder given directory
  print(f"\n Prints 10 filenames from folder {image_dir} ")

  for idx in range(0, 10, 1):
      print("{:2d} file: {:>25}".format(idx + 1, filename_list[idx]) )

  filenames = len(filename_list)
  print("\nNumber of files in the folder =", filenames)
  results_dic = {}
  items_in_dict = len(results_dic)
  if items_in_dict == 0:
    print("\nEmpty Dictionary results_dic - n items=", items_in_dict)

  print("Now adding items to results_dic dictionary with key=filename and value=pet label")

  for idx in range(0, filenames, 1):
      file = filename_list[idx]
      name_without_ext = os.path.splitext(filename_list[idx])[0]

      if file in results_dic:
          print("** Warning: Key=", name_without_ext, "already exists in results_dic with value =", results_dic[name_without_ext])
      else:
          print("** Adding Key=", name_without_ext, "to results_dic")
          if name_without_ext.split('_')[-1].isnumeric():
            pet_label = name_without_ext.split('_')[:-1]
          else:
            pet_label = name_without_ext.split('_')
          word_list = []
          for word in pet_label:
              if word.isalpha():
                  word = word.lower().strip()
              word_list.append(word)
          pet_label = ' '.join(word_list)
          results_dic[file] = [pet_label]

  # Replace None with the results_dic dictionary that you created with this
    # function
  ## Prints resulting pet_name
  print("\nFilename=", name_without_ext, "   Label=", pet_label)
  print("the total number of items in the dictionary results_dic =", len(results_dic))

  return results_dic
