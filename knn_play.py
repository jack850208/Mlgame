"""
The template of the main script of the machine learning process
"""
from sklearn.neighbors import KNeighborsClassifier 
import pickle
import numpy as np

model_name = r"C:\Users\AIC\Desktop\MLGame-master\games\arkanoid\ml\KNN_model.sav"
f = open(model_name,'rb')
KNN_model = pickle.load(f)

class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.ball_served = False

    def update(self, scene_info):
        """
        Generate the command according to the received `scene_info`.
        """
        #show scene_info content
        
        print (scene_info['ball'])
        
        # Make the caller to invoke `reset()` for the next round.
        if (scene_info["status"] == "GAME_OVER" or
            scene_info["status"] == "GAME_PASS"):
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            command = "SERVE_TO_LEFT"
        else:
            
            ball_position = np.array(scene_info['ball'])
            
            predict = KNN_model.predict(ball_position[np.newaxis])
            platform_position = np.array(scene_info['platform'])
            
            if platform_position[0] < predict:
                command = "MOVE_RIGHT"
            if platform_position[0] > predict:
                command = "MOVE_LEFT"
            if platform_position[0] == predict:
                command = "NONE"
            
            
            #command = "MOVE_RIGHT" 

        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
