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

starsymbol = """    <symbol id="star" viewBox="0 0 24 24">
        <path d="M12 2l3 7h7l-6 4 2 7-6-4-6 4 2-7-6-4h7z"/>
    </symbol>"""

styletemp = """    <style>
        use { fill: gold; }
    </style>"""

for layer in range(numLayers):
    bgLayer = bgLayerStart + layer * bgLayerDiff
    bgStarLayer = bgStarLayerStart + layer * bgStarLayerDiff

    numStars = numStarsPerLayer + layer * numStarsDiff
    minSize = minSizePerLayer + layer * minSizeDiff
    maxSize = maxSizePerLayer + layer * maxSizeDiff
    minPadding = minPadding + layer * minPaddingDiff

    with open(f"starsbg{bgLayer}.svg", "w") as f:
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

        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {maxX} {maxY}">\n')
        f.write(f"{starsymbol}\n")
        f.write(f"{styletemp}\n")

        for star in stars:
            f.write(f'    <use href="#star" x="{star[0]}" y="{star[1]}" width="{star[2]}" height="{star[2]}" ' +
                  f'transform="rotate({star[3]}deg {star[0] + star[2] // 2} {star[1] + star[2] // 2})" />\n')
        
        f.write('</svg>')