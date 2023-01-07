# ========================================
# Modules
# ========================================

# Import moldules
from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkFont
import tkinter.scrolledtext as scrolledtext
from random import *

from PIL import ImageTk, Image

#DEL import RPi.#DEL GPIO as #DEL GPIO

# ========================================
# Interfacing
# ========================================

coreDark = "#151515"
coreMedium = "#CCCCCC"
coreLight = "#F5F5F5"

orderedRed = "#f94a38"
orderedBlue = "#2f84d4"
orderedYellow = "#fbc338"

orderedGreen = "#77d04c"
orderedGreenLight = "#89d466"
orderedGreenLighter = "#a9e090"
orderedGreenLightest = "#c6edb4"

orderedGreenRelief = "#29b027"

# Create the main Tkinter module
master = Tk()
master.title("Ordernyms")
master.config(background=coreDark)
master.resizable(False, False)

# Save fonts as defined font families
lightBody = tkFont.Font(family="Open Sans Light", size=12)
lightTitle = tkFont.Font(family="Open Sans Light", size=16)
boldTitle = tkFont.Font(family="Open Sans", weight="bold", size=16)

# Save the player expressions as static resources
player1Neutral = ImageTk.PhotoImage(Image.open('Character Icons/Player 1 Neutral.png').resize((105,105), Image.ANTIALIAS))
player1Awaiting = ImageTk.PhotoImage(Image.open('Character Icons/Player 1 Awaiting.png').resize((105,105), Image.ANTIALIAS))
player1Worried = ImageTk.PhotoImage(Image.open('Character Icons/Player 1 Worried.png').resize((105,105), Image.ANTIALIAS))
player1Faceoff = ImageTk.PhotoImage(Image.open('Character Icons/Player 1 Faceoff.png').resize((105,105), Image.ANTIALIAS))
player1Win = ImageTk.PhotoImage(Image.open('Character Icons/Player 1 Win.png').resize((105,105), Image.ANTIALIAS))
player1Lose = ImageTk.PhotoImage(Image.open('Character Icons/Player 1 Lost.png').resize((105,105), Image.ANTIALIAS))

player2Neutral = ImageTk.PhotoImage(Image.open('Character Icons/Player 2 Neutral.png').resize((105,105), Image.ANTIALIAS))
player2Awaiting = ImageTk.PhotoImage(Image.open('Character Icons/Player 2 Awaiting.png').resize((105,105), Image.ANTIALIAS))
player2Worried = ImageTk.PhotoImage(Image.open('Character Icons/Player 2 Worried.png').resize((105,105), Image.ANTIALIAS))
player2Faceoff = ImageTk.PhotoImage(Image.open('Character Icons/Player 2 Faceoff.png').resize((105,105), Image.ANTIALIAS))
player2Win = ImageTk.PhotoImage(Image.open('Character Icons/Player 2 Win.png').resize((105,105), Image.ANTIALIAS))
player2Lose = ImageTk.PhotoImage(Image.open('Character Icons/Player 2 Lost.png').resize((105,105), Image.ANTIALIAS))

# Create the interface sections
exampleSentenceDisplay = Frame(master, height=100, width = 500)
synonymPromptDisplay = Frame(master, height=75, width = 500)

synonymAnswer1Display = Frame(master, height=50, width = 250)
synonymAnswer2Display = Frame(master, height=50, width = 250)
synonymAnswer3Display = Frame(master, height=50, width = 250)
synonymAnswer4Display = Frame(master, height=50, width = 250)
synonymAnswer5Display = Frame(master, height=50, width = 250)

player1ProfilePictureDisplay = Label(master, image=player1Neutral, background=orderedRed, height=100, width = 100)
player2ProfilePictureDisplay = Label(master, image=player1Neutral, background=orderedBlue, height=100, width = 100)

player1ScoreDisplay = Frame(master, height=50, width = 150)
player1WinsDisplay = Frame(master, height=50, width = 150)

player2ScoreDisplay = Frame(master, height=50, width = 150)
player2WinsDisplay = Frame(master, height=50, width = 150)

messageLogDisplay = Frame(master, height=395, width = 450)
messageInputDisplay = Frame(master, height=50, width = 380)
messageButtonDisplay = Frame(master, height=50, width = 50)

# Setup the interface sections
exampleSentenceDisplay.grid(row = 0, column = 0, columnspan=4)
synonymPromptDisplay.grid(row = 1, column = 0, columnspan=4)

synonymAnswer1Display.grid(row = 2, column = 0, columnspan=2, padx=5, pady=5)
synonymAnswer2Display.grid(row = 3, column = 0, columnspan=2, padx=5, pady=5)
synonymAnswer3Display.grid(row = 4, column = 0, columnspan=2, padx=5, pady=5)
synonymAnswer4Display.grid(row = 2, column = 2, columnspan=2, padx=5, pady=5)
synonymAnswer5Display.grid(row = 3, column = 2, columnspan=2, padx=5, pady=5)

player1ProfilePictureDisplay.grid(row = 5, column = 0, rowspan=2, padx=10, pady=10)
player1ScoreDisplay.grid(row = 5, column = 1)
player1WinsDisplay.grid(row = 6, column = 1)

