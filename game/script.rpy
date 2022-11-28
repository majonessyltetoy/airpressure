# You can place the script of your game in this file.

init:
    # Declare images below this line, using the image statement.
    # eg. image eileen happy = "eileen_happy.png"
    image l playful = "images/chara_playful.png"
    image l sad = "images/chara_sad.png"
    image l angry = "images/chara_angry.png"
    image l bored = "images/chara_bored.png"
    image l happy = "images/chara_happy.png"
    image l surprised = "images/chara_surprised.png"
    image l upset = "images/chara_upset.png"
    image l cynical = "images/chara_cynical.png"
    image l annoyed = "images/chara_annoyed.png"
    image nurse = "images/nurse.png"
    
    image l playfulanim = Animation ("images/chara_playful.png", 0.5,
                                                         "images/chara_playfulf1.png", 0.05,
                                                         "images/chara_playfulf2.png", 0.05,
                                                         "images/chara_playfulf3.png", 0.05,
                                                         "images/chara_playfulf2.png", 0.05,
                                                         "images/chara_playfulf3.png", 0.05,
                                                         "images/chara_playfulf4.png", 0.05,
                                                         "images/chara_playfulf5.png", 0.05,
                                                         "images/chara_playfulf4.png", 0.05,
                                                         "images/chara_playfulf5.png", 0.05,
                                                         "images/chara_playfulf6.png", 0.05,
                                                         "images/chara_playfulf7.png", 0.05,
                                                         "images/chara_playfulf6.png", 0.05,
                                                         "images/chara_playfulf7.png", 0.05,
                                                         "images/chara_playful.png", 0.5)
                                                        
        
        
    image l sadanim = Animation ("images/chara_sad.png", 0.5,
                                                         "images/chara_sadf1.png", 0.05,
                                                         "images/chara_sadf2.png", 0.05,
                                                         "images/chara_sadf3.png", 0.05,
                                                         "images/chara_sadf2.png", 0.05,
                                                         "images/chara_sadf3.png", 0.05,
                                                         "images/chara_sadf4.png", 0.05,
                                                         "images/chara_sadf5.png", 0.05,
                                                         "images/chara_sadf4.png", 0.05,
                                                         "images/chara_sadf5.png", 0.05,
                                                         "images/chara_sadf6.png", 0.05,
                                                         "images/chara_sadf7.png", 0.05,
                                                         "images/chara_sadf6.png", 0.05,
                                                         "images/chara_sadf7.png", 0.05,
                                                         "images/chara_sad.png", 0.5)
    
    image l happyanim = Animation ("images/chara_happy.png", 0.5,
                                                         "images/chara_happyf1.png", 0.05,
                                                         "images/chara_happyf2.png", 0.05,
                                                         "images/chara_happyf3.png", 0.05,
                                                         "images/chara_happyf2.png", 0.05,
                                                         "images/chara_happyf3.png", 0.05,
                                                         "images/chara_happyf4.png", 0.05,
                                                         "images/chara_happyf5.png", 0.05,
                                                         "images/chara_happyf4.png", 0.05,
                                                         "images/chara_happyf5.png", 0.05,
                                                         "images/chara_happyf6.png", 0.05,
                                                         "images/chara_happyf7.png", 0.05,
                                                         "images/chara_happyf6.png", 0.05,
                                                         "images/chara_happyf7.png", 0.05,
                                                         "images/chara_happy.png", 0.5)
    
    image l annoyedanim = Animation ("images/chara_annoyed.png", 0.5,
                                                         "images/chara_annoyedf1.png", 0.05,
                                                         "images/chara_annoyedf2.png", 0.05,
                                                         "images/chara_annoyedf3.png", 0.05,
                                                         "images/chara_annoyedf2.png", 0.05,
                                                         "images/chara_annoyedf3.png", 0.05,
                                                         "images/chara_annoyedf4.png", 0.05,
                                                         "images/chara_annoyedf5.png", 0.05,
                                                         "images/chara_annoyedf4.png", 0.05,
                                                         "images/chara_annoyedf5.png", 0.05,
                                                         "images/chara_annoyedf6.png", 0.05,
                                                         "images/chara_annoyedf7.png", 0.05,
                                                         "images/chara_annoyedf6.png", 0.05,
                                                         "images/chara_annoyedf7.png", 0.05,
                                                         "images/chara_annoyed.png", 0.5)
    
    image l cynicalanim = Animation ("images/chara_cynical.png", 0.5,
                                                         "images/chara_cynicalf1.png", 0.05,
                                                         "images/chara_cynicalf2.png", 0.05,
                                                         "images/chara_cynicalf3.png", 0.05,
                                                         "images/chara_cynicalf2.png", 0.05,
                                                         "images/chara_cynicalf3.png", 0.05,
                                                         "images/chara_cynicalf4.png", 0.05,
                                                         "images/chara_cynicalf5.png", 0.05,
                                                         "images/chara_cynicalf4.png", 0.05,
                                                         "images/chara_cynicalf5.png", 0.05,
                                                         "images/chara_cynicalf6.png", 0.05,
                                                         "images/chara_cynicalf7.png", 0.05,
                                                         "images/chara_cynicalf6.png", 0.05,
                                                         "images/chara_cynicalf7.png", 0.05,
                                                         "images/chara_cynical.png", 0.5)
    
    image l angryanim = Animation ("images/chara_angry.png", 0.5,
                                                         "images/chara_angryf1.png", 0.05,
                                                         "images/chara_angryf2.png", 0.05,
                                                         "images/chara_angryf3.png", 0.05,
                                                         "images/chara_angryf2.png", 0.05,
                                                         "images/chara_angryf3.png", 0.05,
                                                         "images/chara_angryf4.png", 0.05,
                                                         "images/chara_angryf5.png", 0.05,
                                                         "images/chara_angryf4.png", 0.05,
                                                         "images/chara_angryf5.png", 0.05,
                                                         "images/chara_angryf6.png", 0.05,
                                                         "images/chara_angryf7.png", 0.05,
                                                         "images/chara_angryf6.png", 0.05,
                                                         "images/chara_angryf7.png", 0.05,
                                                         "images/chara_angry.png", 0.5)
    image l boredanim = Animation ("images/chara_bored.png", 0.5,
                                                         "images/chara_boredf1.png", 0.05,
                                                         "images/chara_boredf2.png", 0.05,
                                                         "images/chara_boredf3.png", 0.05,
                                                         "images/chara_boredf2.png", 0.05,
                                                         "images/chara_boredf3.png", 0.05,
                                                         "images/chara_boredf4.png", 0.05,
                                                         "images/chara_boredf5.png", 0.05,
                                                         "images/chara_boredf4.png", 0.05,
                                                         "images/chara_boredf5.png", 0.05,
                                                         "images/chara_boredf6.png", 0.05,
                                                         "images/chara_boredf7.png", 0.05,
                                                         "images/chara_boredf6.png", 0.05,
                                                         "images/chara_boredf7.png", 0.05,
                                                         "images/chara_bored.png", 0.5)
    
    image intro01 = "images/intro01.png"
    image bg black = "images/bg_black.png"
    image bg house = "images/bg_house.png"
    image bg park = "images/bg_park.png"
    image bg town = "images/bg_town.png"
    image bg hosp = "images/bg_hosp.png"
    image bg end = "images/bg_black.png"
    
    image splash = "images/logo.png"
    image end = "images/end.png"

    
    # Declare characters used by this game.
    $ m = Character(what_color="#dabd34")
    $ l = Character('Leigh', color="#ffffff")
    $ nurse = Character('Nurse', color="#ffffff")

    $_game_menu_screen = "_quit_prompt"

    
# The game starts here.


label splashscreen:
    $ renpy.pause(0)
    scene black
    with Pause(0.5)

    show splash
    with fade
    with Pause(2.0)

    scene black
    with fade
    with Pause(1.0)

    return
    



label start:
    scene intro01 with pixellate
    play music "images/airpressure.mp3" 
    m "{i}I met her when I was a teenager.{/i}"
    $ config.rollback_enabled = False


    m "{i}From the second we met, she wrapped herself around my left arm, and has stuck there ever since.{/i}"
    scene bg house with pixellate
    m "{i}It's several years later now. She's still here with me.{/i}"
    show l playful    
    l "How's it going?"
    
    m "{i}I'm not sure how I feel about her being around anymore.{/i}"
    
    "Fine... "
    show l happy
    l "That's good."
    show l playful
    l "Hey, do you know what day it is? It's the anniversary of the day we met."
     
    m "{i}Of course it is.{/i}"
    show l happy
    l "So do you want to do anything?"
     
    "Huh. How about..."
 
    menu:
        
        "Let's just stay in.":
            "Let's just stay in together."
            show l sad
            l "You sure? That's a little boring."
            jump chapter1_1
        "I'm going out.":
            "...I think I'm just going to go for a walk."
            show l sad
            l "Uh, OK."
            jump chapter1_3
            
            
            
