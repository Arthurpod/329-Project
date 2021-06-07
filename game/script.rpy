# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define kyle = Character("X Æ A-12", who_color="eb2c10", what_color="2890d1")

define grimes = Character ("Mom", who_color="fce840", what_color="878785")

define jeff = Character ("Mr. Bezos", who_color="eb6610", what_color="cecece")

define pepe = Character ("Pepe", who_color="0520bf", what_color="037c10")

define web = Character("", kind = nvl)

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

    

    # This ends the game.

    return
