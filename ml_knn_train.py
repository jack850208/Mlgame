"""
The template of the main script of the machine learning process
"""
ball_position_history=[]


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
        ball_destination =0
        
        # Make the caller to invoke `reset()` for the next round.
        if (scene_info["status"] == "GAME_OVER" or
            scene_info["status"] == "GAME_PASS"):
            return "RESET"
        ball_position_history.append(scene_info["ball"])#Get ball location
        platform_center_x = scene_info["platform"][0]+20#Get platform location
        
        #Restart Game
        if not self.ball_served:
            self.ball_served = True
            command = "SERVE_TO_LEFT"
            return command
        
        #count Vector_x & Vector_y
        #Define if Ball is going down
        if len(ball_position_history)==1:
            ball_going_down = 0
        elif ball_position_history[-1][1]-ball_position_history[-2][1]>0:
            ball_going_down = 1
            vy =ball_position_history[-1][1]-ball_position_history[-2][1]
            vx =ball_position_history[-1][0]-ball_position_history[-2][0]
        else: ball_going_down = 0
        
        #Predict hit location of ball
        if ball_going_down == 1 and ball_position_history[-1][1]>=0:
            ball_destination = ball_position_history[-1][0]+ ((((395-ball_position_history[-1][1]))/vy)*vx)

        if ball_destination >= 195:
            ball_destination = 195-(ball_destination-195)
        elif ball_destination <= 0:
            ball_destination = - ball_destination
        else:
            ball_destination = ball_destination
        
        #Move platform to the hit location
        if ball_going_down == 1 and platform_center_x > (ball_destination + 5):
             command = "MOVE_LEFT"
        elif ball_going_down == 1 and platform_center_x < (ball_destination + 5):
             command = "MOVE_RIGHT"
        elif ball_going_down == 1 and platform_center_x == ball_destination + 5:
             command = "NONE"
        else:
             command = "NONE"
        
        #when ball raising, let platform return to center
        if ball_going_down == 0 and platform_center_x > 93:
             command = "MOVE_LEFT"
        elif ball_going_down == 0 and platform_center_x < 93:
             command = "MOVE_RIGHT" 
        elif ball_going_down == 0 and platform_center_x == 93:
             command = "NONE"
        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