label chapter1_1:
#This is the route through which you get the girl. The dilemma is how you met.
    show l happy
    m "{i}Really, this anniversary doesn't mean that much to me.{/i}"
    
    "It's just another day..."
    show l surprised
    l "Excuse me?"
    
    "I- I mean..."
    
    menu:
        
        "I'm sorry.":
            "I'm sorry, I forgot it was coming up."
            show l playful
            l "Hah, don't worry."
            jump chapter1_1q1
        
        "I'm with you all the time.":
            "Well we've been together for so long..."
            show l playful
            l "Right..."
            jump chapter1_1q2
    
    
    
label chapter1_1q1:

    m "{i}Memory is strange. This date always seems to fall out my head.{/i}"
    m "{i}But I remember other things about that day, like the song which was playing when we met.{/i}"
    m "{i}It makes me feel a little nostalgic.{/i}"
    
    show l sad
    l "Are you sure you're alright?"  
    "Oh yeah. I was just thinking..."
    
    menu:
        "...About the day we met.":
            "About the day we met."
            show l happy
            l "Oh, really?"
            jump chapter1_1q3
            
        "Do you want to listen to some music?":
            "Do you want to listen to some music?"
            show l happy
            l "Sure, whatever you want."
            jump chapter1_1q4
        
label chapter1_1q2:
    
    "...And, uh..."
    
    menu:
        "So every day is equally special!":
            "So, every day I'm with you is as special as the last."
            show l playful
            l "Haha, right. That's so cheesy! Good one!"
            jump chapter1_1q5
        
        "I just didn't notice the date.":
            "I guess I didn't realise it was anything special."
            show l upset
            l "..."
            jump chapter1_1q6

label chapter1_1q3:
    
    "Yes... I was thinking how much has changed since we met."
    show l happy
    l "Haha, I hope it's good change!"
    m "{i}Actually, thinking back to how I was before we met...{/i}"
    m "{i}...I realised I was much happier then.{/i}"
    m "{i}Is staying here with her really such a good idea?{/i}"
    
    menu:
        "Yes.":
            m "{i}Yes, my life is different than I could have ever imagined...{/i}"
            m "{i}...But now, I'm so comfortable with her that I can't imagine anything else.{/i}"
            scene bg black with pixellate
            m "{i}Maybe life was better before...{/i}"
            m "{i}...But I can't say that life after her would be any better than it is right now.{/i}"
            m "{i}Perhaps if we work together, we can make our lives better.{/i}"
            jump chapter2_1
        
        "I'm not sure.":
            m "{i}I just don't know anymore.{/i}"
            show l surprised
            l "Hey, you look like you need some fresh air."
            scene bg black with pixellate
            m "{i}She all but dragged me out the door.{/i}"
            m "{i}I hope she doesn't find my lack of enthusiasm offensive.{/i}"
            m "{i}I don't have the energy to resist her.{/i}"
            jump chapter2_3

label chapter1_1q4:
    
    m "{i}I wonder if she remembers things like that as well.{/i}"
    show l happy
    l "..."
    m "{i}...{/i}"
    show l bored
    l "..."
    l "Hmm?"
    "Do you remember this song?"
    show l surprised
    l "Ah..."
    show l playful
    l "Uhm, must be before my time."
    "Hey, you're not any younger than I am!"
    m "{i}And I bought this CD on the week that we met.{/i}"
    show l surprised
    l "Sorry."
    m "{i}I thought she might remember... What should I do?{/i}"
    
    menu:
        "Forgive her.":
            "It's not a big deal."
            show l sad
            l "Ah, I'm sorry! I didn't realise it was so important."
            "Hey, it's no problem."
            scene bg black with pixellate
            m "{i}We listened to the rest of the CD.{/i}"
            m "{i}I couldn't tell her how much I wanted her to remember.{/i}"
            m "{i}Maybe being together means more to me than it does to her.{/i}"
            jump chapter2_1
        
        "Make her feel a little bad.":
            "Really? This song was playing when we met!"
            l "..!"
            show l sad
            l "I- I'm really sorry. After I hassled you about the forgetting the date myself."
            "..."
            show l upset
            l "..."
            "...Why don't we go out for a little while?"
            scene bg black with pixellate
            m "{i}I was probably a little bit unfair to her.{/i}"
            m "{i}I thought if we went out, the change of scenery would help us relax a bit.{/i}"
            m "{i}We spend so long in that house, going to the park would be good for us.{/i}"
            jump chapter2_2

label chapter1_1q5:
    
    "No! I mean it."
    show l surprised
    l "Haha, reeeally?"
    
    menu:
        "Yes.":
            "Yes. Haha, it's a little over the top, but I am glad each day that I have you."
            show l playful
            l "Hehe, that's cute."
            scene bg black with pixellate
            m "{i}Yes, I just told her that to make her feel better.{/i}"
            m "{i}To make myself feel better too.{/i}"
            m "{i}I felt bad for forgetting the anniversary. I hope she doesn't mind.{/i}"
            jump chapter2_1
        
        "No.":
            "No, no, I'm just teasing you."
            show l sad
            l "That's mean."
            "..?"
            show l upset
            l "..."
            "...Sorry."
            scene bg black with pixellate
            m "{i}She didn't make any conversation for a couple of hours after that.{/i}"
            m "{i}Then she declared that she wanted to go out for a bit.{/i}"
            m "{i}I felt like I needed to make it up to her, so I went with her.{/i}"
            jump chapter2_2
            
            

label chapter1_1q6:
    
    show l annoyed
    l "Th-that's pretty offensive."
    l "It's bad enough that you don't remember that today is the day we met, but it's worse that you don't even care."
    "..."
    menu:
        "I'm sorry.":
            "I'm sorry."
            show l upset
            l "..."
            scene bg black with pixellate
            m "{i}She said she wanted some fresh air, and I followed her, not knowing what else to do.{/i}"
            m "{i}I don't know why I was being so off. I was probably just frustrated.{/i}"
            m "{i}I always end up taking everything out on her.{/i}"
            jump chapter2_2
        
        "...":
            show l angry
            l "And you don't even have anything to say for yourself?!"
            l "..."
            scene bg black with pixellate
            m "{i}I'm not sure why, but I felt that she had no reason to get annoyed.{/i}"
            m "{i}This anniversary is not a good or happy day for me.{/i}"
            m "{i}Yet, I still followed her when she stormed out.{/i}"
            jump chapter2_2

#label chapter1_2:
#This is the average route. The dilemma is being seen?
    
#    "This is chapter1_2"
#THIS CHAPTER NO LONGER NEEDED!!!    
    
    




####START OF CHAPTER1_3!#######
label chapter1_3:
#This is the lose the girl route. The dilemma is being alone.
    
    scene bg town
    m "{i}I thought I would head out into the town for a while.{/i}"
    m "{i}It was busy; people everywhere.{/i}"
    m "{i}I wanted to get lost amongst the crowd for a while.{/i}"
    m "{i}Maybe even feel like a normal person for a bit.{/i}"
    m "{i}But then... I hear someone.{/i}"
    
    menu:
        "I should stop.":
            l "Hey!"
            l "Hey, wait!"
            show l playful
            "Oh, hi."
            jump chapter1_3q1
        
        "Carry on.":
            m "{i}I don't stop walking.{/i}"
            show l sad
            l "Oi, are you ignoring me?"
            jump chapter1_3q2
    

label chapter1_3q1:
    
    m "{i}What is she doing here?{/i}"
    show l happy
    l "S-sorry... I thought you might like the company."
    "Hmm..."
    
    menu:
        "Yeah, I wouldn't mind.":
            "Yeah, I'm glad you're here."
            l "I wondered if something was up..?"
            jump chapter1_3q3
        
        "No, I'm fine.":
            "Actually, I wanted to do some stuff alone."
            show l playful
            l "Oh, I see..."
            "Huh?"
            l "Buying me something, hmm? That's fine, I'll get out of your hair."
            jump chapter1_3q4

