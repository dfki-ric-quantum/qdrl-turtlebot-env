import argparse
import time
import qturtle

from functools import partial
import inspect
from IPython.terminal.embed import InteractiveShellEmbed  # type: ignore


# Working trajectories for each of the three environments
T_SMALL = [
    0, 0, 0, 2, 0, 0, 2, 0, 0, 0,
    0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0
]

T_MEDI = [
    0, 0, 0, 0, 0, 0, 2, 0, 0, 0,
    0, 0, 2, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 0, 0,
]

T_LARGE = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 2, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 2, 0, 0, 0, 0, 2, 0, 0,
    0, 0, 0, 1, 0, 0, 0, 0, 0, 1,
    0, 0, 0, 0,
]


def parse_args():
    """Parse command line args

    Returns
    -------
    Namespace
        The parsed arguments
    """
    parser = argparse.ArgumentParser(description="Test default env")
    parser.add_argument(
        "-w", type=str, required=True, dest="world", choices=["3x3", "4x4", "5x5", "LDC"]
    )

    return parser.parse_args()


def db_stop():
    """Stop program execution and launch ipython REPL at current stack frame

    Returns
    -------
    bool
        True if shell was launched, False otherwise
    """
    ipython_shell = InteractiveShellEmbed(
        banner1="--- Turtlebot environment -----",
    )

    frame = inspect.currentframe()

    if frame:
        frame = frame.f_back
        filename = frame.f_code.co_filename  # type: ignore
        linenumber = frame.f_lineno  # type: ignore

        msg = f"Stopped at {filename} at line {linenumber}"
        ipython_shell(msg, stack_depth=2)

        return True
    else:
        return False


def drive_random(env, max_steps):
    """Drive random trajectory
    env : environment
        The envionment
    max_steps : int
        Maximum number of steps for the random trajectory
    """
    steps = 0

    env.reset()
    while steps < max_steps:
        _, _, done, _ = env.step(env.action_space.sample())
        time.sleep(0.25)
        steps += 1

        if done:
            break


def drive_trajectory(env, trajectory):
    """Drive a given trajectory in the environment

    Parameters
    ----------
    env : environment
        The environment
    trajectory : list[int]
        List of actions to execute
    """
    steps = 0
    total_reward = 0
    done = False

    env.reset()

    for t in trajectory:
        state, reward, done, _ = env.step(t)
        time.sleep(0.25)
        total_reward += reward

        print(f"State: {state}, reward: {reward}, done: {done}")

        if done:
            break

        steps += 1

    print(f"Total steps: {steps}, total reward: {total_reward}")


if __name__ == "__main__":
    envs = {
        "3x3": ("DEFAULT_3x3_V0", T_SMALL),
        "4x4": ("DEFAULT_4x4_V0", T_MEDI),
        "5x5": ("DEFAULT_5x5_V0", T_LARGE),
        "LDC": ("LIDAR_LDC_V0", []),
    }

    args = parse_args()

    env = qturtle.make(envs[args.world][0], gui=True)
    env.reset()

    drive = partial(drive_trajectory, env, envs[args.world][1])

    debug = db_stop()

    if not debug:
        print("Not started with ipython, running trajectory in 5 seconds...")
        time.sleep(5)
        print("... go!")
        drive()
