#IMPORTS DRAWING FEA
import turtle

#CREATES THE TREE
def tree(branchLength, t, size):
    if branchLength > -1:
        if branchLength > 70:
            t.color("brown")
        else:
            t.color("green")
        t.forward(branchLength)
        t.pensize(size)
        t.right(20)
        tree(branchLength - 10, t, size - 2)
        t.left(40)
        tree(branchLength - 10, t, size - 2)
        t.right(20)
        t.backward(branchLength)
        t.pensize(size)
#RUNS THE TREE FUNCTION
def main():
    #SIMPLIFIES TURTLE TO "T"
    t = turtle.Turtle()
    #CREATES SCREEN
    daWindow = turtle.Screen()
    t.speed(0)
    t.pensize(20)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(100, t, 20)
    #CLOSES SCREEN WHEN CLICKED ON
    daWindow.exitonclick()

main()