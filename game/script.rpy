# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("---", what_slow_cps=40, who_color="#dda0dd00", what_color= "#aaeaff", what_xalign=0.5, what_text_align=0.5, what_yalign=0.5, what_outlines=[(3, "#5C1F56")])
define p = Character("Lia", what_slow_cps=40, who_color="#dda0dd00", what_color= "#ffaed3", what_xalign=0.5, what_text_align=0.5, what_yalign=0.5, what_outlines=[(3, "#5C1F56")])
define pa = Character("Lia", what_slow_cps=80, who_color="#dda0dd00", what_color= "#ffaed3", what_xalign=0.5, what_text_align=0.5, what_yalign=0.5, what_outlines=[(3, "#5C1F56")])
define s = Character("Sinner", what_slow_cps=40, who_color="#dda0dd", what_color= "#ffaed3", what_xalign=0.5, what_text_align=0.5, what_yalign=0.5, what_outlines=[(3, "#5C1F56")], who_outlines=[(3, "#5C1F56")])
define l = Character(" ", what_slow_cps=40, what_font="GermaniaOne-Regular.ttf", what_outlines=[(3, "#5C1F56")], what_xalign=0.5, what_text_align=0.5, what_yalign=0.5)
define nlv = Character("", kind=nvl, what_slow_cps=40, color="#c8c8ff", what_outlines=[(3, "#ff0059ae")], what_font="GermaniaOne-Regular.ttf", what_xalign=0.5, what_text_align=0.5, what_yalign=0.5)

default persistent.temple = 0
default persistent.ty = 0
default persistent.again = False

#open
label splashscreen:
    scene black
    with Pause(1)

    show logo2 with dissolve
    with Pause(2)

    return

# The game starts here.