player2ProfilePictureDisplay.grid(row = 5, column = 2, rowspan=2, padx=10, pady=10)
player2ScoreDisplay.grid(row = 5, column = 3)
player2WinsDisplay.grid(row = 6, column = 3)

messageLogDisplay.grid (row = 0, column = 4, rowspan = 6, columnspan=2, sticky = S, padx=10)
messageInputDisplay.grid (row = 6, column = 4)
messageButtonDisplay.grid (row = 6, column = 5, pady=10)

# Pack propogate the interface sections so the elements fill
exampleSentenceDisplay.pack_propagate(0)
synonymPromptDisplay.pack_propagate(0)

synonymAnswer1Display.pack_propagate(0)
synonymAnswer2Display.pack_propagate(0)
synonymAnswer3Display.pack_propagate(0)
synonymAnswer4Display.pack_propagate(0)
synonymAnswer5Display.pack_propagate(0)

player1ScoreDisplay.pack_propagate(0)
player1WinsDisplay.pack_propagate(0)
player2ScoreDisplay.pack_propagate(0)
player2WinsDisplay.pack_propagate(0)

messageLogDisplay.pack_propagate(0)
messageInputDisplay.pack_propagate(0)
messageButtonDisplay.pack_propagate(0)

# Create the interface elements
exampleSentenceLabel = Label(exampleSentenceDisplay, background=coreDark, foreground=coreLight, text="Welcome to Ordernyms, an ultimate battle of the vocabularies! Who is the better writer?", font = lightTitle, wraplength=500)
synonymPromptLabel = Label(synonymPromptDisplay, background=coreDark, foreground=coreLight, text="Hope you have a great game.", font = boldTitle, wraplength=500)

synonymAnswer1Label = Label(synonymAnswer1Display, background=coreMedium, font = lightTitle)
synonymAnswer2Label = Label(synonymAnswer2Display, background=coreMedium, font = lightTitle)
synonymAnswer3Label = Label(synonymAnswer3Display, background=coreMedium, font = lightTitle)
synonymAnswer4Label = Label(synonymAnswer4Display, background=coreMedium, font = lightTitle)
synonymAnswer5Label = Label(synonymAnswer5Display, background=coreMedium, font = lightTitle)

player1ScoreLabel = Label(player1ScoreDisplay, background=coreDark, foreground=coreLight, font = boldTitle)
player1WinsLabel = Label(player1WinsDisplay, background=coreDark, foreground=coreLight, font = boldTitle)

player2ScoreLabel = Label(player2ScoreDisplay, background=coreDark, foreground=coreLight, font = boldTitle)
player2WinsLabel = Label(player2WinsDisplay, background=coreDark, foreground=coreLight, font = boldTitle)

messageLogLabel = scrolledtext.ScrolledText(messageLogDisplay, width=400, font=lightBody, wrap=WORD, spacing3=5)

ttk.Style().configure('pad.TEntry', padding='10')
messageInputEntry = ttk.Entry(messageInputDisplay, font=lightTitle, style='pad.TEntry')

messageInputButton = Button(messageButtonDisplay, font=boldTitle,text="OK", background=orderedGreen, activebackground=orderedGreenRelief, relief=FLAT)

# Setup the interface elements
exampleSentenceLabel.pack(fill=BOTH, expand=1)
synonymPromptLabel.pack(fill=BOTH, expand=1)

player1ScoreLabel.pack(fill=BOTH, expand=1)
player1WinsLabel.pack(fill=BOTH, expand=1)

player2ScoreLabel.pack(fill=BOTH, expand=1)
player2WinsLabel.pack(fill=BOTH, expand=1)

synonymAnswer1Label.pack(fill=BOTH, expand=1)
synonymAnswer2Label.pack(fill=BOTH, expand=1)
synonymAnswer3Label.pack(fill=BOTH, expand=1)
synonymAnswer4Label.pack(fill=BOTH, expand=1)
synonymAnswer5Label.pack(fill=BOTH, expand=1)

messageLogLabel.pack(anchor=W, side=BOTTOM)
messageInputEntry.pack(fill=BOTH, expand=1)
messageInputButton.pack(fill=BOTH, expand=1)

# ========================================
# Interface Management
# ========================================

def PrintToLog(message):
    messageLogLabel.config(state=NORMAL)

    # Insert the message to the message log and scroll to the end
    messageLogLabel.insert(END, message + "\n")
    messageLogLabel.see(END)

    messageLogLabel.config(state=DISABLED)
    
def PrintMessageAsync(message):
    # Manage the message timing
    global rollingDelay
    global messageSpeed

    # Queue the message printing asyncronously and adjust the delay for the next message 
    master.after(rollingDelay, PrintToLog, message)
    rollingDelay += messageSpeed

def SetAwaitStateAsync(state):
    global awaitState
    awaitState = state

