from tkinter import*
import random
names = []
score=0
asked = []
#my dictionary which has all my questions and answers
questions_answers = {
    1: ["What is the smallest country in the world?", 'Vatican City', 'Monaco','Guam', 'Fiji' ,'Vatican City',1],
    2: ["Which country is the origin of the cocktail Mojito?:",'Cuba','Columbia','Argentina','Brazil','Cuba',1],
    3: ["Who came second in the FIFA Women's World Cup in 2019?", 'Argentina','USA', 'Netherlands','Jamaica','Netherlads',3],
    4: ["What year did Margaret Thatcher die?", '2015','2012', '2014','2013','2013',4],
    5: ["How many episodes of Scrubs were there?", '182','175', '181','184','181',3],
    6: ["How many elements are there in the periodic table?", '120','118', '115','110','118',2],
    7: ["How many bones does a shark have?", 'None','206', '115','110','None',1],
    8: ["How many time zones are there in Russia?", '12','11','13','10','11',2],
    9: ["What year was Heinz established?", '1870','1865','1869','1900','1869',3],
    10: ["What month was Prince George born?", 'April','September','May','July','July',4],
}

def randomiser():
    global qnum
    qnum = random.randint(1,10)
    if qnum not in asked:
      asked.append(qnum)
    elif qnum in asked:
      randomiser()
      
# this is my introduction page which greats the user to my quiz
class IntroductionStarter:
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
        Instructionsstarter(root)
#this is my instructions page and its job is to explain what the quiz is about and how it works
class Instructionsstarter:
  def __init__(self, parent):
    background_color="Black"
   
    self.instructions_frame = Frame(parent, bg = background_color, padx=100, pady=100)
    self.instructions_frame.grid()

    self.heading_label=Label(self.instructions_frame, text = "Instructions", font =( "times new roman","18","bold"),bg="gold")
    self.heading_label.grid(row= 0, padx=20)

    self.var1=IntVar()

    self.user_label=Label(self.instructions_frame, text="This is a general knowledge quiz which will \n test your knowledge about \n all topics around the world. Every time you \n get a question right you will have 1 \n point added to your score and \n when you get a question wrong no points will \n be added to your score. Good Luck and Have Fun ",font=( "times new roman","18","bold"),bg="gold")
    self.user_label.grid(row=1, padx=20, pady=20)

    

    self.continue_button = Button(self.instructions_frame, text="Continue", font=( "times new roman","13","bold"), bg="gold",command=self.name_collection)
    self.continue_button.grid(row=3,padx=20, pady=20)

  def name_collection(self):
        self.instructions_frame.destroy()
        Quiz(root)

# this is where the quiz starts and where the questions will be displayed   
class Quiz:

   def __init__(self, parent):
    background_color="black"
   
    self.quiz_frame = Frame(parent, bg = background_color, padx=40, pady=40)
    self.quiz_frame.grid()

    randomiser()

    self.question_label=Label(self.quiz_frame, text = questions_answers[qnum][0], font =(  "times new roman","18","bold"),bg="gold")
    self.question_label.grid(row= 0, padx=10, pady=10)  

    self.var1=IntVar()

    self.rb1 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][1], font=("times new roman", "12"), bg="gold", value=1, variable=self.var1, pady=10)
    self.rb1.grid(row=1, sticky=W)

    self.rb2 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][2], font=("times new roman", "12"), bg="gold", value=1, variable=self.var1, pady=10)
    self.rb2.grid(row=2, sticky=W)

    self.rb3 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][3], font=("times new roman", "12"), bg="gold", value=1, variable=self.var1, pady=10)
    self.rb3.grid(row=3, sticky=W)

    self.rb4 = Radiobutton (self.quiz_frame, text = questions_answers[qnum][4], font=("times new roman", "12"), bg="gold", value=1, variable=self.var1, pady=10)
    self.rb4.grid(row=4, sticky=W)

    self.confirm_button = Button(self.quiz_frame, text="Confrim",bg="gold",command=self.test_progress)
    self.confirm_button.grid(row=6)

    self.score_label  = Label (text ='score')
    self.score_label.grid(row= 7) 
     

  
   def questions_setup(self):
     randomiser()
     self.var1.set(0)
     self.question_label.config(text=questions_answers[qnum][0])
     self.rb1.config(text=questions_answers[qnum][1])
     self.rb2.config(text=questions_answers[qnum][2])
     self.rb3.config(text=questions_answers[qnum][3])
     self.rb4.config(text=questions_answers[qnum][4])

 #this is the score system that tells the users what their score is
   def test_progress(self):
      global score
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
                  self.confirm_button.config(text="Confirmn")
                  self.questions_setup()


def name_collection(self):
  self.confirm_button.destroy()
  Endstarter(root)


    

                

