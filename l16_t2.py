class Turtle:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
    
    def go_up(self):
        self.y += self.s
    
    def go_down(self):
        self.y -= self.s
    
    def go_left(self):
        self.x -= self.s
    
    def go_right(self):
        self.x += self.s
    
    def evolve(self):
        self.s += 1
    
    def degrade(self):
        if self.s <= 1:
            raise ValueError("s не может быть меньше или равно 0")
        self.s -= 1

    def count_moves(self, x2, y2):
        dx = abs(self.x - x2)
        dy = abs(self.y - y2)
        # Определение необходимого количества перемещений по горизонтали и вертикали
        moves_x = (dx + self.s - 1) // self.s
        moves_y = (dy + self.s - 1) // self.s
        return max(moves_x, moves_y) 

# Пример использования класса
turtle = Черепашка(0, 0, 3)
turtle.go_up()
turtle.go_right()
turtle.evolve()
turtle.degrade()
print(turtle.x, turtle.y, turtle.s)  # Ожидаемое состояние после выполнения действий

# Расчет количества ходов до заданной точки
print(turtle.count_moves(10, 15))