def RefreshPositionsDisplay(revealAnswers):
    synomyms = roundData[2:7]

    # If the answers shouldn't be revealed, update the positions display with yellow labels for their guess
    if (revealAnswers == False):
        if (playerGuessConfiguration[0] != None):
            synonymAnswer1Label.config(text="1st: " + synomyms[playerGuessConfiguration[0]])
            synonymAnswer1Label.config(background=orderedYellow)
        else:
            synonymAnswer1Label.config(text="1st: ???")
            synonymAnswer1Label.config(background=coreMedium)

        if (playerGuessConfiguration[1] != None):
            synonymAnswer2Label.config(text="2nd: " + synomyms[playerGuessConfiguration[1]])
            synonymAnswer2Label.config(background=orderedYellow)
        else:
            synonymAnswer2Label.config(text="2nd: ???")
            synonymAnswer2Label.config(background=coreMedium)
            
        if (playerGuessConfiguration[2] != None):
            synonymAnswer3Label.config(text="3rd: " + synomyms[playerGuessConfiguration[2]])
            synonymAnswer3Label.config(background=orderedYellow)
        else:
            synonymAnswer3Label.config(text="3rd: ???")
            synonymAnswer3Label.config(background=coreMedium)
            
        if (playerGuessConfiguration[3] != None):
            synonymAnswer4Label.config(text="4th: " + synomyms[playerGuessConfiguration[3]])
            synonymAnswer4Label.config(background=orderedYellow)
        else:
            synonymAnswer4Label.config(text="4th: ???")
            synonymAnswer4Label.config(background=coreMedium)
            
        if (playerGuessConfiguration[4] != None):
            synonymAnswer5Label.config(text="5th: " + synomyms[playerGuessConfiguration[4]])
            synonymAnswer5Label.config(background=orderedYellow)
        else:
            synonymAnswer5Label.config(text="5th: ???")
            synonymAnswer5Label.config(background=coreMedium)

    # Otherwise, update the positons display with green labels for the correct answers
    else:
        coloringConfiguration = [None,None,None,None,None]

        for position in range (0,5):           
            if (abs(playerGuessConfiguration[position] - position) == 0):
                coloringConfiguration[position] = orderedGreen
                
            elif (abs(playerGuessConfiguration[position] - position) == 1):
                coloringConfiguration[position] = orderedGreenLight

            elif (abs(playerGuessConfiguration[position] - position) == 2):
                coloringConfiguration[position] = orderedGreenLighter

            elif (abs(playerGuessConfiguration[position] - position) == 3):
                coloringConfiguration[position] = orderedGreenLightest

            else:
                coloringConfiguration[position] = coreLight
        
        synonymAnswer1Label.config(text="1st: " + synomyms[0])
        synonymAnswer1Label.config(background=coloringConfiguration[0])
        synonymAnswer2Label.config(text="2nd: " + synomyms[1])
        synonymAnswer2Label.config(background=coloringConfiguration[1])
        synonymAnswer3Label.config(text="3rd: " + synomyms[2])
        synonymAnswer3Label.config(background=coloringConfiguration[2])
        synonymAnswer4Label.config(text="4th: " + synomyms[3])
        synonymAnswer4Label.config(background=coloringConfiguration[3])
        synonymAnswer5Label.config(text="5th: " + synomyms[4])
        synonymAnswer5Label.config(background=coloringConfiguration[4])

def RefreshScoreboardDisplay():
    player1ScoreLabel.config(text = str(player1Score) + " pts.")
    player1WinsLabel.config(text = str(player1Wins) + " wins")

    player2ScoreLabel.config(text = str(player2Score) + " pts.")
    player2WinsLabel.config(text = str(player2Wins) + " wins")

def RefreshSentenceDisplay(sentence, targetWord):
    exampleSentenceLabel.config(text=sentence)
    synonymPromptLabel.config(text="What is the best replacement for " + targetWord + "?")
        
        
def RefreshProfilePictures():
    # If Player 1 has won...
    if (player1Wins == 3):
        player1ProfilePictureDisplay.config(image = player1Win)
        player1ProfilePictureDisplay.image = player1Win
        
        player2ProfilePictureDisplay.config(image = player2Lose)
        player2ProfilePictureDisplay.image = player2Lose
        
    # If Player 2 has won...    
    elif (player2Wins == 3):
        player1ProfilePictureDisplay.config(image = player1Lose)
        player1ProfilePictureDisplay.image = player1Lose
        
        player2ProfilePictureDisplay.config(image = player2Win)
        player2ProfilePictureDisplay.image = player2Win
        
    # If this round is the decider...   
    elif (player1Wins == 2 and player2Wins == 2):
        player1ProfilePictureDisplay.config(image = player1Faceoff)
        player1ProfilePictureDisplay.image = player1Faceoff
        
        player2ProfilePictureDisplay.config(image = player2Faceoff)
        player2ProfilePictureDisplay.image = player2Faceoff
    
    # If Player 1 is dominating...
    elif (player1Wins == 2):
        player1ProfilePictureDisplay.config(image = player1Faceoff)
        player1ProfilePictureDisplay.image = player1Faceoff
        
        player2ProfilePictureDisplay.config(image = player2Worried)
        player2ProfilePictureDisplay.image = player2Worried
        
    # If Player 2 is domianting...
    elif (player2Wins == 2):
        player1ProfilePictureDisplay.config(image = player1Worried)
        player1ProfilePictureDisplay.image = player1Worried
        
        player2ProfilePictureDisplay.config(image = player2Faceoff)
        player2ProfilePictureDisplay.image = player2Faceoff
        
    # If it is Player 1's turn...
    elif (currentPlayer == 1):
        player1ProfilePictureDisplay.config(image = player1Awaiting)
        player1ProfilePictureDisplay.image = player1Awaiting
        
        player2ProfilePictureDisplay.config(image = player2Neutral)
        player2ProfilePictureDisplay.image = player2Neutral
        
    # If it is Player 2's turn...       
    elif (currentPlayer == 2):
        player1ProfilePictureDisplay.config(image = player1Neutral)
        player1ProfilePictureDisplay.image = player1Neutral
        
        player2ProfilePictureDisplay.config(image = player2Awaiting)
        player2ProfilePictureDisplay.image = player2Awaiting
        
    # Otherwise (should never be fallen into)
    else:
        player1ProfilePictureDisplay.config(image = player1Faceoff)
        player1ProfilePictureDisplay.image = player1Faceoff

