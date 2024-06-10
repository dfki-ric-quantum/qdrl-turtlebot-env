
from ..colors import SOLID_RED, SOLID_BLUE, SOLID_PURPLE
from ..objects import CYLINDER, CUBOID

LIDAR_DYN_COMP = {
    "repr": "Dynamic Lidar env / complex",

    "setup": {
        "x_size": 10,
        "y_size": 12,
        "start": [[5., 6.], 0.],
        "multi_goal": True,
        "goals": [[.5, .5], [9.5, 0.5], [0.5, 11.5], [9.5, 11.5]],
        "resets": []
    },

    "objects": [
        (CYLINDER,
            {"rgba": SOLID_RED},
            {
                "bottom_center": [4.0, 5.0, 0.0],
                "radius": 0.2,
                "height": 0.6
            }
         ),
        (CYLINDER,
            {"rgba": SOLID_RED},
            {
                "bottom_center": [6.0, 5.0, 0.0],
                "radius": 0.2,
                "height": 0.6
            }
         ),
        (CYLINDER,
            {"rgba": SOLID_RED},
            {
                "bottom_center": [4.0, 7.0, 0.0],
                "radius": 0.2,
                "height": 0.6
            }
         ),
        (CYLINDER,
            {"rgba": SOLID_RED},
            {
                "bottom_center": [6.0, 7.0, 0.0],
                "radius": 0.2,
                "height": 0.6
            }
        ),
        (CUBOID,
            {"rgba": SOLID_BLUE},
            {
                "bottom_center": [1.0, 6.0, 0.0],
                "half_extents": [1., 0.2, 0.3]
            }
        ),
        (CUBOID,
            {"rgba": SOLID_BLUE},
            {
                "bottom_center": [2.2, 6.0, 0.0],
                "half_extents": [0.2, 2.5, 0.3]
            }
        ),
        (CUBOID,
            {"rgba": SOLID_BLUE},
            {
                "bottom_center": [2.5, 0.5, 0.0],
                "half_extents": [0.5, 0.5, 0.3]
            }
        ),
        (CUBOID,
            {"rgba": SOLID_BLUE},
            {
                "bottom_center": [3.5, 11.5, 0.0],
                "half_extents": [0.5, 0.5, 0.3]
            }
        ),
        (CUBOID,
            {"rgba": SOLID_BLUE},
            {
                "bottom_center": [8.0, 3.0, 0.0],
                "half_extents": [1.2, 0.2, 0.3]
            }
        ),
        (CUBOID,
            {"rgba": SOLID_BLUE},
            {
                "bottom_center": [8.0, 0.5, 0.0],
                "half_extents": [0.2, 0.5, 0.3]
            }
        ),
        (CUBOID,
            {"rgba": SOLID_BLUE},
            {
                "bottom_center": [8.0, 6.0, 0.0],
                "half_extents": [0.4, 0.4, 0.3]
            }
        ),
        (CUBOID,
            {"rgba": SOLID_BLUE},
            {
                "bottom_center": [7.0, 10.5, 0.0],
                "half_extents": [0.2, 1.5, 0.3]
            }
        ),
        (CUBOID,
            {"rgba": SOLID_BLUE},
            {
                "bottom_center": [9.5, 9.5, 0.0],
                "half_extents": [0.5, 0.2, 0.3]
            }
        ),
    ],

    "dyn_objects": [
        (CYLINDER,
            {"rgba": SOLID_PURPLE},
            {
                "bottom_center": [3.0, 2.0, 0.0],
                "radius": 0.2,
                "height": 0.6
            },
            {
                "endpoints": ([4.5, 0.5], [0.5, 4.5]),
                "velocity": [0.1, -0.1, 0.]
            }
         ),
        (CYLINDER,
            {"rgba": SOLID_PURPLE},
            {
                "bottom_center": [4.0, 10.0, 0.0],
                "radius": 0.2,
                "height": 0.6
            },
            {
                "endpoints": ([3.0, 9.0], [5.5, 11.5]),
                "velocity": [-0.15, -0.15, 0.]
            }
         ),
        (CYLINDER,
            {"rgba": SOLID_PURPLE},
            {
                "bottom_center": [8.0, 5.0, 0.0],
                "radius": 0.2,
                "height": 0.6
            },
            {
                "endpoints": ([4.5, 1.5], [9.5, 6.5]),
                "velocity": [-0.1, -0.1, 0.]
            }
         ),
        (CYLINDER,
            {"rgba": SOLID_PURPLE},
            {
                "bottom_center": [8.5, 8.5, 0.0],
                "radius": 0.2,
                "height": 0.6
            },
            {
                "endpoints": ([9.5, 8.5], [3.5, 8.5]),
                "velocity": [0.2, 0., 0.]
            }
         ),
    ]
}
