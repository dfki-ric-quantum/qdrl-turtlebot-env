from .builders import default_builder, lidar_env_builder


def make(env, **kwargs):
    """Make a qturtle environment
    env : str
        Key to identify the environment to build, currently supported DEFAULT_3x3_V0,
        DEFAULT_4x4_V0 and DEFAULT_5x5_V0
    **kwargs
        Additional parameters to pass to the builder function

    Returns
    -------
    qturtle.env.GymEnvironment
        The build environment
    """
    tokens = env.split('_')
    key = tokens[0]
    world = tokens[1]
    # version = tokens[2]

    builder_kwargs = {
        "world": world
    }

    if key == 'DEFAULT':
        builder = default_builder
    elif key == 'LIDAR':
        builder = lidar_env_builder
    else:
        raise ValueError(f"{env} has no builder function specified")

    return builder(**builder_kwargs, **kwargs)
