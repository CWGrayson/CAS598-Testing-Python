NORMAL_LOW = 97  # normal human body temp lower end
NORMAL_HIGH = 99  # normal human body temp higher end
"""Creates the cut off threasholds for normal human body tempratures """

def sort_temperatures(measurements):
    """
    Inputs:
    Array of real numbers
    Outputs:
    3 arrays, low medium and high 
    containing the input arrays values sorted acording to how they
    fall with respect to the normal range of human body tempratures

    Sorting is carried out by an if elif statment to identify thse above, and bellow the normal and
    sorts remaning into the normal temprature array
    """
    low = []
    normal = []
    high = []

    for temperature in measurements:
        if temperature < NORMAL_LOW:
            low.append(temperature)
        elif temperature > NORMAL_HIGH:
            high.append(temperature)
        else:
            normal.append(temperature)

    return low, normal, high


def convert_from_fahrenheit(temps):
    """
    Purpose of fucntion is to convert the temprature from deggrees F (Deg F) into degrees C (Deg C)
    Inputs: array of real numbers representing temprature in Deg F
    Output: array of real numbers converted from Deg F to Deg C

    Method: (Temprature -32) divided by 1.8
    """
    results = [] 
    for temp in temps:
        results.append((temp-32)/1.8) #Each deg C increment is 9/5 of a deg F thus the division by 1.8

    return results

def convert_to_fahrenheit(temps):
        """
    Purpose is to convert a temprature reading from Deg C to Deg F
    Inputs: array of real numbers representing temprature in Deg C
    Output: array of real numbers converted from Deg C to Deg F

    Method: Temprature*1.8 +32
    """
    results = []
    for temp in temps:
        results.append(temp*1.8+32)

    return results