# ========================================
# #DEL GPIO Management
# ========================================

def SetupPinModes():
    #DEL GPIO.setmode(#DEL GPIO.BCM)
    
    # Setup scoreboard pins to the OUTPUT mode (2-4, 17, 27)    
    #DEL GPIO.setup(scoreboardPins[0], #DEL GPIO.OUT)
    #DEL GPIO.setup(scoreboardPins[1], #DEL GPIO.OUT)
    #DEL GPIO.setup(scoreboardPins[2], #DEL GPIO.OUT)
    #DEL GPIO.setup(scoreboardPins[3], #DEL GPIO.OUT)
    #DEL GPIO.setup(scoreboardPins[4], #DEL GPIO.OUT)

    # Setup turn pins to the OUTPUT mode (9, 11)    
    #DEL GPIO.setup(playerTurnPins[0], #DEL GPIO.OUT)
    #DEL GPIO.setup(playerTurnPins[1], #DEL GPIO.OUT)

    # Setup position pins to the OUTPUT mode (5, 6, 13, 19, 26)  
    #DEL GPIO.setup(positionPins[0], #DEL GPIO.OUT)
    #DEL GPIO.setup(positionPins[1], #DEL GPIO.OUT)
    #DEL GPIO.setup(positionPins[2], #DEL GPIO.OUT)
    #DEL GPIO.setup(positionPins[3], #DEL GPIO.OUT)
    #DEL GPIO.setup(positionPins[4], #DEL GPIO.OUT)

    # Setup button pins to the INPUT mode (14, 15, 18) 
    #DEL GPIO.setup(16, #DEL GPIO.IN, pull_up_down=#DEL GPIO.PUD_UP)
    #DEL GPIO.setup(20, #DEL GPIO.IN, pull_up_down=#DEL GPIO.PUD_UP)
    #DEL GPIO.setup(21, #DEL GPIO.IN, pull_up_down=#DEL GPIO.PUD_UP)

    pass
    
def SetLEDState(pin, state):
    #DEL GPIO.output(pin, state)
    pass
          
def RefreshScoreboardPins():
    global scoreboardPins
    
    # If player 1 has won a single round, activate the appropriate pin
    if (player1Wins == 1):
        scoreboardPinStates[0] = 1
        
    # If player 1 has won two round, activate the appropriate pin
    if (player1Wins == 2):
        scoreboardPinStates[1] = 1
        
    # If player 2 has won a single round, activate the appropriate pin
    if (player2Wins == 1):
        scoreboardPinStates[4] = 1
    
    # If player 2 has won two round, activate the appropriate pin
    if (player2Wins == 2):
        scoreboardPinStates[3] = 1
        
    # If player 1 has won the game, activate and deactivate the appropriate pins
    if (player1Wins == 3):
        scoreboardPinStates[2] = 1
        scoreboardPinStates[3] = 0     
        scoreboardPinStates[4] = 0
        
    # If player 2 has won the game, activate and deactivate the appropriate pins
    if (player2Wins == 3):
        scoreboardPinStates[0] = 0     
        scoreboardPinStates[1] = 0
        scoreboardPinStates[2] = 1
    
    # Update the scoreboard pins' states
    SetLEDState(scoreboardPins[0], scoreboardPinStates[0])
    SetLEDState(scoreboardPins[1], scoreboardPinStates[1])
    SetLEDState(scoreboardPins[2], scoreboardPinStates[2])
    SetLEDState(scoreboardPins[3], scoreboardPinStates[3])
    SetLEDState(scoreboardPins[4], scoreboardPinStates[4])   
       
def RefreshPlayerTurnPins():
    # Update the turn pins' states
    SetLEDState(playerTurnPins[0], playerTurnPinStates[0])
    SetLEDState(playerTurnPins[1], playerTurnPinStates[1])
    
