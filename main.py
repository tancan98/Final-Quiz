from tkinter import*
import random
names = []
global questions_answers
asked = []

questions_answers = {
    1: ["What is the smallest country in the world?", 'Vatican City', 'Monaco','Guam', 'Fiji' ,1],
    2: ["Which country is the origin of the cocktail Mojito?:",'Cuba','Columbia','Argentina','Brazil',1],
    3: ["When coming up to a pedestrian crossing without a raised traffic island, what must you do?", 'Speed up before the pedestrians cross','Stop and give way to pedestrians on any part of the crossing', 'Sound the horn on your vehicle to warn the perestrians','slow down to 30kmh','Stop and give way to pedestrians on any part of the crossing',2],
}

def randomiser():
    global qnum
    qnum = random.randint(1,3)
    if qnum not in asked:
      asked.append(qnum)
    elif qnum in asked:
      randomiser()
      

class QuizStarter:
  def __init__(self, parent):
    background_color="Black"
   
    self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
    self.quiz_frame.grid()

    self.heading_label=Label(self.quiz_frame, text = "General Knowledge Quiz", font =( "times new roman","18","bold"),bg="gold")
    self.heading_label.grid(row= 0, padx=20)

    self.var1=IntVar()

    self.user_label=Label(self.quiz_frame, text="Please Enter your Username Below: ", font=( "times new roman","18","bold"),bg="gold")
    self.user_label.grid(row=1, padx=20, pady=20)

    self.entry_box=Entry(self.quiz_frame)
    self.entry_box.grid(row=2,padx=20, pady=20)

    self.continue_button = Button(self.quiz_frame, text="Continue", font=( "times new roman","13","bold"), bg="gold",command=self.name_collection)
    self.continue_button.grid(row=3,padx=20, pady=20)

  def name_collection(self):
        name=self.entry_box.get()
        names.append(name)
        self.quiz_frame.destroy()
        Quiz(root)


class Quiz:

   def __init__(self, parent):
    background_color="black"
   
    self.quiz_frame = Frame(parent, bg = background_color, padx=40, pady=40)
    self.quiz_frame.grid()

    randomiser()

    self.question_label=Label(self.quiz_frame, text = questions_answers[qnum][0], font =(  "Tw Cen MT","18","bold"),bg="gold")
    self.question_label.grid(row= 0, padx=10, pady=10)  

    self.var1=IntVar()

    self.rb1 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg="gold", value=1, variable=self.var1, pady=10)
    self.rb1.grid(row=1, sticky=W)

    self.rb2 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg="gold", value=1, variable=self.var1, pady=10)
    self.rb2.grid(row=2, sticky=W)

    self.rb3 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg="gold", value=1, variable=self.var1, pady=10)
    self.rb3.grid(row=3, sticky=W)

    self.rb4 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg="gold", value=1, variable=self.var1, pady=10)
    self.rb4.grid(row=4, sticky=W)

    self.confirm_button = Button(self.quiz_frame, text="Confrim",bg="gold",command=self.test_progress)
    self.confirm_button.grid(row=6)
     
     
   def questions_setup(self):
     randomiser()
     self.varl.set(0)
     self.question_label.config(text=questions_answers[qnum][0])
     self.rb1.config(text=questions_answers[qnum][1])
     self.rb2.config(text=questions_answers[qnum][2])
     self.rb3.config(text=questions_answers[qnum][3])
     self.rb4.config(text=questions_answers[qnum][4])

 
   def test_progress(self):
      def test_progress(self):
       global score
      score = 0
      scr_label=self.score_label
      choice=self.var1.get()
      if len(asked)>9:
        if choice == questions_answers[qnum][6]:
          score +=1
          scr_label.configure(text=score)
          self.confirm_button.config(text="Confirm")
        else:
          score+=0
          scr_label.configure(text="The correct answer was: "+ questions_answers[qnum][5] )
          self.confirm_button.config(text="confirm")
     
      else:
            if choice==0:
              self.confirm_button.config(text="Try Again, you didn't select an option then submit again" )
              choice=self.var1.get()
            else:
              if choice == questions_answers[qnum][6]:
                score+=1
                scr_label.configure(text=score)
                self.confirm_button.config(text="confirm")
                self.questions_setup()
 
              else:
                  score+=0
                  scr_label.configure(text="The correct answer was: " + questions_answers[qnum][5])
                  self.confirm_button.config(text="Confirm")
                  self.questions_setup()
       
if __name__ == "__main__":
  root = Tk()
  root.title("NZ Road Rules Quiz")
  quiz_instance = QuizStarter(root)
  root.mainloop()
