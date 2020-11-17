# import library:

import glob    
import numpy as np
import pickle
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Code bellow:

pickle_file_path='/mnt/chromeos/removable/Linux_Mint/MLGame-master/games/arkanoid/log/*.pickle'
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

   ball_position.append(data_list['ml']['scene_info'][index]['ball'])
   platform_position.append(data_list['ml']['scene_info'][index]['platform'])
   #ball_status.append(data_list['ml']['scene_info'][1][''])


