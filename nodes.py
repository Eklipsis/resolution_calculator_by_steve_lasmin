# Resolution Calculator by Steve Lasmin
# https://boosty.to/stevelasmin

import math

class Resolution_Calculator_by_Steve_Lasmin:
    """
    Calculates width and height based on a maximum dimension,
    aspect ratio (as width:height), and a target multiplier.
    Ensures the final dimensions are divisible by the multiplier.

    Resolution Calculator by Steve Lasmin
    https://boosty.to/stevelasmin
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "resolution": ("INT", {
                    "default": 1024,
                    "min": 64,
                    "max": 2048,
                    "step": 64,
                    "display": "slider"
                }),
                "width_ratio": ("INT", {
                    "default": 16,
                    "min": 1,
                    "max": 999999,
                    "step": 1,
                    "display": "number"
                }),
                "height_ratio": ("INT", {
                    "default": 9,
                    "min": 1,
                    "max": 999999,
                    "step": 1,
                    "display": "number"
                }),
                "multiplier": ([16, 32, 64], {
                    "default": 32
                }),
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "calculate"
    CATEGORY = "utils"

    def calculate(self, resolution, width_ratio, height_ratio, multiplier):
        aspect = width_ratio / height_ratio

        # Resolution = maximum dimension (longest side)
        if aspect >= 1:
            width = resolution
            height = resolution / aspect
        else:
            height = resolution
            width = resolution * aspect

        # Round to nearest multiple of multiplier
        width = round(width / multiplier) * multiplier
        height = round(height / multiplier) * multiplier

        # Ensure minimum dimensions
        width = max(multiplier, width)
        height = max(multiplier, height)

        return (int(width), int(height))


NODE_CLASS_MAPPINGS = {
    "Resolution_Calculator_by_Steve_Lasmin": Resolution_Calculator_by_Steve_Lasmin,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Resolution_Calculator_by_Steve_Lasmin": "Resolution Calculator by Steve Lasmin",
}
