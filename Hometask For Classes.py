import random

class Student:
    def __init__ (self, name):
        self.name= name
        self.gladness= 50
        self.progress= 0
        self.cash= 100
        self.hunger= 0
        self.alive= True

    def to_study(self):
        print("Time to study")
        self.gladness -=15
        self.progress +=3
        self.hunger +=5
        self.cash +=0.5

    def to_sleep(self):
        print("Time to sleep")
        self.gladness +=10
        self.progress -=0.5
        self.hunger +=4

    def to_chill(self):
        print("Time to do anything you want")
        self.progress -=2.5
        self.gladness +=5
        self.cash -=5
        self.hunger +=1

    def to_work(self):
        print("Time to work")
        self.progress +=0.5
        self.gladness -=2.5
        self.cash +=10
        self.hunger +=15

    def to_eat(self):
        print("Time to eat")
        self.gladness +=2.5
        self.cash -=15
        self.hunger -=12

    def to_workout(self):
        print("Time to workout")
        self.gladness -=2.5
        self.hunger +=15
        self.cash -=10

    def analysing(self):
        if self.cash <=15:
            self.to_work()
        elif self.gladness <=5:
            self.to_chill()
        elif self.progress <=1.5:
            self.to_study()
        elif self.hunger >=60:
            self.to_eat()
        elif self.hunger <=-20:
            self.to_workout()

    def is_alive(self):
        if self.progress <-3:
            print("Student has been eliminated from university...")
            self.alive = False
        if self.gladness <=0:
            print("Student has got a depression")
            self.alive = False
        if self.progress >6.5:
            print("Student has successfuly passed his exams!")
            self.alive = False
        if self.hunger >=95:
            print("Student has been exhausted by hunger")
            self.alive = False
        if self.hunger <=-30:
            print("Student has suffered from excessive obesity...")
        if self.cash ==0:
            print("Student can't support himself anymore")
            self.alive = False

    def end_of_day (self):
        print(f'Gladness ={self.gladness}')
        print(f'Progress ={self.progress}')
        print(f'Cash ={self.cash}')
        print(f'Hunger ={self.hunger}')

    def live(self, day):
        day= 'Day '+ str(day)+ ' of '+ self.name+ "'s"+ ' life'
        print(f'{day:=^70}')
        print("=====Plans of the day:=====")
        live_circle= random.randint(1,6)
        if live_circle == 1:
            self.to_study()
        elif live_circle == 2:
            self.to_sleep()
        elif live_circle == 3:
            self.to_chill()
        elif live_circle == 4:
            self.to_work()
        elif live_circle == 5:
            self.to_eat()
        elif live_circle == 6:
            self.to_workout()
        self.analysing()
        self.end_of_day()
        self.is_alive()

studec= Student(name="Pasha")

for day in range(1,366):
    if studec.alive == False:
        break
    studec.live(day)