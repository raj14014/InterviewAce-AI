"""
InterviewAce AI
Professional Gaze Estimator
"""

from app.ai.utils import distance


class GazeEstimator:

    @staticmethod
    def horizontal_ratio(iris_center, eye_outer, eye_inner):
        """
        Horizontal iris position inside the eye.

        Returns:
            ratio (0.0 - 1.0)
        """

        x_outer = eye_outer[0]
        x_inner = eye_inner[0]
        x_iris = iris_center[0]

        left = min(x_outer, x_inner)
        right = max(x_outer, x_inner)

        width = right - left

        if width <= 1:
            return 0.5

        ratio = (x_iris - left) / width

        ratio = max(0.0, min(1.0, ratio))

        return ratio

    @staticmethod
    def estimate(
        left_center,
        right_center,
        left_outer,
        left_inner,
        right_outer,
        right_inner,
    ):

        left_ratio = GazeEstimator.horizontal_ratio(
            left_center,
            left_outer,
            left_inner,
        )

        right_ratio = GazeEstimator.horizontal_ratio(
            right_center,
            right_outer,
            right_inner,
        )

        average = (left_ratio + right_ratio) / 2

        return (
            average,
            left_ratio,
            right_ratio,
        )