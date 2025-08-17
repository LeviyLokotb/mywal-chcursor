import numpy as np
from PIL import Image
from sklearn.cluster import KMeans

import argparse
from termcolor import colored

def getColors(imagePath : str, colorsCount : int = 1):
    img = Image.open(imagePath)

    # Меняем размер для ускорения
    img = img.resize( (200, 300) )
    arr = np.array(img)

    # Преобразование в список пикселей в RGB
    pixels = arr.reshape(-1, 3)
    
    # Вычисление кластеров
    clusters = KMeans(n_clusters=colorsCount) # , random_state=42) # сид для рандома
    clusters.fit(pixels)

    # Получаем основные цвета - центры кластеров
    colors = clusters.cluster_centers_.astype(int)

    if len(colors) <= 1:
        return colors
    
    # Вычисляем яркость каждого цвета
    MAGIC_RATIO = [0.299, 0.587, 0.114] # специальные коэффициенты для "человеческой" яркости
    brightness = colors @ MAGIC_RATIO   # @ - матричное умножение в NumPy

    # Сортируем по яркости
    sortedColors = colors[np.argsort(brightness)]

    sortedColors = sorted(colors, key=lambda c: (c[0] - c[1])**2 + (c[1] - c[2])**2 + (c[2] - c[0])**2 )
    return sortedColors

def savePaletteTo(data : str, outputFile : str):
    with open(outputFile, 'w') as f:
        f.write(data)



def main():
    # Создаём парсер аргументов
    parser = argparse.ArgumentParser(description="Определение основных цветов изображения")

    parser.add_argument("-i", "--image", type=str, help="путь к изображению", required=True)
    parser.add_argument("-c", "--count", type=int, default=1, help="число определяемых цветов")
    parser.add_argument("-m", "--minimalism", action="store_true", help="Вывести только код первого цвета")
    parser.add_argument("-p", "--pixels", action="store_true", help="вывести только цвет в терминале")
    parser.add_argument("-o", "--output", type=str, help="сохранить в файл")
    parser.add_argument("-x", "--hex", action="store_true", help="цвета в 16-ричном формате")


    # Парсим args
    args = parser.parse_args()

    saved = ""
    # Запускаем программу
    colors = getColors(args.image, args.count)

    if args.minimalism:
        r, g, b = colors[-1]
        if args.hex:
            thing = f"{r:02x} {g:02x} {b:02x}"
        else:
            thing = f"{r} {g} {b}"
        print(thing)
        return

    for color in colors:
        r, g, b = color
        if args.pixels:
            thing = colored("■■■", (r, g, b) )
        else:
            if args.hex:
                thing = f"{r:02x} {g:02x} {b:02x}"
            else:
                thing = f"{r} {g} {b}"
        print(colored(thing, (r, g, b)))
        if args.output:
            saved += thing + '\n'

    if args.output:
        savePaletteTo(saved, args.output)


if __name__ == "__main__":
    main()


