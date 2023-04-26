from copy import deepcopy
import itertools
import random

from .parts import Walls, draw_goal
from .objects import create_object

from .configs.mini import FREE_POSITIONS, FREE_ANGLES


class World:
    """ The simulated world for the robot """

    BASE_Z = 0.05

    def __init__(self, config, sim):
        """The constructor

        Parameters
        ----------
        config : dict
            World configuration
        sim : BulletClient
            Simulation client object
        """
        self.config = config
        self.sim = sim
        self.collision_objects = []

        self._parse_config()
        self._build()

    def __repr__(self):
        return f"{self.__class__}: {self.repr}"

    def sample_start(self):
        """Sample a starting position and orientation

        Returns
        -------
        list, float
            The starting position (x,y,z) and orientation
        """
        sample = random.choice(self.resets)

        return [*sample[0], self.BASE_Z], sample[1]

    def _build(self):
        self.walls = Walls(self.x_size, self.y_size, sim=self.sim)
        self.objects = [
            create_object(obj_type, obj_kwargs, sim=self.sim, **general_kwargs)
            for (obj_type, general_kwargs, obj_kwargs)
            in self.config["objects"]
        ]

        self.goal_obj = draw_goal(*self.goal, sim=self.sim)

        self.collision_objects.extend(self.objects)
        self.collision_objects.extend(self.walls.objects)

    def _parse_config(self):
        self.repr = self.config["repr"]

        setup = self.config["setup"]

        self.x_size = setup["x_size"]
        self.y_size = setup["y_size"]
        self.start_pos = [*setup["start"][0], self.BASE_Z]
        self.start_angle = setup["start"][1]
        self.goal = setup["goal"]
        self.resets = setup.get("resets", [])
        self.resets.append(setup["start"])


class MiniWorld(World):
    def __init__(self, config, sim):
        super().__init__(config, sim)

        _r_pos = deepcopy(FREE_POSITIONS)
        _r_pos.remove(self.goal)

        self.resets = list(itertools.product(_r_pos, FREE_ANGLES))
