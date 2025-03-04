from random import randint
from datetime import datetime
import itertools
import os.path

class SakClass:
   def __init__(self):
      self.bag=[]
      self.prepare()

   def prepare(self):#προετοιμασία γραμμάτων στο σακουλάκι/επαρίθμηση γραμμάτων, ώστε μετά να επιλέγουμε τυχαία έναν ακέραιο που αντιπροσωπεύει το γράμμα
      arxikos={'Α':[12,1],'Β':[1,8],'Γ':[2,4],'Δ':[2,4],'Ε':[8,1],
        'Ζ':[1,10],'Η':[7,1],'Θ':[1,10],'Ι':[8,1],'Κ':[4,2],
        'Λ':[3,3],'Μ':[3,3],'Ν':[6,1],'Ξ':[1,10],'Ο':[9,1],
        'Π':[4,2],'Ρ':[5,2],'Σ':[7,1],'Τ':[8,1],'Υ':[4,2],
        'Φ':[1,8],'Χ':[1,8],'Ψ':[1,10],'Ω':[3,3]
        }
      for key in arxikos:
         for i in range(0,arxikos[key][0]):
            self.bag.append({"letter":key,"value":arxikos[key][1]})

   def getletter(self):#πώς παίρνω ένα γράμμα
      num=randint(0,len(self.bag)-1)
      randletter=self.bag[num]
      self.bag.pop(num)
      return randletter

   def getletters(self,numbrofletters):#πώς παίρνω ν=numbrofletters γραμματα
      if numbrofletters<len(self.bag):#αν ζητήσω λιγότερα γράμματα από αυτά που έχει το σακουλάκι
         randletters=[]
         for i in range(0,numbrofletters):
            randletter=self.getletter()
            randletters.append(randletter)
         return randletters
      else:#αλλιώς παίρνω όσα γραμματα έχει το σακουλάκι
         temporary_list=[]
         for letter in self.bag:
            temporary_list.append(letter)
         self.bag.clear()   
         return temporary_list  

   def putbackletters(self,letter_list): #επιστροφή γραμμάτων στο σακουλάκι
      self.bag=self.bag+letter_list

   def getnumberofletters(self):#πόσα γραμματα εχει το σακουλάκι
      return len(self.bag)   

   def __repr__(self) :
       return "\nΣτο σακουλάκι: "+str(self.getnumberofletters()) +" γράμματα."   

class Language:#κλάση που φτιάχνει το λεξικό που θα χρησιμοποιηθεί

   def __init__(self,filename):
      self.filename=filename
      self.dictionary={}
      self.read_words()

   def read_words(self):#διαβάζει τις λέξεις από ένα αρχείο και φτάχνει ένα λεξικό όπου κλειδί είναι το πρώτο γράμμα και τιμή μια λίστα λέξεων που ξεκινούν από αυτό το γράμμα
      with open(self.filename,'r',encoding="utf-8") as f:
         for line in f:
            line=line.replace("\n","")#για να παραλείψουμε τον κρυφό χαρακτήρα "\n" που αλλάζει την σειρά, τον αντικαθιστούμε με κενό ("")
            first_letter=line[0]
            if first_letter in self.dictionary: #αν υπάρχει ήδη το κλειδί
               self.dictionary[first_letter].append(line)
            else: #αν δεν υπάρχει το κλειδί
               self.dictionary[first_letter]=[]   
               self.dictionary[first_letter].append(line)

   def elegxos_leksis(self,lexi):#ελέγχει αν η λέξη υπάρχει στο λεξικό ή όχι
      first_letter=lexi[0]    
     
      if first_letter in list(self.dictionary.keys()):      
         if lexi in self.dictionary[first_letter]:
            return "Έγκυρη Λέξη"
         else:
            return"Άκυρη Λέξη"
      else:
            return"Άκυρη Λέξη"   


