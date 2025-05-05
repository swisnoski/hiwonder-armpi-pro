from hiwonder import HiwonderRobot
import numpy as np
from time import sleep

from camera_cv import get_coordinates
from arm_models import FiveDOFRobot

robot = HiwonderRobot()

def main():
    while True: 
        robot.move_to_home_position()
        sleep(1)

        x, y, z, block_color = get_coordinates()
        sleep(1)

        robot.go_to_position_high([x,y])
        sleep(1)

        theta = robot.go_to_position_low([x,y])
        sleep(1)

        robot.close(theta)
        sleep(2)

        theta = robot.sort(block_color)
        sleep(1)

        robot.open(theta)
        sleep(2)

        robot.move_to_home_position()






if __name__ == "__main__":
    main()