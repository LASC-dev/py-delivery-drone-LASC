class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    """
    Representation of a common robot that can move along two cartesian axes.

    Attributes:
        name (str): name of the robot.
        weight (int | float): represents how many kg it weighs.
        coords (list): coordinates with two cartesian axes [x, y].
    """

    def __init__(
        self,
        name: str,
        weight: int | float,
        coords: list
    ) -> None:
        self.name = name
        self.weight = weight
        if self.coords is None:
            self.coords = [0, 0]
        self.coords = coords

    def go_forward(
        self,
        step: int = 1
    ) -> None:
        """
        Moves the robot forward by increasing the Y axis.

        Args:
            step (int): Number of steps to move. Defaults to 1.
        """
        self.coords[1] += step

    def go_back(
        self,
        step: int = 1
    ) -> None:
        """
        Moves the robot backward by decreasing the Y axis.

        Args:
            step (int): Number of steps to move. Defaults to 1.
        """
        self.coords[1] -= step

    def go_right(
        self,
        step: int = 1
    ) -> None:
        """
        Moves the robot to the right by increasing the X axis.

        Args:
            step (int): Number of steps to move. Defaults to 1.
        """
        self.coords[0] += step

    def go_left(
        self,
        step: int = 1
    ) -> None:
        """
        Moves the robot to the left by decreasing the X axis.

        Args:
            step (int): Number of steps to move. Defaults to 1.
        """
        self.coords[0] -= step

    def get_info(
        self
    ) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    """
    It represents a robot with the ability to fly.

    Aargs:
        name (str): the robot's name.
        weight (int | float): the robot's weight.
        coords (list[int]): the cardinal position along the
            three axes [x, y, z].
    """

    def __init__(
        self,
        name: str,
        weight: int | float,
        coords: list[int]
    ) -> None:
        super().__init__(name, weight)
        if coords is None:
            self.coords = [0, 0, 0]
        self.coords = coords

    def go_up(
        self,
        step: int = 1
    ) -> None:
        """
        Move the robot upwards by incrementing the z-axis.

        Args:
            step (int): Number of steps to move. The default value is 1.
        """
        self.coords[2] += step

    def go_down(
        self,
        step: int = 1
    ) -> None:
        """
        Move the robot downwards by decreasing the z-axis.

        Args:
        step (int): Number of steps to move. The default value is 1.
        """
        self.coords[2] -= step
