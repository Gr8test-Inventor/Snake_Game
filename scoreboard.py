from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Consolas', 22, 'normal')



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as highscore_data: #Saving file to variable called highscore_data
            self.high_score = int(highscore_data.read())
        self.penup()
        self.color("white")
        self.goto(x= 0, y= 267)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        with open("data.txt", mode="w") as data:
            data.write(str(self.high_score))
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align = ALIGNMENT, font= FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()




