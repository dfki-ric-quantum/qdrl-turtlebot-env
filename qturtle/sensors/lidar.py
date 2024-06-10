import numpy as np

MAX_RAY_LEN = 100
RAY_COLOR = [0.88, 0.56, 0.06]


class Lidar:
    def __init__(self, n_rays, half_range=np.pi / 2.0, gui=False):
        assert n_rays > 1 and half_range <= np.pi

        self.n_rays = n_rays
        self.half_range = half_range
        self.gui = gui

    def __call__(self, sim, robot):
        link_info = sim.getLinkState(robot.robot, robot.LIDAR_LINK)
        rho = sim.getEulerFromQuaternion(link_info[1])[2]
        pos = link_info[0]

        angle = rho - self.half_range
        step = (2 * self.half_range) / (self.n_rays - 1)
        ray_from = []
        ray_to = []

        for _ in range(self.n_rays):
            ray_from.append(pos)
            ray_to.append(
                [
                    pos[0] + MAX_RAY_LEN * np.cos(angle),
                    pos[1] + MAX_RAY_LEN * np.sin(angle),
                    pos[2],
                ]
            )
            angle += step

        intersections = sim.rayTestBatch(ray_from, ray_to, numThreads=0)
        distances = []

        for rf, rt, ins in zip(ray_from, ray_to, intersections):
            target = rt

            if ins[0] < 0:
                distances.append(MAX_RAY_LEN)
            else:
                target = ins[3]
                distances.append(np.linalg.norm(np.array(rf) - np.array(target)))

            if self.gui:
                sim.addUserDebugLine(rf, target, RAY_COLOR)

        sim.removeAllUserDebugItems()

        return distances
