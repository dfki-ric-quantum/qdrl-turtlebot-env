from .colors import GOAL_COLOR, WALL_COLOR
from .objects import create_cuboid, create_spheroid


class Walls:
    def __init__(self, x_size, y_size, sim, height=0.6, thickness=0.04):
        self.x_size = x_size
        self.y_size = y_size

        self.sim = sim

        self.height = height
        self.thickness = thickness

        self.objects = []

        self._build_walls()

    def _build_walls(self):
        t_ext = self.thickness / 2.
        x_ext = self.x_size / 2.
        y_ext = self.y_size / 2.
        z_ext = self.height / 2.

        # Don't ask... just accept :)
        walls = [
            ([-t_ext, y_ext, 0.], [t_ext, y_ext, z_ext]),
            ([self.x_size + t_ext, y_ext, 0.], [t_ext, y_ext, z_ext]),
            ([x_ext, -t_ext, 0.], [x_ext + t_ext, t_ext, z_ext]),
            ([x_ext, self.y_size + t_ext, 0.], [x_ext + t_ext, t_ext, z_ext])
        ]

        for (pos, size) in walls:
            self.objects.append(
                create_cuboid(half_extents=size,
                              bottom_center=pos,
                              rgba=WALL_COLOR,
                              sim=self.sim)
            )


def draw_goal(x, y, sim, radius=0.4):
    return create_spheroid(center=[x, y, 0.],
                           radius=radius,
                           rgba=GOAL_COLOR,
                           collision=False,
                           sim=sim)
