from industrial_robot import industrial

class gantry(industrial):
    """Gantry robot class, derived class from Industrial Robot class.

    Args:
        indusrial_robot (class): Base class used to initialize some of the gantry robot parameters and methods.
    """
    
    def __init__(self, name: str, payload: float, application: list, small_rail_length: float, long_rail_length: float, small_rail_velocity: float, long_rail_velocity: float, company= 'NIST'):            
        """[summary]

        Args:
            name (str): Name of the robot. This attribute canonly be accessed outside the class definition and cannot be set.
            payload (float): Payload for the robot’s arm(s). This attribute can be both accessed and set outside the class definition.
            application (list): List of applications the robot can perform. For instance,gantry_robot can do both kitting and assembly while ground_robot can only do kitting. This attribute can be both accessed and set outside the class definition.
            company (str, optional): Name of the robot’s vendor. By default this is set to "Nist". This attribute canonly be accessed outsidethe class definition and cannot be set.
            small_rail_length (float): [description]
            long_rail_length (float): [description]
            small_rail_velocity (float): [description]
            long_rail_velocity (float): [description]
        """
        super().__init__(name, payload, application, company=company)
        self.small_rail_length = small_rail_length
        self.long_rail_length = long_rail_length
        self.small_rail_velocity = small_rail_velocity
        self.long_rail_velocity = long_rail_velocity

    def __str__(self):
        
        return f'Name: {self._name}, Payload: {self.payload}, Application: {self.application}, Small Rail Length: {self.small_rail_length}, Ling Rail Length: {self.long_rail_length}, Small Rail Velocity: {self.small_rail_velocity}, Long Rail Velocity: {self.long_rail_velocity}, Company: {self._company}'

    def activate_camera(self):
        """Print the gantry robot activates the camera.
        """
        
        print(f'{self._name} activates camera')

    def flip_part(self, parttype: str):
        """Print the gantry robot flips the provided part.

        Args:
            parttype (str): Four part types are available in the environment, red_battery, blue_battery, green_regulator, and blue_sensor.
        """
        
        print(f'{self._name} flips {parttype}')
    
    def pick_up(self, parttype: str, bin: str):
        """Gantry robot picks up part then activates its camera, calls the base class pick_up nethod,then flips the part. 

        Args:
            parttype (str): Four part types are available in the environment, red_battery, blue_battery, green_regulator, and blue_sensor.
            bin (str): Parts are stored in bins 1-8.
        """

        print(f'{self._name} picks up {parttype} from {bin}')
        self.activate_camera()
        super().pick_up(parttype, bin)
        self.flip_part(parttype)

if __name__ == '__main__':
    # robot = indusrial_robot('Shon', 1.2, ['s', 'd'])
    # robot.pick_up('red battery', 'bin 1')
    # robot.put_down('red battery', 'bin 1')
    # robot.attach_gripper('three_finger')
    # robot.detach_gripper('three_finger')
    # robot.move_to_bin('bin 1')
    # robot.move_to_agv('agv 1')
    # robot.move_from_bin('bin 1')
    # robot.move_from_agv('agv 1')
    # robot.move_to_gripper_station('gripper changing station')
    # robot.move_from_gripper_station('gripper changing station')

    g_robot = gantry('Shon', 2.0, ['s', 'a'], 1.0, 2.0, 10, 11, 'NIST')
    print(g_robot)
    g_robot.pick_up('red battery', 'bin 2')