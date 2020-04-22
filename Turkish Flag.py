import turtle #turtle modülünü import ettik
def main():
    turtle.tracer(0, 0) #çizim hızını 0layarak beklemeden ekrana bastırdık
    kalem = turtle.Turtle() #Turtle classını kalem nesnemize importladık
    turtle.bgcolor("red") # arka plan rengi
    hilalCiz(kalem, -60, 0, 200, "white") # hilalin beyaz kısmını bastırdık
    hilalCiz(kalem, -35, 0, 170, "red") # hilalin arka plan rengi olan kısmını bastırdık
    yildizCiz(kalem, 30, -30, 90) #yıldızı bastırdık
    turtle.mainloop() #olay döngüsünü başlatır
def hilalCiz(object, xAxis, yAxis, rad, color): #hilalCiz adında fonksiyon oluşturduk
    object.up()
    object.goto(xAxis, yAxis)
    object.dot(rad, color)
def yildizCiz(object, xAxis, yAxis, large): #yildizCiz adında fonksiyon oluşturduk
    object.pencolor("white") #iç ve kalem renklerini belirledik
    object.fillcolor("white")
    object.goto(xAxis, yAxis) #yıldızın konumunu belirledik
    object.left(45) #45 derece sola yatırdık
    object.begin_fill()
    for i in range(6): #yıldızı çizdirdik
        object.forward(large)
        object.left(144)
    object.end_fill()
main()