label chapter1_3q2:
    
    "..."
    show l surprised
    l "You are, aren't you?!"
    "Uh..."
    
    menu:
        "No, I'm not.":
            "No, sorry. I was just thinking."
            show l sad
            l "Really?"
            l "What are you thinking about?"
            jump chapter1_3q5
        
        "...":
            "..."
            show l angry
            l "Hey!!!"
            "I want to be alone, I'm sorry."
            show l upset
            l "Right. Whatever."
            jump chapter1_3q6

label chapter1_3q3:
    
    "No, nothing."
    m "{i}At least, nothing which can't be solved now you're here.{/i}"
    show l happy
    l "Ah, I'm glad."
    l "So do you want to go somewhere?"
    "Yeah..."
    
    menu:
        "Sure, let's go sit somewhere quiet.":
            "Sure, shall we find somewhere quiet? It's so busy 'round here."
            show l playful
            l "How about the park over there?"
            scene bg black with pixellate
            m "{i}I was glad, in the end, that she showed up.{/i}"
            m "{i}But I can't help but feel a little disappointed in myself.{/i}"
            m "{i}I thought I could cope without her...{/i}"
            jump chapter2_3
        
        "Why don't we head back home?":
            "I'm tired, so let's go back home."
            l "Oh, sure."
            scene bg black with pixellate
            m "{i}I was glad she showed up.{/i}"
            m "{i}But also, I'm frustrated that I couldn't be without her for even a little while.{/i}"
            m "{i}I wonder if I'm stuck with her...{/i}"
            jump chapter2_1

label chapter1_3q4:
    
    hide l
    m "{i}No, really, I just wanted to be alone.{/i}"
    m "{i}I walked around for a couple of hours.{/i}"
    m "{i}I don't know if I was lonely, or tired, but the bustle of the people started to make my head swim.{/i}"
    m "{i}...{/i}"
    
    menu:
        "I wish she was here now.":
            m "{i}I wish she was here right now.{/i}"
            show l surprised
            l "..?"
            l "You OK there?"
            "..."
            scene bg black with pixellate
            m "{i}I don't know how she did it.{/i}"
            m "{i}She always manages to appear at a moment's notice.{/i}"
            m "{i}Was she following me the whole time?{/i}"
            jump chapter2_3
            
        
        "I'll be fine.":
            m "{i}I decide to take a break and find somewhere to sit.{/i}"
            scene bg black with pixellate
            m "{i}I settled on going to a park nearby.{/i}"
            m "{i}I was glad for the time alone.{/i}"
            m "{i}Some time when I didn't feel her immediate presence.{/i}"
            jump chapter2_4

label chapter1_3q5:
    
    show l playful
    l "Penny for your thoughts? That's about all they're worth!"
    "Haha!"
    m "{i}The crowds are giving me a headache. But because she's here it's starting to lift.{/i}"
    show l happy
    l "Hehehe."
    m "{i}Having her here is making me feel much better!{/i}"
    
    menu:
        "I'm so glad":
            m "{i}I'm glad.{/i}"
            show l sad
            l "Are you OK? You seem distant."
            "Yeah, I'm fine. Do you want to go sit somewhere quiet?"
            show l happy
            l "Yes!"
            scene bg black with pixellate
            m "{i}We walked to the park together.{/i}"
            m "{i}On the way, I thought about how I really do need her around.{/i}"
            m "{i}I'm still not sure how I feel about that...{/i}"
            jump chapter2_3
        
        "I hate it.":
            m "{i}I hate it.{/i}"
            m "{i}I don't want to be tied to her forever.{/i}"
            show l sad
            l "Are you OK? You seem distant."
            "Yeah... Hey, I'll see you at home later, yeah?"
            show l upset
            l "Oh, yeah."
            scene bg black with pixellate
            m "{i}I headed somewhere where I could be alone.{/i}"
            m "{i}So I could think in peace, I wandered into a nearby park.{/i}"
            jump chapter2_4
            

label chapter1_3q6:
    
    "..."
    l "..."
    menu:
        "Look, it's not you...":
            "Look, it's not you... I just wanted to be alone for a while."
            show l sad
            l "..."
            scene bg black with pixellate
            m "{i}As hard as I was on her, I know I'll be trying to make it up to her later.{/i}"
            m "{i}I'm just an idiot like that.{/i}"
            m "{i}I know I can't live without her.{/i}"
            jump chapter2_4
        "What are you doing here anyway?":
            "Why are you here?"
            show l annoyed
            l "Stupidly, I thought you needed me."
            l "Clearly I am wrong!"
            "..."
            l "...!"
            l "Urgh!"
            scene bg black with pixellate
            m "{i}...What an idiot I am.{/i}"
            m "{i}She walked away in a huff...{/i}"
            m "{i}...And I'm the idiot, because I followed her.{/i}"
            jump chapter2_2



#######THIS IS THE START OF CHAPTER2_1######
label chapter2_1:
#This is the continuation of getting the girl route. The dilemma is reliance.
    scene bg house with pixellate
    m "{i}A couple of hours passed. I started to get this nagging feeling...{/i}"
    "Hey..."
    show l bored
    l "Hmm?"
    "I was wondering..."
    menu:
        "Why are you here?":
            "Why are you here?"
            l "Because you wanted to stay home with me..?"
            "That's not what I mean. Why do you stay with me?"
            show l happy
            l "Oh simple. You need me, don't you?"
            l "As long as you do, I'm happy to be with you."
            jump chapter2_1q1
        "Do you like me?":
            "Do you like me?"
            show l surprised
            l "Haha what a weird question. Of course I do."
            "But why?"
            show l happy
            l "Why shouldn't I?"
            jump chapter2_1q2

label chapter2_1q1:
    m "{i}Do I need her?{/i}"
    m "{i}I suppose I must do. But...{/i}"
    menu:
        "What makes you say that?":
            "What makes you say that?"
            show l surprised
            l "Y-you think you don't need me?"
            "Ah! That's not what I meant..."
            l "..."
            jump chapter2_1q3
        "Is it really that obvious?":
            "Is it really that obvious?"
            show l playful
            l "Haha well..."
            "..."
            l "Hahaha, don't look at me like that. It's not bad to need someone, is it?"
            jump chapter2_1q4
            
            
label chapter2_1q2:
    m "{i}I'm ashamed to admit that I'm a little paranoid about this...{/i}"
    "I don't know... I think..."
    menu:
        "I'm not a very nice person.":
            "I'm not a very nice person."
            show l happy
            l "You seem nice to me."
            "Hmm..."
            show l playful
            l "Besides, you can rely on me to keep you nice!"
            jump chapter2_1q5
        "Maybe I need more friends.":
            "Maybe I need more friends."
            show l sad
            l "Hmph."
            l "More friends, or do you mean better friends?"
            jump chapter2_1q6
            
            
label chapter2_1q3:
    "Hey, I do need you, alright?"
    show l upset
    l "..."
    show l sad
    l "...Really?"
    menu:
        "Yes.":
            "Yes. I can't imagine life without you."
            show l happy
            m "{i}Where did that come from?{/i}"
            scene bg black with pixellate
            m "{i}I surprised myself a bit.{/i}"
            m "{i}It is true though, I rely on her whenever I get into trouble.{/i}"
            m "{i}I wonder if that's a good thing or not...{/i}"
            jump chapter3_1
        "Uh...":
            "Uh... Yes. Of course."
            show l happy
            l "Heh."
            scene bg black with pixellate
            m "{i}I hope she didn't realise how uncertain I was.{/i}"
            m "{i}I do need her, but I don't know whether that's something I'm comfortable admitting.{/i}"
            m "{i}Maybe I would like to not have to need her anymore.{/i}"
            jump chapter3_2
            
    
label chapter2_1q4:
    "No, not at all."
    show l happy
    m "{i}Although, it does make me wonder...{/i}"
    m "{i}Is it really right to rely on her?{/i}"
    menu:
        "There's no harm in it.":
            m "{i}There's no harm in it.{/i}"
            m "{i}It's normal.{/i}"
            m "{i}Besides, she needs me too.{/i}"
            scene bg black with pixellate
            m "{i}I know I need her. I'm hopeless.{/i}"
            m "{i}I know I cannot be strong without her.{/i}"
            m "{i}Should I be happy that I'm this way?{/i}"
            jump chapter3_1
        "I could be more independent.":
            m "{i}I could be more independent.{/i}"
            m "{i}But that doesn't mean I have to abandon her.{/i}"
            m "{i}Perhaps we could be independent together!{/i}"
            scene bg black with pixellate
            m "{i}Yes, that makes no sense.{/i}"
            m "{i}I'm so comfortable relying on her I'm scared to make any bold moves by myself anymore.{/i}"
            m "{i}Is being comfortable really so wrong?{/i}"
            jump chapter3_2
            
            
