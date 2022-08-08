import random

class Object:
    def __repr__(self):
        return '<%s>' % getattr(self,'__name__',self.__class__.__name__)
   

class Agent(Object):
    def __init__(self):
        def program(percept):abstract
        self.program=program

##YOU WILL NEED TWO OTHER LOCATIONS
        
loc_A,loc_B,loc_C,loc_D='A','B','C','D'
        
class vaccumEnvironment():

    def __init__(self):

        ## MODIFY ACCORDING TO THE TASK ENVIRONMENT
        
        self.status={ loc_A:random.choice(['Clean','Dirty']),
                      loc_B:random.choice(['Clean','Dirty']),
                      loc_C:random.choice(['Clean','Dirty']),
                      loc_D:random.choice(['Clean','Dirty'])
                      }
        
    def add_object(self,object,location=None):
        object.location=location or self.default_location(object)

    def default_location(self,object):
        return random.choice([loc_A,loc_B,loc_C,loc_D])

    def percept(self,agent):
        return (agent.location,self.status[agent.location])

    def execute_action(self,agent,action):

            ## MODIFY ACCORDING TO THE TASK ENVIRONMENT
        
        if agent.location==loc_A and action=='Right' : agent.location=loc_B
        elif agent.location==loc_A and action=='Down' : agent.location=loc_C
        elif agent.location==loc_B and action=='Left' : agent.location=loc_A
        elif agent.location==loc_B and action=='Down' : agent.location=loc_D
        elif agent.location==loc_C and action=='Up' : agent.location=loc_A
        elif agent.location==loc_C and action=='Right' : agent.location=loc_D
        elif agent.location==loc_D and action=='Up' : agent.location=loc_B
        elif agent.location==loc_D and action=='Left' : agent.location=loc_C
        elif action=='Suck': self.status[agent.location]='Clean'
            #if self.status[agent.location]=='Dirty'
            
      

class tableDrivenAgent(Agent):

    def __init__(self,table):
        Agent.__init__(self)
        percepts=[]

        def program(percept):
            percepts.append(percept)
            print(percepts)
            action=table.get(tuple(percepts))
            print('Agent perceives ', percept, ' and does ', action)
            return action

        self.program=program



def tableDrivenVaccumAgent():
    table = {
              ((loc_A,'Clean'),): random.choice(['Right','Down']),
              ((loc_A,'Dirty'),):'Suck',
              ((loc_A,'Clean'),(loc_B,'Clean')): random.choice(['Left','Down']),
              ((loc_A,'Clean'),(loc_B,'Dirty')):'Suck',
              ((loc_A,'Clean'),(loc_C,'Clean')): random.choice(['Right','Up']),
              ((loc_A,'Clean'),(loc_C,'Dirty')):'Suck',
              ((loc_A,'Clean'),(loc_C,'Clean'),(loc_D,'Clean')): random.choice(['Left','Up']),
              ((loc_A,'Clean'),(loc_C,'Clean'),(loc_D,'Dirty')): 'Suck',
              ((loc_A,'Clean'),(loc_B,'Clean'),(loc_D,'Clean')): random.choice(['Left','Up']),
              ((loc_A,'Clean'),(loc_B,'Clean'),(loc_D,'Dirty')): 'Suck',
              ((loc_B,'Clean'),): random.choice(['Left','Down']),
              ((loc_B,'Dirty'),):'Suck',
              ((loc_B,'Clean'),(loc_A,'Clean')): random.choice(['Right','Down']),
              ((loc_B,'Clean'),(loc_A,'Dirty')):'Suck',
              ((loc_B,'Clean'),(loc_D,'Clean')): random.choice(['Left','Up']),
              ((loc_B,'Clean'),(loc_D,'Dirty')):'Suck',
              ((loc_B,'Clean'),(loc_A,'Clean'),(loc_C,'Clean')): random.choice(['Right','Up']),
              ((loc_B,'Clean'),(loc_A,'Clean'),(loc_C,'Dirty')): 'Suck',
              ((loc_B,'Clean'),(loc_D,'Clean'),(loc_C,'Clean')): random.choice(['Up','Right']),
              ((loc_B,'Clean'),(loc_D,'Clean'),(loc_C,'Dirty')): 'Suck',
              ((loc_C,'Clean'),): random.choice(['Up','Right']),
              ((loc_C,'Dirty'),):'Suck',
              ((loc_C,'Clean'),(loc_A,'Clean')): random.choice(['Right','Down']),
              ((loc_C,'Clean'),(loc_A,'Dirty')):'Suck',
              ((loc_C,'Clean'),(loc_D,'Clean')): random.choice(['Left','Up']),
              ((loc_C,'Clean'),(loc_D,'Dirty')):'Suck',
              ((loc_C,'Clean'),(loc_A,'Clean'),(loc_B,'Clean')): random.choice(['Left','Down']),
              ((loc_C,'Clean'),(loc_A,'Clean'),(loc_B,'Dirty')): 'Suck',
              ((loc_C,'Clean'),(loc_D,'Clean'),(loc_B,'Clean')): random.choice(['Left','Down']),
              ((loc_C,'Clean'),(loc_D,'Clean'),(loc_B,'Dirty')): 'Suck',
              ((loc_D,'Clean'),): random.choice(['Up','Left']),
              ((loc_D,'Dirty'),):'Suck',
              ((loc_D,'Clean'),(loc_B,'Clean')): random.choice(['Left','Down']),
              ((loc_D,'Clean'),(loc_B,'Dirty')):'Suck',
              ((loc_D,'Clean'),(loc_C,'Clean')): random.choice(['Up','Right']),
              ((loc_D,'Clean'),(loc_C,'Dirty')):'Suck',
              ((loc_D,'Clean'),(loc_B,'Clean'),(loc_A,'Clean')): random.choice(['Right','Down']),
              ((loc_D,'Clean'),(loc_B,'Clean'),(loc_A,'Dirty')): 'Suck',
              ((loc_D,'Clean'),(loc_C,'Clean'),(loc_A,'Clean')): random.choice(['Right','Down']),
              ((loc_D,'Clean'),(loc_C,'Clean'),(loc_A,'Dirty')): 'Suck'
              
##            WRITE TABLE ACCORDING TO THE TASK ENVIRONMENT

            }
    return tableDrivenAgent(table)

