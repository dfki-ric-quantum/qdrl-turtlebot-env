from gym.spaces import Discrete


class StepControl:
    def __init__(self, base_speed, steps, seed=None):
        """ The constructor
        base_speed : float
            Base velocity by which to scale in each step
        steps : list
            list of tuples containing scaling for the left and right wheel, as well as the number
            of simulation steps to execute the target velocities. Length of the list defines the
            number of actions.
        seed : int
            random seed for the action space obhect to sample from
        """
        self.base_speed = base_speed
        self.n_actions = len(steps)
        self.seed = seed

        self.steps = []

        for (left, right, sim_steps) in steps:
            self.steps.append((
                self.base_speed * left,
                self.base_speed * right,
                sim_steps
            ))

    def __call__(self, input):
        """ Call control and get target velocities
        input : int
            index for self.steps

        Returns
        -------
        tuple[float, float, int]
            Target velocity for left and right wheel, as well as the number of simulation steps.
        """
        return self.steps[input]

    def get_action_space(self):
        return Discrete(n=self.n_actions, seed=self.seed)
