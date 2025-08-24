import random

numLayers = 3
bgLayerStart = 18
bgLayerDiff = 1
bgStarLayerStart = 18
bgStarLayerDiff = 1

numStarsPerLayer = 65
numStarsDiff = 25
minSizePerLayer = 18
minSizeDiff = -5
maxSizePerLayer = 30
maxSizeDiff = -7
minPadding = 10
minPaddingDiff = 0

maxX = 1920
maxY = 1920

layer = 0
while layer < numLayers:
    bgLayer = bgLayerStart + layer * bgLayerDiff
    bgStarLayer = bgStarLayerStart + layer * bgStarLayerDiff

    numStars = numStarsPerLayer + layer * numStarsDiff
    minSize = minSizePerLayer + layer * minSizeDiff
    maxSize = maxSizePerLayer + layer * maxSizeDiff
    minPadding = minPadding + layer * minPaddingDiff

    print(f'<div class="bg{bgLayer}">')
    print(f'<svg class="bg{bgStarLayer}-stars" xmlns="http://www.w3.org/2000/svg">')

    stars = []

    i = 0
    while i < numStars:
        x = random.randint(0, maxX)
        y = random.randint(0, maxY)
        size = random.randint(minSize, maxSize)
        rotation = random.randint(0, 360)

        fail = False
        for star in stars:
            if (x - star[0]) ** 2 + (y - star[1]) ** 2 < (size + star[2] + minPadding) ** 2:
                fail = True
                break
        if not fail:
            stars.append((x, y, size, rotation))
            i += 1

    for star in stars:
        print(f'<use xlink:href="#star" x="{star[0]}" y="{star[1]}" width="{star[2]}" height="{star[2]}" ' +
            f'transform="rotate({star[3]} {star[0] + star[2] // 2} {star[1] + star[2] // 2})"/>')

    print("</svg>")
    print("</div>")

    layer += 1