import pyvista as pv
from pyvista.demos import logo
alien_str = """
    %         %
      %     %
    % % % % % %
  % %   % %   % %
% % % % % % % % % %
%   % % % % % %   %
%   %         %   %
%   % %     % %   %
      %     %
    %         %
"""


alien = []
for line in alien_str.splitlines()[1:]:  # skip first linebreak
    if not line:
        continue
    if len(line) < 20:
        line += (20 - len(line)) * ' '
    alien.append([line[i : i + 2] == '% ' for i in range(0, len(line), 2)])

def draw_pixels(plotter, pixels, center, color):
    bounds = [
        center[0] - 1.0,
        center[0] + 1.0,
        center[1] - 1.0,
        center[1] + 1.0,
        -10.0,
        +10.0,
    ]
    for rows in pixels:
        for pixel in rows:
            if pixel:
                box = pv.Box(bounds=bounds)
                plotter.add_mesh(box, color=color)
            bounds[0] += 2.0
            bounds[1] += 2.0
        bounds[0] = center[0] - 1.0
        bounds[1] = center[0] + 1.0
        bounds[2] += -2.0
        bounds[3] += -2.0
    return plotter

# Display MONSTERS
p = pv.Plotter()
p = draw_pixels(p, alien, [-22.0, 22.0], "green")
p = draw_pixels(p, alien, [0.0, 22.0], "green")
p = draw_pixels(p, alien, [22.0, 22.0], "green")
p = draw_pixels(p, alien, [-22.0, 0.0], "blue")
p = draw_pixels(p, alien, [0.0, 0.0], "blue")
p = draw_pixels(p, alien, [22.0, 0.0], "blue")
p = draw_pixels(p, alien, [-22.0, -22.0], "red")
p = draw_pixels(p, alien, [0.0, -22.0], "red")
p = draw_pixels(p, alien, [22.0, -22.0], "red")

text = logo.text_3d("ALIEN MONSTERS", depth=10.0)
text.points = text.points * 4.0
text.translate([-20.0, 24.0, 0.0], inplace=True)

p.add_mesh(text, color="yellow")
p.show(cpos="xy")