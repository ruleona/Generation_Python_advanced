import turtle


turtle.showturtle()

# Задать направление движения
turtle.forward(100)
turtle.backward(100)
turtle.right(100)
turtle.left(100)

# Установка углового направления черепашки
turtle.setheading(90)

#Получение текущего углового направления черепашки
turtle.heading()

# Изменение внешнего вида черепашки
turtle.shape('square')
# square (квадрат);
# arrow (стрелка);
# circle (круг);
# turtle (черепашка);
# triangle (треугольник);
# classic (классическая стрелка)
При необходимости можно использовать свои рисунки:
turtle.Screen().addshape('rocketship.gif')  # регистрируем изображение
turtle.shape('rocketship.gif')



turtle.shape('turtle')

turtle.done()