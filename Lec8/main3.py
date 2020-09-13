class BaseFigure:
    def __init__(self, color_var:str="0fffffff", material_var:str="xxxxxxx"):
        print("BaseFigure construct")
        self.color = color_var
        self.material = material_var   

    def __str__(self):
        return "<BaseFigure[color:{}, material:{}]>".format(self.color, self.material)

    def __del__(self):
        print("Destruct for BaseFigure!")


class Rectangle(BaseFigure):
    def __init__(self, length_var:int = 0, width_var:int=0, color_var:str="0fffffff", material_var:str="xxxxxxx"):
        super().__init__(color_var, material_var) # Вызываю родительский конструктор
        BaseFigure.__init__(self,color_var, material_var ) # Вызов род.констр без super()
        self.length = length_var # Спец для дочернего конструктора
        self.width = width_var

    def __str__(self):
        return "<Rectangle [color:{}, material:{}, length:{}, width:{}]>".format(self.color, self.material, self.length, self.width)


class Triangle(BaseFigure):
    pass 
r = Rectangle(10, 20, "white", "iron")
print(r)