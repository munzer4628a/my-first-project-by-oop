class Player:
     def __init__(self):
        pass
     # هون حلقة اللاعب الاول
     def player_1(self):
         while True:
          name1=input("pleas enter your name\n")
          symbol1=input("please choose x or o \n")
      #هون لحتى يدخل بس حرف
          if name1.isalpha() and symbol1=="x" or symbol1== "o":
           if len (symbol1)<=1:
            self.name1=name1
            self.symbol1=symbol1
            break
          else:
            print("please input correct")
                #هون للاعب الثاني
     def player_2(self):
        while True:
         name2=input("pleas enter your name \n")
         symbol2=input("please choose x or o \n")
         if name2.isalpha()and symbol2=="x" or symbol2== "o":
           if len(symbol2)<2:
            self.name2=name2
            self.symbol2=symbol2
            break
         return("thanks")
     def display1(self):
        print(f"your name {self.name1} and your letter {self.symbol1}")
     def display2(self):
        print(f"your name {self.name2} and your letter {self.symbol2}")
class Board:
      def __init__(self,board_diagram):
       self.board_diagram=board_diagram
      def display_(self):
       #شكل اللوح ل رح يلعب عليه
        row1=print("|".join((self.board_diagram[0:3])))
        row2= print( "|".join((self.board_diagram[3:6])))
        row3=print ("|".join((self.board_diagram[6:9])))  
              #للتحديث  
      def ubdate(self,symbol):
          self.chosse_user= input("please enter number board\n")
          if len(self.chosse_user)<1:
             print("please correct answer number")
             
          else:
             if self.board_diagram[int(self.chosse_user)-1] in ["x","o"]:
              return False
          self.board_diagram[int(self.chosse_user)-1]=symbol
          return True
class Menue:
   def display_menue(self):
    print("welcom to my tic tac toe")
    while True:
     start_game= input("choice 1 start game\n 2restart game\n 3quite game\n")
     if start_game=="1":
       print( "start_game")
       break
     elif start_game=="2":
      print("restart")
      return start_game
     elif start_game=="3":
        return start_game
     else:
      print("please enter correct number")    
class Game:
     def __init__(self):
         self.player_obj=Player()
         self.board_obj=Board(["1","2","3","4","5","6","7","8","9"])
         self.menue_obj=Menue()
     def start_player(self):
         self.player_obj.player_1()
         self.player_obj.display1()
         self.player_obj.player_2()
         self.player_obj.display2()
     def start(self):
      curint_player=1
      draw=0
      while True:
        self.board_obj.display_()
        if curint_player==1:
           name=self.player_obj.name1
           print(f"turn {name}")
           symbol=self.player_obj.symbol1
        else:
            name=self.player_obj.name2
            print(f"turn {name}")
            symbol=self.player_obj.symbol2
        if self.board_obj.ubdate(symbol):
            draw+=1
            if self.cheek_win(name):
               break 
            if draw==9:
               print("draw")
               break
            if curint_player==1:
               curint_player=2
            else:
               curint_player=1
        else:
          print("again")
      
      s= self.menue_obj.display_menue()
      if s=="2":
         self.board_obj.board_diagram=["1","2","3","4","5","6","7","8","9"]
         self.start_player()
         self.start()
         self.cheek_win()
      if s=="3":
            print("thanks you play my game")
            return
     def cheek_win(self,name):
      if (self.board_obj.board_diagram[0]==self.board_obj.board_diagram[1]==self.board_obj.board_diagram[2]
      or self.board_obj.board_diagram[0]==self.board_obj.board_diagram[3]==self.board_obj.board_diagram[6] 
      or self.board_obj.board_diagram[0]==self.board_obj.board_diagram[4]==self.board_obj.board_diagram[8] 
      or self.board_obj.board_diagram[1]==self.board_obj.board_diagram[4]==self.board_obj.board_diagram[7] 
      or self.board_obj.board_diagram[2]==self.board_obj.board_diagram[5]==self.board_obj.board_diagram[8] 
      or self.board_obj.board_diagram[2]==self.board_obj.board_diagram[4]==self.board_obj.board_diagram[6]
      or self.board_obj.board_diagram[3]==self.board_obj.board_diagram[4]==self.board_obj.board_diagram[5] 
      or self.board_obj.board_diagram[6]==self.board_obj.board_diagram[7]==self.board_obj.board_diagram[8] ):
       print (f"winer {name}")
       return True
test=Menue()
test.display_menue()
my=Game()
my.start_player()
my.start()