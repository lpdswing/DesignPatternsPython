# 桥接模式

class DrawingApi1:
    def draw_circle(self, x, y, radius):
        print(f'api1.circle at {x},{y},radius{radius}')


class DrawingApi2:
    def draw_circle(self, x, y, radius):
        print(f'api2.circle at {x},{y},radius{radius}')


class CircleShape:
    def __init__(self,x,y,radius,drawing_api):
        self.x = x
        self.y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        self._drawing_api.draw_circle(self.x,self.y,self._radius)

    def scale(self, pct):
        self._radius *= pct

def main():
    shapes = (
        CircleShape(1,2,3,DrawingApi1()),
        CircleShape(5,7,11,DrawingApi2())
    )
    for shape in shapes:
        shape.scale(2.5)
        shape.draw()

if __name__ == '__main__':
    main()