label chapter2_1q5:
    m "{i}Huh? Is that what I really rely on her for?{/i}"
    m "{i}Is that all I get out of being with her?{/i}"
    menu:
        "Yes.":
            m "{i}Yes. I hate to admit it.{/i}"
            m "{i}I'm just using her to reflect back myself.{/i}"
            m "{i}Selfishly, without her, I wouldn't have any way to offload any guilt or unpleasant feelings I have.{/i}"
            scene bg black with pixellate
            m "{i}She seems to think that I'm not a bad person...{/i}"
            m "{i}But am I really a good person?{/i}"
            m "{i}As long as I doubt her, I can't get closer to her.{/i}"
            jump chapter3_2
        "No.":
            m "{i}No, that's not the only reason I like to have her around.{/i}"
            m "{i}She's such a part of my life now, she's almost a part of me!{/i}"
            scene bg black with pixellate
            m "{i}Maybe I do rely on her too much.{/i}"
            m "{i}But is that so bad?{/i}"
            m "{i}While she is around, I feel like I can be a better person.{/i}"
            jump chapter3_1
            
            
label chapter2_1q6:
    "W-where did you get that from?"
    show l upset
    l "..."
    m "{i}Urk, I better say something...{/i}"
    "Look..."
    menu:
        "I don't mean it like that.":
            "I don't mean it like that."
            show l sad
            l "..."
            "Wouldn't you like to meet more people too?"
            show l bored
            l "...I don't need anyone else."
            scene bg black with pixellate
            m "{i}I wonder why she said that.{/i}"
            m "{i}I feel bad for her, being the only person that she knows.{/i}"
            m "{i}I wish I could introduce her to people... but I know she wouldn't like it.{/i}"
            jump chapter3_2
        "Is it wrong for me to want more friends?":
            "is it wrong for me to want more friends?"
            l "..."
            show l upset
            l "I-I think... maybe you won't need me anymore."
            "..."
            scene bg black with pixellate
            m "{i}She was right to be worried, I guess.{/i}"
            m "{i}I feel myself pulling away from her.{/i}"
            m "{i}I think my personality is starting to shift.{/i}"
            jump chapter3_3

            
            
            
#####START OF CHAPTER2_2###########           
label chapter2_2:
    scene bg park with pixellate
    show l bored
    m "{i}I walked beside her.{/i}"
    m "{i}...Well, a little behind her too.{/i}"
    m "{i}She's quiet. Probably annoyed with me.{/i}"
    menu:
        "Apologise.":
            "Uh, I'm sorry."
            l "..."
            show l upset
            l "I know."
            jump chapter2_2q1
        
        "Stay silent.":
            "..."
            l "..."
            show l angry
            l "..."
            l "Are you going to say anything?"
            jump chapter2_2q2
            
    
    
label chapter2_2q1:
    show l sad
    l "...But why are you sorry?"
    m "{i}Huh?{/i}"
    m "{i}Isn't it obvious?{/i}"
    menu:
        "It's my fault.":
            "It's my fault."
            "I'm sorry, I'm so ungrateful sometimes."
            l "..."
            show l happy
            l "...It's fine."
            jump chapter2_2q3
        
        "...Because.":
            "Just, because."
            show l upset
            l "Oh."
            "Well, I don't know."
            jump chapter2_2q4
    
    
    
label chapter2_2q2:
    "..."
    "...I can't think of anything."
    show l cynical
    l "Heh."
    l "I'm tired. I don't want to help you anymore."
    show l bored
    l "You rely on me too much."
    "..."
    menu:
        "Wait...":
            "...Wait."
            show l annoyed
            l "..."
            jump chapter2_2q5
        
        "...I don't care.":
            "I don't care."
            show l cynical
            l "Oh, really?"
            jump chapter2_2q6
        
    
    
    
label chapter2_2q3:
    m "{i}I always forget how much she helps me.{/i}"
    m "{i}I fall out with her so easily.{/i}"
    m "{i}I wonder if I doubt her too much...{/i}"
    menu:
        "Yes.":
            m "{i}Yes, I should be more trusting of her.{/i}"
            m "{i}I can trust her more than I trust myself sometimes.{/i}"
            m "{i}And more than anyone else I have ever met.{/i}"
            show l playful
            l "..?"
            "Heh, it's nothing."
            m "{i}Where would I be without her?{/i}"
            scene bg black with pixellate
            m "{i}We walked home.{/i}"
            m "{i}I decided, I should stop letting stupid things annoy me so much.{/i}"
            m "{i}At least, I can try.{/i}"
            jump chapter3_1
            
        "No.":
            m "{i}No, I must be feeling this for a reason.{/i}"
            m "{i}I should trust myself a little more.{/i}"
            m "{i}But I don't know... It's scary to be independent of her.{/i}"
            show l playful
            l "..?"
            "Heh, it's nothing!"
            m "{i}When did I start to rely on her so much?{/i}"
            scene bg black with pixellate
            m "{i}As we walked home, I thought more.{/i}"
            m "{i}I'd apologised, but I didn't honestly mean it.{/i}"
            m "{i}But on the other hand, I don't want to annoy her.{/i}"
            m "{i}I don't know... What should I do?{/i}"
            jump chapter3_2
    
    
label chapter2_2q4:
    show l sad
    l "Huh. OK."
    "Well..."
    menu:
        "I don't know how else to fix things.":
            "I don't know what else I can do to fix things."
            show l happy
            l "Hmm... you could trust me a little more."
            "I suppose."
            show l playful
            l "And appreciate how much I help you."
            m "{i}She's right, of course.{/i}"
            m "{i}I always forget how much she's helped over the years.{/i}"
            scene bg black with pixellate
            m "{i}We walked back home together.{/i}"
            m "{i}I thought about whether I should rely on her more.{/i}"
            m "{i}Maybe that's all I can do to show her she's needed.{/i}"
            jump chapter3_1
            
        
        "Don't accept it then!":
            "Don't accept my apology then!"
            show l surprised
            l "..!"
            "Ah I don't know why I bothered."
            "I should have known you'd prod at it."
            show l upset
            l "..."
            scene bg black with pixellate
            m "{i}I can't have any secrets from her, I guess.{/i}"
            m "{i}She always dissects everything I say or do.{/i}"
            m "{i}But why do I let her?{/i}"
            m "{i}Do I need her to keep me in check?{/i}"
            jump chapter3_2
    
    
    
label chapter2_2q5:
    "Since when do you think I rely on you too much?"
    show l upset
    l "..."
    "Maybe I do... but it's not fair to blame me."
    show l annoyed
    l "Hmm."
    m "{i}Maybe I'm asking too much.{/i}"
    menu:
        "Apologise.":
            "...Sorry."
            show l upset
            l "It's fine."
            "I know I'm being unfair."
            "Please, don't stop helping me."
            l "..."
            scene bg black with pixellate
            m "{i}We walked home together.{/i}"
            m "{i}I hoped I had appeased her a little.{/i}"
            m "{i}I hoped she could stop me being an idiot in future.{/i}"
            jump chapter3_2
        
        "It's not unreasonable.":
            "I don't think it's unreasonable."
            show l surprised
            l "..!"
            "The only reason you stay here is because of me anyway!"
            "I don't need you if you're going to be like this."
            show l upset
            l "..."
            scene bg black with pixellate
            m "{i}I don't like her anymore.{/i}"
            m "{i}I'm tired of putting up with her.{/i}"
            m "{i}Yes, I'm being awful, but I don't care.{/i}"
            m "{i}We walked home in silence.{/i}"
            jump chapter3_3
            
    
    
    
