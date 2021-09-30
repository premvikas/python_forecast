# # Import turtle package
# import turtle

# # Creating a turtle object(pen)
# pen = turtle.Turtle()

# # Defining a method to draw curve
# def curve():
# 	for i in range(200):

# 		# Defining step by step curve motion
# 		pen.right(1)
# 		pen.forward(1)

# # Defining method to draw a full heart
# def heart():

# 	# Set the fill color to red
# 	pen.fillcolor('red')

# 	# Start filling the color
# 	pen.begin_fill()

# 	# Draw the left line
# 	pen.left(140)
# 	pen.forward(113)

# 	# Draw the left curve
# 	curve()
# 	pen.left(120)

# 	# Draw the right curve
# 	curve()

# 	# Draw the right line
# 	pen.forward(112)

# 	# Ending the filling of the color
# 	pen.end_fill()

# # Defining method to write text
# def txt():

# 	# Move turtle to air
# 	pen.up()

# 	# Move turtle to a given position
# 	pen.setpos(-68, 95)

# 	# Move the turtle to the ground
# 	pen.down()

# 	# Set the text color to lightgreen
# 	pen.color('lightgreen')

# 	# Write the specified text in
# 	# specified font style and size
# 	pen.write("Premitha", font=(
# 	"Verdana", 12, "bold"))


# # Draw a heart
# heart()

# # Write text
# txt()

# # To hide turtle
# pen.ht()
# Import turtle package
import turtle

# Creating a turtle screen object
sc = turtle.Screen()

# Creating a turtle object(pen)
pen = turtle.Turtle()

# Defining a method to form a semicircle
# with a dynamic radius and color
def semi_circle(col, rad, val):

	# Set the fill color of the semicircle
	pen.color(col)

	# Draw a circle
	pen.circle(rad, -180)

	# Move the turtle to air
	pen.up()

	# Move the turtle to a given position
	pen.setpos(val, 0)

	# Move the turtle to the ground
	pen.down()

	pen.right(180)


# Set the colors for drawing
col = ['violet', 'indigo', 'blue',
	'green', 'yellow', 'orange', 'red']

# Setup the screen features
sc.setup(600, 600)

# Set the screen color to black
sc.bgcolor('black')

# Setup the turtle features
pen.right(90)
pen.width(10)
pen.speed(7)

# Loop to draw 7 semicircles
for i in range(7):
	semi_circle(col[i], 10*(
	i + 8), -10*(i + 1))

# Hide the turtle
pen.hideturtle()

