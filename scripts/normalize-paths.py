import os
from svgpathtools import svg2paths, wsvg, Path, Line, CubicBezier, QuadraticBezier, Arc

def arc_to_cubic(segment):
    """Convert Arc segments to CubicBezier segments; keep other segments unchanged."""
    if isinstance(segment, Arc):
        return segment.as_cubic_curves()
    else:
        return [segment]

def normalize_svg_paths(input_file, output_file):
    paths, attributes = svg2paths(input_file)

    new_paths = []
    new_attributes = []

    for path, attr in zip(paths, attributes):
        new_segments = []
        for segment in path:
            new_segments.extend(arc_to_cubic(segment))
        new_paths.append(Path(*new_segments))
        new_attributes.append(attr)

    wsvg(new_paths, attributes=new_attributes, filename=output_file)
    print(f"Normalized SVG saved to {output_file}")

if __name__ == "__main__":
    # Example usage: process multiple SVGs in a folder
    input_svgs = [f"clouds/cccloud({i}).svg" for i in range(1, 25)]  # replace with your SVG filenames
    output_dir = "normalized_svgs"
    os.makedirs(output_dir, exist_ok=True)

    for svg_file in input_svgs:
        output_file = os.path.join(output_dir, os.path.basename(svg_file))
        normalize_svg_paths(svg_file, output_file)