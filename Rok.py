import pyautogui
import mouse
import time
import cv2
import keyboard
import argparse

running = True


parser = argparse.ArgumentParser()
parser.add_argument('-a','--action', type=int)
args = parser.parse_args()

def collect_vill():
    try:
            x = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\x.png", confidence=.8)
            pyautogui.leftClick(x)
    except:
        pass
    time.sleep(.8)
    try:
        found = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\found.png", confidence=.9)
        pyautogui.leftClick(found)
        time.sleep(.8)
        
        try:
            Vil = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\villages\villages.png", confidence=.8)
            pyautogui.leftClick(Vil)
            time.sleep(.8)
            try:
                go = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\villages\go.png", confidence=.8)
                pyautogui.leftClick(go)
                time.sleep(3.8)
                screen_width, screen_height = pyautogui.size()
                center_x = screen_width / 2
                center_y = screen_height / 2
                pyautogui.leftClick((center_x), (center_y))
                time.sleep(1.8)
                
                try:
                    
                    City = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\city.png", confidence=.8)
                    pyautogui.leftClick(City)
                except:
                    pass    
                        
                
            except:
                pass
        except:
            pass
    except:
        pass
    try:
        ReadyScout = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\ready_explore.png", confidence=.8)
        pyautogui.leftClick(((ReadyScout[0]), (ReadyScout[1]+175)))#click open training
        time.sleep(.8)
        try:
            OpenScout = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\open_scout.png", confidence=.8)
            pyautogui.leftClick(OpenScout)
            time.sleep(.8)
            try:
                Vil = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\villages\villages.png", confidence=.8)
                pyautogui.leftClick(Vil)
                time.sleep(.8)
                try:
                    go = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\villages\go.png", confidence=.8)
                    pyautogui.leftClick(go)
                    time.sleep(3.8)
                    screen_width, screen_height = pyautogui.size()
                    center_x = screen_width / 2
                    center_y = screen_height / 2
                    pyautogui.leftClick((center_x), (center_y))
                    time.sleep(1.8)
                
                    try:
                    
                        City = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\city.png", confidence=.8)
                        pyautogui.leftClick(City)
                    except:
                        pass    
                        
                
                except:
                    pass
            except:
                pass
        except:
            pass
    except:
        pass

def collect_caves():
    
    try:
            x = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\x.png", confidence=.8)
            pyautogui.leftClick(x)
    except:
        pass
    time.sleep(.8)
    try:
        found = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\found.png", confidence=.9)
        pyautogui.leftClick(found)
        time.sleep(1)
        
        try:
            Explore = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\explore.png", confidence=.9)
            pyautogui.leftClick(Explore)
            time.sleep(3.0)
            try:
                Explore2 = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\explore.png", confidence=.8)
                pyautogui.leftClick(Explore2)
                time.sleep(1.0)
                try:
                    Send = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\send.png", confidence=.8)
                    pyautogui.leftClick(Send)
                    time.sleep(.8)
                    try:
                        City = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\city.png", confidence=.8)
                        pyautogui.leftClick(City)
                    except:
                        pass
                except:
                    try:
                        City = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\city.png", confidence=.8)
                        pyautogui.leftClick(City)
                    except:
                        pass
                    pass
            except:
                pass
        except:
            pass
        try:
            x = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\x.png", confidence=.8)
            pyautogui.leftClick(x)
        except:
            pass
    except:
        pass
    try:
        ReadyScout = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\ready_explore.png", confidence=.8)
        pyautogui.leftClick(((ReadyScout[0]), (ReadyScout[1]+200)))#click open training
        time.sleep(.8)
        try:
            OpenScout = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\open_scout.png", confidence=.8)
            pyautogui.leftClick(OpenScout)
            time.sleep(.8)
            try:
                caves = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\cave\caves.png", confidence=.7)
                pyautogui.leftClick(caves)
                time.sleep(1.0)
                try:
                    go = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\cave\go.png", confidence=.8)
                    pyautogui.leftClick(go)
                    time.sleep(3.0)
                    screen_width, screen_height = pyautogui.size()
                    center_x = screen_width / 2
                    center_y = screen_height / 2
                    pyautogui.leftClick((center_x), (center_y-25))
                    time.sleep(1.8)
                    try:
                            inv = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\cave\Invest.png", confidence=.8)
                            pyautogui.leftClick(inv)
                            time.sleep(.8)
                            try:
                                Send = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\send.png", confidence=.8)
                       
                                pyautogui.leftClick(Send)
                                time.sleep(.8)
                                try:
                                    City = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\city.png", confidence=.8)
                                    pyautogui.leftClick(City)
                                except:
                                    pass
                            except:
                                try:
                                    City = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\city.png", confidence=.8)
                                    pyautogui.leftClick(City)
                                except:
                                    pass
                                pass
                    except:
                        try:
                            City = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\city.png", confidence=.8)
                            pyautogui.leftClick(City)
                        except:
                            pass
                        pass
                    
                except:
                    pass
            except:
                pass
        except:
            pass
    except:
        pass


