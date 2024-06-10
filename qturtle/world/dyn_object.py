import numpy as np
from .objects import create_object


class DynamicObject:
    def __init__(self, object_type, object_kwargs, sim, rgba, endpoints, velocity):
        self.object = create_object(
            object_type, object_kwargs=object_kwargs, sim=sim, rgba=rgba
        )
        sim.resetBaseVelocity(self.object, velocity, [0., 0., 0.])

        self.endpoints = endpoints
        self.turnaround = 0
        self.velocity = velocity

    def update(self, sim):
        pos, _ = sim.getBasePositionAndOrientation(self.object)
        turn = np.array(self.endpoints[self.turnaround])
        dist = np.linalg.norm(np.array(pos[0:2]) - turn)

        if dist <= 0.1:
            self.velocity = [v * -1 for v in self.velocity]
            sim.resetBaseVelocity(self.object, self.velocity, [0., 0., 0.])
            self.turnaround = (self.turnaround + 1) % 2
