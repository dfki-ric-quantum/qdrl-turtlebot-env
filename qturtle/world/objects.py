CUBOID = "cuboid"
SPHEROID = "spheroid"
CYLINDER = "cylinder"


def create_object(object_type,
                  object_kwargs,
                  sim,
                  rgba,
                  mass=0.,
                  collision=True):
    BUILDERS = {
        CUBOID: create_cuboid,
        SPHEROID: create_spheroid,
        CYLINDER: create_cylinder,
    }

    return BUILDERS[object_type](rgba=rgba,
                                 mass=mass,
                                 sim=sim,
                                 collision=collision,
                                 **object_kwargs)


def create_cuboid(sim,
                  half_extents,
                  bottom_center,
                  rgba,
                  mass=0.,
                  collision=True):

    base_position = bottom_center
    base_position[2] += half_extents[2]

    if collision:
        collision_shape = sim.createCollisionShape(sim.GEOM_BOX,
                                                   halfExtents=half_extents)
    else:
        collision_shape = -1

    return sim.createMultiBody(
        mass,
        baseCollisionShapeIndex=collision_shape,
        baseVisualShapeIndex=sim.createVisualShape(
            sim.GEOM_BOX, halfExtents=half_extents,
            rgbaColor=rgba),
        basePosition=base_position,
        baseOrientation=sim.getQuaternionFromEuler([0., 0., 0.])
    )


def create_spheroid(sim,
                    center,
                    radius,
                    rgba,
                    mass=0.,
                    collision=True):

    if collision:
        collision_shape = sim.createCollisionShape(sim.GEOM_SPHERE,
                                                   radius=radius)
    else:
        collision_shape = -1

    return sim.createMultiBody(
        mass,
        baseCollisionShapeIndex=collision_shape,
        baseVisualShapeIndex=sim.createVisualShape(sim.GEOM_SPHERE,
                                                   rgbaColor=rgba,
                                                   radius=radius),
        basePosition=center,
        baseOrientation=sim.getQuaternionFromEuler([0., 0., 0.])
    )


def create_cylinder(sim,
                    bottom_center,
                    radius,
                    height,
                    rgba,
                    mass=0.,
                    collision=True):

    center = bottom_center
    center[2] = height/2.

    if collision:
        collision_shape = sim.createCollisionShape(sim.GEOM_SPHERE,
                                                   height=height,
                                                   radius=radius)
    else:
        collision_shape = -1

    return sim.createMultiBody(
        mass,
        baseCollisionShapeIndex=collision_shape,
        baseVisualShapeIndex=sim.createVisualShape(sim.GEOM_CYLINDER,
                                                   rgbaColor=rgba,
                                                   radius=radius,
                                                   length=height),
        basePosition=center,
        baseOrientation=sim.getQuaternionFromEuler([0., 0., 0.])
    )
