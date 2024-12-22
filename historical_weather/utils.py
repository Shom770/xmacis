"""Utility functions and classes packed with the historical_weather package itself."""

__all__ = ["calculate_awssi_index"]


def calculate_awssi_index(
    maximum_temperature: int,
    minimum_temperature: int,
    snowfall: int,
    snow_depth: int
) -> int:
    """Calculates the AWSSI index for a given day.
    The AWSSI index was created by the Midwestern Regional Climate Center and more information on it can be found at https://mrcc.purdue.edu/research/awssi.

    :param maximum_temperature: The high temperature for a day.
    :param minimum_temperature: The low temperature for a day.
    :param snowfall: The snow that fell on a certain day.
    :param snow_depth: The snow depth on a certain day.
    :return: The accumulated AWSSI index for a certain day.
    """
    # For our purposes, a trace of snow won't change the pointage.
    snowfall = 0 if snowfall == "T" else snowfall
    snow_depth = 0 if snow_depth == "T" else snow_depth

    points = 0

    # Calculate points based off the high temperature.
    if 25 <= maximum_temperature <= 32:
        points += 1
    elif 20 <= maximum_temperature <= 24:
        points += 2
    elif 15 <= maximum_temperature <= 19:
        points += 3
    elif 10 <= maximum_temperature <= 14:
        points += 4
    elif 5 <= maximum_temperature <= 9:
        points += 5
    elif 0 <= maximum_temperature <= 4:
        points += 6
    elif -5 <= maximum_temperature <= -1:
        points += 7
    elif -10 <= maximum_temperature <= -6:
        points += 8
    elif -15 <= maximum_temperature <= -11:
        points += 9
    elif -20 <= maximum_temperature <= -16:
        points += 10
    elif maximum_temperature < -20:
        points += 15

    # Calculate points based off the low temperature
    if 25 <= minimum_temperature <= 32:
        points += 1
    elif 20 <= minimum_temperature <= 24:
        points += 2
    elif 15 <= minimum_temperature <= 19:
        points += 3
    elif 10 <= minimum_temperature <= 14:
        points += 4
    elif 5 <= minimum_temperature <= 9:
        points += 5
    elif 0 <= minimum_temperature <= 4:
        points += 6
    elif -5 <= minimum_temperature <= -1:
        points += 7
    elif -10 <= minimum_temperature <= -6:
        points += 8
    elif -15 <= minimum_temperature <= -11:
        points += 9
    elif -20 <= minimum_temperature <= -16:
        points += 10
    elif -25 <= minimum_temperature <= -21:
        points += 11
    elif -35 <= minimum_temperature <= -26:
        points += 15
    elif minimum_temperature < -35:
        points += 20

    # Calculate points based off the snow that fell on that day.
    if 0.1 <= snowfall <= 0.9:
        points += 1
    elif 1 <= snowfall <= 1.9:
        points += 2
    elif 2 <= snowfall <= 2.9:
        points += 3
    elif 3 <= snowfall <= 3.9:
        points += 4
    elif 4 <= snowfall <= 4.9:
        points += 6
    elif 5 <= snowfall <= 5.9:
        points += 7
    elif 6 <= snowfall <= 6.9:
        points += 9
    elif 7 <= snowfall <= 7.9:
        points += 10
    elif 8 <= snowfall <= 8.9:
        points += 12
    elif 9 <= snowfall <= 9.9:
        points += 13
    elif 10 <= snowfall <= 11.9:
        points += 14
    elif 12 <= snowfall <= 14.9:
        points += 18
    elif 15 <= snowfall <= 17.9:
        points += 22
    elif 18 <= snowfall <= 23.9:
        points += 26
    elif 24 <= snowfall <= 29.9:
        points += 36
    elif snowfall >= 30:
        points += 45

    # Calculate points based off the snow that's on the ground.
    if snow_depth == 1:
        points += 1
    elif snow_depth == 2:
        points += 2
    elif snow_depth == 3:
        points += 3
    elif 4 <= snow_depth <= 5:
        points += 4
    elif 6 <= snow_depth <= 8:
        points += 5
    elif 9 <= snow_depth <= 11:
        points += 6
    elif 12 <= snow_depth <= 14:
        points += 7
    elif 15 <= snow_depth <= 17:
        points += 8
    elif 18 <= snow_depth <= 23:
        points += 9
    elif 24 <= snow_depth <= 35:
        points += 10
    elif snow_depth >= 36:
        points += 15

    return points