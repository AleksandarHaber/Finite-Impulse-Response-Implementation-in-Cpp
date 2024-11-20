'''
Python file that 
1) Generates a noisy input data for a FIR filter implemented in C++
2) Saves the noisy input data in a txt file 
3) Loads the filtered data from a txt file 
4) Plots both the input and output data

Author: Aleksandar Haber, PhD
SEE THE LICENSE FILE
'''

# Importing libraries that will be used
import numpy as np
import matplotlib.pyplot as plt 

# number of data samples
S=1000
 
# name of the file to save the input raw data
# this file is an input to the C++ code implementing the FIR filter 
input_filename = 'input_data.txt'
# name of the file containing the filtered data
# this file is the output of the FIR filter and it is produced by the C++ code
filtered_filename='output_data.txt'

# create an input array
# input array
input_array=np.zeros(shape=(S,1));

# generate a noisy input data
dt=0.01
for i in range(len(input_array)):
    input_array[i,0]=np.sin(i*dt)+0.2*np.random.randn()


# plot the input array 
plt.figure(figsize=(10,6))
plt.plot(input_array, color='blue',linewidth=2, label="Input")
plt.legend()
plt.grid(visible=True)
plt.savefig('input.png',dpi=600)
plt.show()


# Save the array to a text file
np.savetxt(input_filename, input_array) 

#####
# Now, you need to run the C++ code to generate the filtered data
#####

# load the filtered data
output_array = np.loadtxt(filtered_filename)


#plot the output array
plt.figure(figsize=(10,6))
plt.plot(output_array, color='red',linewidth=4, label="Filtered output")
plt.legend()
plt.grid(visible=True)
plt.savefig('filtered_output.png',dpi=600)
plt.show()

# plot both the input and output array on the same graph for comparison
plt.figure(figsize=(10,6))
plt.plot(input_array, color='blue',linewidth=4, label="Input")
plt.plot(output_array, color='red',linewidth=4, label="Filtered output")
plt.legend()
plt.grid(visible=True)
plt.savefig('input_output.png',dpi=600)
plt.show()




