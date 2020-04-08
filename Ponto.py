class Ponto:
    def __init__(self, x,y,w=1):
        self.x = x
        self.y = y
        self.w = w

    def subtract(self, p):
    	return Ponto(self.x - p.x, self.y - p.y)