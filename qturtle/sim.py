import pybullet_utils.bullet_client as bc  # type: ignore
import pybullet as p  # type: ignore

import importlib.resources as pkg_resources

from . import robot

GRAVITY = -9.81


def setup_pybullet(dt, gui=False):
    """ Setup the pybullet simulation client

    Parameters
    ----------
    dt : float
        time resolution of the forward physics simulation
    gui : boolean
        Show the simulation gui?

    Returns
    -------
    BelletClient
        The pybullet simulation client
    """
    if gui:
        pb_sim = bc.BulletClient(connection_mode=p.GUI)
        pb_sim.resetDebugVisualizerCamera(cameraDistance=6.1,
                                          cameraYaw=90.,
                                          cameraPitch=-55.8,
                                          cameraTargetPosition=[-0.18,
                                                                1.88,
                                                                -1.3])
    else:
        pb_sim = bc.BulletClient(connection_mode=p.DIRECT)

    pb_sim.setRealTimeSimulation(0)
    pb_sim.setTimeStep(dt)
    pb_sim.setGravity(0., 0., GRAVITY)

    with pkg_resources.path(robot, 'plane.urdf') as urdf_path:
        pb_sim.loadURDF(str(urdf_path.resolve()))

    return pb_sim


def close_pybullet(pb_sim):
    """Close a simulation client

    Parameters
    ----------
    pb_sim : BulletClient
        The client to close
    """
    pb_sim.disconnect()
