import numpy as np


class GoalThreshold:
    """ Termination criterion based on a threshold distance to the goal """

    def __init__(self, goal, threshold, on_collision=True):
        """The constructor

        Parameters
        ----------
        goal : list
            Goal position
        threshold : float
            Threshold distance to consider the goal reached
        on_collision : boolean
            Termination on collisions?
        """
        self.goal = np.array(goal)
        self.threshold = threshold
        self.on_collision = on_collision

    def __call__(self, state, collisions):
        """Check the criterion

        Parameters
        ----------
        state : list
            Current state of the robot in the environment
        collisions : boolean
            Are there any collisions

        Returns
        -------
        boolean
            Criterion reached?
        """
        if self.on_collision and collisions:
            return True

        pos = np.array([state[0][0], state[0][1]])

        return np.linalg.norm(self.goal - pos) <= self.threshold

    def reset(self, goal=None):
        """Reset goal"""

        if goal:
            self.goal = np.array(goal)
