import sys
import os
import cv2
import numpy as np
import time


                    
def replace_nth_character(input_string, n, new_char):
    # Convert the string to a list of characters
    char_list = list(input_string)
    
    # Replace the nth character (0-based index)
    if 0 <= n < len(char_list):
        char_list[n] = new_char
    else:
        raise IndexError("Index out of range")
    
    # Convert the list back to a string
    return ''.join(char_list)

def is_nth_char_two(input_string, n):
    # Check if n is within the valid range
    if 0 <= n < len(input_string):
        return input_string[n] == '2'
    else:
        raise IndexError("Index out of range")

for line in sys.stdin:
    sys.stdout.write(line)
    if "STOR" in line:
        #print(line)
        # Your input string
        input_string = line
        # Split the string by spaces
        components = input_string.split()
        # Print the components
        print(components[5])
        #check if this is the smaller image
        n = 24  # Replace the 10th character (0-based index)
        if is_nth_char_two(components[5],n):
            input_string = "/home/deepak/deepak/134-2-2-20241209165449.jpg"
            new_char = '1'
            result = replace_nth_character(components[5], n, new_char)
            print(result)
            # Load the larger image and the template image
            large_image = cv2.imread(result)
            template = cv2.imread(components[5])

            # Convert images to grayscale
            large_image_gray = cv2.cvtColor(large_image, cv2.COLOR_BGR2GRAY)
            template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

            # Get the dimensions of the template
            w, h = template_gray.shape[::-1]

            # Perform template matching
            result = cv2.matchTemplate(large_image_gray, template_gray, cv2.TM_CCOEFF_NORMED)

            # Set a threshold
            threshold = 0.8
            loc = np.where(result >= threshold)

            # Draw rectangles around matched regions
            for pt in zip(*loc[::-1]):
                cv2.rectangle(large_image, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

            # Display the result
            cv2.imshow('Detected', large_image)
            cv2.waitKey(3000)
            #time.sleep(5)
            cv2.destroyAllWindows()
                    
