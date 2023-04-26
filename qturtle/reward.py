import numpy as np


class BaseGoalReward:
    """ Abstract base class for Reward functions based on distance to goal """

    def __init__(self,
                 start=None,
                 goal=None,
                 threshold=0.4,
                 goal_reward=100.,
                 collision_reward=-10.,
                 step_reward=-1.):
        """The constructor

        Parameters
        ----------
        start : list
            Start position
        goal : list
            goal position
        threshold : float
            Threshold to consider the goal reached
        goal_reward : float
            reward for reaching the goal
        collision_reward : float
            reward/penalty for colliding with an obstacle
        step_reward : float
            default reward per step
        """
        if start:
            self.start = np.array(start[:2])

        if goal:
            self.goal = np.array(goal)

        self.threshold = threshold
        self.goal_reward = goal_reward
        self.collision_reward = collision_reward
        self.step_reward = step_reward

        self.reward_range = (collision_reward, goal_reward)

    def __call__(self, state, collision):
        """Get the reward

        Parameters
        ----------
        state : list
            current state
        collision : boolean
            is there a collision?
        """
        raise NotImplementedError("Abstract Base class")

    def _goal_reached(self, state):
        pos = np.array(state[0][:2])

        return np.linalg.norm(pos - self.goal) <= self.threshold


class DistanceDecreaseReward(BaseGoalReward):
    def __init__(self,
                 start,
                 goal,
                 threshold,
                 goal_reward=100.,
                 collision_reward=-10.,
                 step_reward=-0.5
                 ):
        """The constructor

        Parameters
        ----------
        start : list
            Start position
        goal : list
            goal position
        threshold : float
            Threshold to consider the goal reached
        goal_reward : float
            reward for reaching the goal
        collision_reward : float
            reward/penalty for colliding with an obstacle
        step_reward : float
            default reward per step
        """

        super().__init__(start=start,
                         goal=goal,
                         threshold=threshold,
                         goal_reward=goal_reward,
                         collision_reward=collision_reward,
                         step_reward=step_reward)

        self.reset()

    def __call__(self, state, collision):
        """Get the reward

        Parameters
        ----------
        state : list
            current state
        collision : boolean
            is there a collision?
        """
        if self._goal_reached(state):
            return self.goal_reward

        if collision:
            return self.collision_reward

        dist = np.linalg.norm(np.array(state[0][:2]) - self.goal)

        if (self.dist - dist) > 0.1:
            reward = self.step_reward
        else:
            reward = self.step_reward * -2.

        self.dist = dist
        return reward

    def reset(self):
        self.dist = np.linalg.norm(self.goal - self.start)
