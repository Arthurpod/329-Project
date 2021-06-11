# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define kyle = Character("X Æ A-12", who_color="eb2c10", what_color="2890d1")

define grimes = Character ("Mom", who_color="fce840", what_color="878785")

define jeff = Character ("Mr. Bezos", who_color="eb6610", what_color="cecece")

define pepe = Character ("Pepe", who_color="0520bf", what_color="037c10")

define web = Character("", kind = nvl)

define poster = Character("", kind = nvl)

define tim = Character("Tim", who_color="fcfcfc", what_color="fcfcfc")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bedroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show kyle base

    # These display lines of dialogue.

    "It’s May 30 2021 and X Æ A-12 Musk just woke up in dad’s $41M mansion."
    "Enter his mother."
    show kyle base at left with move
    show isabelle base at right with move

    grimes "Good morning X Æ A-12. Happy 16th birthday!"

    kyle "Thanks mom! Where is dad?"

    grimes "I'm sorry, darling, your farther is away on a business meeting"
    grimes "He said it was very important, he's going to revolutionize DogeCoin today."
    grimes "But we got you this birthday present!"
    "She hands X Æ A-12 a wrapped box."

    kyle "Thanks mom!"
    "He opens the gift."
    kyle "Wow, a SpacePhone X! I wish dad were here too, but I guess DogeCoin is pretty important."

    grimes "You're welcome sweetheart, I hope you like your new phone! Why don't you turn it on and set up your account?"
    hide isabelle base

    "X Æ A-12 turns on his new SpacePhone X and is prompted to log in or create a new SpaceNet account to access his phone with."
    "After entering the username MarsmanKyle, X Æ A-12 needs to enter a password."
    kyle "Alright, I've narrowed it down to 4 passwords, now I just need to figure out which one is best"
    "A good password is longer than 8 characters, has upper case and lowercase letters, has a few numbers and symbols, and is easy to remember."
    "Here are some links that can help you learn about how to make better passwords \n{a=https://password.kaspersky.com}Kaspersky Password Strength Checker{/a} \n{a=https://support.kaspersky.com/common/windows/3730}Kaspersky Strong Password Guidelines{/a}"

    menu:
        "Password1":
            jump q1a1
        "P@55w0rd":
            jump q1a2
        "mKxA3a12!":
            jump q1a3
        "Musky@Melon05":
            jump q1a4

    label q1a1:
        $ q1 = 1
        kyle "This password is the easiest to remember, i'll use that one."
        jump q1_done

    label q1a2:
        $ q1 = 2
        kyle "This password seems easy to remember, and is probably pretty secure because of all these symbols and numbers."
        jump q1_done

    label q1a3:
        $ q1 = 3
        kyle "This password is almost gibberish, I bet it's super secure, I better not forget it."
        jump q1_done

    label q1a4:
        $ q1 = 4
        kyle "This password is easy to remember and follows all the rules of creating a good password."
        jump q1_done

    label q1_done:

    "Next X Æ A-12 needs to set up a password to unlock his SpacePhone X."
    kyle "I can use a PIN, a password, or... {w} Wow! I can use gestures and pictures to unlock my phone."
    kyle "It even has a fingerprint scanner. I wonder which I should use."
    "A PIN is a 4 digit code that X Æ A-12 needs to type into his phone to unlock it.{p}A password is like a PIN, except that it can be longer than 4 characters, and may include numbers, letters, or symbols."
    "When using gestures or pictures to unlock the phone, X Æ A-12 will be shown a picture of his choice, or a grid of 9 dots, and he will have to trace a pattern with his finger."
    "Fingerprint scanning is the simplest unlocking method, it allows X Æ A-12 to place a chosen finger on the scanner and his phone will unlock after sensing the correct finger."

    menu:
        "PIN":
            jump q2a1
        "Password":
            jump q2a2
        "Gesture or Picture":
            jump q2a3
        "Fingerprint":
            jump q2a4

    label q2a1:
        $ q2 = 1
        kyle "It won't be hard to remember a 4 digit code."
        jump q2_done

    label q2a2:
        $ q2 = 2
        kyle "Another password would be pretty secure, I could just use the same password as my SpaceNet account, but that wouldn't be very wise."
        jump q2_done

    label q2a3:
        $ q2 = 3
        kyle "A gesture will be easy to remember, but ."
        jump q2_done

    label q2a4:
        $ q2 = 4
        kyle "This password is easy to remember and follows all the rules of creating a good password."
        jump q2_done

    label q2_done:

    kyle "It's getting late, I should probably get to bed now"

    scene bg black with dissolve

    "The next day, X Æ A-12 goes to his school, Harambee High."

    scene bg classroom with dissolve

    jeff "Good morning class. Before we start today's lesson I want everyone to log in to their Harambee high CBE accounts."
    jeff "Our School's IT staff just implemented a new security protocol that requires all students to log in to their accounts with two-factor authentication."
    jeff "What this means is when you log in to your account on the school websites, you will have to input a code as well as your username and password. The code will come from an app on your phone which you will connect to your account."

    show pepe base at right
    pepe "Why are we doing this Mr. Bezos? This is just a big inconvenience!"

    jeff "Because this way, Pepe, even if someone has managed to get your ID and password,{p}they still can't log in to your school account."
    jeff "They don't have access to your phone, so they won't be able to get a code from the authenticator app which is required to log in."
    jeff "This will help protect our system from cybercriminals."

    pepe "I get it now, it's like an extra layer of difficulty that cybercriminals will have to deal with."

    jeff "Exactly."

    hide pepe base

    "X Æ A-12 opens up his SpaceBook Pro and opens up the Tesla browser to log in. The website shows a screen reading:"

    web "Welcome to Harambe High CBE Account Prefences.\nYou will be adding 2FA to your Harambe High CBE account. Please take the following steps:"
    web "1. Download the SpaceNet Authenticator app to begin."
    web "2. Scan this QR code using the app to connect the authenticator to your account."
    web "3. The authenticator will give you a code now. Input the code in the textbox below."
    nvl hide

    "After successfully logging in with 2FA enabled, X Æ A-12 opens up his email and finds he has three unread emails. X Æ A-12 remembers that last week Mr. Bezos discussed the importance of email safety and determining if an email is phishing."

    kyle "I remember what Mr. Bezos told us last week, phishing emails usually come from weird email addresses and usually have links to suspicious URLs in them."
    "Phishing emails pretend to be from a legitimate source, such as google, or your bank. They try to trick into thinking that you need to log in, but they provide a fake URL that will steal your info if you try to log in, or will download malware to your device."
    "You can test out this knowledge in Google's {a=https://phishingquiz.withgoogle.com/}phishing email quiz{/q}."

    show email phishing1:
        xalign 0.5
        yalign 0.0
    "Is this a phishing email?"
    menu:
        "Yes.":
            jump phishing1_yes
        "No.":
            jump phishing1_no

    label phishing1_yes:
        $ phishing1 = 1
        kyle "This email is a scam, the link uses a fake URL that isn't actually used by google."
        jump phishing1_done

    label phishing1_no:
        $ phishing1 = 0
        kyle "Hmm, I don't know anyone named Luke, but I wonder what's in that doc! I'll look at it when I get home."
        jump phishing1_done

    label phishing1_done:

    show email phishing2:
        xalign 0.5
        yalign 0.0
    "Is this a phishing email?"
    menu:
        "Yes.":
            jump phishing2_yes
        "No.":
            jump phishing2_no

    label phishing2_yes:
        $ phishing2 = 1
        kyle "This email is obviously a scam, the URL contains a weird domain, and they didn't even spell fax right in the email address!"
        jump phishing2_done

    label phishing2_no:
        $ phishing2 = 0
        kyle "Ooh, I wonder who sent me a fax, I can't use the school printers for non-school reasons so I'll save this for when I get home."
        jump phishing2_done

    label phishing2_done:

    show email phishing3:
        xalign 0.5
        yalign 0.0
    "Is this a phishing email?"
    menu:
        "Yes.":
            jump phishing3_yes
        "No.":
            jump phishing3_no

    label phishing3_yes:
        $ phishing3 = 1
        kyle "What a weird email address, this URL links to a website called sytez.net, I think this is another scam."
        jump phishing3_done

    label phishing3_no:
        $ phishing3 = 0
        kyle "Wow, who could this be? I can't wait to see this photo when I get home."
        jump phishing3_done

    label phishing3_done:

    show email legit1:
        xalign 0.5
        yalign 0.0
    "Is this a phishing email?"
    menu:
        "Yes.":
            jump phishing4_yes
        "No.":
            jump phishing4_no

    label phishing4_yes:
        $ phishing4 = 1
        kyle "This one might be a scam as well, i'm not sure if dropboxmail.com is the address that Dropbox sends emails from."
        jump phishing4_done

    label phishing4_no:
        $ phishing4 = 0
        kyle "This email is legitimate. All the links lead to dropbox.com and the email address is also the correct address used by Dropbox."
        jump phishing4_done

    label phishing4_done:

    scene bg classroom

    "*Ding dong* class is over and it's now time for lunch"

    kyle "Hey Tim, do you wanna grab Subway for lunch?"

    tim "Sure! I'm starving."

    scene bg tosubway

    tim "Hey have you thought about working this summer? Maybe your dad could give you a job."

    kyle "Oh no I haven't really thought about it."

    "X Æ A-12 and Tim pass a bus stop with a poster"

    show qr poster:
        xalign 0.5
        yalign 0.5

    tim "Yo, look at this poster! Didn’t you turn 16 today? Happy birthday by the way. But hey, you should apply to this. Just scan the code with your new phone."

    kyle "Thanks! Yeah okay, I wonder what type of job this is. It doesn’t say much on the poster."

    "X Æ A-12 scans the QR code and a URL opens up"

    kyle "I can't lie this is giving me serious sus vibes. Looks like they spelt 'experience' and 'eligibility' wrong and there's no description of the job."

    tim "Really? You seemed like you really wanted some money for a new Xbox series X."

    "Click the link?"
    menu:
        "Yes.":
            jump qrlink_yes
        "No.":
            jump qrlink_no

    label qrlink_yes:
        $ qrlink = 1
        "As X Æ A-12’s phone searches for the URL, his browser closes itself automatically, then it just freezes"
        kyle "What’s going on, my phone is frozen! I can’t do anything."
        tim "Wait for sometime bro, hopefully it gets back to normal."
        kyle "RATS!!!!! All my apps, pictures are deleted, it’s even asking me to sign in to my SpaceNet account again! Aw man, I shouldn’t have followed that URL!"
        "X Æ A-12 rips the sign down and throws it in the trash, so that nobody else gets tricked by this suspicious QR code."
        jump qrlink_done

    label qrlink_no:
        $ qrlink = 0
        kyle "This link is probably a virus. It doesn’t even use a common domain like .ca, .net, or .org. I’m not clicking this link."
        jump qrlink_done

    label qrlink_done:

    scene bg tosubway

    scene bg black with dissolve

    "X Æ A-12 returns to class after lunch"

    scene bg classroom with dissolve

    jeff "Alright, class. We’re going to run through a research assignment. I’m going to need everyone to download MichaelScott Word. Open up your laptops and search ‘MichaelScott Word download’ in SpaceNet and click the first link."

    "X Æ A-12 searches for MichaelScott Word download and clicks the first link. An execution downloads and he opens it. The file asks,
    “Which folder location would you like to save this application to?”"

    menu:
        "/harambee/admin/…":
            jump folder1
        "/harambee/students/XÆA-12/":
            jump folder2
        "/harambee/Program Files/…":
            jump folder1
        "/harambee/MSWin/…":
            jump folder1

    label folder1:
        $ folder = 1
        "USER VIOLATION ERROR: User does not have permission to write to this folder"
        jeff "Class, make sure you select the proper folder. Remember some folders don’t give full read, write, and execute permissions. For example, the /harambee/admin/ folder only gives read permissions to all students. Your specific folder however gives you full permission rights."
        jeff "Meaning you can read, write and execute all files in your own folder."

    label folder2:
        $ folder = 2
        "Software download complete, run MichaelScott Word?"
        jeff "Mr. Bezos says, “Class, make sure you select the proper folder."
        jeff "Remember some folders don’t give full read, write, and execute permissions. For example, the /harambee/admin/ folder only gives read permissions to all students. Your specific folder however gives you full permission rights."
        jeff "Meaning you can read, write and execute all files in your own folder."

    jeff "Alright students, you’re going to be researching how crypto works and writing about it in…"

    "*Ding dong* Class is done for today"

    kyle "Alright! Finally time to go home."

    scene bg outside

    "On the way home, X Æ A-12 finds a USB stick on the sidewalk"

    kyle "Sweet! Free USB drive. This thing is 128GB, sick!"

    menu:
        "Pick it up":
            jump usb1
        "Leave it behind":
            jump usb2

    label usb1:
        $ usb = 1
        "X Æ A-12 plugs in the usb on his SpaceBook Pro at home, and now a suspicious file is installed on his PC. Apparently it was a virus"
        jump usbdone

    label usb2:
        $ usb = 2
        "But it might have been a virus or something on it. Someone wouldn’t just drop a USB stick that big. I’ll just ignore it"
        jump usbdone

    label usbdone:

    show bg black with dissolve
    "The next day"

    show bg classroom

    jeff "Good morning class! Today I want to teach you how to encrypt messages."
    jeff "Have any of you seen the Martian? Do you remember the scene where Matt Damon’s character communicates with NASA using ASCII symbols. We are going to do the same by converting your names to binary."
    jeff "I want you to convert your name into binary. Each letter is eight bits (either a 0 or 1)"
    jeff "X Æ A-12, you can just spell “KYLE” for simplicity."

    kyle "Thanks Mr. Bezos."

    show ascii:
        xalign 0.5
        yalign 0.0

    "Spell KYLE in binary"

    label ascii_tryagain:

    menu:
        "01000101 01011001 01011010 01001001":
            jump ascii1
        "01001011 01011001 01001100 01000101":
            jump asciidone
        "10010101 10101111 00010101 11101010":
            jump ascii1
        "01010100 01000001 01000011 01001111":
            jump ascii1

    label ascii1:
        "That answer is incorrect"
        jump ascii_tryagain

    label asciidone:

    jeff "Well done class! You’ve completed your introduction to ASCII characters. Now, we are going to take a step further and add an element of encryption."
    jeff "To do this we will use the following the key: 01001011"
    jeff "Now, at each position of a letter, convert the bit using an XOR gate. The logic gate looks like the following:"

    show xor:
        xalign 0.5
        yalign 0.0

    "Insert Question Here"

    hide ascii
    hide xor

    jeff "Well done class! You’ve completed your introduction to ASCII characters. Now, we are going to take a step further and add an element of encryption."

    show bg black with dissolve

    show bg home

    "After school, X Æ A-12 goes home and decides to work o his homework. While trying to learn how to solve an algebra problem from a math website, X Æ A-12 gets a pop up ad."

    show popup

    "Should X Æ A-12 click on the prize and follow instructions?"

    menu:
        "Yes":
            jump popup1
        "No":
            jump popup2

    label popup1:
        $ popup = 1
        "The pop up ad was a scam and a potentially unwanted application PUA is downloaded on Kyle’s laptop"
        kyle "What the heck did just happen. An application is installed? Wasn’t it supposed to give away a prize?"
        "The application could now possess a threat of losing the sensitive private information and identity theft on Kyle’s laptop "
        jump popupdone

    label popup2:
        $ popup = 2
        "X Æ A-12 does not click on the prize button"
        kyle "I think I should not click on the prize choose button as it seems fishy that I made the 5-billionth search on the Tesla browser."
        kyle "Also it appears weird that this math website is notifying me about my searches rather than the browser itself."
        kyle "Aha! seems suspicious and yes I remember last month Mr. Bezos informed the class to not click on any links and ads which promise unbelievable and impractical benefits/gifts, since they can be a scam."
        jump popupdone

    label popupdone:

    kyle "Hmmm! This could be a great save from a spam. Well, what should I do to avoid such pop up ads which seem to be a scam, so that my PC should not be at a risk?"

    "What should X Æ A-12 do to avoid pop up ad scams and the installation of unwanted applications on his PC?"

    #menu:
    #    "Do not click on suspicious and untrustworthy links and deceptive websites."
    #    "Enable adblock to block pop-ups when the suspicious ads are noticed."
    #    "Regularly monitor the applications installed on your computer."
    #    "Enable Anti-malware and Anti-virus software to check for malware."



    # This ends the game.

    return
