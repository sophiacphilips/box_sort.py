#Name: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 01/31/23
#This project is designed to get three values for a box (length, width, and height), calculate the volume for each box, and use insertion
#sorting to organize each box from largest volume to smallest.


class Box:
    """ The Box class takes parameters length, width, and height and initializes them to their data members"""
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height

    def volume(self):
        """method to calculate volume of a box length x width x height"""
        return self._length*self._width*self._height

    def get_length(self):
        """get method for length"""
        return self._length

    def get_width(self):
        """get method for width"""
        return self._width

    def get_height(self):
        """get method for height"""
        return self._height


def box_sort(box_list):
    """This function is designed to use insertion sorting to sort a list of boxes
    from greatest volume to least volume"""
    for index in range(1, len(box_list)):
        value = box_list[index]
        pos = index - 1
        while pos >= 0 and value.volume() > box_list[pos].volume():
            box_list[pos + 1] = box_list[pos]
            pos -= 1
        box_list[pos + 1] = value








