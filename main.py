from tkinter import*#for Gui
import random#for randoniser
from tkinter import messagebox # for message box
names = []#list
score=0#list
asked = []#list
asked = []#list
#my dictionary which has all my questions and answers
question_solution = {
    1: ["What is the smallest country in the world?", 'Vatican City', 'Monaco','Guam', 'Fiji' ,'Vatican City',1],#Q1
    2: ["Which country is the origin of the cocktail Mojito?:",'Cuba','Columbia','Argentina','Brazil','Cuba',1],#Q2
    3: ["Who came second in the FIFA Women's World Cup in 2019?", 'Argentina','USA', 'Netherlands','Jamaica','Netherlads',3],#Q3
    4: ["What year did Margaret Thatcher die?", '2015','2012', '2014','2013','2013',4],#Q4
    5: ["How many episodes of Scrubs were there?", '182','175', '181','184','181',3],#Q5
    6: ["How many elements are there in the periodic table?", '120','118', '115','110','118',2],#Q6
    7: ["How many bones does a shark have?", 'None','206', '115','110','None',1],#Q7
    8: ["How many time zones are there in Russia?", '12','11','13','10','11',2],#Q8
    9: ["What year was Heinz established?", '1870','1865','1869','1900','1869',3],#Q9
    10: ["What month was Prince George born?", 'April','September','May','July','July',4],#Q
}

def randomiser():#randomises the questions
    global qnum#key of the dictionary
    qnum = random.randint(1,10)#the number of questions
    if qnum not in asked:#a list is declared, atart with any number will be added
      asked.append(qnum)
    elif qnum in asked:
      randomiser()
      
# this is my introduction page which greats the user to my quiz
class IntroductionStarter:
  def __init__(self, parent):
    background_color="Black"#background colour
   
    self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
    self.quiz_frame.grid()

    self.heading_tab=Label(self.quiz_frame, text = "General Knowledge Quiz", font =( "times new roman","18","bold"),bg="gold")
    self.heading_tab.grid(row= 0, padx=20)#heading of the quiz

    self.var1=IntVar()

    self.user_tab=Label(self.quiz_frame, text="Please Enter your Username Below: ", font=( "times new roman","18","bold"),bg="gold")#username headind
    self.user_tab.grid(row=1, padx=20, pady=20)

    self.entry_case=Entry(self.quiz_frame)
    self.entry_case.grid(row=2,padx=20, pady=20)#where you enter your name

    self.continue_button = Button(self.quiz_frame, text="Continue", font=( "times new roman","13","bold"), bg="gold",command=self.name_collection)
    self.continue_button.grid(row=3,padx=20, pady=20)#continue button


  

  def name_collection(self):#collectes name
      name = self.entry_case.get()
        # component 6 error handling
      if name == '':
            messagebox.showerror('Name is needed!', ' Enter your name!')
      elif len(name) > 15: # to make sure name entered is between 2-15
        messagebox.showerror('error has happened!', 'Maximum amount of characters reached')
      elif len(name) < 2: # to make sure name entered is between 2-15
            messagebox.showerror('error has happened',
                                 'username is not to the required length')
      elif name.isnumeric():
            messagebox.showerror('error has happened!', 'Username can only have letters!')
      elif not name.replace(' ','').isalpha: # to make sure that letters are entered not number
        messagebox.showerror('error has happened!', 'No Foreign Symbols! Please Enter Username Again!')
      else:# to make sure letteres are entered not symbols
        name=self.entry_case.get()
        names.append(name)#adds name to the list
        self.quiz_frame.destroy()#destroys quiz frame
        Instructionsstarter(root)#take user to the nest page
#this is my instructions page and its job is to explain what the quiz is about and how it works
class Instructionsstarter:
  def __init__(self, parent):
    background_color="Black"#background colour
   
    self.instructions_frame = Frame(parent, bg = background_color, padx=100, pady=100)
    self.instructions_frame.grid()

    self.heading_tab=Label(self.instructions_frame, text = "Instructions", font =( "times new roman","18","bold"),bg="gold")#main heading
    self.heading_tab.grid(row= 0, padx=20)

    self.var1=IntVar()

    self.user_tab=Label(self.instructions_frame, text="This is a general knowledge quiz which will \n test your knowledge about \n all topics around the world. Every time you \n get a question right you will have 1 \n point added to your score and \n when you get a question wrong no points will \n be added to your score. Good Luck and Have Fun ",font=( "times new roman","18","bold"),bg="gold")
    self.user_tab.grid(row=1, padx=20, pady=20)#instructions

    

    self.continue_button = Button(self.instructions_frame, text="Continue", font=( "times new roman","13","bold"), bg="gold",command=self.name_collection)
    self.continue_button.grid(row=3,padx=20, pady=20)#continue button

  def name_collection(self):
        self.instructions_frame.destroy()#destroys instructions frame
        Quiz(root)#take user to next page


