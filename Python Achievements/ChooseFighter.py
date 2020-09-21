print("Choose your Fighter!")
print("But first! Select your title!")
print("A. Street Fighter  B. Dragon Ball FighterZ  C. Guilty Gear")
inputA = "Street Fighter"
inputB = "Dragon Ball FighterZ"
inputC = "Guilty Gear"
inputPlayer1 = input("SELECT YOUR TITLE: ")
if(inputPlayer1 == inputA):
    print("So you picked the poster boy? Yeah that makes sense!")
    print("Now, choose your game!")
    print("A. Super Street Fighter II Turbo  B. Street Fighter Alpha III  C. Street Fighter III: 3rd Strike")
    SFGameInputA = "Super Street Fighter II Turbo"
    SFGameInputB = "Street Fighter Alpha III"
    SFGameInputC = "Street Fighter III: 3rd Strike"
    inputSFGame = input("CHOOSE YOUR GAME: ")
    if(inputSFGame == SFGameInputA):
        print("Back to the classics I see, I like your style!")
        print("Select your fighting style!")
        print("A. Rushdown  B. Zoner  C. Grappler")
        inputSTPlaystyleA = "Rushdown"
        inputSTPlaystyleB = "Zoner"
        inputSTPlaystyleC = "Grappler"
        STPlaystyle = input("SELECT YOUR GROOVE: ")
        if(STPlaystyle == inputSTPlaystyleA):
            print("These are the characters where you can maul your competition! Now choose your fighter!")
            print("A. Fei Long  B. Cammy  C. Dee Jay  D. M.Bison  E. Balrog  F. Vega  G. Akuma")
            inputSTRushA = "Fei Long"
            inputSTRushB = "Cammy"
            inputSTRushC = "Dee Jay"
            inputSTRushD = "M.Bison"
            inputSTRushE = "Balrog"
            inputSTRushF = "Vega"
            inputSTRushG = "Akuma"
            STRushdown = input("CHOOSE YOUR FIGHTER: ")    
            print("Congratulations! You have found your character! Now GO FOR BROKE!")
        if(STPlaystyle == inputSTPlaystyleB):
            print("The following characters can cripple even the most competent fighters from afar!")
            print("A. Ryu  B. Sagat  C. Dhalsim  D. Ken")
            inputSTZoneA = "Ryu"
            inputSTZoneB = "Sagat"
            inputSTZoneC = "Dhalsim"
            inputSTZoneD = "Ken"
            STZoner = input("CHOOSE YOUR FIGHTER: ")
            print("Congratulations! You have found your character! Now GO FOR BROKE!")
        if(STPlaystyle == inputSTPlaystyleC):
            print("These brutes will crush anyone in their way!")
            print("A. T.Hawk  B. Zangief  C. E.Honda")
            inputSTGrabA = "T.Hawk"
            inputSTGrabB = "Zangief"
            inputSTGrabC = "E.Honda"
            STGrappler = input("CHOOSE YOUR FIGHTER: ")
            print("Congratulations! You have found your character! Now GO FOR BROKE!")
    if(inputSFGame == SFGameInputB):
        print("This is Street Fighter Alpha 3!")
        print("Select your fighting style!")
        print("A. Rushdown  B. Zoner  C. Grappler")
        inputA3PlaystyleA = "Rushdown"
        inputA3PlaystyleB = "Zoner"
        inputA3PlaystyleC = "Grappler"
        A3Playstyle = input("SELECT YOUR GROOVE: ")
        if(A3Playstyle == inputA3PlaystyleA):
            print("These are the characters where you can maul your competition! Now choose your fighter!")
            print("A. Sakura  B. Ken  C. Akuma  D. Cammy  E. Gen  F. Guy  G. Cody  H. Karin  I. Vega  J. Balrog  K. Evil Ryu L. Adon")
            inputA3RushA = "Sakura"
            inputA3RushB = "Ken"
            inputA3RushC = "Akuma"
            inputA3RushD = "Cammy"
            inputA3RushE = "Gen"
            inputA3RushF = "Guy"
            inputA3RushG = "Cody"
            inputA3RushH = "Karin"
            inputA3RushI = "Vega"
            inputA3RushJ = "Balrog"
            inputA3RushK = "Evil Ryu"
            inputA3RushL = "Adon"
            A3Rushdown = input("CHOOSE YOUR FIGHTER: ")
            print("Congratulations! You have found your character! Now GO FOR BROKE!")
        if(A3Playstyle == inputA3PlaystyleB):
            print("The following characters can cripple even the most competent fighters from afar!")
            print("A. Ryu  B. Sagat  C. Charlie  D. Guile  E. Rose  F. Dhalsim")
            inputA3ZoneA = "Ryu"
            inputA3ZoneB = "Sagat"
            inputA3ZoneC = "Charlie"
            inputA3ZoneD = "Guile"
            inputA3ZoneE = "Rose"
            inputA3ZoneF = "Dhalsim"
            A3Zoner = input("CHOOSE YOUR FIGHTER: ")
            print("Congratulations! You have found your character! Now GO FOR BROKE!")
        if(A3Playstyle == inputA3PlaystyleC):
            print("These brutes will crush anyone in their way!")
            print("A. E.Honda  B. Zangief  C. R.Mika  D. Birdie  E. T.Hawk")
            inputA3GrabA = "E.Honda"
            inputA3GrabB = "Zangief"
            inputA3GrabC = "R.Mika"
            inputA3GrabD = "Birdie" 
            inputA3GrabE = "T.Hawk"
            A3Grappler = input("CHOOSE YOUR FIGHTER: ")
            print("Congratulations! You have found your character! Now GO FOR BROKE!")
    if(inputSFGame == SFGameInputC):
        print("Welcome to the world of Street Fighter III, prepare for battle!")
        print("Let's get it on now! Select and make your first pick!")
        print("A. Rushdown  B. Zoner  C. Grappler")
        input3SPlaystyleA = "Rushdown"
        input3SPlaystyleB = "Zoner"
        input3SPlaystyleC = "Grappler"
        TrdStrikePlaystyle = input("SELECT YOUR GROOVE: ")
        if(TrdStrikePlaystyle == input3SPlaystyleA):
            print("All right, that's cool! Choose and pick the best one!")
            print("A. Dudley  B. Ken  C. Akuma  D. Yang  E. Yun  F. Urien  G. Q  H. Sean  I. Ibuki  J. Makoto")
            input3SRushA = "Dudley"
            input3SRushB = "Ken"
            input3SRushC = "Akuma"
            input3SRushD = "Yang"
            input3SRushE = "Yun"
            input3SRushF = "Urien"
            input3SRushG = "Q"
            input3SRushH = "Sean"
            input3SRushI = "Ibuki"
            input3SRushJ = "Makoto"
            TrdStrikeRushdown = input("CHOOSE YOUR FIGHTER: ")
            if(TrdStrikeRushdown == input3SRushC):
                print("MESSATSU!")
            else: 
                print("Yeah, that makes sense! Prepare to strike!")


            
                  
