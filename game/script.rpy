# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define kyle = Character("Kyle", who_color="eb2c10", what_color="2890d1")

define grimes = Character ("Mom", who_color="fce840", what_color="878785")

define jeff = Character ("Mr. Bezos", who_color="eb6610", what_color="cecece")

### define pepe = Character ("Pepe", who_color="0520bf", what_color="037c10")

define web = Character("", kind = nvl)

define poster = Character("", kind = nvl)

define alice = Character("Alice", who_color="ff7326", what_color="008DC7")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bedroom

    play music "audio/bday.mp3"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    ### show kyle base

    # These display lines of dialogue.

    "It’s May 30 2021 and Kyle Musk just woke up in dad’s $41M mansion."
    "Enter his mother."
    ### show kyle base at left with move
    show mom

    grimes "Good morning Kyle. Happy 16th birthday!"

    kyle "Thanks mom! Where is dad?"

    hide mom
    show mom talk
    grimes "I'm sorry, darling, your father is away on a business meeting"

    hide mom talk
    show mom talk2
    grimes "He said it was very important, he's going to revolutionize DogeCoin today."

    hide mom talk2
    show mom happy
    grimes "But we got you this birthday present!"
    "She hands Kyle a wrapped box."

    kyle "Thanks mom!"
    "He opens the gift."
    kyle "Wow, a SpacePhone X! I wish dad were here too, but I guess DogeCoin is pretty important."

    hide mom happy
    show mom
    grimes "You're welcome sweetheart, I hope you like your new phone! Why don't you turn it on and set up your account?"
    hide mom
    hide kyle base

    play sound "audio/Samsung_Startup_Sound.mp3"
    "Kyle turns on his new SpacePhone X and is prompted to log in or create a new SpaceNet account to access his phone with."
    "After entering the username MarsmanKyle, Kyle needs to enter a password."
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

    "Next Kyle needs to set up a password to unlock his SpacePhone X."
    "There are four basic ways of authenticating a user."
    "1, Something the user knows like a password or the answer to a security question.{p}2, Something the user has like a credit card or key"
    "3, Physical characteristics of the user, such as fingerprint or voice pattern.{p}4, Something about the user’s context, their location, the time, devices in proximity."
    "Cell phones often use physical characteristics or something the user knows, to authenticate."

    kyle "I can use a PIN, a password, or... {w} Wow! I can use gestures and pictures to unlock my phone."
    kyle "It even has a fingerprint scanner. I wonder which I should use."
    "A PIN is a 4 digit code that Kyle needs to type into his phone to unlock it.{p}A password is like a PIN, except that it can be longer than 4 characters, and may include numbers, letters, or symbols."
    "When using gestures or pictures to unlock the phone, Kyle will be shown a picture of his choice, or a grid of 9 dots, and he will have to trace a pattern with his finger."
    "Fingerprint scanning is the simplest unlocking method, it allows Kyle to place a chosen finger on the scanner and his phone will unlock after sensing the correct finger."

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
        kyle "A gesture will be easy to remember, but if someone looks over my shoulder, they'll know it and remember it. I better be careful where I unlock my phone."
        jump q2_done

    label q2a4:
        $ q2 = 4
        kyle "I won't need to remember anything if I use a fingerprint to unlock my phone. Nobody else but me will be able to unlock it, this is perfect!"
        "Kyle taps his finger on the scanner a few times until the phone recognizes his fingerprint."
        jump q2_done

    label q2_done:

    kyle "It's getting late, I should probably get to bed now"

    scene bg black with dissolve
    stop music fadeout 1.0

    "The next day, Kyle goes to his school, Harambee High."

    play music "audio/3.mp3"
    scene bg classroom with dissolve

    show talking2
    jeff "Good morning class. Before we start today's cyber security lesson I want everyone to log in to their Harambee high CBE accounts."
    jeff "Our School's IT staff just implemented a new security protocol that requires all students to log in to their accounts with two-factor authentication."
    jeff "What this means is when you log in to your account on the school websites, you will have to input a code as well as your username and password. The code will come from an app on your phone which you will connect to your account."

    show alice at right
    alice "Why are we doing this Mr. Bezos? This is just a big inconvenience!"

    hide talking2
    show talking
    jeff "Because this way, Alice, even if someone has managed to get your ID and password,{p}they still can't log in to your school account."
    jeff "They don't have access to your phone, so they won't be able to get a code from the authenticator app which is required to log in."
    jeff "This will help protect our system from cybercriminals."

    hide alice
    show alice enthusiastic at right
    alice "I get it now, it's like an extra layer of difficulty that cybercriminals will have to deal with."

    hide talking
    show teacher
    jeff "Exactly."

    hide alice ethusiastic
    hide teacher
    "Kyle opens up his SpaceBook Pro and opens up the Tesla browser to log in. The website shows a screen reading:"

    web "Welcome to Harambe High CBE Account Prefences.\nYou will be adding 2FA to your Harambe High CBE account. Please take the following steps:"
    web "1. Download the SpaceNet Authenticator app to begin."
    web "2. Scan this QR code using the app to connect the authenticator to your account."
    web "3. The authenticator will give you a code now. Input the code in the textbox below."
    nvl hide

    "After successfully logging in with 2FA enabled, Kyle opens up his email and finds he has three unread emails. Kyle remembers that last week Mr. Bezos discussed the importance of email safety and determining if an email is phishing."

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

    play sound "audio/school-bell-sound.mp3"
    "*Ding dong* class is over and it's now time for lunch"

    kyle "Hey Alice, do you wanna grab Subway for lunch?"

    show alice
    alice "Sure! I'm starving."
    hide alice
    scene bg tosubway

    alice "Hey did you hear about the new Xbox series X coming out?!"

    kyle "Yes! I'm planning to get one but I'm flat out broke right now, and my parent's don't give me an allowance."

    show alice enthusiastic
    alice "Have you thought about working this summer? Maybe your dad could give you a job."
    hide alice enthusiastic

    show alice
    kyle "Oh no I haven't really thought about it. Dad's all business though, so I don't think he'll have a job for me."

    "Kyle and Alice pass a bus stop with a poster"
    hide alice
    show qr poster:
        xalign 0.5
        yalign 0.5

    alice "Yo, look at this poster! Didn’t you turn 16 today? Happy birthday by the way. But hey, you should apply to this. Just scan the code with your new phone."

    kyle "Thanks! Yeah okay, I wonder what type of job this is. It doesn’t say much on the poster."

    "Kyle scans the QR code and a URL opens up"

    kyle "I can't lie this is giving me serious sus vibes. Looks like they spelt 'experience' and 'eligibility' wrong and there's no description of the job."

    alice "Really? You seemed like you really wanted some money for a new Xbox series X."

    "Click the link?"
    menu:
        "Yes.":
            jump qrlink_yes
        "No.":
            jump qrlink_no

    label qrlink_yes:
        $ qrlink = 1
        hide qr poster
        "As Kyle’s phone searches for the URL, his browser closes itself automatically, then it just freezes"
        kyle "What’s going on, my phone is frozen! I can’t do anything."
        show alice hope
        alice "Wait for sometime bro, hopefully it gets back to normal."
        kyle "RATS!!!!! All my apps, and pictures are deleted, it’s even asking me to sign in to my SpaceNet account again! Aw man, I shouldn’t have followed that URL!"
        "Kyle rips the sign down and throws it in the trash, so that nobody else gets tricked by this suspicious QR code."
        hide alice hope
        jump qrlink_done

    label qrlink_no:
        $ qrlink = 0
        kyle "This link is probably a virus. It doesn’t even use a common domain like .ca, .net, or .org. I’m not clicking this link."
        jump qrlink_done

    label qrlink_done:

    scene bg tosubway

    scene bg black with dissolve

    "Kyle returns to class after lunch"

    scene bg classroom with dissolve

    show talking3
    jeff "Alright, class. We’re going to run through a research assignment. I’m going to need everyone to download MichaelScott Word. Open up your laptops and search ‘MichaelScott Word download’ in SpaceNet and click the first link."
    hide talking3

    "Kyle follows instructions. An execution downloads and he opens it. The file asks,"
    "Which folder location would you like to save this application to?"

