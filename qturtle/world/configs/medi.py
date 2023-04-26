from ..colors import SOLID_RED, SOLID_BLUE
from ..objects import CUBOID, CYLINDER

MEDI_WORLD_V0 = {
    "repr": "Medi World V0",

    "setup": {
        "x_size": 4,
        "y_size": 4,
        "start": [[0.5, 0.5], 0.],
        "goal": [3.5, 3.5],
        "resets": []
    },

    "objects": [
        (CUBOID,
            {"rgba": SOLID_BLUE},
            {
                "bottom_center": [0.75, 1., 0.0],
                "half_extents": [0.75, 0.1, 0.3]
            }
         ),
        (CUBOID,
            {"rgba": SOLID_BLUE},
            {
                "bottom_center": [1.0, 3.5, 0.0],
                "half_extents": [1.0, 0.5, 0.3]
            }
         ),
        (CUBOID,
            {"rgba": SOLID_BLUE},
            {
                "bottom_center": [3.5, 0.5, 0.0],
                "half_extents": [0.5, 0.5, 0.3]
            }
         ),
        (CYLINDER,
            {"rgba": SOLID_RED},
            {
                "bottom_center": [1.8, 2.0, 0.0],
                "radius": 0.2,
                "height": 0.6
            }
         ),
        (CYLINDER,
            {"rgba": SOLID_RED},
            {
                "bottom_center": [3.0, 2.0, 0.0],
                "radius": 0.2,
                "height": 0.6
            }
         ),
    ]
}