label start:

    #$ persistent.temple = 0
    #$ persistent.ty = 0
    #$ persistent.again = False
    $ numerito = 9
    #simboliwis
    $ lista = ["▗▔▕▖▝▝▘▞", "▗▔▕▖▝▝▘▞▖▝▝", "▝▝▝▝▔▕▖", "▖▝▝▘"]
    #Arrays of dialoge displayed in order <----
    #looking arround at the walls
    $ walls = ["Wall", "More wall", "...", "Wall, wall", "Well"]
    #looking up to the sky (wall up)
    $ lups = ["I have a bad feeling", "My neck hurts", "{i}Haha{/i}...", "I don’t like this", "It looks taller", "I want to go home", "I can't climb that", "Why it's so slippery?", "It never ends", "So tall"]
    #looking at the sky
    $ ups = ["...","I'm looking up or down?", "It's staring at me", "CAN i climb?", "It {i}scares{/i} me but, staying also scares me", "So{size=-3}me{/size}{i}one{/i} {size=-5}he{/size}{size=-7}lp{/size}", "I's as it wants to {b}consume{/b} {i}me{/i}","So weird...{p} it almost makes me happy to be here", "Where I'm?", "The sky seems weird"]
    #In the middle of loking at wall and sky
    $ looking = ["The possibility of someone just showing in time was abysmal and nobody was looking for her", "In the middle of the forest, in de bottom of a well, Who would just casually appear to help?", "Without tools there was no way to climb up", "On the top of that is was all slippery", "The wall around her was so tall and the crevasses of the wall so subtle and soft…", "She knew"]



    $ n = renpy.random.randint(0, 3)
    $ d = 0
    $ wall = walls[n]
    $ lis = lista[n]
    $ name = ""
    ########## if - jump

    play music ["audio/cave.ogg","audio/cave.ogg"]  volume 0.75 fadeout 1.0 fadein 1.0

    if persistent.again == True:
        jump whoim

    if persistent.temple == 6:
        scene lia v
        p "..."
        if persistent.ty < 3:
            $ persistent.ty = persistent.ty + 1
        if persistent.ty > 2:
            menu:
                "Bring her back":
                    l "Poor soul"
                    l "But, as you wish"
                    l "I will replay this role as long as you want"
                    $ persistent.temple = 0
                    $ persistent.again = True
                    jump start
                " ":
                    pass
        jump end

    scene fall_0005
    nlv "Once upon a time there was a {font=seguisym.ttf}▒▒▒{/font}, a regular {font=seguisym.ttf}▒▒▒▒▒▒{/font}."
    nvl clear
    nlv "Not too ugly or pretty"
    nvl clear
    nlv "Not too smart or clumsy"
    nvl clear
    nlv "If we had to highlight something about them"
    nvl clear
    nlv "{cps=1}...{/cps}"
    nvl clear
    nlv "It’d be their luck."
    nvl clear
    nlv "Being in a bad place at a bad time with the wrong people"
    nvl clear
    l "they fell into..."
    scene pink with Dissolve(1, alpha=True)


    play sound "audio/caida.ogg" volume 0.5
    pause 0.5

    scene well at Zoom((1920, 1080), (150, 50, 1920, 1080), (0, 0, 2304, 1296), 90.0) with Dissolve(1, alpha=True)

    scene lia sleep with Dissolve(1, alpha=True)

    pause 1
    l " "
    $ renpy.notify("The bottom of the well")
    show lia sleep
    e ""
    show lia wake

    label waking:

        pause 0.5
        p "What?"

        scene well at Zoom((1920, 1080), (150, 50, 1920, 1080), (0, 0, 2304, 1296), 90.0)
        hide lia

        p "I…{p} {cps=60}I almost {b}died{/b}…{/cps}"
        p "{cps=5}At least{/cps} it feels like it"
        p "…"
        p "I just fell{cps=2}...{/cps} {i}right?{/i}{p} but…"
        p "My body"
        p "It…{p} it doesn’t hurt"
        p "So weird..."
        p "{cps=1}...{/cps}"
        p "It's so tall, too tall"
        p "How i'm gonna get out?"
        p "Can I climb that?"
        p ""
        p "I need to get up"

        scene fall_0005 with Dissolve(0.5, alpha=True)
        
        nlv "In the dark of the night, that {font=seguisym.ttf}▒▒▒▒{/font} found herself in the bottom of a dry well"
        nvl clear
        nlv "And remembered that, just moments ago she was with her coworkers looking for {font=seguisym.ttf}[lis]{/font} in the forest"
        nvl clear

        p "{p=0.1}{nw}"
        scene wall with eyeopen
        pause 0.5
        show l v with Dissolve(0.5, alpha=True)
        p "I wonder if they are still around here… "
        show l n with Dissolve(0.5, alpha=True)
        p "If I ask for help maybe"
        show l al
        p "..."
        show l nl
        p "Haha...{p} yeah"
        show l n
        p "They probably are happy that I fell…"
        p "I... fell?"
        show l v with Dissolve(0.1, alpha=True)
        hide l with Dissolve(0.1, alpha=True)
        play sound "audio/wuo.ogg" volume 0.3
        nlv "Did they push her? she didn’t remember the moment of the fall" 
        nvl clear
        nlv "She dind't remember {font=seguisym.ttf}▒▒▒▒▒▒{/font} or {font=seguisym.ttf}▒▒▒▒▒▒▒▒▒{/font}"
        nvl clear
        nlv "Just the fact that she was falling down"
        nvl clear
        nlv "And waking up in the well"
        nvl clear
        p "..."
        p "They wouldn’t help even if they knew… "
        scene wall up
        nlv "With that thought came the realization; she was trapped in that well. "
        nvl clear
        play music ["audio/cave2.ogg","audio/cave2.ogg"]  volume 0.75 fadeout 1.0 fadein 1.0
        nlv "{cps=10}Slowly…{/cps} an ever growing feeling of doom started to sink in the bottom of her stomach."
        nvl clear
        
        p "Ugh..."
        if d > 14:
            jump start
        else:
            jump inWell


    #######################################
    #######################################

    label inWell:

        if numerito < 0:

            scene caved_0000 with Dissolve(0.1, alpha=True)
            if d < 3:
                show gli x
            if d >= 3 and d > 6:
                show gli a
            if d >= 6 and d > 9:
                show gli b
            if d >= 9 and d > 12:
                show gli c
            if d >= 12 and d > 15:
                show gli d           
            if d >= 15 and d > 18:
                show gli e
            if d >= 18 and d > 21:
                show gli f
            if d >= 21:
                #End 1, waited too
                play sound "audio/wuo.ogg" volume 0.5
                nlv "She waited"
                nvl clear   
                nlv "Waited and waited"
                nvl clear
                nlv "Waited, waited, waited" with hpunch
                nvl clear
                nlv "{cps=100}WAITED WAITED WAITED WAITED WAITED WAITED{/cps}" with vpunch
                nvl clear
                nlv "{cps=150}{size=+5}WAITED WAITED WAITED{/size}{/cps}{nw}" with hpunch
                nvl clear
                nlv "{cps=160}{size=+10}WAITED WAITED WAITED{/size}{/cps}{nw}" with vpunch
                nvl clear
                nlv "{cps=170}{size=+15}WAITED WAITED WAITED{/size}{/cps}{nw}" with hpunch
                nvl clear
                show lia v
                nlv "But nobody came"
                nvl clear
                pause
                jump end

            if d == 19:
                play music ["audio/help.ogg","audio/help.ogg"]  volume 0.75 fadeout 5.0 fadein 5.0

            menu:
                "I'm going in...":
                    jump tunel
                "Look up":
                    scene well at Zoom((1920, 1080), (150, 50, 1920, 1080), (0, 0, 2304, 1296), 90.0) with Dissolve(0.2, alpha=True)
                    if d < 3:
                        show gli x
                    if d >= 3 and d > 6:
                        show gli a
                    if d >= 6 and d > 9:
                        show gli b
                    if d >= 9 and d > 12:
                        show gli c
                    if d >= 12 and d > 15:
                        show gli d           
                    if d >= 15 and d > 18:
                        show gli e
                    if d >= 18 and d > 21:
                        show gli f
                    
                    show dot
                    p ""
                    $ d = d + 1
                    jump inWell
                "Look around":
                    $ d = d + 1
                    $ miniloop = 3
                    label miniloop:
                        
                        scene wall with pushright
                        if d < 3:
                            show gli x
                        if d >= 3 and d > 6:
                            show gli a
                        if d >= 6 and d > 9:
                            show gli b
                        if d >= 9 and d > 12:
                            show gli c
                        if d >= 12 and d > 15:
                            show gli d           
                        if d >= 15 and d > 18:
                            show gli e
                        if d >= 18 and d > 21:
                            show gli e
                        if miniloop > 0:
                            $ miniloop = miniloop -1
                            jump miniloop
                        jump out

                    label out:
                        scene caved_0000 with pushright
                        if d < 3:
                            show gli x
                        if d >= 3 and d > 6:
                            show gli a
                        if d >= 6 and d > 9:
                            show gli b
                        if d >= 9 and d > 12:
                            show gli c
                        if d >= 12 and d > 15:
                            show gli d           
                        if d >= 15 and d > 18:
                            show gli e
                        if d >= 18 and d > 21:
                            show gli f

                        jump inWell

                "Just wait":
                    $ d = d + 1
                    p "..."
                    jump inWell

        else:
            
            scene wall with Dissolve(0.1, alpha=True)

            if numerito >= 0 and numerito < 6:
                $ txt = looking[numerito]
                nlv "[txt]"
                nvl clear

            if numerito == 0:
                menu:
                    "Look up":
                        scene wall down
                        $ txt = lups[numerito]
                        p "[txt]"
                        scene well at Zoom((1920, 1080), (150, 50, 1920, 1080), (0, 0, 2304, 1296), 90.0) with Dissolve(0.2, alpha=True)
                        $ txt = ups[numerito]
                        p "[txt]"
                        $ numerito = numerito - 1

                        #######################################################################
                        #to part 2
                        #######################################################################
                        if numerito <= 0:

                            p "How did i end up in a place like this?"

                            p "She told me to go with her… to tell me something and..."

                            show fall
                            play music ["audio/cave4.ogg","audio/cave4.ogg"]  volume 0.75 fadeout 5.0 fadein 5.0
                            pause 0.9
                            $ numerito = numerito - 1
                            play sound "audio/caida.ogg" volume 0.8
                            pause 0.5
                            p "..."
                            p "..."
                            p "...?"
                            p "Eh?"
                            scene caved_0000 with eyeopen
                            p "A tunnel?"
                            p "Why? How?"
                            show l v with Dissolve(0.5, alpha=True)
                            show l n with Dissolve(0.5, alpha=True)
                            p ""
                            p "I don’t know if it's safe but…"
                            show l nl with Dissolve(0.5, alpha=True)
                            p "I guess that it's good? It has to go somewhere"
                            p "And maybe it's the only way out"
                            p "..."
                            hide l with Dissolve(0.5, alpha=True)
                            menu:
                                "I want to go":
                                    p "Nobody is going to help"
                                    menu:
                                        "I’d rather do something":
                                            menu:
                                                "I can do it!!":
                                                    p "Yeah, yeah, I can, I will find a way out "
                                                    jump tunel
                                                "I’m afraid":
                                                    nlv "No need to fear"
                                                    nvl clear
                                                    $ d = d + 1
                                                    jump inWell
                                        "But maybe...":
                                            nlv "No need to wait anymore"
                                            nvl clear
                                            $ d = d + 1
                                            jump inWell

                                "But maybe help will come…":
                                    nlv "Help will {b}not{/b} come {p} you know? {p} there is a difference between being hopeful and being passive, to just wait here is dangerous..."
                                    nvl clear
                                    $ d = d + 1
                                    jump inWell

                        jump inWell

            #Why do i have this again?????????
            menu:
                "Look up":
                    scene wall down
                    $ txt = lups[numerito]
                    p "[txt]"
                    scene well at Zoom((1920, 1080), (150, 50, 1920, 1080), (0, 0, 2304, 1296), 90.0) with Dissolve(0.2, alpha=True)
                    $ txt = ups[numerito]
                    p "[txt]"
                    $ numerito = numerito - 1

                    #######################################################################
                    #to part 2
                    #######################################################################
                    if numerito <= 0:

                        p "How did i end up in a place like this?"

                        p "She told me to go with her… to tell me something and..."

                        show fall
                        play music ["audio/cave4.ogg","audio/cave4.ogg"]  volume 0.75 fadeout 5.0 fadein 5.0
                        pause 0.9
                        $ numerito = numerito - 1
                        play sound "audio/caida.ogg" volume 0.8
                        pause 0.5
                        p "..."
                        p "..."
                        p "...?"
                        p "Eh?"
                        scene caved_0000 with eyeopen
                        p "A tunnel?"
                        p "Why? How?"
                        show l v with Dissolve(0.5, alpha=True)
                        show l n with Dissolve(0.5, alpha=True)
                        p ""
                        p "I don’t know if it's is safe but…"
                        show l nl with Dissolve(0.5, alpha=True)
                        p "I guess that is good? It has to go somewhere"
                        p "And maybe it's the only way out"
                        p "..."
                        hide l with Dissolve(0.5, alpha=True)
                        menu:
                            "I want to try":
                                p "Nobody is going to help"
                                menu:
                                    "I’d rather do something":
                                        menu:
                                            "I can do it!!":
                                                p "Yeah, yeah, I can, I will find a way out "
                                                jump tunel
                                            "I’m afraid":
                                                nlv "No need to fear"
                                                nvl clear
                                                $ d = d + 1
                                                jump inWell
                                    "But maybe...":
                                        nlv "No need to wait anymore"
                                        nvl clear
                                        $ d = d + 1
                                        jump inWell

                            "But maybe help will come…":
                                nlv "Help will {b}not{/b} come {p} you know? {p} there is a difference between being hopeful and being passive, to just wait here is dangerous..."
                                nvl clear
                                $ d = d + 1
                                jump inWell

                    jump inWell

                "Look around":
                    scene wall with pushright
                    if numerito > 0:
                        $ numerito = numerito - 1
                        $ n = renpy.random.randint(0, 4)
                        $ wall = walls[n]
                        p "[wall]"

                    jump inWell


    ##########################################################################
    ##########################################################################
    ##########################################################################
    
    label tunel:
        scene cavedark
        play music ["audio/cave6.ogg","audio/cave6.ogg"]  volume 0.75 fadeout 1.0 fadein 1.0

        p "It’s going to be ok"
        p "I will find a way out"
        p "Ah…"
        p "Why did I listen to her?"
        p "Why did I go to work today?"
        p "It was supposed to be a day off"
        show l v with Dissolve(0.5, alpha=True)
        show l a with Dissolve(0.5, alpha=True)
        p "Stupid boss..." 
        p "“Oh, my son doesn’t want to come tomorrow”,{p} “the patrols are too risky for him”,{p} “you have more experience”" 
        show l n
        p "“why don’t you have fun with an extra night of work?” “You surely don't have something better to do”"
        ###############################
        #img
        ###############################
        show l al with Dissolve(0.5, alpha=True)
        p "As if he is doing me a favour"
        p "…"
        p "Great…{p} now I’m angry and scared"
        p "…"
        show l a with Dissolve(0.5, alpha=True)
        p "But… it’s… ugh... I hate it so much, why does he insist in grouping me with {b}her{/b}, he knows that {b}she{/b} hates me I’m sure that…"
        p "…"
        show l al with Dissolve(0.5, alpha=True)
        p "{b}She{/b}… wants to kill me… or something…"
        p "Wait…"
        show l n with Dissolve(0.5, alpha=True)
        p "Did she?"
        
        if d < 7:
            scene cavelight with Dissolve(2, alpha=True)
            p "...!?"
            scene pink with Dissolve(1, alpha=True)
            nlv "Their life was not the best"
            nvl clear
            nlv "And the grass always seems more green in the other side"
            nvl clear
            nlv "Or so they say"
            nvl clear
            nlv "And sometimes it's true, it's greener"
            nvl clear
            nlv "However"
            nvl clear
            nlv "I wonder how true it was for them"
            nvl clear
            nlv "When they came close"
            nvl clear
            nlv "I heard their wish"
            nvl clear
            scene purple with Dissolve(1, alpha=True)
            nlv "{size=40}I wanna be her{/size}"
            nvl clear
            show lilith a with chaosdissolve
            nlv "{size=45}Life would be so easy in their shoes{/size}" with vpunch
            nvl clear
            nlv "{size=50}I want that, I deserve that, they don't{/size}" with hpunch
            nvl clear
            l "And, you know? I’m quite a charitable soul"
            l "I can’t let prayers like that to stay unheard"
            l "So i said:"
            l "{size=45}I can grant your whish{/size}"
            l "{size=45}But if you transform in that person, what will be of the original one? {p}what will be of you{/size}"
            l "{size=45}If you want their life{/size}"
            l "{size=45}Don't you think that you are missing a step?{/size}"
            l "{size=45}One has to disappear{p} don't you think?{/size}"            

        show l v with Dissolve(0.5, alpha=True)
        e ""
        show m 00
        e ""
        show m 0000
        e ""
        show m 0001
        e ""
        show m 0002
        e ""
        show m 0003
        e ""
        show m 0004
        e ""
        show m 0005
        e ""
        play music ["audio/help.ogg","audio/help.ogg"]  volume 0.75 fadeout 1.0 fadein 1.0
        show m a
        e ""
        $ numerito = 10

        label loop:
        $ numerito = numerito - 1
        $ n = renpy.random.randint(0, 3)
        $ lis = lista[n]
        e "[lis]"
        if numerito == 0:
            scene pink with Dissolve(1, alpha=True)
            if d < 4:
                jump temple
            else:
                jump shefoudherself
        else:
            jump loop

    ##########################################################################
    ##########################################################################
    ##########################################################################

    label temple:

        play music ["audio/safe.ogg","audio/safe.ogg"]  volume 0.75 fadeout 0.3 fadein 0.3
        scene temple with Dissolve(0.5, alpha=True)
        show lilith a
        pause 2
        show fire with Dissolve(1, alpha=True)
        
        nlv "Finding a room she felt hope"
        nvl clear
        nlv "{size=45}'There has to be a way out'{/size}"
        nvl clear
        nlv "She thought that but
        {p}There was no exit in sight" 
        nvl clear
        nlv "So I spoke to her"
        nvl clear
        l "Hello my dear"        
        if persistent.temple > 0:
            l "Welcome back"
            show lilith h
            l "Do you want another chance to get out?"
            show lilith a
            l "It's ok, I'm quite merciful"
            if persistent.ty > 2:
                show lilith n
                nlv "And I {i}totally{/i} don’t mind you going out then coming in again, not at all"
                nvl clear
                show lilith d
                pause
                show lilith a
                l "Oh well..."      
        
        if persistent.temple == 0:
            $ persistent.temple = 1

        l "You surely remember that we made a deal"
        p "I..."
        if persistent.temple > 1:
            l "And~ that i made you a new offer"
            l "So, you want to take my deal?"
            show l n with Dissolve(0.5, alpha=True)
        else:
            l "{size=40}You{/size} want to get out {i}right{/i}?"
            show l n with Dissolve(0.5, alpha=True)
            p "..."
            nlv "I let you out {p} you give me your {font=seguisym.ttf}▊▋█▌▍▊▋█▌▍{/font}"
            play sound "audio/wuo.ogg" volume 0.5
            l "Deal?"
            nvl clear
            $ persistent.temple = 2
        
        label thedeal:
            menu:
                "I... want to get out":
                    jump thanks
                "What?":
                    if persistent.temple > 2:
                        l "you already know what i want"
                        p "Do i?"
                        show l a with Dissolve(0.5, alpha=True)
                        p "I'm sorry but i don't trust random mysterious voices"
                        p "Who even are you?"
                        l "{size=40}Who are you?{/size}"
                        p "{cps=60}WHY ARE YOU?!{/cps}"
                        l "Do you know?"
                        menu:
                            l "Who are you?"
                            "I'm...":
                                jump who
                            "That doesn’t matter!":
                                show gli a
                                l "..."
                                show gli c
                                l "Do you think so?"
                                hide gli
                                l "Well, you asked about me"
                                l "You can think of me as a demon"
                                l "A demon who doesn't want to give a name"
                                show l n with Dissolve(0.5, alpha=True)
                                l "But who are you? what are you?"
                                l "I know but do you?"
                                l "Oh! {p}We can play a game"
                                l "You know, we demons LOVE that"
                                show l al with Dissolve(0.5, alpha=True)
                                l "I can let you get out if you win"
                                show l a with Dissolve(0.5, alpha=True)
                                pa "I don't believe you"
                                l "You don't know how bad you have it"
                                l "I will consume your soul if you stay too long"
                                pa "Is that a threat?"
                                l "It's a fact"
                                l "Damn if you do damn if you don't"
                                l "Better to give it a try"
                                menu:
                                    "Ok...":
                                        jump game
                                    "No":
                                        l "Then you can go back to your hole"
                                        $ d = 9
                                        jump shefoudherself
                    else:
                        p "Sorry i don't understand  what you want"
                        l "It's not so hard, i want your {font=seguisym.ttf}▊▋█▌▍▊▋█▌▍{/font}"
                        l "{cps=500}Your identity silly{/cps}{nw}"
                        p "...?"
                        l "You could say that i want your body sweety"
                        show l nl with Dissolve(0.5, alpha=True)
                        p "I don't know if i like that"
                        l "Don't worry i will only take it if you’re dead"
                        show l a with Dissolve(0.5, alpha=True)
                        p "If? not when?"
                        pause 1
                        show lilith h
                        l "My bad~"
                        show lilith a
                        $ persistent.temple = 3
                        l "Then?"
                        jump thedeal

        label game:
            play sound "audio/wuo.ogg" volume 0.5
            l "Deal?"
            play music ["audio/temple2.ogg","audio/temple2.ogg"]  volume 0.75 fadeout 0.3 fadein 0.3 
            pa "I don't like this"
            l "Don't worry dear"
            l "{cps=0}I almost only deal with sinful people{/cps}{p=0.1}{nw}"
            l "{cps=0}I {color=#ff4989}only{/color} deal with sinful people{/cps}"
            l "So you {b}deserve{/b} everything{nw}"
            pa "What do you mean?"
            l "Anyway~"
            $ numerito = 33
            jump who

            label rep:
                l "Just repeat '{font=LibreBarcode39-Regular.ttf}i give my body and soul to you{/font}'"
                $ rep = renpy.input("Repeat", allow="abcdefghijklmnñopqrstuvwxyz ")
                if rep == "fuck" or rep == "fuck you" or rep == "damn" or rep == "damn you" or rep == "shit":
                    l "How rude"
                    l ""
                    jump end
                if rep == "i give my body and soul to you" or rep == "si" or rep == "yes" or rep == "igivemybodyandsoultoyou"  or rep == "te entrego mi cuerpo y alma" or rep == "teentregomicuerpoyalma":
                    l "You know? i already have them"
                    l "But..."
                    jump thanks
                if rep == "no" or rep == "nop" or rep == "nope":
                    l "Ok"
                    l ""
                    jump end
                else:
                    jump rep

        label who:
            $ name = renpy.input("What is your name?", length=3, allow="lia")
            if name == "lia":
                l "Really?"
            else:
                play sound "audio/wuo.ogg" volume 0.5
                e "{cps=800}lia{/cps}{nw}"
                jump who

            show l n with Dissolve(0.5, alpha=True)

            menu:
                l "Where do you work?"
                "At the police":
                    pass
            l "Cool"
            menu:
                l "Where do you live?"
                "District 5":
                    pass
                "My home":
                    show lilith h with Dissolve(0.5, alpha=True)
                    l "Haha"
                    show lilith a with Dissolve(0.5, alpha=True)
            l "How general"
            
            menu:
                l "Your parents are?"
                "They are...":
                    menu:
                        "Something with... a?":
                            p "Their names where..."
                            p "Eh...?"
                        "Not here":
                            pass
            show l vn with chaosdissolve
            menu:
                l "Favourite food?"
                "...":
                    pass
                "Eh?":
                    pass
                "I... liked... sweet stuff?":
                    pass
            
            menu:
                l "Favourite colour?"
                "░▒░":
                    pass
                "░▒░░▒░░▒░░▒░":
                    pass
                "Why?":
                    pass
            
            
            show l v with pixellate
            menu:
                l "The colour of your room"
                "I...":
                    pass
            menu:
                l "Are you alive?"
                "YES!":
                    l "Really?"
                " ":
                    pass
            hide l with chaosdissolve
            l "I granted a Wish"
            l "'I wanna be her'"
            l "For that someone had to disappear"
            menu:
                l "Did you take the deal?"
                " ":
                    pass
                " ":
                    pass
            l "Someone pushed another"
            l "If someone wishes to be another person"
            l "And their wish is granted"

            menu:
                l "Do you think they will remember who they were?"
                "Yes?":
                    pass
                "...?!":
                    p "Are you saying?"
                    pass
            l "When someone wishes for the life of another"
            menu:
                l "Do they want the real one?"
                " ":
                    pass

            l "I guess it depends"
            l "But i think they want the life they perceive"
            l "So they yearn for something incomplete and illusory"
            l "And illusions become delusions"
            nlv "And have a thing for becoming nightmares"
            nvl clear
            l "Well, it doesn't matter"
            l "Is stupid to kill someone if you want their life"
            l "If a Killer becomes their victim"
            l "Then they are the victim"
            l "But both made a wish"
            play music ["audio/help.ogg","audio/help.ogg"]  volume 0.75 fadeout 0.3 fadein 0.3 
            l "And my condition was that {b}one{/b} had to dissapear"
            l "So granted two wishes"
            l "The victim became the victimizer"
            l "The victimizer became the victim"
            l "One replaced the other"
            l "And then the other"
            l "And the other, and the other, and the other"
            l "Or so i say"
            l "So, the one in front of me"
            nlv "Are you really Lia, the one who fell?"
            nvl clear
            menu:
                "Yes":
                    pass
                "No":
                    pass
                "It doesn’t matter":
                    menu:
                        "I just want to get out":
                            if numerito == 33:
                                l "Well, let's go back to the game"
                                jump rep
                            l "Then take the deal"
                            menu:
                                "Yes":
                                    jump thanks
                                "No":
                                    jump start


            l "Are you sure?"
            e "{fast} I'm {p=0.1}{nw}"
            $ renpy.notify("Who are you?")
            p "{cps=0}{fast} Not {p=0.1}{nw}{/cps}"
            e "{cps=0}{fast} Yes {p=0.1}{nw}{/cps}"
            e "{cps=0}{fast} Meybe {p=0.1}{nw}{/cps}"
            p "{cps=0}{fast} ▟▛▊▋█▅▖▗▝▝▌▍▎ {p=0.1}{nw}{/cps}"
            e "{cps=0}{fast} ▗▝▝▘▞▚▙▟░ {p=0.1}{nw}{/cps}"
            e "{cps=0}{fast} I'm me {p=0.1}{nw}{/cps}"
            e "{cps=0}{fast} I'm her {p=0.1}{nw}{/cps}"
            p "{cps=0}{fast} I'm ▉▆▅▄▃▪ {p=0.1}{nw}{/cps}"
            p "{cps=0}{fast} ▗▝▝▪▫▬▭▮▯ {p=0.1}{nw}{/cps}"
            e "{cps=0}{fast} ▗▝▝▌ {p=0.1}{nw}{/cps}"
            e "{cps=0}{fast} ▖▗▝▝▕▖▗▝▝▘▞{p=0.1}{nw}{/cps}"


            jump end


    label thanks:
        stop music
        l "Thank you for your patronage"
        scene out with chaosdissolve
        pause 1
        $ renpy.notify("outside?")
        pause 5
        scene out2
        $ persistent.temple = 6
        scene purple with eyeclose
        pause 1
        scene purple with chaosdissolve
        nlv "{size=50}I Wanna be her{/size}"
        nvl clear
        nlv "By Taumi {p} The licorice space jellyfish"
        nvl clear
        jump end

    label whoim:
        play music ["audio/safe.ogg","audio/safe.ogg"]  volume 0.75 fadeout 1.0 fadein 1.0
        scene pink with pixellate
        show caida a
        l "When the fall became imminent they extended their hand"
        show caida b
        l "It was the desire for something more insidious than survival"

        nlv "{b}{size=50}Retribution{/size}{/b}"
        nvl clear
        
        l "{size=50}“Die with me”{/size}"
        show caida c
        l "Graving her, they let their hart fester in malice"
        scene falling_0024
        l "To distract themselves from the fear of death"
        show fall inve
        show wellp with Dissolve(1, alpha=True)
        pause 0.5
        scene pink with chaosdissolve
        l "In the end, both fell"
        nlv "And the {i}something{/i} here {p}is one, the other, both and neither"
        nvl clear
        $ persistent.again = False
        jump start

    label shefoudherself:

        scene well with chaosdissolve
        show fall
        pause 0.9
        play music ["audio/help.ogg","audio/help.ogg"]  volume 0.75 fadeout 0.3 fadein 0.3
        play sound "audio/caida.ogg" volume 0.8
        pause 2
        show lia sleep
        nlv "Suddenly"
        nvl clear
        l "She found herself"
        show lia wake
        pause 1
        l "In the bottom of the well"
        show lia shewas
        l "And then she found herself"
        l "She found herself in"
        show gli a
        l "She was"
        l "Was in the bottom"
        l "There was a well"
        show gli b
        l "A well"
        l "The well"
        l "They were"
        show gli c
        l "Together"
        l "Discussing"
        show gli d
        nlv "Jealosy"
        nvl clear
        nlv "Can be so dangerous"
        nvl clear
        scene pink with chaosdissolve
        nlv "They made a wish"
        nvl clear
        l "And then she found herself in the bottom of the well"
        $ renpy.notify("the bottom of the well")
        nlv "In the bottom of the well"
        nvl clear

        if d < 7:
            jump temple
        if d > 14 and d < 19:
            jump waking
        jump end

    # This ends the game.
    label end:
        if persistent.temple == 6:
            scene purple with chaosdissolve
        else:
            scene purple with chaosdissolve
            nlv "{size=50}I Wanna be her{/size}"
            nvl clear
            nlv "By Taumi {p} The licorice Space Jellyfish"
            nvl clear
            pause 2
    return