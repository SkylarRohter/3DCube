three = __import__('3d.Render3D')
two = __import__('2d.Render2D')
threedee = False


if threedee:
    three.Render3D.render()
else:
    two.Render2D.render()