#Tagent=tableDrivenVaccumAgent()
#env=vaccumEnvironment()
#env.add_object(Tagent)
##
#for _ in range(10):
#    action=Tagent.program(env.percept(Tagent))
#    env.execute_action(Tagent,action)

class reflexVaccumAgent(Agent):
    
    def __init__(self):
        Agent.__init__(self)        

        def program(percept):
            location=percept[0]
            status=percept[1]

##            MODIFY THE CONDITION-ACTION RULE BELOW

            if status=='Dirty': action= 'Suck'
            elif location==loc_A: action= random.choice(['Right','Down'])
            elif location==loc_B: action= random.choice(['Left','Down'])
            elif location==loc_C: action= random.choice(['Up','Right'])
            elif location==loc_D: action= random.choice(['Left','Up'])

            percept=(location,status)
            print('Agent perceives ', percept, ' and does ', action)

            return action
        
            
            
        self.program=program


### YOU NEED TO CREATE AGENT AND ENVIRONMENT INSTANT AND ITERATE HERE
### TAKE IDEA FROM TABLE DRIVEN AGENT INSTANT RUNNING
#Rangent=reflexVaccumAgent()
#env=vaccumEnvironment()
#env.add_object(Rangent)
##
#for _ in range(15):
#    action=Rangent.program(env.percept(Rangent))
#    env.execute_action(Rangent,action)

        
class modelBasedVaccumAgent(Agent):
    def __init__(self):
        Agent.__init__(self)
        
        model={loc_A:None,loc_B:None,loc_C:None,loc_D:None}

        def program(percept):
            location=percept[0]
            status=percept[1]
##            
            model[location]=status
            
            ##            WRITE YOUR CODE HERE
            if model[loc_A]==model[loc_B]==model[loc_C]==model[loc_D]=='Clean': return 'None'
            elif status=='Dirty': action= 'Suck'
            elif location==loc_A: action= random.choice(['Right','Down'])
            elif location==loc_B: action= random.choice(['Left','Down'])
            elif location==loc_C: action= random.choice(['Up','Right'])
            elif location==loc_D: action= random.choice(['Left','Up'])

            percept=(location,status)
            print('Agent perceives ', percept, ' and does ', action)

            return action                    
            
        self.program=program
        

### YOU NEED TO CREATE AGENT AND ENVIRONMENT INSTANT AND ITERATE HERE
### TAKE IDEA FROM TABLE DRIVEN AGENT INSTANT RUNNING
Magent=modelBasedVaccumAgent()
env=vaccumEnvironment()
env.add_object(Magent)
##
for _ in range(105):
    action=Magent.program(env.percept(Magent))
    env.execute_action(Magent,action)
