import numpy as np
from termcolor import colored
import subprocess

# Список тем и их цвета
THEMES = {
    "oreo_black_cursors":            ( 66, 66, 66    ),
    "oreo_blue_cursors":             ( 99, 96, 242   ),
    "oreo_grey_cursors":             ( 82, 109, 123  ),
    "oreo_pink_cursors":             ( 253, 4, 133   ),
    "oreo_purple_cursors":           ( 143, 20, 198  ),
    "oreo_red_cursors":              ( 255, 0, 37    ),
    "oreo_spark_blue_cursors":       ( 121, 0, 255   ),
    "oreo_spark_dark_cursors":       ( 34, 34, 34    ),
    "oreo_spark_green_cursors":      ( 20, 169, 0    ),
    "oreo_spark_light_pink_cursors": ( 255, 117, 199 ),
    "oreo_spark_lime_cursors":       ( 218, 254, 0   ),
    "oreo_spark_lite_cursors":       ( 254, 254, 254 ),
    "oreo_spark_orange_cursors":     ( 255, 171, 0   ),
    "oreo_spark_pink_cursors":       ( 255, 0, 166   ),
    "oreo_spark_purple_cursors":     ( 174, 0, 255   ),
    "oreo_spark_red_cursors":        ( 255, 42,  76  ),
    "oreo_spark_violet_cursors":     ( 124, 0, 205   ),
    "oreo_teal_cursors":             ( 0, 158, 138   ),
    "oreo_white_cursors":            ( 198, 198, 198 )
}

# Корень не вычисляем, нам нужно только относительное расстояние
def GetDistanceSqr(color1, color2) -> int :
    return sum( (c1 - c2 )**4 for c1, c2 in zip(color1, color2) )


# Определяем ближайший цвет из списка
def WhatSimiliarColor(color, colors = THEMES) -> str :
    return min(colors, key = lambda c : GetDistanceSqr(colors[c], color))

def main():
    r, g, b = map(int, (input().split()))

    color = (r, g, b)
    print(colored(f"for color: {color}", color))

    theme = WhatSimiliarColor(color)
    print(colored(f"theme is {theme}", THEMES[theme]))
    
    subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "cursor-theme", f"\"{theme}\""])

if __name__ == "__main__":
    main()