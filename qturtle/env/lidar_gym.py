from .gym import GymEnvironment


class LidarGymEnvironment(GymEnvironment):
    """ Qturtle composable environment following the OpenAI Gym API """

    def __init__(self,
                 sim,
                 sim_steps,
                 turtlebot,
                 world,
                 control,
                 reward,
                 termination,
                 lidar):

        """The constructor

        Parameters
        ----------
        sim : pybullet client
            The Simulation object
        sim_steps : int
            Default number of simulation steps per action
        turtlebot : qturtle.Turtlebot
            The robot object
        world : qturtle.world.World
            The world (walls, obstacles, start, goal) for the environment
        control : qturtle.control.Control
            Control scheme for the robot
        reward : qturtle.reward.Reward
            Reward function
        termination : qturtle.termination.Termination
            Termination criterion
        lidar: qturtle.sensors.lidar.Lidar
            The LIDAR sensor implementation
        """
        super().__init__(sim, sim_steps, turtlebot, world, control, reward, termination)

        self.lidar = lidar

    def step(self, action):
        """ One step of the agent in the environment

        Parameters
        ----------
        action : Any
            The action to take

        Returns
        -------
        Tuple[Any, float, boolean, dict]
            The next state, reward, flag indicating if the environment is finished and extra info
            (empty)
        """
        pos_orientation, reward, done, _ = super().step(action)
        dist, angle = self.world.dist_angle_from_goal(pos_orientation[0])
        next_state = self.lidar(self.sim, self.turtlebot)
        next_state += [dist, angle]

        return [next_state], reward, done, {}

    def reset(self, random=False):
        pos_orientation = super().reset(random=random)
        dist, angle = self.world.dist_angle_from_goal(pos_orientation[0])
        next_state = self.lidar(self.sim, self.turtlebot)
        next_state += [dist, angle]

        return [next_state]

    def _run_sim_steps(self, steps, check_collisions=True):
        super()._run_sim_steps(steps, check_collisions=check_collisions)
        self.world.update_dynamic_objects()
