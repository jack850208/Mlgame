# import library:

import glob    
import numpy as np
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Code bellow:

pickle_file_path=r'C:\Users\AIC\Desktop\MLGame-master\games\arkanoid\log\ml_EASY_1_2020-11-11_09-00-55.pickle'
file_list = glob.glob(pickle_file_path)

data_list = pickle.load(open(file_list[0],'rb'))


"""
   Create a container to save the info from 'scene_info' dictionary
"""

ball_position = []   # storage ball (x, y) position
platform_position = []   #storage platform (x,y) position
ball_status = []   #storage ball movement status{up, down, left, right}



"""
   split the scene_info in several part, and put them into the container we
   create before (at top line)
"""

for index in  range(0, len(data_list['ml']['scene_info'])):
   
   # get the information of ball position from scene_info list
   ball_position.append(data_list['ml']['scene_info'][index]['ball'])
   # get the information of platform position frome scene_info list
   platform_position.append(data_list['ml']['scene_info'][index]['platform'])
   #ball_status.append(data_list['ml']['scene_info'][1][''])


ball_pos_array = np.array(ball_position) # convert to numpy type array
platform_pos_array = np.array(platform_position) # convert to numpy type array
platform_next_pos_array = np.array(platform_position[1:])

# Combine the vector you create above that you would like to train later 
knn_eigen_vector = np.hstack((ball_pos_array, platform_pos_array))