def RefreshPositionPins():
    global positionPinStates

    # Activate the position pin if the player has entered an answer for that position
    for position in range(0,5):
        if (playerGuessConfiguration[position] != None):
            positionPinStates[position] = 1          
        else:
            positionPinStates[position]  = 0

    # Update the position pins' states
    SetLEDState(positionPins[0], positionPinStates[0])
    SetLEDState(positionPins[1], positionPinStates[1])
    SetLEDState(positionPins[2], positionPinStates[2])
    SetLEDState(positionPins[3], positionPinStates[3])
    SetLEDState(positionPins[4], positionPinStates[4])

def ButtonListeners():
    global selectButtonActive
    global buttonCharge
    
    # If the buttons have not been pressed for 0.5 seconds...
    
    if (True == False): #buttonCharge > 500):
        # If the left button is pressed...
        if (GPIO.input(buttonPins[0]) == False):
            MoveSynonymSelectionLeft(currentPosition)
            
        # If the right button is pressed...
        if (GPIO.input(buttonPins[2]) == False):
            MoveSynonymSelectionRight(currentPosition)
            
        # If the select button is pressed...
        if (GPIO.input(buttonPins[1]) == False):
            selectButtonActive = True
            OKButtonPress()
            selectButtonActive = False
            
        # Deactivate the button
        buttonCharge = 0
                   
def FlashForSelectedAppearance(position):
    if (confirmedWords != 5):
        SetLEDState(positionPins[position], False)
        master.after(100, SetLEDState, positionPins[position], True)
        
# ========================================
# Button Commands
# ========================================

def MoveSynonymSelectionLeft(position):
    global currentPosition
    
    # By default, the target position is one left of the current position
    targetPosition = DecrementSelection(position)
    
    # Skip active positons
    while (positionPinStates[targetPosition] == 1):
        targetPosition = DecrementSelection(targetPosition)
        
    # Reset the previous current position pin and update the current position
    SetLEDState(positionPins[position], False)
    currentPosition = targetPosition

                
def MoveSynonymSelectionRight(position):
    global currentPosition
    
    # By default, the target position is one left of the current position
    targetPosition = IncrementSelection(position)
    
    # Skip active positons
    while (positionPinStates[targetPosition] == 1):
        targetPosition = IncrementSelection(targetPosition)
        
    # Reset the previous current position pin and update the current position
    SetLEDState(positionPins[position], False)
    currentPosition = targetPosition
    
def OKButtonPress(event = None):
    # Reset the rolling delay in preparation for further commentation
    global rollingDelay
    rollingDelay = 0

    # If we are awaiting the player to confirm that their turn has begun (after a tutorial, round end or game end)...
    if (awaitState == "Turn Start"):
        SetAwaitStateAsync("Inactive")
        CommentateTurnStart()

    # If we are waiting for the player to confirm a ranking for a synonym...
    elif (awaitState == "Ranking"):
        SetAwaitStateAsync("Inactive")
        ConfirmSynonymRanking()

    # If we are waiting for the player to confirm that their turn has ended...
    elif (awaitState == "Turn End"):
        SetAwaitStateAsync("Inactive")
        CommentateTurnEnd()

    # If we are awaiting the player to confirm that the round has ended...
    elif (awaitState == "Round End"):
        SetAwaitStateAsync("Inactive")
        CommentateRoundEnd()

def DecrementSelection(position):
    if (position > 0):
        return position - 1
    else:
        return 4
    
def IncrementSelection(position):
    if (position < 4):
        return position + 1
    else:
        return 0

# ========================================
# Game Logic
# ========================================
    
def GenerateRoundData():
    global bannedRoundIDs
    roundID = randint(0,len(roundDatabase)-1)

    if (len(bannedRoundIDs) < len(roundDatabase)):
        while (roundID in bannedRoundIDs):
            roundID = randint(0,len(roundDatabase)-1)

    bannedRoundIDs.append(roundID)
    return roundDatabase[roundID]
    
def CommentateGameStart():
    # Commentate the tutorial
    PrintMessageAsync(">>> TUTORIAL <<<")
    PrintMessageAsync("Welcome to Ordernyms, where two students will battle it out to prove who has the best vocabulary.")
    PrintMessageAsync("There will be five rounds. On your turn, you will get a prompt, target word, and five synonyms for that word. You then must rank the synonyms, from 1st to 5th, by how well they describe the word.")
    PrintMessageAsync("After you've confirmed your synonym rankings, they will be compared to the true order. If your guess is spot-on, you'll get 5 points. If you were one position away, you'll get 4 points. Two away, you'll get 3: and so on.")
    PrintMessageAsync("Then, your opponent will get a different prompt and try to score more than you. Whoever gets the most points in a single round wins, and whoever wins the most rounds, takes the title as champion!")
    PrintMessageAsync("Good luck, and happy ranking! Press OK to continue.")
    
    master.after(rollingDelay, SetAwaitStateAsync, "Turn Start") 
    
