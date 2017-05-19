# Problem 5


class Ball(object):

    WALL_X = 5  # A vertical line on a 2D coordinate system at x = 5

    def __init__(self, _vx=0.5, _vy=0.5):
        self.running = False
        self.x = 0  # Position X
        self.y = 0  # Position Y
        self.vx = _vx  # Velocity X
        self.vy = _vy  # Velocity Y

    def step(self):
        self.x += self.vx
        self.y += self.vy
        print("Stepped to %s, %s" % (self.x, self.y))

    def run(self, steps=50):
        if not self.running:
            self.running = True
            for s in range(steps):
                if self.x < self.WALL_X:
                    self.step()
                self.running = False
            print('Ball bounced off the wall ')


b = Ball()
b.run()