label chapter2_2q6:
    show l cynical
    l "So you would be fine if I stopped helping you completely?"
    "...You wouldn't."
    l "Heh..."
    show l angry
    l "You think you can get by without me to back you up?"
    "Well..."
    menu:
        "...No.":
            "...No, you're right."
            show l annoyed
            l "..."
            "Sorry."
            "Please don't be upset with me!"
            show l upset
            l "..."
            scene bg black with pixellate
            m "{i}I didn't want to be alone.{/i}"
            m "{i}Maybe I just use her to stop myself feeling lonely.{/i}"
            m "{i}I am pathetic like that.{/i}"
            jump chapter3_2
        
        "Yes!":
            "Yes. Well, I would like to try."
            show l cynical
            l "Heh, and come running to me when you fail!"
            "Not if you're not going to help."
            show l surprised
            l "..."
            show l upset
            l "Don't be like that."
            "..."
            l "You know I'll always help you."
            l "No matter how bad things seem."
            "..."
            scene bg black with pixellate
            m "{i}We argued a little more on the way home.{/i}"
            m "{i}I think I'm realising that I don't want her around.{/i}"
            m "{i}She can threaten me with leaving, but I think she's more scared of it than I am.{/i}"
            jump chapter3_3

            
            



    
label chapter2_3:
#This is the continuation of the average route. The girl is happy

    scene bg park with pixellate
    show l happy
    m "{i}We sat together on the grass in the park.{/i}"
    m "{i}She's so cheerful.{/i}"
    m "{i}It just shows me how oblivious she can be to my thoughts.{/i}"
    show l playful
    l "It's nice out here, huh?"
    m "{i}Totally oblivious.{/i}"
    m "{i}I know I'm being unfair. What I should do is...{/i}"
    menu:
        "Buy ice cream.":
            m "{i}Yeah, I should try be as happy as she is.{/i}"
            "Mm. Hey, do you wanna get some ice cream?"
            show l happy
            l "Yeah, sure!"
            m "{i}...{/i}"
            jump chapter2_3q1
        "Confess.":
            m "{i}I should tell her what's up.{/i}"
            "Uhm, listen..."
            show l happy
            l "Hmm?"
            "Do you think... Do you think I rely on you too much?"
            show l surprised
            l "How do you mean? We're friends aren't we?"
            jump chapter2_3q2

label chapter2_3q1:
    m "{i}So, I bought ice cream.{/i}"
    m "{i}As we sat around eating, I started to think if I could bring up the subject in a gentle way.{/i}"
    "Hey."
    "Mmn?"
    "Do you think..."
    menu:
        "...we should go sit by the river?":
            "There might be cute ducks on the river."
            show l playful
            l "Oh yeah. Haha, I wonder if ducks like ice cream!"
            m "{i}Ducks eat anything.{/i}"
            jump chapter2_3q3
        "...I rely on you too much?":
            "...I rely on you too much?"
            show l sad
            l "Do you think you do?"
            "I don't know."
            l "Is it so bad to rely on me every so often?"
            jump chapter2_3q4
            

label chapter2_3q2:
    m "{i}She's right, we are friends. But is this what I really want?{/i}"
    menu:
        "Yes.":
            "Y-yes."
            show l sad
            l "You sound unsure."
            "W-well, I still think it would be a good idea if I made some other friends."
            "Just so I don't have to depend on you for everything."
            jump chapter2_3q5
        "No.":
            "W-well, I guess."
            show l sad
            l "..?"
            "I think I just need to be alone for a while."
            show l annoyed
            l "Huh. I make effort to cheer you up and you don't need me?"
            jump chapter2_3q6

label chapter2_3q3:
    m "{i}I'm such a coward.{/i}"
    m "{i}If I can't tell her, then I have to...{/i}"
    menu:
        "Forget it.":
            m "{i}I'll have to just forget this stupid feeling.{/i}"
            m "{i}Relying on her isn't so bad.{/i}"
            m "{i}Maybe I should be happy that I have someone like her to depend on instead?{/i}"
            scene bg black with pixellate
            m "{i}We went back home.{/i}"
            m "{i}Not everything has to be perfect, does it?{/i}"
            m "{i}Perhaps relying on her is the best I can ever hope for.{/i}"
            m "{i}I should be grateful and embrace the things that I do have.{/i}"
            jump chapter3_1
            
        "Learn to live with it.":
            m "{i}I'll just have to learn to get by as it is.{/i}"
            m "{i}I'm sure I can summon the strength to do so.{/i}"
            m "{i}I've been OK so far...{/i}"
            show l playful
            l "Let's go home."
            scene bg black with pixellate
            m "{i}I don't need to change anything, I told myself.{/i}"
            m "{i}We went home.{/i}"                 
            m "{i}Same as always.{/i}"
            jump chapter3_2

label chapter2_3q4:
    m "{i}It's no good, I have to say...{/i}"
    menu:
        "No.":
            "No, I guess it's OK."
            show l playful
            l "Haha, sound a little more sure."
            "Heh, well, I don't like being a burden."
            show l happy
            l "It's not a problem."
            "I suppose."
            scene bg black with pixellate
            m "{i}She reassured me everything's all OK.{/i}"
            m "{i}Maybe I don't need to change, I just need to be fine with everything staying the same.{/i}"
            m "{i}I wonder if it will stay the same forever. Whether she will change her mind.{/i}"
            jump chapter3_1
        "Yes.":
            "I just think I should be more self-sufficient."
            show l surprised
            l "...Really?"
            "Yes."
            show l upset
            l "Hah, sometimes I think you're trying to get rid of me."
            "..."
            "...Not exactly."
            "I just think we could tone it down a little."
            show l sad
            l "..."
            scene bg black with pixellate
            m "{i}She went home without me.{/i}"
            m "{i}I started to feel awful.{/i}"
            m "{i}And then I felt worse when I realised how tied to her I was.{/i}"
            m "{i}I should make some steps to resolve these feelings.{/i}"
            jump chapter3_3

label chapter2_3q5:
    l "Hmm."
    "What?"
    show l upset
    l "Do you mean more friends, or friends instead of me?"
    m "{i}Huh, I mean...{/i}"
    menu:
        "More friends.":
            "Just more friends, of course!"
            "There's no way I'd leave you behind."
            show l happy
            l "Really?"
            "Really."
            m "{i}But I wonder, if I met new people, would they get on with her as well as I do?{/i}"
            scene bg black with pixellate
            m "{i}We stayed in the park for a while, and then headed home.{/i}"
            m "{i}She was happy now I'd assured her I wasn't going to abandon her.{/i}"
            m "{i}When it comes down to it, I need her more than anything or anyone else.{/i}"
            jump chapter3_2
        "Instead of you.":
            "I don't know. I think it would be good for both of us to have different friends."
            show l annoyed
            l "I don't need different friends."
            "Well I do!"
            "I'm sorry, I just need time alone. I can't spend all my time with you!"
            show l upset
            l "...Fine."
            hide l
            m "{i}She left.{/i}"
            scene bg black with pixellate
            m "{i}I know I am cruel.{/i}"
            m "{i}If I'm not though, she'll be with me forever...{/i}"
            m "{i}...And I'll never be able to move on.{/i}"
            m "{i}I feel like I need to try to move on.{/i}"
            jump chapter3_3

label chapter2_3q6:
    m "{i}Urgh, made her angry...{/i}"
    menu:
        "Apologise.":
            "...Sorry. It's not like that."
            show l upset
            l "..."
            "Sorry, I'm just confused. Of course I need you."
            show l sad
            l "..."
            l "Shall we head home?"
            scene bg black with pixellate
            m "{i}I don't want to rely on her, but it's so easy!{/i}"
            m "{i}I can't decide if I am better off with her or without her.{/i}"
            m "{i}We went home, and I didn't mention it for the rest of the day.{/i}"
            jump chapter3_2
        "Let her leave.":
            "Sorry, not right now."
            l "..."
            "I just don't need cheering up like this. I need time to think."
            show l cynical
            l "Fine. I'll see you later, I guess."
            scene bg black with pixellate
            m "{i}She headed back home without me.{/i}"
            m "{i}I thought about my relationship with her.{/i}"
            m "{i}I wonder, if I am ready or even able to meet new people.{/i}"
            jump chapter3_3
            


label chapter2_4:
#This is the continuation of the lose the girl route.
    scene bg park with pixellate
    m "{i}I've been walking around the park for a few minutes.{/i}"
    m "{i}...Starting to feel a little aimless.{/i}"
    m "{i}I should...{/i}"
    menu:
        "Sit down.":
            m "{i}I sit down on the grass and start people watching.{/i}"
            m "{i}Watching everyone milling around in pairs and groups, I start to feel really disconnected from it all.{/i}"
            jump chapter2_4q1
        "Keep walking.":
            m "{i}I'll keep walking.{/i}"
            m "{i}I can ignore other people easier while I walk.{/i}"
            m "{i}It gives me chance to think clearly.{/i}"
            jump chapter2_4q2
        