def CommentateTurnStart():
    global roundData
    global roundConfiguration

    # Reset the positions display
    RefreshPositionsDisplay(False)

    # Generate the round's data and write them to local variables
    roundData = GenerateRoundData()
    sentence = roundData[0]
    targetWord = roundData[1]
    synomyms = roundData[2:7]

    RefreshSentenceDisplay(sentence, targetWord)

    PrintMessageAsync(">>> ROUND " +  positionAnalogues[roundNumber - 1][1].upper() + " / PLAYER " + str(currentPlayer) + "'S TURN <<<")
    PrintMessageAsync("It's Player " + str(currentPlayer) + "'s turn. Good luck Player " + str(currentPlayer) + "!")

    randomisedRank = randint(0,4)

    while(len(roundConfiguration) < 5):
        
        if (randomisedRank in roundConfiguration):
            randomisedRank = randint(0,4)
            
        else:
            roundConfiguration.append(randomisedRank)
            
    PrintMessageAsync(sentence + " In this sentence, the top 5 synonyms for " + targetWord + " are:")

    for synonym in roundConfiguration:
         PrintMessageAsync("- " + synomyms[synonym])

    CommentateSynonymRanking()
    master.after(rollingDelay, SetAwaitStateAsync, "Ranking") 

def CommentateSynonymRanking():
    global roundConfiguration
      
    targetWord = roundData[1]
    synomyms = roundData[2:7]
    
    PrintMessageAsync("From this list, how would you rank " + synomyms[roundConfiguration[confirmedWords]] + " as being a good synoynm for " + targetWord + "?")

def ConfirmSynonymRanking():
    global confirmedWords
    global playerGuessConfiguration
    global currentPosition
    
    # If this input originates from a physical button press...
    if (selectButtonActive == True):
        ConfirmPlayerGuess()
        
    else:
        ValidateCurrentPositionFromInput()


def ValidateCurrentPositionFromInput():
    global currentPosition
    
    rawInputPosition = messageInputEntry.get().lower()
    inputPosition = None
    messageInputEntry.delete(0, 'end')

    # Attach to the position the user has indicated
    if (rawInputPosition in firstAnalogues):
        inputPosition = 0

    elif (rawInputPosition in secondAnalogues):
        inputPosition = 1

    elif (rawInputPosition in thirdAnalogues):
        inputPosition = 2

    elif (rawInputPosition in fourthAnalogues):
        inputPosition = 3

    elif (rawInputPosition in fifthAnalogues):
        inputPosition = 4

    # If no position was attached to, and so, the user's input is invalid...
    if (inputPosition == None):
        master.after(rollingDelay, SetAwaitStateAsync, "Ranking")
        PrintMessageAsync("Please enter a valid rank (1st, 2nd, 3rd, 4th or 5th).")
        return

    # If the position is not None, hence, it is already filled...
    if (playerGuessConfiguration[inputPosition] != None):
        master.after(rollingDelay, SetAwaitStateAsync, "Ranking")
        PrintMessageAsync("You've already placed a word in that rank! Choose an nused (grey) rank.")
        return

    # If a position is validly hooked into, update the #DEL GPIO and write it to the player's guess configuration, advancing the round.
    currentPosition = inputPosition
    ConfirmPlayerGuess()


def ConfirmPlayerGuess():
    global confirmedWords
    global roundConfiguration
    global playerGuessConfiguration
    
    playerGuessConfiguration[currentPosition] = roundConfiguration[confirmedWords]
    confirmedWords += 1
    RefreshPositionsDisplay(False)    
    MoveSynonymSelectionRight(currentPosition)

    # If the player has not given a rank for all words, continue asking them for ranks. Otherwise, calculate their points and change over the turn.
    if (confirmedWords < 5):
        master.after(rollingDelay, SetAwaitStateAsync, "Ranking")
        CommentateSynonymRanking()
        
    else:
        PrintMessageAsync("Well, that wraps up your turn! Press OK to see how well you did.")
        master.after(rollingDelay, SetAwaitStateAsync, "Turn End")

def CommentateTurnEnd():
    global currentPlayer
    global playerTurnPinStates
    global player1Score
    global player2Score

    targetWord = roundData[1]
    synomyms = roundData[2:7]

    roundScore = 0

    # Display the results on the interface and in the message log
    RefreshPositionsDisplay(True)    
    for position in range (0,5):
        guessedWord = synomyms[playerGuessConfiguration[position]]
        guessScore = 5 - abs(playerGuessConfiguration[position] - position)
        roundScore += guessScore            
        PrintMessageAsync("You ranked " + guessedWord + " as the " + positionAnalogues[position][0] + " best synonym, but it is actually the " + positionAnalogues[roundConfiguration[roundConfiguration.index(playerGuessConfiguration[position])]][0] + " best! This earns you " + str(guessScore) + " points.")

    if (currentPlayer == 1):
        # Update and display Player 1's score
        player1Score = roundScore
        RefreshScoreboardDisplay()
        playerTurnPinStates = [0,1]        
        PrintMessageAsync("You scored " + str(roundScore) + "/25 points this round Player 1. Let's see if Player 2 can beat you! Press OK to continue.")

        # Advance the game by setting the current player to 2 and resetting the round data
        currentPlayer = 2
        ResetRoundData(False, False)

        master.after(rollingDelay, SetAwaitStateAsync, "Turn Start")

    elif (currentPlayer == 2):
        # Update and dispaly player 2's score
        player2Score = roundScore
        RefreshScoreboardDisplay()
        playerTurnPinStates = [1,0]
        PrintMessageAsync("You scored " + str(roundScore) + "/25 points this round Player 2. So, who did better? Press OK to find out.")

        master.after(rollingDelay, SetAwaitStateAsync, "Round End")
        

