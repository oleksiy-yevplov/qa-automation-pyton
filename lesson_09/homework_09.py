class Diamond:
    def __init__(self, side, alpha):
        if side>0:
            self.side=side
        else:    
            print("Сторона має бути більше 0")
        if 0<alpha>180:
            self.alpha=alpha
            self.beta=180-alpha
        else:
            print("Кут має бути від 0 до 180 градусів")        