label foldertry:
    menu:
        "/harambee/admin/…":
            jump folder1
        "/harambee/students/kylemusk/":
            jump folder2
        "/harambee/Program Files/…":
            jump folder1
        "/harambee/MSWin/…":
            jump folder1


    label folder1:
        $ folder = 1
        "USER VIOLATION ERROR: User does not have permission to write to this folder"
        show talking
        jeff "Class, make sure you select the proper folder. Remember some folders don’t give full read, write, and execute permissions. For example, the /harambee/admin/ folder only gives read permissions to all students."
        jeff "Your specific folder however gives you full permission rights. Meaning you can read, write and execute all files in your own folder."
        hide talking
        jump foldertry

    label folder2:
        $ folder = 2
        "Software download complete, run MichaelScott Word?"
        show happy
        jeff "Mr. Bezos says, “Class, make sure you select the proper folder. Remember some folders don’t give full read, write, and execute permissions. For example, the /harambee/admin/ folder only gives"
        jeff "read permissions to all students. Your specific folder however gives you full permission rights. Meaning you can read, write and execute all files in your own folder."
        hide happy

    jeff "Alright students, you’re going to be researching how crypto works and writing about it in…"

    play sound "audio/school-bell-sound.mp3"

    kyle "Alright! Finally time to go home."

    kyle "Hey Alice do you want to want to go home together?"

    show alice

    alice "Sorry I can't today. I've got club activities with Bob and Eve."

    kyle "Dang ok. Well say hi to Bob for me. I'll see you tomorrow"

    hide alice
    show alice enthusiastic

    alice "For sure, see ya tomorrow Kyle!."

    hide alice enthusiastic

    stop music fadeout 1.0
    scene bg tosubway with dissolve

    play music "audio/1.mp3"
    kyle "Ugh I have so much homework Mr. Besos doesn't have any mercy."

    kyle "I can't believe he also gave us a research project about cryptography."
    kyle "It is kinda cool how the ancient Greeks used it to code their messages though."


    "As he walks home, Kyle finds a USB stick on the  sidewalk"

    show usb:
        xalign 0.5
        yalign 0.5

    kyle "Sweet!"

    menu:
        "Pick it up":
            jump pickUSB
        "Leave it behind":
            jump leaveUSB

    label pickUSB:
        hide usb
        scene bg bedroom with dissolve
        "As soon as he arrives at home, Kyle plugs the USB into his SpaceBook Pro."
        "There is a file on the USB drive."
        menu:
            "Execute it to see what it does.":
                $ usbFlag = 0
                "The laptop screen freezes for a bit, then it shuts off. Kyle can't tell just by looking, but a keylogger virus has installed itself."
                "Keyloggers remember everything you type on your keyboard and send the information to an attacker who will use the data to obtain any passwords you may have typed."
                "Kyle's credit card data could now be stolen if he were to buy something online using a credit card, or his accounts could be stolen."
                jump usb_done
            "Format the USB":
                $ usbFlag = 1
                kyle "This weird file is probably nothing interesting, besides it could be dangerous. I'll reformat the drive so that it will be completely empty."
                "Kyle formats the drive. After waiting a little while, the USB drive is now completely empty and safe to re-use."
                jump usb_done
    label leaveUSB:
        $ usbFlag = 2
        hide usb
        kyle "I don't need a shady ground USB. It may have a virus on it. Why would somebody drop a perfectly good USB that's that big?"
        "Kyle arrives at home."
        scene bg bedroom with dissolve
        jump usb_done

    label usb_done:

    scene bg black with dissolve
    stop music fadeout 1.0

    "Kyle prepares for the next day."

    scene bg classroom with dissolve
    play music "audio/3.mp3"

    show teacher
    jeff "Good morning class! Today I want to teach you how to encrypt messages. Have any of you seen The Martian?"
    hide teacher
    show teacher1
    jeff "In one scene, Matt Damon communicates with NASA using ASCII symbols. We are going to do the same by converting your names to binary."
    hide teacher1
    show teacher
    jeff "Binary uses digits called bits which can either be a 0 or a 1. Each letter in your name will be converted to Hexadecimal or Hex code according to the chart I pass out."
    jeff "Hex numbers can then be convereted into 4 bits each, so every letter in your name will be converted to 8 bits of binary."
    hide teacher
    show talking2
    jeff "You can convert hex to binary manually, or by using a website to calculate your math for you."
    hide talking2

    "The Hex number system is like our decimal system that we use, only there are extra digits A B C D E and F to represent the numbers 10, 11, 12, 13, 14, and 15."
    "In binary there are only the numbers 1 and 0 but which position they are in will tell you which power of 2 they represent."
    "You can convert between Hex and Binary here {a=https://www.rapidtables.com/convert/number/hex-to-binary.html}at this link{/a}."

    show hex chart:
        yalign 0
        xalign 0.5

    kyle "So the uppercase K in my name is 4B in Hexadecimal, which is the number 4 concatenated with the number 11. 4 in binary is 0100 because the third place represents 2^2 which equals 4, and 11 in binary is 1011 because the fourth place represents 2^3 = 8,"
    kyle "and the first and second place represent 2^1 = 2 and 2^0 = 1 for a grand total of 11."
    kyle "That means lowercase Y converts to 79 in Hex which converts to 0111 1001 in Binary, lowercase L converts to 6C in Hex which converts to 0110 1100, and lowercase E converts to 65 in Hex and 0110 0101 in Binary."
    kyle "If I put all that together, that means my name in Binary is 01001011 01111001 01101100 01100101. Pretty cool!"

    hide hex chart

    show happy
    jeff "Well done class! You've completed your introduction to ASCII characters. Now, we are going to take a step further and add an alement of encryption."
    hide happy
    show talking2
    jeff "To do this we will use the following binary number as a key: 01001011."
    jeff "Now, for each bit in your binary name and in the key, convert the two bits in each place into a new bit using an XOR operation. This table will show you how it works."
    show xor chart:
        yalign 0
        xalign 0.5

    hide talking2
    hide xor chart
    show talking
    show xor chart:
        yalign 0
        xalign 0.5
    jeff "XOR means Exclusive Or, which is a type of operation where you consider 2 values, and if at least 1 of them equals 1, then the equation equals 1"
    jeff "But Exclusive Or also has an extra rule, if both values are equal to 1, then the expression is equal to 0."
    jeff "So if the first bit in your binary name is 1 and the first bit in the key is 0, then the first bit of the new number you are generating, will be a 1."
    hide talking
    label ascii_start:


    menu:
        "Using Kyle in binary, and the key that Mr. Bezos provided, XOR every bit in each number to create a new number.{p}Kyle: 01001011 01111001 01101100 01100101 {p}Key:  01001011 01001011 01001011 01001011"
        "00000000 00010000 00000110 00001110":
            jump ascii_1
        "11111111 11101111 11111001 11110001":
            jump ascii_2
        "10010101 10110110 10010111 1011110":
            jump ascii_3
        "01001011 01001001 01001000 01000001":
            jump ascii_4

    label ascii_1:
        "Correct!"
        jump ascii_done
    label ascii_2:
        "Incorrect."
        "Hint: when you XOR bits if the bits have different values the result is 1. Eg 1 XOR 0 = 1"
        "Hint: when you XOR bits if the bits have the same value the result is 0. Eg 1 XOR 1 = 0"
        jump ascii_start
    label ascii_3:
        "Incorrect."
        "Hint: when you XOR bits if the bits have different values the result is 1. Eg 1 XOR 0 = 1"
        "Hint: when you XOR bits if the bits have the same value the result is 0. Eg 1 XOR 1 = 0"
        jump ascii_start
    label ascii_4:
        "Incorrect!"
        "Hint: when you XOR bits if the bits have different values the result is 1. Eg 1 XOR 0 = 1"
        "Hint: when you XOR bits if the bits have the same value the result is 0. Eg 0 XOR 0 = 0"
        jump ascii_start

    label ascii_done:
    hide xor chart

    show happy
    jeff "Great job, class. You have no encrypted your names."
    hide happy

    stop music fadeout 1.0
    scene bg black with dissolve
    scene bg bedroom with dissolve

    play music "audio/1.mp3"

    "After school, Kyle goes home. He decides to finish his homework that his math teacher Mr. Gates assigned. While trying to find resources to help him understand the subject, the math website he is on gives him a pop-up ad."
    show pop ad

    kyle "What! I made the 5-billionth search on the Tesla browser? Damn! This lady won a Galaxy S10 and this guy won an Apple Watch 3. It would be a dream come true if I won an Apple Watch."
    kyle "It says to choose one of the prizes from below."
    "Click on the prize and follow the instructions?"

    menu:
        "Yes":
            jump popad_yes
        "No":
            jump popad_no

    label popad_yes:
        $ popadFlag = 1
        "The pop-up ad shows Kyle undesirable advertising, and downloads an app in the backgrounds which he notices."
        kyle "What the heck just happened? An application installed itself, it supposed to give me a prize."
        "The applciation installed could contain any kind of malware. It could destroy his computer, steal his data, and could spread "
        "It could also use his computer as a way to access the rest of the computers in his home network, which means his family computers may also be damaged by the virus."
        jump popad_done

    label popad_no:
        $ popadFlag = 0
        "I shouldn't click on the prize button, as it seems fishy that I made the 5-billionth search on the Tesla browser."
        "It also seems weird that the math website is telling me that I am the Tesla Browser's 5-billionth search."
        "I should look up a way to deal with these annoying advertisements."
        jump popad_done

    label popad_done:
    hide pop ad
    #"What would be a good way to avoid being harmed by pop-up ads?"
    #menu:
    #    "Do not click on suspicious and untrustworthy links and deceptive websites.":
    #        jump popad_done
    #    "Enable adblock or disable pop-ups in your browser to block pop-ups.":
    #        jump popad_done
    #    "Enable Anti-malware and Anti-virus software to check for malware.":
    #        jump popad_done
    #    "Both a and c.":
    #        jump popad_done
    #    "None of the above.":
    #        jump popad_done
    #    "Both b and d.":
    #        jump popad_done
    #    "All of the above.":
    #        jump popad_allabove


    #label popad_allabove:
    #    "The best ways to avoid pop-ups are to disable them on your browser. Having an anti-virus software will help protect your computer from suspicious downloads as well, and staying on trustworthy websites will keep you even safer."

    "Having had a long week of school, Kyle is ready for the weekend."
    "Before he goes to bed he thinks about his life since he got his new phone."
    "In that space of time he has learned a lot about security and malware."
    "But has he really been applying what he was learning? Did he behave with cyber security in mind he wonders."
    "With all these thoughts in mind Kyle has a weird dream that night."


    show bg black with dissolve
    # "Having had a long week of school, Kyle is ready for the weekend. He goes to bed thinking about how much he learned about malware and security."

    # Dream/Ending section



    stop music fadeout 1.0
    show bg black with dissolve
    show dream with dissolve
    play music "audio/Decision.mp3"

    ### show shadow kyle
    $ overall_score = 0

    if q1 == 1:
        $ overall_score += 5
        kyle "I chose 'Password1' for my new Spacenet account password."
        kyle "Sure it's easy to remember but this password is not at all secure."
        kyle "I should definitely change it when I get the chance."

    if q1 == 2:
        $ overall_score += 5
        kyle "I chose 'P@55w0rd' for my new Spacenet account password."
        kyle "I basically chose the word 'Password' but in the l33t spelling, giving it a symbol and some numbers."
        kyle "While this password is easy to remember it's unsecure since it is too short and is based on the word 'Password.'"
        kyle "I should definitely change it when I get the chance."

    if q1 == 3:
        $ overall_score += 1
        kyle "I chose 'mKxA3a12!' for my new Spacenet account password."
        kyle "This password is secure but it's hard to memorize. But it might not be much of a problem"
        kyle "I could store this password by writing it down somewhere or by using a password manager."
        kyle "But then I also would have to make sure that the password manager is secure and I would need to remember that password for the manager itself."
        kyle "maybe I'll change my Spacenet account password later on to one that I can remember easier."

    if q1 == 4:
        kyle "I chose 'Musky@Melon05' for my new Spacenet account password."
        kyle "This password is easy to memorize and is very secure."
        kyle "Yup i'm going to keep this password."

    "A good password is longer than 8 characters, has upper case and lowercase letters, has a few numbers and symbols, and is easy to remember."
    "You can check your password strength using websites like https://howsecureismypassword.net/"

    kyle "I remember getting some weird emails."
    if phishing1 == 0:
        $ overall_score += 5
        show email phishing1:
            xalign 0.5
            yalign 0.0
        kyle "Oh right remember this email. It didn't seem suspicious at the time but looking at it again something does seem fishy."
        kyle "The google drive link uses a fake URL that isn't actually used by google."
        kyle "I shouldn't click on the link."
        hide email phishing1

    if phishing2 == 0:
        $ overall_score += 5
        show email phishing2:
            xalign 0.5
            yalign 0.0
        kyle "This email I got earlier didn't seem suspicious but now that I look at it something is off."
        kyle "The URL has a weird domain. The word Fax isn't even spelled right."
        hide email phishing2

    if phishing3 == 0:
        $ overall_score += 5
        show email phishing3:
            xalign 0.5
            yalign 0.0
        kyle "I was really curious about this email. Looking at it again it uses a weird email address."
        kyle "Plus the link goes to a website called sytez.net which is suspicious."
        kyle "As tempting as it is I should not click on the link."
        hide email phishing3

    if phishing4 == 1:
        $ overall_score += 1
        show email legit1:
            xalign 0.5
            yalign 0.0
        kyle "I thought this email was suspicious but maybe I was overly cautious."
        kyle "All the links lead to dropbox.com and the email address is also the correct address used by Dropbox."
        hide email phishing4

    "Phishing emails are emails that pretend to be harmless or impersonate legitimate websites like google but actually link to harmful websites or scams."
    "When you get emails remember to check the sender's email address to see if it is from a trusted email service. Don't open emails from people you do not know or are suspicious about."
    "Make sure before clicking on links that they send you to legitimate trusted websites."
    "Phishing emails and scams will sometimes have spelling errors."

    kyle "With Alice I remember we ran across a poster on the way to subway."
    show qr poster:
        xalign 0.5
        yalign 0.0

    if qrlink == 1:
        $ overall_score += 5

        kyle "I remember that my phone froze when I followed the link the QR code gave me. That was definitely the wrong choice"

    "QR codes often can hide malicious links. Do not scan a QR code from an untrusted source."
    "If possible use a QR scanner that does not automatically send you to the link without your confirmation first. That way you can see if the link can be trusted yourself."
    hide qr poster

    kyle "I passed by a USB on the way home from school that one time. Pretty decent storage size too."
    show usb:
        xalign 0.5
        yalign 0.5

    if usbFlag == 0:
        $ overall_score += 5
        kyle "I made the wrong decision picking up that USB and plugging it in to my PC."

    "Malware is harmful software. One way malware spreads is sharing files through storage and media like USBs and CDs."
    "One type of malware are keyloggers. They record keystrokes on your device, sending personal information you type like passwords to a remote source."
    "It can be very hard to dectect viruses."
    "They are hard to tell apart from non-harmful software."
    "Viruses have characterstics called signatures which can be used to detect viruses. However some viruses have the ability to change their code to avoid being recognized."
    "Another way to detect viruses is by behaviour rather than signatures. Looking at how your system behaves, seeing if anything matching how a certain kind of virus works"

    hide usb

    kyle "Then there was that pop up ad I encountered just before I fell asleep."
    show pop ad

    if popadFlag == 1:
        $ overall_score += 5
        kyle "I shouldn't have clicked on it, that wasn't a fun experience."

    "A good way to defend yourself from pop up ads and malware that comes from them is to..."
    "1. Do not click on suspicious and untrustworthy links and deceptive websites."
    "2. Enable adblock or disable pop-ups in your browser to block pop-ups."
    "3. Enable Anti-malware and Anti-virus software to check for malware."

    kyle "Now that I think about it the things that happened to me these few days are pretty common."
    kyle "It's pretty important that I am careful when I go online in my everyday life."
    kyle "Im going to start paying more attention to Mr. Bezos' class."

    hide pop ad
    stop music fadeout 1.0
    play music "audio/bday.mp3"
    if overall_score == 0:
        "Your Score: S Rank - You have a perfect score!"
    elif overall_score <= 10:
        "Your Score: A Rank - Good Job!"
    elif overall_score <= 20:
        "Your Score: B Rank "
    else:
        "Your Score: C Rank"




    # This ends the game.

    return