def CommentateRoundEnd():
    global currentPlayer
    global player1Score
    global player2Score
    global player1Wins
    global player2Wins
    global roundNumber

    PrintMessageAsync(">>> ROUND " +  positionAnalogues[roundNumber-1][1].upper() + " RESULTS <<<")
    
    # If player 1 has won this round, commentate and save this
    if (player1Score > player2Score):
        player1Wins += 1
        roundNumber += 1
        PrintMessageAsync("Well, Player 1 did!")

        # If player 1 has not won the game, commentate this and start a new turn
        if (player1Wins < 3):
            PrintMessageAsync("Congrats Player 1, you're only " + str(3 - player1Wins) + " wins away from synonym champion!")
            PrintMessageAsync("Don't worry though, Player 2. You're " + str(3 - player2Wins) + " wins away.")
            PrintMessageAsync("What a close game it is! Press OK to start the next round.")
            master.after(rollingDelay, SetAwaitStateAsync, "Turn Start")
            
        else:
            PrintMessageAsync("And with that...")
            PrintMessageAsync(">>> PLAYER 1 WINS! <<<")
            PrintMessageAsync("Congrats to the both players, you fought well!")
            PrintMessageAsync("I hope you learnt a thing or two about synonyms along the way.")
            master.after(rollingDelay, SetAwaitStateAsync, "Inactive")

    # If player 2 has won this round, commentate and save this
    elif (player1Score < player2Score):
        player2Wins += 1
        roundNumber += 1
        PrintMessageAsync("Well, Player 2 did!")
        
        # If player 2 has not won the game, commentate this and start a new turn
        if (player2Wins < 3):
            PrintMessageAsync("Congrats Player 2, you're only " + str(3 - player2Wins) + " wins away from synonym champion!")
            PrintMessageAsync("Don't worry though, Player 1. You're " + str(3 - player1Wins) + " wins away.")
            PrintMessageAsync("What a close game it is! Press OK to start the next round.")
            master.after(rollingDelay, SetAwaitStateAsync, "Turn Start")
            
        else:
            PrintMessageAsync("And with that...")
            PrintMessageAsync(">>> PLAYER 2 WINS! <<<")
            PrintMessageAsync("Congrats to the both players, you fought well!")
            PrintMessageAsync("I hope you learnt a thing or two about synonyms along the way.")
            master.after(rollingDelay, SetAwaitStateAsync, "Inactive")
            
    elif (player1Score == player2Score):
        PrintMessageAsync("Well, it was a tie! Looks like we're going to have to redo this round!")
        master.after(rollingDelay, SetAwaitStateAsync, "Turn Start")

    RefreshScoreboardDisplay()
    ResetRoundData(True, False)
    
    # Advance the game by setting the current player to 1 and resetting the round data
    currentPlayer = 1    

def ResetRoundData(roundEnd, gameEnd):
    global roundData
    global roundConfiguration
    global playerGuessConfiguration
    global confirmedWords
    global currentPosition
    global player1Score
    global player1Wins
    global player2Score
    global player2Wins
     
    # Reset round variables
    roundData = []
    roundConfiguration = []
    playerGuessConfiguration = [None,None,None,None,None]
    confirmedWords = 0
    currentPosition = 0
    
    # If the round is over, reset the scores
    if(roundEnd):
        player1Score = 0
        player2Score = 0

    # If the game is over, reset the wins
    if (gameEnd):
        player1Wins = 0
        player2Wins = 0

messageInputButton.config(command=OKButtonPress)
messageInputEntry.bind('<Return>', OKButtonPress)

# Global game management variables
awaitState = "Inactive"
selectButtonActive = False

roundData = []
roundConfiguration = []
playerGuessConfiguration = [None,None,None,None,None]
confirmedWords = 0

currentPlayer = 1
roundNumber = 1

bannedRoundIDs = []

# Player score variables
player1Score = 0
player2Score = 0

# Player wins variables
player1Wins = 0
player2Wins = 0

# Global message management variables
rollingDelay = 0
messageSpeed = 100

# Global button variables
buttonPins = [16,20,21]
buttonCharge = 0

# Global scoreboard variables
scoreboardPins = [26,19,13,6,5]
scoreboardPinStates = [0,0,0,0,0]

# Global turn LED variables
playerTurnPins = [9,10]
playerTurnPinStates = [1,0]

# Global position LED variables
positionPins = [27,17,4,3,2]
positionPinStates = [0,0,0,0,0]
currentPosition = 0