label chapter2_4q1:
    m "{i}I try to relax a bit.{/i}"
    menu:
        "Feel better.":
            m "{i}I start to feel a little better.{/i}"
            m "{i}I think that I don't need her anymore.{/i}"
            m "{i}I can get by on my own!{/i}"
            jump chapter2_4q3
        
        "Feel worse.":
            m "{i}Haha, I knew it wasn't a good idea to come here alone.{/i}"
            m "{i}Right now, I'm just plain useless when I'm on my own.{/i}"
            jump chapter2_4q4
            

label chapter2_4q2:
    m "{i}I start day-dreaming as I walk the length of the park.{/i}"
    menu:
        "Feels better.":
            m "{i}I relax into my own thoughts for a bit.{/i}"
            m "{i}Like some sort of dull mental humming.{/i}"
            jump chapter2_4q5
        
        "Feels worse.":
            m "{i}What was I thinking, coming here alone?!{/i}"
            m "{i}I wish she was here with me.{/i}"
            jump chapter2_4q6


label chapter2_4q3:
    m "{i}A-at least, I think I can...{/i}"
    menu:
        "Confront her.":
            m "{i}I don't know if I don't try.{/i}"
            scene bg black with pixellate
            m "{i}I headed home.{/i}"
            m "{i}I was nervous about what I would say when I arrived.{/i}"
            m "{i}It's tough, but I know I have to do it.{/i}"
            jump chapter3_3
        
        "Forget it.":
            m "{i}I-I think I need to think this through a bit more...{/i}"
            scene bg black with pixellate
            m "{i}I sat around a while thinking.{/i}"
            m "{i}There's just too much uncertainty in life.{/i}"
            m "{i}It would be reckless of me to lose the one dependable thing I have.{/i}"
            jump chapter3_2


label chapter2_4q4:
    m "{i}It makes me realise...{/i}"
    menu:
        "...This is unhealthy.":
            m "{i}This is not a healthy way to get by.{/i}"
            m "{i}Whether I like it or not, it has to stop.{/i}"
            m "{i}I cannot stay this stuck forever.{/i}"
            scene bg black with pixellate
            m "{i}I started walking home.{/i}"
            m "{i}Going to tell her we need to end it...{/i}"
            m "{i}...To put an end to this selfishness.{/i}"
            jump chapter3_3
        
        "...I should go back.":
            m "{i}I'm just not myself without her.{/i}"
            m "{i}I can't feel connected to anyone else.{/i}"
            scene bg black with pixellate
            m "{i}I had to leave.{/i}"
            m "{i}I went straight back home to apologise.{/i}"
            m "{i}I hate being so weak.{/i}"
            jump chapter3_2


label chapter2_4q5:
    m "{i}There's only one thing on my mind right now...{/i}"
    menu:
        "Leaving her.":
            m "{i}I know that I have to leave her.{/i}"
            m "{i}It scares me though.{/i}"
            scene bg black with pixellate
            m "{i}I walked home.{/i}"
            m "{i}Unsure of what to say, I started rehearsing the conversation in my head.{/i}"
            m "{i}It didn't go well.{/i}"
            jump chapter3_3
        
        "Staying with her.":
            m "{i}I think of how much a part of my life she is.{/i}"
            m "{i}I can't deny that.{/i}"
            scene bg black with pixellate
            m "{i}I walked home, intending to apologise.{/i}"
            m "{i}Maybe it's not a smart decision...{/i}"
            m "{i}...but it's the one I've stuck with time and time again.{/i}"
            jump chapter3_2
    
    
label chapter2_4q6:
    show l surprised
    l "..!"
    show l happy
    l "Hello."
    m "{i}Huh, how long was she there?{/i}"
    "Hey."
    show l playful
    l "I had the feeling you needed something."
    "Hmm."
    menu:
        "I need her.":
            "Nothing important!"
            show l happy
            l "Oh."
            "I'm just glad you're here."
            scene bg black with pixellate
            m "{i}We walked home together.{/i}"
            m "{i}I felt a little ashamed that I always give in to her...{/i}"
            m "{i}...But also glad that she could help me feel more comfortable.{/i}"
            jump chapter3_2
        
        "We need to talk.":
            "We need to talk."
            show l sad
            l "..."
            show l upset
            l "That's never good."
            scene bg black with pixellate
            m "{i}Rather than confront her in public, we walked home.{/i}"
            m "{i}We were awkwardly silent the whole way.{/i}"
            m "{i}I wondered if she already knew what I was going to say.{/i}"
            jump chapter3_3
    
    

label chapter3_1:
#This is the final part of get the girl. The dilemma is crisis of personality.
    scene bg house with pixellate
    m "{i}It was the day after our anniversary.{/i}"
    m "{i}I was feeling some sort of nervous excitement.{/i}"
    m "{i}It was hard to stop my hands shaking.{/i}"
    show l happy
    l "..?"
    l "What are you thinking?"
    "Uh..."
    menu:
        "Thinking about us.":
            "I was just thinking about us."
            show l playful
            l "Really? Haha."
            jump chapter3_1q1
        
        "...Just thinking.":
            "Just... Nothing."
            show l playful
            l "Hmm... I'm not so sure."
            jump chapter3_1q2
            

label chapter3_1q1:
    "Yeah."
    show l happyanim
    l "Cute."
    m "{i}Huh?{/i}"
    m "{i}Am I seeing things?!{/i}"
    show l happy
    m "{i}For a second there, it looked like...{/i}"
    menu:
        "Get closer.":
            m "{i}It's nothing, I'm sure.{/i}"
            jump chapter3_1q3
        
        "Wait.":
            m "{i}...{/i}"
            show l sad
            l "Is something wrong?"
            jump chapter3_1q4
    
label chapter3_1q2:
    m "{i}...!{/i}"
    show l happy
    l "Come on, you can tell me anything!"
    m "{i}Really?{/i}"
    "Ah, I just worry."
    show l sadanim
    l "About what?"
    menu:
        "Being stuck.":
            "I sometimes think that I'm stuck here."
            show l upset
            l "Oh."
            jump chapter3_1q5
        
        "What was that?":
            "Did you see that?"
            show l surprised
            l "Huh?"
            jump chapter3_1q6

    
    
label chapter3_1q3:
    show l happyanim
    l "Well..?"
    "I've been thinking, that we should..."
    m "{i}This again.{/i}"
    show l happy
    "I think we need to be closer."
    "There's so much more I want to know about you..."
    show l playfulanim
    l "Really? You mean it?"
    menu:
        "Yes.":
            "Yes, I'm sure."
            m "{i}I knew it, that I couldn't get by without her.{/i}"
            m "{i}Without her, it's like something important is missing from me.{/i}"
            scene bg black with pixellate
            m "{i}That night we were closer than we'd ever been.{/i}"
            m "{i}I felt relief, now that I'd finally done it.{/i}"
            jump finale1
        
        "Wait, what was that?":
            "H-hold on..."
            show l surprised
            l "What?"
            "I-I don't know. I don't think this is a good idea."
            show l sad
            l "..."
            show l upset
            l "You changed your mind?"
            "No... it's just..."
            scene bg black with pixellate
            m "{i}I couldn't go through with it.{/i}"
            m "{i}I'm a weak person really.{/i}"
            m "{i}Although, I know it's a bad idea to get closer to her.{/i}"
            m "{i}Because then there's no way back...{/i}"
            jump finale2
    
    
    
    
label chapter3_1q4:
    "N-no."
    show l happyanim
    m "{i}This is too much.{/i}"
    m "{i}There's only one way to stop this feeling.{/i}"
    menu:
        "Get closer.":
            show l surprised
            l "..!"
            "I have to know..."
            show l happy
            l "Mm?"
            "You can help me, right?"
            l "..."
            show l playful
            l "Right."
            scene bg black with pixellate
            m "{i}I knew it.{/i}"
            m "{i}I knew she could make me feel better.{/i}"
            m "{i}From the moment we met, this is what I'd been building up to.{/i}"          
            jump finale1
        
        "Pull back.":
            "I-I can't do this."
            show l sad
            l "What?"
            "I'm sorry. I'm just not sure about anything, still."
            show l upset
            l "Hmm."
            "Let's just... forget it."
            show l sad
            l "..."
            scene bg black with pixellate
            m "{i}I didn't have to ask. I knew she would forgive me.{/i}"
            m "{i}As with every other time, she'll always be there.{/i}"
            m "{i}Always, even though I am too much of a coward to make any real decisions.{/i}"
            jump finale2
    
    
    
