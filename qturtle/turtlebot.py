import importlib.resources as pkg_resources

from . import robot


class Turtlebot:
    """ The turtlebot in the simulated environment """
    LEFT_WHEEL = 0
    RIGHT_WHEEL = 1

    LIDAR_LINK = 25

    def __init__(self, sim, base_position, base_angle=0.):
        """The constructor

        Parameters
        ----------
        sim : BulletClient
            pybullet simulation client
        base_position : list
            Base position of the robot
        base_angle : float
            base orientation of the robot
        """
        self.sim = sim
        self.base_position = base_position
        self.base_orientation = self.sim.getQuaternionFromEuler(
            [0., 0., base_angle]
        )

        with pkg_resources.path(robot, 'turtlebot.urdf') as urdf_path:
            self.robot = self.sim.loadURDF(str(urdf_path.resolve()),
                                           self.base_position,
                                           self.base_orientation)

    def set_velocities(self, left, right):
        """Set the velocities on both motors of the robot

        Parameters
        ----------
        left : float
            Left wheel velocity
        right : float
            right wheel velocity
        """
        self.sim.setJointMotorControlArray(self.robot,
                                           jointIndices=[self.LEFT_WHEEL,
                                                         self.RIGHT_WHEEL],
                                           controlMode=self.sim.VELOCITY_CONTROL,
                                           targetVelocities=[left, right])

    def stop(self):
        """ Stop the robot """
        self.set_velocities(0., 0.)

    def reset(self, pos=None, angle=None):
        """Reset the robot. Stops and sets either to given position and orientation or to the base
        position and base orientation.

        Parameters
        ----------
        pos : list
            Optional position to reset to
        angle : float
            Optional angle to reset orientation to
        """
        self.stop()

        position = pos or self.base_position
        orientation = self.sim.getQuaternionFromEuler([0., 0., angle])\
            if angle else self.base_orientation

        self.sim.resetBasePositionAndOrientation(self.robot,
                                                 position,
                                                 orientation)

    def get_pos_and_orientation(self):
        """Get the robots current position and orientation

        Returns
        -------
        Tuple[float, float, float]
            x, y and rho
        """
        pos, orientation = self.sim.getBasePositionAndOrientation(self.robot)
        angle = self.sim.getEulerFromQuaternion(orientation)[2]

        return pos[0], pos[1], angle

    def get_velocity(self):
        """Get the robots velocities

        Returns
        -------
        Tuple[float, float, float]
            dx, dy, drho
        """
        velocity = self.sim.getBaseVelocity(self.robot)

        return velocity[0][0], velocity[0][1], velocity[1][2]
