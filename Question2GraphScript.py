'''
Question1GraphScript.py
  Author(s): Felix Nguyen (1316719)
  Earlier contributors(s): Andrew Hamilton-Wright, Amirhossein Nafissi (1319709), Arya Rahimian Emam (1319709)

  Project: Milestone III
  Date of Last Update: March 13, 2025.

  Functional Summary
      
        1. Takes the csv file and stores industry names, index for most frequent and index for second most frequent
        2. Industry names is set to the x-axis and Index value for the y-axis
        3. Adjusted some minor fixes to make the industry names readable and the size of the graph
        4. Display the information in a visual bar chart with legend to see which bar is which
        
      References
        The data is taked from https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410037201&cubeTimeFrame.startMonth=01&cubeTimeFrame.startYear=2023&cubeTimeFrame.endMonth=12&cubeTimeFrame.endYear=2023&referencePeriods=20230101%2C20231201
        and https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410020401&pickMembers%5B0%5D=1.1&pickMembers%5B1%5D=2.1&pickMembers%5B2%5D=3.1&cubeTimeFrame.startYear=2019&cubeTimeFrame.endYear=2023&referencePeriods=20190101%2C20230101

        Youtube video used to help with plotting the graph: https://www.youtube.com/watch?v=zwSJeIcRFuQ and https://www.youtube.com/watch?v=1M65rAAcl5E 

'''

import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib
import numpy

# Read the CSV file
file = pd.read_csv("question_2_output.csv")

'''Data Set'''
# Take the occupation names and display them on the x-axis
occupation = file['Occupation'].tolist()
# the index will be display on y-axis
index = file['Most_Frequent_Index']
positions = numpy.arange(len(index))


# Second Most Frequent Index
index2 = file['Second_Most_Frequent_Index']
positions2 = numpy.arange(len(index2))
width = 0.4

# This loop is used to the industries name readable in the graph
for i in range(len(occupation)):
    occupation[i] = occupation[i].replace(" ", "\n")



# Setting Figure Size
plt.figure(figsize=(14, 6))

# Label for x-axis, y-axis and title
plt.xlabel('Industry')
plt.ylabel('Most Frequent Index')
plt.title('How does the average educational level vary across different employment sectors in Canada?')

# Replace axis label 
plt.xticks(positions, occupation, rotation=0, ha='center', fontsize=7)

# The industry names were being cut off so add larger bottom margin
plt.subplots_adjust(bottom=0.2)

# Plot bar graph
plt.bar(positions-width/2, index, width, label='Most Frequent Index', color='red')
plt.bar(positions+width/2, index2, width, label='Second Most Frequent Index', color='blue')

# Display Legend Top Right
plt.legend()

# Display bar graph
plt.show()