def check_scout():
    try:
            x = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\x.png", confidence=.8)
            pyautogui.leftClick(x)
    except:
        pass
    time.sleep(.8)
    try:
        found = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\found.png", confidence=.7)
        pyautogui.leftClick(found)
        time.sleep(1)
        
        try:
            Explore = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\explore.png", confidence=.7)
            pyautogui.leftClick(Explore)
            time.sleep(3.5)
            try:
                Explore2 = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\explore.png", confidence=.8)
                pyautogui.leftClick(Explore2)
                time.sleep(2)
                try:
                    Send = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\send.png", confidence=.8)
                    pyautogui.leftClick(Send)
                    time.sleep(.8)
                    try:
                        City = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\city.png", confidence=.8)
                        pyautogui.leftClick(City)
                    except:
                        pass
                except:
                    try:
                        City = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\city.png", confidence=.8)
                        pyautogui.leftClick(City)
                    except:
                        pass
                    pass
            except:
                pass
        except:
            pass
        try:
            x = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\x.png", confidence=.8)
            pyautogui.leftClick(x)
        except:
            pass
    except:
        pass
    try:
        ReadyScout = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\ready_explore.png", confidence=.8)
        pyautogui.leftClick(((ReadyScout[0]), (ReadyScout[1]+200)))#click open training
        time.sleep(.8)
        try:
            OpenScout = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\open_scout.png", confidence=.8)
            pyautogui.leftClick(OpenScout)
            time.sleep(.8)
            try:
                Explore = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\explore.png", confidence=.7)
                pyautogui.leftClick(Explore)
                time.sleep(3.2)
                try:
                    Explore2 = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\explore.png", confidence=.8)
                    pyautogui.leftClick(Explore2)
                    time.sleep(2)
                    try:
                        Send = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\send.png", confidence=.8)
                        pyautogui.leftClick(Send)
                        time.sleep(.8)
                        try:
                            City = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\city.png", confidence=.8)
                            pyautogui.leftClick(City)
                        except:
                            pass
                    except:
                        try:
                            City = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\ex\city.png", confidence=.8)
                            pyautogui.leftClick(City)
                        except:
                            pass
                        pass
                except:
                    pass
            except:
                pass
        except:
            pass
    except:
        pass



def check_training():
    t1inf = None
    t1arch = None
    t1cav = None
    t1seige = None
    try:
       
        t1inf = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\inf\T1_ready_to_collect.png", confidence=.9)
        train_inf(t1inf)
    except:
        pass
    time.sleep(.8)
    try:
       
        t1arch = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\arch\T1_ready_to_collect.png", confidence=.9)
        train_arch(t1arch)
    except:
        pass
    time.sleep(.8)
    try:
       
        t1cav = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\cav\T1_ready_to_collect.png", confidence=.9)
        train_cav(t1cav)
    except:
        pass
    time.sleep(.8)
    try:
       
        t1seige = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\seige\T1_ready_to_collect.png", confidence=.9)
        train_seige(t1seige)
    except:
        pass
   

def train_inf(loc):
    opentrain = None
    train = None
    pyautogui.leftClick(loc) # collect
    pyautogui.leftClick(((loc[0]), (loc[1]+75))) # open menu 
    time.sleep(.8)
    try:
        opentrain = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\inf\Open_training.png", confidence=.8)
        
        pyautogui.leftClick(opentrain)#click open training
        time.sleep(.8)
        try:
            train = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\inf\Train.png", confidence=.8)
            pyautogui.leftClick(train)
        except:
            pass
    except:
        pass
   
def train_arch(loc):
    opentrain = None
    train = None
    pyautogui.leftClick(loc) # collect
    pyautogui.leftClick(((loc[0]), (loc[1]+75))) # open menu 
    time.sleep(.8)
    try:
        opentrain = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\arch\Open_training.png", confidence=.8)
        
        pyautogui.leftClick(opentrain)#click open training
        time.sleep(.8)
        try:
            train = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\arch\Train.png", confidence=.8)
            pyautogui.leftClick(train)
        except:
            pass
    except:
        pass        
    
    
def train_cav(loc):
    opentrain = None
    train = None
    pyautogui.leftClick(loc) # collect
    pyautogui.leftClick(((loc[0]), (loc[1]+75))) # open menu 
    time.sleep(.8)
    try:
        opentrain = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\cav\Open_training.png", confidence=.8)
        
        pyautogui.leftClick(opentrain)#click open training
        time.sleep(.8)
        try:
            train = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\cav\Train.png", confidence=.8)
            pyautogui.leftClick(train)
        except:
            pass
    except:
        pass                
  

def train_seige(loc):
    opentrain = None
    train = None
    pyautogui.leftClick(loc) # collect
    pyautogui.leftClick(((loc[0]), (loc[1]+100))) # open menu 
    time.sleep(.8)
    try:
        opentrain = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\seige\Open_training.png", confidence=.8)
        
        pyautogui.leftClick(opentrain)#click open training
        time.sleep(.8)
        try:
            train = pyautogui.locateCenterOnScreen(Default_Path+r"\Rok img\seige\Train.png", confidence=.8)
            pyautogui.leftClick(train)
        except:
            pass
    except:
        pass        


   
while running:

    if keyboard.is_pressed("ctrl+c"):
        running = False
    
    if(args.action == 1):
        #scout
        time.sleep(10)
        check_scout()
    elif(args.action == 2):
        time.sleep(.5)
        #vil
        collect_vill()
    elif(args.action == 3):
        time.sleep(.5)
        #cave
        collect_caves()
    else:
        print("1: Scout + train | 2: Collect villages+ train | 3: Collect Caves + train")
        quit()
   
    time.sleep(1)
    
    check_training()
    
  