class Player:
   def __init__(self,name="Pc"):
      self.name=name
      self.points=0
      self.letterlist=[]
      self.moves=0

   def giveletters(self,letter_list):#δίνει γράμματα στον παίκτη
      self.letterlist=self.letterlist+letter_list

   def passturn(self,sak):#όταν καποιος παίκτης πάει πάσο, επιστρέφει τα γράμματά του στο σακουλάκι και του δίνονται καινούργια
      letter_list=[]#προσωρινή λίστα
      for i in range(0,len(self.letterlist)):
         letter_list.append(self.letterlist[i])
      self.letterlist.clear()
      sak.putbackletters(letter_list)
      new_letters=sak.getletters(7)
      self.giveletters(new_letters)

   def number_of_letters(self):#πόσα γράμματα έχει ένας παίκτης
      return len(self.letterlist)   

   def get_letters_display(self):#δείχνει στους παίκτες τα γράμματα που έχουν και την αξία τους
      display=''
      for letter in self.letterlist:
         display+=letter["letter"]+","+str(letter["value"])+" - "
      return display   

   def __repr__(self):
      return "Παίζεις "+self.name+ "\nΔιαθέσιμα γράμματα: "+ self.get_letters_display()  

   def display_points(self):
      print("Συνολικοί Πόντοι: "+str(self.points))   

   def get_all_posible_words(self,language,sak)  :
      #φτιάχνω όλες τις πιθανές λέξεις που μπορώ μεταθέτοντας τα γράμματα που έχω
      all_letters=""
      perm_dict={}#λίστα που περιλαμβάνει όλες τις μεταθέσεις των γραμμάτων που έχει ο pc ανά 2 έως και ανά όσα γράμματα έχει
      for i in range(0,len(self.letterlist)):
         all_letters+=self.letterlist[i]["letter"]
      for i in range(2,len(self.letterlist)+1):
         perm_list=itertools.permutations(all_letters,i)
         for perm in perm_list:
            word=""
            for letter in perm:#ενώνει τα γράμματα από τις μεταθέσεις δημιουργώντας λέξεις
               word+=letter
            elegxos=language.elegxos_leksis(word)    #έλεγχος αν η λέξη ανήκει στο λεξικό.
            if elegxos=="Έγκυρη Λέξη":
               word_points=0
               for letter in word:
                  for i in range(0,len(self.letterlist)) :
                     dictionary=self.letterlist[i]
                     if letter==dictionary["letter"] :
                        word_points+=dictionary["value"] #μετράει τους πόντους κάθε λέξης
                        break
               perm_dict[word]=word_points #Λεξικό που εχει ως κλειδιά τις λέξεις και ως τιμές τους πόντους
      return perm_dict    
   def get_best_word(self,language,sak):
      perm_dict=self.get_all_posible_words(language,sak)  
      if len(list(perm_dict.keys()))==0: #αν το λεξικό είναι κενό, δεν υπάρχει καμία αποδεκτή λέξη
         final_choice=""
         max_value=0
      else:   
         point_list=list(perm_dict.values())#λίστα με τους πόντους
         max_value=max(point_list)#παίρνω την μέγιστη τιμή
         max_pos=point_list.index(max_value)#παίρνω τον δείκτη της μέγιστης τιμές
         final_choice=list(perm_dict.keys())[max_pos]#βρίσκω την λέξη μέσω του δείκτη  
      return final_choice,max_value     

class Human(Player):
   def __init__(self, name):
       super().__init__(name=name)
       self.mode="1" #προεπιλογή στις ρυθμίσεις του παιχνιδιού

   def play(self,lexi,language,sak):
      if lexi.lower()=="p":#έλεγχος για πάσο
         self.moves+=1
         self.passturn(sak)
         return True
      elif lexi.lower()=="q"  :#έλεγχος για quit
         self.moves+=1
         return "quit" 
      letter_list=[] #φτιάχνω μια προσωρινή λίστα από την οποία θα αφαιρώ ένα ένα τα γράμματα που βρίσκω ότι υπάρχουν στα γράμματα που έχουν δοθεί στον χρήστη
       #έλεγχος για το αν γίνεται με τα γράμματα που έχει ο χρήστης να γράψει την λέξη που έδωσε
       #ελέγχω ένα ένα τα γράμματα της λέξης αν υπάρχουν στα γράμματα που έχει ο χρήστης
      for i in range(0,len(self.letterlist)):
         letter_list.append(self.letterlist[i])  
      counter=0 
      for letter in lexi:
         num_of_letters=len(letter_list)
         for i in range(0,num_of_letters) :
            dictionary=letter_list[i]
            if letter==dictionary["letter"] :
               letter_list.pop(i)
               counter+=1
               break
      if counter==len(lexi):#αν το μήκος της λέξης ισούται με τον μετρητή που όριστηκε, 
                           # ο οποίος αυξάνεται κατά ένα κάθε φορά που βρίσκει ότι ένα γράμμα της λέξης που δόθηκε υπάρχει και στα γράμματα που έχει ο χρήστης
         elegxos=language.elegxos_leksis(lexi)#έλεγχος αν η λέξη ανήκει στο λεξικό greek7
         print (elegxos)
         if elegxos=="Άκυρη Λέξη": #η λέξη δεν ανήκει στο λεξικό           
            return False
         else:#η λέξη ανήκει στο λεξικό, οπότε μετράμε τους πόντους της
            self.moves+=1 #μόνο αν είναι η λέξη έγκυρη, αυξάνονται οι κινήσεις του παίκτη
            word_points=0
            for letter in lexi:
               counter_for_pop=0
               number_of_letters=len(self.letterlist)
               for i in range(0,number_of_letters) :
                  dictionary=self.letterlist[i-counter_for_pop]
                  if letter==dictionary["letter"] :
                     self.points+=dictionary["value"] #αυξάνονται οι πόντοι του παίχτη ανάλογα με την αξία των χρησιμοποιηθέντων γραμμάτων
                     word_points+=dictionary["value"]
                     self.letterlist.pop(i-counter_for_pop)
                     counter_for_pop+=1    
                     break
            print("Πόντοι Λέξης: ",word_points)   
            return True                     
      else: #δεν γίνεται να γράψει την λέξη που έδωσε με τα γράμματα που έχει
         print("Δεν γίνεται να γράψεις με τα γραμματά σου αυτή την λέξη : "+lexi) 
         return False
         
   def teach(self,language):#δείχνει στον παίκτη την καλύτερη επιλογή
      best_choice_list=self.get_best_word(language,self.letterlist)
      best_choice=best_choice_list[0]
      max_value=best_choice_list[1]
      return best_choice,max_value

   def __repr__(self):
       return super().__repr__()
    