label chapter3_1q5:
    show l sad
    l "Well, it's your choice, right? I'm not forcing you to stay."
    "I know."
    m "{i}The more I'm around her, the more stuck I feel.{/i}"
    m "{i}Feels like I'm not in control anymore.{/i}"
    menu:
        "I don't need control...":
            show l sadanim
            m "{i}Maybe I don't need to be in control of everything.{/i}"
            m "{i}Maybe giving in to her will help.{/i}"
            m "{i}Maybe I don't want to fight it anymore.{/i}"
            scene bg black with pixellate
            m "{i}Finally...{/i}"
            m "{i}I gave in to her.{/i}"
            m "{i}But it was my decision to stop resisting her.{/i}"
            jump finale1

        "I need to change.":
            m "{i}I can't give up.{/i}"
            m "{i}I'll only end up resenting her.{/i}"
            m "{i}Maybe I'll change... one day.{/i}"
            scene bg black with pixellate
            m "{i}I thought I could leave her.{/i}"
            m "{i}I told myself I would, eventually, when I was stronger...{/i}"
            m "{i}...But in the end...{/i}"
            jump finale2
        
        
label chapter3_1q6:
    show l sad
    l "See what?"
    m "{i}Oh, it's gone now.{/i}"
    "For a second there..."
    menu:
        "There was something weird.":
            "I saw something weird."
            show l happy
            l "Heh, are you tired or something?"
            "No, I don't feel tired."
            l "Well, maybe just relax anyway."
            "..."
            "Fine, fine."
            scene bg black with pixellate
            m "{i}We spent the rest of the day talking about nothing important.{/i}"
            m "{i}I can never talk about anything important, especially when it comes to her.{/i}"
            m "{i}But I think that's something I just have to live with.{/i}"
            jump finale2
        
        "...Never mind.":
            "Never mind, ignore me."
            show l happy
            l "Heh, you're being odd."
            "...Sorry."
            l "Tsk, no need to apologise."
            "..."
            l "But you don't have to keep everything to yourself."
            "...Thanks."
            m "{i}I can't tell her how much I need her...{/i}"
            scene bg black with pixellate
            m "{i}Does she just pity me?{/i}"
            m "{i}Maybe that's why I can't get closer to her.{/i}"
            m "{i}...I wonder what it's like.{/i}"
            jump finale2
    
    
    

label chapter3_2:
#This is the final part of the average route. The dilemma is entropy.

    scene bg house with pixellate
    show l bored
    m "{i}It was the day after our anniversary.{/i}"
    show l boredanim
    m "{i}I had a dull sense of pressure in my head.{/i}"
    m "{i}It felt like I was surrounded.{/i}"
    menu:
        "Hey...":
            "Uh, hey."
            show l happy
            l "Mm?"
            "I was thinking..."
            jump chapter3_2q1
        
        "...":
            "..."
            m "{i}This isn't right.{/i}"
            jump chapter3_2q2
            
label chapter3_2q1:
    show l playful
    l "...For a change!"
    "Haha..."
    "Are you happy?"
    show l happy
    l "Sure, I'm OK."
    show l sadanim
    l "Are you not happy?"
    "No, I am. Just..."
    menu:
        "I want us to be closer.":
            "I think we could be closer than we are."
            show l bored
            l "Hmm. I guess so."
            show l happy
            l "I always left it up to you."
            l "If you're sure that's what you want..."
            jump chapter3_2q3
        
        
        "I was just checking.":
            "I was just making sure."
            show l happy
            l "Heheh."
            l "I know."
            jump chapter3_2q4
            
    
    
label chapter3_2q2:
    m "{i}I shouldn't feel this irritated.{/i}"
    m "{i}I need to...{/i}"
    menu:
        "Stop thinking.":
            m "{i}Stop thinking about it.{/i}"
            m "{i}I need to do something.{/i}"
            jump chapter3_2q5
        
        "Keep thinking.":
            m "{i}I have to focus. Have to tell her.{/i}"
            "Hey..."
            show l happy
            l "Mm?"
            jump chapter3_2q6



label chapter3_2q3:
    show l happyanim
    "I-I'm..."
    menu:
        "I'm sure.":
            "Yes, I'm sure of it."
            show l playfulanim
            l "..."
            l "Hold still."
            scene bg black with pixellate
            m "{i}I couldn't stand it anymore.{/i}"
            m "{i}I didn't want to stay the same forever.{/i}"
            m "{i}I wanted to make a decision, even if it was a reckless one.{/i}"
            jump finale1
        
        "W-wait...":
            "..."
            show l sadanim
            l "..?"
            show l upset
            l "I knew it."
            l "It's fine. Never mind."
            scene bg black with pixellate
            m "{i}Something stopped me.{/i}"
            m "{i}I think I'm still afraid.{/i}"
            m "{i}I can't trust her, not completely.{/i}"
            jump finale2


label chapter3_2q4:
    show l playfulanim
    l "I can't help you with this decision."
    l "You have to make it."
    show l playful
    "Uhm..."
    menu:
        "I'll just see what happens.":
            "I'm fine just seeing what happens."
            show l sad
            l "Really?"
            "Yes. I think so."
            scene bg black with pixellate
            m "{i}Of course I was too scared.{/i}"
            m "{i}I knew what I'd be getting myself into.{/i}"
            m "{i}I was too afraid to take any risks.{/i}"
            jump finale2
        
        "Take control.":
            "Then..."
            "I want to be closer to you."
            show l happyanim
            l "..."
            l "Then..."
            scene bg black with pixellate
            m "{i}I know it was a reckless decision.{/i}"
            m "{i}I know she's not good for me.{/i}"
            m "{i}I had to know what it felt like.{/i}"
            jump finale1


label chapter3_2q5:
    "Hey."
    show l happy
    l "Yes?"
    "I..."
    menu:
        "Am happy.":
            "...Want you to promise."
            l "What?"
            "You'll always be here."
            show l playful
            l "You know I will."
            "..."
            "...Of course."
            scene bg black with pixellate
            m "{i}It's a relief that nothing changes.{/i}"
            m "{i}I can cope if everything is the same.{/i}"
            m "{i}I don't have to worry about losing her, or losing myself.{/i}"
            jump finale2
        
        "Need to be alone.":
            "I need you to leave."
            show l surprised
            l "!!!"
            show l sad
            l "That's..."
            show l upset
            l "...Not surprising."
            "..."
            l "It's OK."
            show l sad
            l "Maybe one day you'll need me again."
            scene bg black with pixellate
            m "{i}I hope she's wrong.{/i}"
            m "{i}But I know I'll still think of her.{/i}"
            m "{i}I can't help but be reminded by the marks she left.{/i}"
            jump finale3



label chapter3_2q6:
    "I'm not happy with... this anymore."
    show l sad
    l "Oh."
    show l annoyed
    l "What do you want me to do?"
    "I don't know."
    "..."
    "I think I'd prefer to be alone."
    l "Hmm."
    show l cynical
    l "Do you really think you can cope alone?"
    menu:
        "Yes.":
            "Yes."
            "I want to try, anyway."
            show l sad
            l "..."
            l "You know, I can come back anytime."
            "Yes."
            show l cynical
            l "I don't think you'll be OK, but..."
            "I will."
            show l sad
            l "..."
            scene bg black with pixellate
            m "{i}She complained a lot.{/i}"
            m "{i}I didn't give in to her.{/i}"
            m "{i}For the first time in a long while, my head started to clear.{/i}"
            jump finale3
        
        "No.":
            "...No. You're right."
            show l happy
            l "Heh."
            show l playful
            l "I'm sorry."
            "No, I know you're right."
            "I'm just sorry for doubting you."
            scene bg black with pixellate
            m "{i}She'll always look out for me.{/i}"
            m "{i}Familiar and frightening at the same time.{/i}"
            m "{i}But never as frightening as being alone would be.{/i}"
            jump finale2
            

label chapter3_3:
#This is the final part of lose the girl. The dilemma is crisis of personality.

    scene bg house with pixellate
    show l sad
    l "..."
    "We need to talk."
    show l upset
    l "T-that's never good."
    l "Can't we just carry on as always?"
    show l sad
    l "It's alright, isn't it?"
    menu:
        "No.":
            "No."
            "Sorry, I can't do this anymore."
            show l cynical
            l "Heh."
            jump chapter3_3q1
        
        "...Maybe.":
            "Maybe."
            show l happy
            l "Good."
            show l sad
            l "What's upset you anyway?"
            jump chapter3_3q2

            
