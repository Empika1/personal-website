import random

numLayers = 6
bgLayerStart = 15
bgLayerDiff = 1
bgStarLayerStart = 15
bgStarLayerDiff = 1

numStarsPerLayer = 25
numStarsDiff = 2
minSizePerLayer = 20
minSizeDiff = -3
maxSizePerLayer = 28
maxSizeDiff = -4
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
        print(f'<use href="#star" x={star[0]}px y={star[1]}px width={star[2]}px height={star[2]}px ' +
            f'style="transform-origin: {star[0] + star[2] // 2}px {star[1] + star[2] // 2}px; transform: rotate({star[3]}deg);"/>')

    print("</svg>")
    print("</div>")

    layer += 1