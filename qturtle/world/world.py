from copy import deepcopy
import itertools
import random
import numpy as np

from .dyn_object import DynamicObject
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

    def dist_angle_from_goal(self, pos_orientation):
        pos = np.array(pos_orientation[0:2])
        rho = pos_orientation[2]

        direction = np.array([np.cos(rho), np.sin(rho)])
        goal = np.array(self.goal)

        dist = np.linalg.norm(goal - pos)
        angle = np.arccos(np.dot(direction, goal-pos)/dist)

        return dist, angle

    def reset(self):
        if self.multi_goal:
            self._sample_goal()

    def update_dynamic_objects(self):
        for do in self.dyn_objects:
            do.update(self.sim)

    def _build(self):
        self.walls = Walls(self.x_size, self.y_size, sim=self.sim)
        self.objects = [
            create_object(obj_type, obj_kwargs, sim=self.sim, **general_kwargs)
            for (obj_type, general_kwargs, obj_kwargs)
            in self.config["objects"]
        ]

        dyn_objects = self.config.get("dyn_objects", [])

        self.dyn_objects = [
            DynamicObject(obj_type, obj_kwargs, sim=self.sim, **general_kwargs, **dyn_kwargs)
            for (obj_type, general_kwargs, obj_kwargs, dyn_kwargs)
            in dyn_objects
        ]

        self.goal_obj = draw_goal(*self.goal, sim=self.sim)

        self.collision_objects.extend(self.objects)
        self.collision_objects.extend(self.walls.objects)

        for do in self.dyn_objects:
            self.collision_objects.append(do.object)

    def _parse_config(self):
        self.repr = self.config["repr"]

        setup = self.config["setup"]

        self.x_size = setup["x_size"]
        self.y_size = setup["y_size"]
        self.start_pos = [*setup["start"][0], self.BASE_Z]
        self.start_angle = setup["start"][1]
        self.resets = setup.get("resets", [])
        self.resets.append(setup["start"])

        self.multi_goal = setup.get("multi_goal", False)
        if self.multi_goal:
            self.goals = setup["goals"]
            self._sample_goal()
        else:
            self.goal = setup["goal"]

    def _sample_goal(self):
        self.goal = random.choice(self.goals)


class MiniWorld(World):
    def __init__(self, config, sim):
        super().__init__(config, sim)

        _r_pos = deepcopy(FREE_POSITIONS)
        _r_pos.remove(self.goal)

        self.resets = list(itertools.product(_r_pos, FREE_ANGLES))