class Computer(Player):
   def __init__(self, name="Pc"):
       super().__init__(name=name)   

   def play(self,language,sak):
      final_choice_list=self.get_best_word(language,sak)
      final_choice=final_choice_list[0]
      max_value=final_choice_list[1]
      print("Λέξη: ",final_choice,max_value,"πόντοι")
      if final_choice=="":#αν δεν έχει επιστραφεί κάποια λέξη από την συνάρτηση get_best_word της υπερκλάσης Player, ο υπολογιστής πάει πάσο
         self.passturn(sak)
         self.moves+=1
      else:   
         self.moves+=1
         self.points+=max_value
         for letter in final_choice:#αφαιρούνται τα γράμματα που χρησιμοποίησε ο υπολογιστής
            counter_for_pop=0
            number_of_letters=len(self.letterlist)
            for i in range(0,number_of_letters) :
               dictionary=self.letterlist[i-counter_for_pop]
               if letter==dictionary["letter"] :              
                  self.letterlist.pop(i-counter_for_pop)
                  counter_for_pop+=1    
                  break
      return final_choice
      
   def __repr__(self):
       return super().__repr__()

class Game:
   def __init__(self,filename) :
      self.language=Language(filename)
      self.sak=SakClass()    
      self.number_of_letters=7
      self.filename="SCORES.json"
      self.mode="1"
      self.setup()

   def setup(self):
      choice="99"# "ψεύτικη" τιμή για να μπει στην λούπα του while
      while(choice !="1" and choice !="2" and choice !="3" and choice!="q" ):
         print('\n***** SCRABBLE *****' )
         print("--------------------")   
         print( '1: Σκορ')
         print( '2: Ρυθμίσεις')
         print( '3: Παιχνίδι')
         print( 'q: Έξοδος')
         print("--------------------")  
         choice=input("Παρακαλώ Επιλέξτε :\n")
         if choice=="1":
            if os.path.exists(self.filename)==True:#αν υπάρχει το αρχείο, το διαβάζω
               with open(self.filename,'r',encoding='utf-8') as file:
                  data=file.read()
                  data_dict=eval(data)#μετατρέπουμε το κείμενο σε λεξικό
                  ar=0 #αριθμός παινχιδιού
                  print("")
                  for imeronia in data_dict.keys():
                     ar+=1
                     print(ar,".",imeronia)
                     im_dict=eval(data_dict[imeronia])
                     print("pc : ","moves:",im_dict["pc"]["moves"],"points:",im_dict["pc"]["points"])
                     print(im_dict['human']['name'],":","moves:",im_dict["human"]["moves"],"points:",im_dict["human"]["points"])
                     print("")
            else:
               print('Δεν υπάρχουν προηγούμενα παιχνίδια.')      
            choice="99"# "ψεύτικη" τιμή για να μπει στην λούπα του while και να γυρίσει στο κεντρικό μενού   
         elif choice=="2":
            print("")
            print('Η τωρινή ρύθμιση είναι ',self.mode)
            mode_choice=input("Παρακαλώ επιλέξτε\n1.Smart-Teach\n2.Smart\n")
            self.mode=mode_choice
            choice="99"# "ψεύτικη" τιμή για να μπει στην λούπα του while και να γυρίσει στο κεντρικό μενού   
            print("")
         elif choice=="3":
            print("")
            print("Κατά την διάρκεια του παιχνιδιού, αν θέλετε να πάτε πάσο, πατήστε p, ενώ αν θέλετε να σταματήσετε, πατήστε q.\n")
            name=input("Παρακαλώστε δώστε όνομα:\n")
            self.human=Human(name)
            self.human.mode=self.mode
            self.pc=Computer()
            self.give_letters_player(self.human)
            self.give_letters_player(self.pc)
            self.run()
         elif choice=="q":
            quit()
         else:
            print("Λάθος επιλογή, παρακαλώ ξαναδώστε")   

   def run(self):
      while True: #δίνει στον άνθρωπο 7 μείον όσα γράμματα έχει ήδη
         #παίζει ο άνθρωπος
         correct=False
         while correct==False:
            print(self.sak)
            print(self.human)
            word=input("Δώσε Λέξη: ")
            word=word.upper()#μετατρέπει τους πεζούς χαρακτήρες σε κεφαλαίους
            
            best_choice,max_value=self.human.teach(self.language)
            if best_choice=="" and len(self.sak.bag)==0:
               print("Δεν υπάρχει κάποια έγκυρη λέξη που μπορείς να γράψεις με τα γράμματα που έχεις και το σακουλάκι είναι άδειο.")
               self.end()
               quit()
            correct=self.human.play(word,self.language,self.sak)
            self.human.display_points()
            if self.human.mode=="1":         
               if best_choice==word:
                  print("Έκανες την καλύτερη επιλογή λέξης. Μπράβο σου!")               
               else:
                  print("Θα μπορούσες να είχες γράψει την λέξη "+best_choice+" η οποία θα μετρούσε για "+str(max_value)+" πόντους.")
            if correct=="quit":
               self.end()
               quit()   
         self.give_letters_player(self.human)

         input("Παρακαλώ Πατήστε Enter για συνέχεια\n")
         
         #Παίζει ο υπολογιστής
         print(self.sak)
         print(self.pc)
         final_choice=self.pc.play(self.language,self.sak)
         self.pc.display_points()
         if final_choice=="" and len(self.sak.bag)==0:
               print("Δεν υπάρχει κάποια έγκυρη λέξη που μπορεί να γράψει ο υπολογιστής με τα γράμματα που έχει και το σακουλάκι είναι άδειο.")
               self.end()
               quit()
         self.give_letters_player(self.pc)
         input("Παρακαλώ Πατήστε Enter για συνέχεια\n")
         
   def give_letters_player(self,player):
      player_letters=player.number_of_letters()
      player_letter_list=self.sak.getletters(self.number_of_letters-player_letters)
      player.giveletters(player_letter_list)

   def end(self):
      if self.human.points>self.pc.points:
         print("\nΣυγχαρητήρια "+self.human.name+" ,νίκησες! Συγκέντρωσες "+str(self.human.points)+" πόντους, ενώ ο υπολογιστής συγκέντρωσε "+str(self.pc.points)+".")
      else:
         print("\nΔυστυχώς, έχασες "+self.human.name+", συγκετρώνοντας "+str(self.human.points)+" πόντους, έναντι "+str(self.pc.points)+", που συγκέντρωσε ο υπολογιστής.")
      now = datetime.now()
      dt_string = now.strftime("%Y_%m_%d-%H_%M_%S")
      
      statistics={
      "pc":{
            "moves":self.pc.moves,
            "points":self.pc.points
         },
         "human":{
            "name":self.human.name,
            "moves":self.human.moves,
            "points":self.human.points
         }
      }
      newline=str(statistics)
      if os.path.exists(self.filename)==False:#αν δεν υπάρχει το αρχείο, το δημιουργώ
         with open(self.filename,'w',encoding='utf-8') as f:
            f.write(str({dt_string:newline}))#νέο λεξικό με κλειδί την ημερομηνία του παιχνιδιού και τιμή τα στατιστικά
         print("")
         print ("Tο παιχνίδι τελείωσε. Το αρχείο με τα στατιστικά: "+self.filename+ " δημιουργήθηκε.")  
         print("")
      else:#αν υπάρχει, διαβάζω τα δεδομένα του, 
         with open(self.filename,'r',encoding='utf-8') as file:
            data=file.read()
            data_dict=eval(data)#μετατρέπουμε το κείμενο σε λεξικό
            data_dict[dt_string]=newline
         with open(self.filename,'w',encoding='utf-8') as file:
            file.write(str(data_dict))
         print("")
         print ("Tο παιχνίδι τελείωσε. Το αρχείο με τα στατιστικά: "+self.filename+ " ενημερώθηκε.")  
         print("")