# Global position analogue lookup tables
firstAnalogues = ["1st", "1", "one", "first", "top"]
secondAnalogues = ["2nd", "2", "two", "second", "high"]
thirdAnalogues = ["3rd", "3", "three", "third", "mid"]
fourthAnalogues = ["4th", "4", "four", "fourth", "low"]
fifthAnalogues = ["5th", "5", "five", "fifth", "bot"]

positionAnalogues = [firstAnalogues, secondAnalogues, thirdAnalogues, fourthAnalogues, fifthAnalogues]

roundDatabase = [["Mary had a little lamb, her fleece was white as snow.", "Little", "Small", "Minitature", "Tiny", "Miniscule", "Microscopic"],
                 ["I used my pencil to complete my mathematics test.", "Used", "Utilised", "Employed", "Wielded", "Applied", "Exerted"],
                 ["If I had woken up just 10 minutes earlier, I could have made it to school on time.", "Earlier", "Sooner", "Beforehand", "Prior", "Previous", "Faster"],
                 ["Luke, I am your father.", "Father", "Dad", "Daddy", "Ancestor", "Patriarch", "Pastor"],
                 ["Incy wincy spider, climbed up the water spout.", "Climbed", "Clambered", "Scrambled", "Rose", "Soared", "Rocketed"],
                 ["Row, row, row your boat, gently down the stream.", "Gently", "Softly", "Tenderly", "Gradually", "Quietly", "Kindly"],
                 ["Row, row, row your boat, gently down the stream.", "Stream", "River", "Brook", "Creek", "Torrent", "Flow"],
                 ["Humpty Dumpty sat on the wall. Humpty Dumpty had a great fall!", "Fall", "Tumble", "Plummet", "Drop", "Plunge", "Crash"],
                 ["Life is like a box of chocolates, you never know what you're gonna get.", "Get", "Receive", "Have", "Find", "Gain", "Ascertain"],
                 ["Every manager should be able to recite at least ten nursury rhymes, backwards.", "Recite", "Perform", "Deliver", "Rehearse", "List", "Count"],
                 ["The sign said there were road works ahead, so he decided to speed up.", "Sign", "Placard", "Notice", "Board", "Billboard", "Poster"],
                 ["You'll see the rainbow bridge after it rains cats and dogs.", "Downpours", "Showers", "Notice", "Deluges", "Rainfalls", "Showers"],
                 ["The journey awaits.", "Journey", "Trip", "Trek", "Voyage", "Excursion", "Tour"],
                 ["I put a spoonfull of cake in my mouth, already knowing it was going to taste bad.", "Bad", "Terrible", "Awful", "Dreadful", "Poor", "Rotten"],
                 ["I ran to the store while it was raining.", "Ran", "Sprinted", "Rushed", "Darted", "Moved", "Went"],
                 ["Be sure to use online resources which are appropriate to the topic, to develop an answer.", "Appropriate", "Suitable", "Revelant", "Applicable", "Related", "Apt"],
                 ["The family went on long vacation.", "Long", "Extended", "Extensive", "Enlongated", "Lengthy", "Stretched"],
                 ["The battle ended between the two brothers.", "Ended", "Finished", "Was Over", "Concluded", "Was Done", "Completed"],
                 ["Bill and Ted went on quite the fun rollercoaster ride.", "Fun", "Entertaining", "Enjoyable", "Exciting", "Great", "Cool"],
                 ["After being knocked off the table, the box dropped to the floor.", "Dropped", "Fell", "Tumbled", "Plunged", "Plumetted", "Slumped"],
                 ["The patient died during the complicated surgery.", "Died", "Perished", "Expired", "Deceased", "Passed", "Stopped"],
                 ["With such a great day ahread of her, Jill knew that nothing can stop her.", "Great", "Wonderful", "Fantastic", "Terrific", "Promising", "Good"],
                 ["The race was a stunning event, as the cars drifted across the track.", "Stunning", "Astonishing", "Shocking", "Startling", "Entralling", "Captivating"],
                 ["The race was a stunning event, as the cars drifted across the track.", "Across", "Along", "Around", "Through", "Within", "Throughout"],
                 ["The race was a stunning event, as the cars drifted across the track.", "Across", "Along", "Around", "Through", "Within", "Throughout"],]

# Setup the LEDs and buttons to their #DEL GPIO pins
SetupPinModes()

# Update the interface's display
RefreshPositionsDisplay(False)
RefreshScoreboardDisplay()
    
# Show the current position the player is in
FlashForSelectedAppearance(currentPosition)

# Begin the game
CommentateGameStart()

def ContinutallyUpdatedMainloop():
    global buttonCharge
    
    # Record that 200 ms has passed, and listen out for a button press
    buttonCharge += 200      
    ButtonListeners()
    
    # Update the hardware display
    RefreshPositionPins()
    RefreshPlayerTurnPins()
    RefreshScoreboardPins()
    RefreshProfilePictures()
    
    # Keep the selected position pin flashing
    FlashForSelectedAppearance(currentPosition)

    # Repeat this function every 200ms
    master.after(200, ContinutallyUpdatedMainloop)

# Listen out for button presses and keep the interface refreshed
ContinutallyUpdatedMainloop()

# Run the interface
master.mainloop() 
