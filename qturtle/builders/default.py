from ..control import StepControl
from ..env.gym import GymEnvironment
from ..reward import DistanceDecreaseReward
from ..sim import setup_pybullet
from ..termination import GoalThreshold
from ..turtlebot import Turtlebot
from ..world.configs import LARGE_WORLD_V0, MEDI_WORLD_V0, MINI_S_CURVE
from ..world.world import World

# Velocities for going forward, right and left (left wheel, right wheel, sim steps)
STEPPING = [
    (1.0, 1.0, 50),
    (0.5, -0.5, 50),
    (-0.5, 0.5, 50),
]

# Basic configuration
CONFIG = {"dt": 1.0 / 100.0, "sim_steps": 50, "base_speed": 10.0, "goal_threshold": 0.4}


class DefaultBuilder:
    """Builder class for the default environment"""

    def __init__(
        self, gui, dt, sim_steps, world_config, base_speed, stepping, goal_threshold
    ):

        """The constructor

        Parameters
        ----------
        gui : boolean
            Show simulator GUI
        dt : float
            Simulation resolution (time)
        sim_steps : int
            Default number of simulation steps to execute per action
        world_config : dict
            Configuration of the world for the envirionment
        base_speed : float
            Base speed for all velocities
        stepping : list
            List of tuples having the velocity scaling and simulation steps for each action
        goal_threshold : float
            Distance to goal considered solved
        """
        self.gui = gui
        self.sim = setup_pybullet(dt, gui)

        self.sim_steps = sim_steps
        self.world_config = world_config
        self.base_speed = base_speed
        self.stepping = stepping
        self.goal_threshold = goal_threshold

    def _build_base_objects(self):
        """ Build basic environment components """

        self.world = World(self.world_config, self.sim)
        self.turtlebot = Turtlebot(
            base_position=self.world.start_pos,
            base_angle=self.world.start_angle,
            sim=self.sim,
        )
        self.termination = GoalThreshold(
            goal=self.world.goal, threshold=self.goal_threshold
        )
        self.reward = DistanceDecreaseReward(
            start=self.world.start_pos,
            goal=self.world.goal,
            threshold=self.goal_threshold,
            step_reward=0.1,
            collision_reward=-1.0,
            goal_reward=10.0,
        )

    def _build_control(self):
        """ Build control scheme based on stepping configuration """
        self.control = StepControl(base_speed=self.base_speed, steps=self.stepping)

    def get(self):

        """Build and return the enfironment

        Returns
        -------
        GymEnvironment
            The environment
        """
        self._build_base_objects()
        self._build_control()

        return GymEnvironment(
            sim=self.sim,
            sim_steps=self.sim_steps,
            turtlebot=self.turtlebot,
            world=self.world,
            control=self.control,
            reward=self.reward,
            termination=self.termination,
        )


def default_builder(world, gui=False):
    """Builder function called from qturtle.make()

    Parameters
    ----------
    world : str
        The world to create in the environment
    gui : boolean
        Show the simulation gui or not

    Returns
    -------
    GymEnvironment
        The environment
    """
    world_configs = {"3x3": MINI_S_CURVE, "4x4": MEDI_WORLD_V0, "5x5": LARGE_WORLD_V0}

    builder = DefaultBuilder(
        gui=gui, world_config=world_configs[world], stepping=STEPPING, **CONFIG
    )

    return builder.get()
