"""Generate isolines from a numpy array of elevation data."""

import numpy as np

def _generate_isoline(elevation, line):
    """Generate an isoline from a numpy array of elevation data.

    Parameters
    ----------
    elevation : numpy array
        A numpy array of elevation data.
    line : float
        The elevation value for which to generate an isoline.

    Returns
    -------
    list
        A list of points in a clockwise traversal of the isoline.

    Notes
    -----
    This function is called by generate_isolines().

    """
    raise NotImplementedError()

def generate_isolines(elevation, lines=None, interval=None, min_elevation=None, max_elevation=None, n_lines=10):
    """Generate isolines from a numpy array of elevation data.

    Parameters
    ----------
    elevation : numpy array
        A numpy array of elevation data.
    lines : list of floats, optional
        A list of elevation values for which to generate isolines.
    interval : float, optional
        The interval between isolines. Used only if nothing is passed for lines.
    min_elevation : float, optional
        The minimum elevation value for which to generate isolines.
    max_elevation : float, optional
        The maximum elevation value for which to generate isolines.
    n_lines : int, optional
        The number of isolines to generate. Used only if nothing is passed for lines or interval. Default is 10.

    Returns
    -------
    list
        A list of isolines, where each isoline is a list of points in a clockwise traversal of the isoline.

    Notes
    -----
    If lines is not None, then interval, min_elevation, max_elevation, and n_lines are ignored.

    """
    raise NotImplementedError()
    