label chapter3_3q1:
    show l annoyedanim
    l "I don't believe you."
    "..."
    l "I know you."
    l "You're useless without me."
    show l angryanim
    l "Just empty, boring, like everyone else."
    "..."
    menu:
        "I've made up my mind.":
            "I've made up my mind."
            show l cynical
            l "Hahaha!"
            jump chapter3_3q3
        
        "H-how dare you!":
            "W-what!"
            show l cynical
            l "Heh."
            jump chapter3_3q4


label chapter3_3q2:
    m "{i}Urgh, do I have to tell her?{/i}"
    "Well..."
    menu:
        "I'm not happy.":
            "Lately I've not been feeling so happy about things."
            show l surprised
            l "Things?"
            "Well, us, I mean."
            show l sad
            l "..."
            jump chapter3_3q5
        
        "Forget it.":
            "Forget it."
            show l sad
            l "..."
            show l annoyed
            l "No."
            jump chapter3_3q6


label chapter3_3q3:
    show l cynicalanim
    l "I doubt it."
    l "You're too scared."
    l "Without me around, you can't do anything."
    show l annoyed
    l "Who else is going to help you? No one."
    menu:
        "Make her leave.":
            "I don't care. You have to go."
            show l angry
            l "..."
            show l upset
            "..."
            l "No one can help you... Not as much as I can."
            "..."
            "You have to go."
            scene bg black with pixellate
            m "{i}Part of me agreed with her, with all those things she said.{/i}"
            m "{i}Of course...{/i}"
            m "{i}I knew I couldn't let myself believe her anymore.{/i}"
            jump finale3
        
        "Wait for her to stop.":
            "..."
            show l cynical
            l "No one will help, because you're alone."
            show l annoyed
            l "No one else can understand you."
            "...Because of you."
            l "Yes."
            show l cynical
            l "You'd rather have me, though, than anyone else."
            "No, actually, not anymore."
            show l upset
            l "..."
            "I used to think I would... but I'm not so sure anymore."
            scene bg black with pixellate
            m "{i}Listening to her talk just gave me more resolve.{/i}"
            m "{i}I'd heard it so many times, it sounded hollow now.{/i}"
            m "{i}I'd finally gathered the strength to disagree with her.{/i}"
            jump finale3
    


label chapter3_3q4:
    show l cynicalanim
    l "You don't want to be like everyone else, right?"
    l "They can't possibly understand you."
    show l annoyed
    l "And if they find out about me, they'll hate you for sure."
    "..."
    show l cynicalanim
    l "You've heard what they say, haven't you?"
    menu:
        "Yes...":
            "Yes. I don't care."
            "I'm more than that, and more than you."
            show l annoyed
            l "...You think?"
            "...I hope so."
            show l cynical
            l "Heheh."
            l "Give it a year, or two. You'll see that it's not so great without me."
            "..."
            scene bg black with pixellate
            m "{i}I hoped she was wrong.{/i}"
            m "{i}Somewhere deep inside I agreed with her, so I hoped I was wrong too.{/i}"
            m "{i}I decided to give life without her a try.{/i}"
            jump finale3
        
        "Shut up!":
            "S-shut up!"
            show l angry
            l "No!"
            l "What will you do when you realise they hate you?"
            l "If I'm not around, who's going to make all that not matter."
            show l annoyed
            l "You know I'm what makes you yourself."
            "..."
            "I know."
            "I... hate that."
            show l upset
            l "It doesn't have to be bad."
            show l sad
            l "Please?"
            "..."
            scene bg black with pixellate
            m "{i}I gave in.{/i}"
            m "{i}She's right. My entire personality is built around her.{/i}"
            m "{i}If I lose her, I might find there's nothing of me left.{/i}"
            jump finale2
    


label chapter3_3q5:
    show l upset
    l "Why?"
    "I... I just don't know that it's right anymore."
    show l sad
    l "Oh."
    menu:
        "Ask her to leave.":
            "I'm sorry."
            "I just need to see what it's like to be by myself."
            l "Hmm."
            "...I'm glad that I met you though."
            show l upset
            l "..."
            scene bg black with pixellate
            m "{i}I had no regrets, in the end, for anything I did.{/i}"
            m "{i}I felt that things had come to their natural end.{/i}"
            m "{i}I hope she realises that too.{/i}"
            jump finale3
            
        
        "Apologise.":
            "Sorry."
            l "..."
            show l upset
            l "Aren't things alright as they are?"
            "Well..."
            show l sad
            l "It's just a bad patch. You don't have to decide now."
            show l happy
            l "Give it a little while. I'm sure things will get better."
            "..."
            scene bg black with pixellate
            m "{i}I let her persuade me.{/i}"
            m "{i}And she was right. I changed my mind a while later.{/i}"
            m "{i}She knows me too well...{/i}"
            jump finale2

label chapter3_3q6:
    show l sad
    l "You can't just tell me to ignore you."
    "..."
    menu:
        "Fine.":
            "Fine. I'm not happy with how things are."
            "I want you to leave."
            show l upset
            l "..."
            show l annoyed
            l "I refuse."
            l "You still need me around, clearly."
            "What?"
            l "It took me dragging it out of you for you to recognise that you're not happy."
            show l sad
            l "And think about it, do you really want to be alone and unhappy?"
            "..."
            show l happy
            l "I can help you not feel alone anymore."
            show l playful
            l "...If you let me."
            scene bg black with pixellate
            m "{i}Of course, I let her do whatever she wanted.{/i}"
            m "{i}I'm powerless to stop her.{/i}"
            m "{i}Just too pathetic to live without her.{/i}"
            jump finale2
        
        "...":
            "...Seriously, it's nothing."
            show l sad
            l "Hmm..."
            show l upset
            l "I know it's not nothing, but if you don't want to talk about it..."
            l "...There's pretty much nothing I can do."
            "..."
            show l sad
            l "I wish you would let me help you."
            "..."
            scene bg black with pixellate
            m "{i}I wished I could let her help.{/i}"
            m "{i}I wished I didn't want her help too.{/i}"
            m "{i}I wished I had never met her, because now I was stuck with her.{/i}"
            jump finale2

label finale1:
#This is the bad ending
    m "{i}I know I made the right decision.{/i}"
    scene bg hosp with pixellate
    show nurse at right
    nurse "You're lucky this time."
    "..."
    nurse "You didn't hit any nerves or arteries."
    m "{i}As if I would be that stupid!{/i}"
    "Uh, when can I go home?"
    nurse "You have to wait to see the doctor in the morning, and we'll see then."
    "Right..."
    nurse "Do you feel better now?"
    "...Yes."
    nurse "So why did you do it?"
    "..."
    scene bg black with pixellate
    m "{i}Of course, it was no problem to talk my way out of the hospital.{/i}"
    m "{i}It was easy, because I honestly never felt so good.{/i}"
    m "{i}I felt complete. I should never have doubted that I needed her.{/i}"
    m "{i}At the end of the day, my flaws are as defining as my good qualities.{/i}"
    m "{i}I need her to carry on being myself. To sustain my personality.{/i}"
    m "{i}I need her to be happy.{/i}"
    jump end

label finale2:
#This is the average ending
    m "{i}I think I made the right decision...{/i}"
    scene bg house with pixellate
    show l boredanim
    m "{i}I think we can stay like this forever.{/i}"
    m "{i}Maybe we won't be happy, but I know we won't be sad.{/i}"
    m "{i}When it comes down to it, I'm too scared to be with her, or without her.{/i}"
    m "{i}I can be satisfied with a comfortable life. I don't need any answers or solutions.{/i}"
    m "{i}I think we can stay like this forever...{/i}"
    jump end
    
label finale3:
#This is the good ending
    m "{i}I hope I made the right decision...{/i}"
    scene bg house with pixellate
    m "{i}She was out of my life within a month. I no longer rely on her.{/i}"
    m "{i}I've gained my independence. I'm happy now!{/i}"
    m "{i}The future feels uncertain, but I'm excited to be free.{/i}"
    m "{i}I hope the day will never come when I want to see her again.{/i}"
    jump end


label end:
    stop music fadeout 3.0
    $ renpy.pause(0)
    scene black
    with pixellate

    show end
    with pixellate
    with Pause(2.0)

    scene black
    with pixellate
    with Pause(1.0)

    return