# this is where the quiz starts and where the questions will be displayed   
class Quiz:#Quiz page
  def __init__(self, parent):
    background_color="black"#background colour
    
   
    self.quiz_frame = Frame(parent, bg = background_color, padx=40, pady=40)
    self.quiz_frame.grid()

    randomiser()# random questions

    self.question_label=Label(self.quiz_frame, text = question_solution [qnum][0], font =(  "times new roman","18","bold"),bg="gold")
    self.question_label.grid(row= 0, padx=10, pady=10)  # question label

    self.var1=IntVar()

    self.rb1 = Radiobutton (self.quiz_frame, text = question_solution [qnum][1], font=("times new roman", "12"), bg="gold", value=1, variable=self.var1, pady=10)
    self.rb1.grid(row=1, sticky=W)#button 1

    self.rb2 = Radiobutton (self.quiz_frame, text = question_solution [qnum][2], font=("times new roman", "12"), bg="gold", value=2, variable=self.var1, pady=10)
    self.rb2.grid(row=2, sticky=W)#button 2

    self.rb3 = Radiobutton (self.quiz_frame, text = question_solution [qnum][3], font=("times new roman", "12"), bg="gold", value=3, variable=self.var1, pady=10)
    self.rb3.grid(row=3, sticky=W)#button 3

    self.rb4 = Radiobutton (self.quiz_frame, text = question_solution [qnum][4], font=("times new roman", "12"), bg="gold", value=4, variable=self.var1, pady=10)
    self.rb4.grid(row=4, sticky=W)#button 4

    self.confirm_button = Button(self.quiz_frame, text="Confrim",bg="gold",command=self.trial_progression)
    self.confirm_button.grid(row=6)#confirm button


    self.leave_tab = Button(self.quiz_frame, text="Leave",bg="red",command=self.end_screen)
    self.leave_tab.grid(row=4)#leave button
      
    
    self.score_label  = Label (text ='score')
    self.score_label.grid(row=9)#score system     
    
    
     
     
  def questions_system(self):
     randomiser()
     self.var1.set(0)
     self.question_label.config(text=question_solution [qnum][0])
     self.rb1.config(text=question_solution [qnum][1])
     self.rb2.config(text=question_solution [qnum][2])
     self.rb3.config(text=question_solution [qnum][3])
     self.rb4.config(text=question_solution [qnum][4])

#this is the score system that tells the users what their score is
  def trial_progression(self):
      global score 
      scr_tab=self.score_label
      choice=self.var1.get()
      if len(asked)>9: #  finds out the last question of the quiz
        if choice == question_solution [qnum][6]: # checks that the key is correct and stores the answer in index 6
          score +=1 # one point is added to score
          scr_tab.configure(text=score)  # will show the new score
          self.confirm_button.config(text="Confirm") # confirm button will change to given text
          self.end_screen() # opens the end page when the quiz is done
        else:
          score+=0
          scr_tab.configure(text="The correct answer was: "+ question_solution [qnum][5] )#tells user the answer is incorrect and tell the user the right answer
          self.confirm_button.config(text="Confirm")
          self.end_screen()
     
      else:
            if choice==0:
              self.confirm_button.config(text=" Please Try Again, you didn't select an answer then submit again" )#when the user has no selected the option this message shows up
              choice=self.var1.get()
            else:
              if choice == question_solution [qnum][6]:
                score+=1
                scr_tab.configure(text=score)
                self.confirm_button.config(text="Confirm")
                self.questions_system()
      
              else:
                  score+=0
                  scr_tab.configure(text="The correct answer was: " + question_solution [qnum][5])##tells user the answer is incorrect and tell the user the right answer
                  self.confirm_button.config(text="Confirmn")
                  self.questions_system()


  def end_screen(self):
    root.destroy()#destroys quiz page
    name = names[0]
    open_end_object = end()#opens end page



class end:# End page


  def __init__(self):
        background_color = 'black' #Background color
        global end_root
        end_root = Tk()
        end_root.title('Exit Box') #page title
        end_root.geometry('600x600') #page size

        self.end_frame = Frame(end_root, width=700, height=600,bg=background_color)
        self.end_frame.grid(row=1)

        self.end_title = Label(end_root,text='Thank You For Participating The Quiz  ',  font=('times new roman', 22, 'bold'), bg="gold") #main heading
        self.end_title.place(x=15, y=35) #heading location

        self.exit_button = Button(end_root,text='Exit',width=10,bg='gold',font=('times new roman', 12, 'bold'),command=self.close_end,) #Exit button
        self.exit_button.place(x=260, y=200) #Location of the heading

        self.list_tab = Label(end_root, text='Please try again if you want to' + str(names),font=('times new roman', 12, 'bold'),width=40, bg="gold") #try again label
        self.list_tab.place(x=110, y=80) #label location
        
        self.final_score = Label(end_root, text=' Final score is ' + str(score), font=('times new roman', 12, 'bold'), width=40, bg="gold") #final score is displayed
        self.final_score.place(x=110, y=150)#label location
        
  
  
  def close_end(self):
      self.end_frame.destroy()#destroys end frame
      self.end_title.destroy()#destorys end title
      self.exit_button.destroy()#destroys exit button
      self.list_tab.destroy()
      end_root.destroy()#ends quiz
  
    



if __name__ == "__main__":
  root = Tk()
  root.title("General Knowledge Quiz")#title for the quiz
  quiz_instance = IntroductionStarter(root)
  root.mainloop()