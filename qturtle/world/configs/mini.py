import numpy as np
from ..colors import SOLID_BLUE
from ..objects import CUBOID

OBSTACLES = [
    (CUBOID,
        {"rgba": SOLID_BLUE},
        {
            "bottom_center": [0.5, 1.5, 0.0],
            "half_extents": [0.5, 0.5, 0.3]
        }
     ),
    (CUBOID,
        {"rgba": SOLID_BLUE},
        {
            "bottom_center": [2.5, 1.5, 0.0],
            "half_extents": [0.5, 0.5, 0.3]
        }
     ),
]

FREE_POSITIONS = [
    [0.5, 0.5], [0.5, 2.5], [1.5, 0.5], [1.5, 1.5],
    [1.5, 2.5], [2.5, 0.5], [2.5, 2.5]
]

FREE_ANGLES = [
    0., np.pi*0.5, np.pi, np.pi*1.5
]

MINI_S_CURVE = {
    "repr": "Mini S Curve",

    "setup": {
        "x_size": 3,
        "y_size": 3,
        "start": [[0.5, 0.5], 0.],
        "goal": [2.5, 2.5],
    },

    "objects": OBSTACLES
}
