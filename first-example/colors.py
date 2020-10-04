from matplotlib.colors import CSS4_COLORS as hexcolors
from matplotlib.colors import to_rgb

COLORS = {}
for name, color in hexcolors.items():
    COLORS[name] = [int(c*255) for c in to_rgb(color)]
