#!/usr/bin/env python
import webbrowser
handle = webbrowser.get()
import time
import os



class Person(object):
	def __init__(self,motivation,fatigue,gpa,poopcount,sleepcount,crycount, armor, attack, health, magic, limit, attackNo, magicNo, potionNo):
		self.motivation = motivation
		self.fatigue = fatigue
		self.gpa = gpa
		self.poopcount = poopcount
		self.sleepcount = sleepcount
		self.crycount = crycount
		self.armor = armor
		self.attack = attack
		self.health = health
		self.magic = magic
		self.limit = limit
		self.attackNo = attackNo
		self.magicNo = magicNo
		self.potionNo = potionNo

gabe = Person(100, 0, 3.5,0,0,0,"basic",0,0,0,15,0,0,0)

print("Hi Hackathon. Welcome to my life up to this point.")
time.sleep(1)
print("Every detail of the story represents the completely")
time.sleep(1)
print("realistic aspects of my yesterday up til now. Have fun")
time.sleep(1)
print("making me sexy. Or wrecking my body. or killing my college")
time.sleep(1)
print("career. but really please don't kill anything cause that")
time.sleep(1)
print("would be bad later in the game.")
time.sleep(2)
print("Let's get started!")
time.sleep(2)



def bed():
	print("It is 8 in the morning, and a unicorn is primed to beat you with a narwhal. what do you do?")
	def bFunc():
		choicelist = "cry, fight, poop"
		print("your choices are: " + choicelist)
		choice = raw_input()
		if "cry" == choice.lower():
			print("You are getting beat by a freaking narwhal")
			time.sleep(.5)
			print("what are you doing crying stop")
			time.sleep(.5)
			bFunc()
		elif "fight" == choice.lower():
			print("the Narwhal's horn has no time")
			time.sleep(.5)
			print("for your weak punches")
			time.sleep(.5)
			bFunc()
		elif "poop" == choice.lower():
			print("good job. You have discovered the bed narwhal's")
			time.sleep(.5) 
			print("weakness. You open his mouth and you proceed to")
			time.sleep(.5)
			print("dump loads of justice into his mouth")
			time.sleep(1)
			print("BEEPBEEPBEEPBEEPBEEPBEEP")
			time.sleep(1)
			realBed()
		else:
			print("Dude what are you thinking this is no time to try to raise an error in terminal")
			time.sleep(.5)
			print("kill that freaking narwhal. MAKE AN ACTUAL CHOICE")
			time.sleep(.5)
			bFunc()
	bFunc()

def realBed():

	clearscreen()
	print("Just kidding you didn't just slay a narwhal.")
	time.sleep(1)
	print("Welcome back to Berkeley.")
	time.sleep(1)
	print("Dumping justice on your midterms will get you killed.")
	time.sleep(1)
	print("Or will it? hmmm...")
	time.sleep(2)
	clearscreen()
	print("Anyways your alarm clock is going off. You are awake.")
	time.sleep(1)
	print("What will you do? will you get out of bed now and feel")
	time.sleep(1)
	print("groggy? Take a nap for 30 minutes and be late for class?")
	time.sleep(1)
	print("Just sleep in? What will you do?")
	time.sleep(1)
	def rFunc():
		choicelist = "cry, poop, get up, nap, sleep in"
		print("your choices are: " + choicelist)
		choice = raw_input()
		if choice.lower() == "get up":
			gabe.motivation += 10
			gabe.fatigue += 20
			print("This is the most unrealistic part of the game.")
			time.sleep(1)
			print("What decent CS major is awake before 2?")
			time.sleep(1)
			print("Anyways, for my full sentiments on your ability")
			time.sleep(1)
			print("to wake up, pay attention to video now: ")
			time.sleep(2)
			handle.open('http://www.youtube.com/watch?v=wDajqW561KM')
			onTimeToDisc()
		elif choice.lower() == "nap":
			gabe.motivation -= 10
			gabe.fatigue += 10
			gabe.gpa -= .25
			print("okay, so you came a bit late to class,") 
			time.sleep(1)
			print("but at least you're not as tired!")
			time.sleep(1)
			lateToDisc()
		elif choice.lower() == "sleep in":
			gabe.sleepcount += 1
			gabe.motivation -= 20
			gabe.gpa -= .5
			print("Unfortunately, you did not encounter another")
			time.sleep(1)
			print("narwhal, however, you did encounter...")
			time.sleep(2)
			handle.open('http://www.youtube.com/watch?v=VJ1dYrjuYf4')
			getSwole()
		elif choice.lower() == "poop":
			gabe.poopcount += 1
			gabe.motivation += 20
			gabe.gpa -= .25
			gabe.fatigue += 10
			print("good job. you just pooped in your bed. You")
			time.sleep(1)
			print("have no toilet paper but cleaning it by mouth")
			time.sleep(1)
			print("isn't that good of an option either. You are")
			time.sleep(1)
			print("slightly late to class due to using a toothbrush,")
			time.sleep(1)
			print("but pooping is always motiational.")
			time.sleep(2)
			lateToDisc()
		elif choice.lower() == "cry":
			gabe.motivation -= 20
			gabe.gpa -= .25
			gabe.fatigue -= 10
			print("CS majors have no emotions. What are you")
			time.sleep(1)
			print("doing. go to class.")
			time.sleep(2)
			lateToDisc()
		else:
			handle.open("http://media.tumblr.com/tumblr_m7wa1truQk1qmvo8l.gif")
			print("They disapprove. MAKE A CHOICE.")
			rFunc()
	rFunc()

def onTimeToDisc():
	clearscreen()
	print("By some miracle you are on time to a morning class.")
	time.sleep(1)
	print("You don't have any clue what the GSI is talking about,")
	time.sleep(1)
	print("but in your mind you are a god for making it.")
	time.sleep(1)
	print("BUT SUDDENLY QUIZ YOU'RE NEVER A GOD IN BERKELEY MATH")
	time.sleep(1)
	print("You start to panic. What will you do? You spent all")
	time.sleep(1)
	print("this time basking in your glory!")
	time.sleep(2)
	clearscreen()
	print("You remember something vague about eigenvalues at")
	time.sleep(1)
	print("first for the first answer...")
	time.sleep(2)
	print("but then again you also just remembered something") 
	time.sleep(1)
	print("about him talking about derivatives...what method")
	time.sleep(1)
	print("do you take to answer?")
	time.sleep(1)
	def oFunc():
		choicelist = "derivatives, eigenvalues, poop, cry"
		print("your choices are: " + choicelist)
		choice = raw_input()
		if choice.lower() == "eigenvalues":
			gabe.gpa -= .25
			gabe.motivation += 10
			print("the answers are going to be revealed...")
			time.sleep(2)
			print("...the results are in...YOUR ORIGINAL ANSWER")
			time.sleep(1)
			print("ABOUT EIGENVALUES WAS RIGHT SOMEHOW...partially...")
			time.sleep(1)
			print("BUT IT WAS STILL SOMEWHAT CORRECT.")
			time.sleep(2)
			handle.open("http://i.imgur.com/TEgJh.gif")
			print("Good job not second guessing yourself.")
			time.sleep(2)
			getSwole()
		elif choice.lower() == "derivatives":
			gabe.gpa -= .5
			gabe.motivation -= 10
			print("the answers are going to be revealed...")
			time.sleep(2)
			print("...the results are in...DARN THE ANSWER WAS")
			time.sleep(1)
			print("ACTUALLY ABOUT EIGENVALUES. You second guessed")
			time.sleep(1)
			print("yourself and you are now frustrated.")
			time.sleep(2)
			getSwole()
		elif choice.lower() == "poop":
			gabe.gpa -= 1.0
			gabe.motivation += 20
			gabe.poopcount += 1
			print("Though you may have soiled your GPA, your dignity will never be soiled.")
			time.sleep(2)
			getSwole()
		elif choice.lower == "cry":
			gabe.gpa -= .5
			gabe.motivation -= 10
			gabe.fatigue -= 10
			gabe.sleepcount += 1
			print("STOP CRYING MATH AIN'T GOT NO TIME FOR YO CRYIN")
			time.sleep(2)
			getSwole()
		else:
			handle.open("http://25.media.tumblr.com/tumblr_m7sd3wRMGI1qz581wo3_250.gif")
			print("The President disapproves. choose something else.")
			oFunc()
	oFunc()

def lateToDisc():
	clearscreen()
	print("Everybody is staring at you. You automatically assume")
	time.sleep(1)
	print("that it is because you, like Nicki Minaj, are the baddest...")
	time.sleep(1)
	print("NO TIME FOR NICKI MINAJ FANTASIES QUIZ TIME NAO")
	time.sleep(1)
	print("You start to panic. What will you do? You spent all")
	time.sleep(1)
	print("this time basking in bein beez in da trap!")
	time.sleep(2)
	clearscreen()
	print("You remember something vague about eigenvalues at")
	time.sleep(1)
	print("first for the first answer...")
	time.sleep(2)
	print("but then again you also just remembered something") 
	time.sleep(1)
	print("about him talking about derivatives...what method") 
	time.sleep(1)
	print("do you take to answer?")
	time.sleep(1)
	def oFunc():
		choicelist = "derivatives, eigenvalues, poop, cry"
		print("your choices are: " + choicelist)
		choice = raw_input()
		if choice.lower() == "eigenvalues":
			gabe.gpa -= .25
			gabe.motivation += 10
			print("the answers are going to be revealed...")
			time.sleep(2)
			print("...the results are in...YOUR ORIGINAL ANSWER")
			time.sleep(1)
			print("ABOUT EIGENVALUES WAS RIGHT SOMEHOW...partially...")
			time.sleep(1)
			print("BUT IT WAS STILL SOMEWHAT CORRECT.")
			time.sleep(2)
			handle.open("http://i.imgur.com/TEgJh.gif")
			print("Good job not second guessing yourself.")
			time.sleep(2)
			getSwole()
		elif choice.lower() == "derivatives":
			gabe.gpa -= .5
			gabe.motivation -= 10
			print("the answers are going to be revealed...")
			time.sleep(2)
			print("...the results are in...DARN THE ANSWER WAS")
			time.sleep(1)
			print("ACTUALLY ABOUT EIGENVALUES. You second guessed")
			time.sleep(1)
			print("yourself and you are now frustrated.")
			time.sleep(2)
			getSwole()
		elif choice.lower() == "poop":
			gabe.gpa -= 1.0
			gabe.motivation += 20
			gabe.poopcount += 1
			print("Though you may have soiled your GPA, your dignity will never be soiled.")
			time.sleep(2)
			getSwole()
		elif choice.lower == "cry":
			gabe.gpa -= .5
			gabe.motivation -= 10
			gabe.fatigue -= 10
			gabe.sleepcount += 1
			print("STOP CRYING MATH AIN'T GOT NO TIME FOR YO CRYIN")
			time.sleep(2)
			getSwole()
		else:
			handle.open("http://25.media.tumblr.com/tumblr_m7sd3wRMGI1qz581wo3_250.gif")
			print("The President disapproves. choose something else.")
			oFunc()
	oFunc()

def getSwole():
	clearscreen()
	print("Whether you chose to sleep in or go to class, ")
	time.sleep(1)
	print("the almighty creator of this program is not sure")
	time.sleep(1)
	print("because of laziness. HOWEVER. You need abs. GO TO ")
	time.sleep(1)
	print("THE GYM.")
	time.sleep(1)
	def sFunc():
		choicelist = "get swole, sleep, poop, kpop"
		print("your choices are: " + choicelist)
		choice = raw_input()
		if choice.lower() == "get swole":
			gabe.fatigue += 20
			gabe.motivation += 20
			print("Congratulations. You now look like this guy: ")
			time.sleep(2)
			handle.open('http://www.youtube.com/watch?v=kx5COTBjcNc&t=3m5s')
			CSHomework()

		elif choice.lower() == "sleep":
			gabe.sleepcount += 1
			gabe.fatigue -= 10
			gabe.motivation -= 20
			print("THERE ARE ABS INSIDE OF YOU AND ALL")
			time.sleep(1)
			print("YOU WANT TO DO IS SLEEP!?")
			time.sleep(1)
			print("At this rate, you will never be like")
			time.sleep(1)
			print("this guy: ")
			time.sleep(2)
			handle.open('http://www.youtube.com/watch?v=kx5COTBjcNc&t=3m5s')
			CSHomework()

		elif choice.lower() == "poop":
			gabe.motivation += 10
			gabe.poopcount += 1
			print("though poop is great motivation...")
			time.sleep(1)
			print("your poop supply is precious.")
			time.sleep(1)
			print("remember that.")
			time.sleep(2)
			print("THINK FAST")
			time.sleep(.5)
			handle.open('http://www.youtube.com/watch?v=kx5COTBjcNc&t=3m5s')
			CSHomework()

		elif choice.lower() == "kpop":
			gabe.fatigue += 10
			gabe.motivation += 10
			print("congratulations. You have learned how to body roll")
			time.sleep(1)
			print("like Rain!")
			time.sleep(1)
			print("You get a great cardio workout from this.")
			time.sleep(2)
			handle.open('http://www.youtube.com/watch?v=kx5COTBjcNc&t=3m5s')
			CSHomework()

		else:
			print("I'm getting tired of finding gifs. It's 3:39 AM in the morning right now.")
			handle.open("http://media.tumblr.com/tumblr_m2hpjw00U41r9px83.gif")
			sFunc()
	sFunc()

def CSHomework():
	clearscreen()
	print("Why are you listening to KPop YOU HAVE TO DO CS HOMEWORK.")
	time.sleep(1)
	print("YOU HAVE TO SUBMIT TODAY.")
	time.sleep(1)
	print("Shall you start now?")
	time.sleep(1)
	def cFunc():
		choicelist = "do homework, kpop, jpop, sleep"
		print("your choices are " + choicelist)
		choice = raw_input()
		handle.open('http://www.facebook.com/')
		CSHomeworkForReal()
	cFunc()

def CSHomeworkForReal():
	clearscreen()
	print("IT CONTROLS YOUR LIFE.")
	time.sleep(1)
	print("Okay, so after 5 hours, you managed to break the control of Facebook.")
	time.sleep(1)
	print("Congratulations. You now have 1 hour to finish. ")
	time.sleep(1)
	print("WHAT WILL YOU DO!?")
	time.sleep(1)
	def cFunc():
		choicelist = "clutch, kpop, cry, facebook"
		print("your choices are " + choicelist)
		choice = raw_input()
		if choice == "clutch":
			gabe.motivation += 20
			gabe.fatigue += 10
			gabe.gpa += .5
			print("CLUTCH SO HARD MOTHER LOVERS WANNA FINE YOU.")
			time.sleep(1)
			print("You have finished CS Homework before deadline! Nice!")
			time.sleep(2)
			PreHackathon()
		elif choice == "kpop":
			gabe.motivation += 10
			gabe.fatigue -= 10
			gabe.gpa -= .25
			print("Kpop is not good for GPA.")
			time.sleep(1)
			print("However, it is insanely motivational.")
			time.sleep(2)
			handle.open('http://loopthetube.com#BnUEC_z-ops&start=116.512&end=118.57900000000001')
			PreHackathon()
		elif choice == "cry":
			gabe.motivation -= 10
			gabe.fatigue -= 10
			gabe.gpa -= .25
			gabe.crycount += 1
			print("NO. STOP CRYING. OH. OH OH. YOU DON'T KNOW YOU'RE BEAUTIFUL.")
			time.sleep(1)
			PreHackathon()
		elif choice == "facebook":
			gabe.motivation -= 20
			gabe.gpa -= .5
			print("You gave back into the control of the Zuck!")
			time.sleep(1)
			print("I shall now make a game to depict your addiction to facebook...")
			time.sleep(2)
			print("after I check my notifications. DUN DUN DUUUUN")
			time.sleep(1)
			PreHackathon()
		else:
			print("OBLIGATORY DISAPPROVING GIF")
			time.sleep(1)
			handle.open('http://media.tumblr.com/tumblr_mchb7ezwGv1qdn14l.gif')		
			cFunc()
	cFunc()

def PreHackathon():
	clearscreen()
	print("Oh, you have a Hackathon coming up! Hopefully")
	time.sleep(1)
	print("you made wise decisions so far.")
	time.sleep(1)
	print("but before you go...one more decision to make!")
	time.sleep(1)
	print("you're a bit rusty on your pygame knowledge...but") 
	time.sleep(1)
	print("then again you only got 4 hours of sleep. what do you do?")
	time.sleep(1)
	def pFunc():
		choicelist = "pygame, sleep, puppy"
		print("Your choices are " + choicelist)
		choice = raw_input()
		if choice == "pygame":
			gabe.motivation += 20
			gabe.fatigue += 30
			gabe.gpa += .5
			print("As you can clearly see, this totally")
			time.sleep(1)
			print("happened in real life.")
			time.sleep(1)
			print("BUT your choice still matters!")
			time.sleep(2)
			NeverGiveUp()
		elif choice == "sleep":
			gabe.motivation -= 20
			gabe.fatigue -= 20
			print("You are rested. However, getting out of bed")
			time.sleep(1)
			print("is like trying to milk a cow")
			time.sleep(1)
			print("with your mouth.")
			time.sleep(2)
			NeverGiveUp()
		elif choice == "puppy":
			gabe.motivation -= 10
			gabe.fatigue -= 10
			print("awwwwwww")
			time.sleep(2)
			print("BUT PUPPIES WON'T HELP YOU HACK.")
			time.sleep(2)
			print("look at the doggy anyways")
			handle.open('http://i.minus.com/iG3nkL944JE6I.gif')
			NeverGiveUp()
		else:
			print("All my other disapproving gifs are")
			time.sleep(1)
			print("a bit profane.")
			time.sleep(1)
			print("JUST MAKE AN ACTUAL CHOICE.")
			time.sleep(1)
			pFunc()
	pFunc()

def NeverGiveUp():
	clearscreen()
	print("Well, a couple of hours in...and your group ain't")
	time.sleep(1)
	print("come up with an idea. you are getting discouraged.")
	time.sleep(1)
	print("They start to leave.")
	time.sleep(1)
	print("you want to leave because they are leaving too.")
	time.sleep(1)
	print("your choices are leave, and leave")
	def leave():
		a = raw_input()
		if a.lower() != "leave":
			print("meh.")
			leave()
		else:
			print("BUT THEN SUDDENLY")
			time.sleep(2)
	leave()
	clearscreen()
	print("A hacker there changes things with a couple of words.")
	time.sleep(1)
	print("'Come on. Make...something.'")
	time.sleep(1)
	print("...")
	time.sleep(1)
	def really():
		choicelist = "leave, code"
		print("your choices are " + choicelist)
		choice = raw_input()
		if choice == "leave":
			gabe.motivation -= 25345235
			print("bad choice. you never know what you could have done.")
			time.sleep(1)
			print("...")
			time.sleep(1)
			print("and you totally just missed out on the 2nd part of the game.")
			time.sleep(1) 
			print("you missed an opportunity. Simply because you followed")
			time.sleep(1)
			print("those around you and gave up.")
			time.sleep(1)
			print("type something and hit enter.")
			a = raw_input()
			return a
		elif choice == "code":
			clearscreen()
			print("Against everyone else around you...you decide to code...something.")
			time.sleep(1)
			print("And that's really what life's about. Always make an effort...")
			time.sleep(1)
			print("...but before this gets too feely...")
			time.sleep(2)
			print("OMG THERE'S A UNICORN ATTACKING SODA HALL. YOU ARE NOW GIVEN STATS")
			time.sleep(2)
		else:
			print("Come on. make a real choice.")
			really()
	really()

def clearscreen(numlines = 30):
	if os.name == "posix":
		os.system('clear')
	elif os.name in ('nt', 'dos', 'ce'):
		os.system('cls')
	else:
		print '\n' * numlines

clearscreen()
bed()
print(gabe.motivation)
print(gabe.fatigue)
print(gabe.gpa)
print(gabe.poopcount)
print(gabe.crycount)
print(gabe.sleepcount)

if gabe.poopcount > 2:
	gabe.armor = "Holy armor of feces"
	gabe.attack = 5
	gabe.health = 10
	gabe.magic = 1
	
elif gabe.crycount > 2:
	gabe.armor = "man stop crying"
	gabe.attack = 5
	gabe.health = 5
	gabe.magic = 10
	
elif gabe.sleepcount > 2:
	gabe.armor = "armor of laziness"
	gabe.attack = 15
	gabe.health = 5
	gabe.magic = 15
	
elif gabe.motivation > 100 and gabe.fatigue < 0 and gabe.gpa > 3.0:
	gabe.armor = "armor of the red mage"
	gabe.attack = 15
	gabe.health = 15
	gabe.magic = 15
	
elif gabe.motivation > 100 and gabe.fatigue > 0 and gabe.gpa > 3.0:
	gabe.armor = "robe of the black mage"
	gabe.attack = 5
	gabe.health = 10
	gabe.magic = 15
	
elif gabe.motivation > 100 and gabe.fatigue > 0 and gabe.gpa < 3.0:
	gabe.armor = "brave knight armor"
	gabe.attack = 15
	gabe.health = 10
	gabe.magic = 5
	
elif gabe.motivation < 100 and gabe.fatigue < 0 and gabe.gpa > 3.0:
	gabe.armor = "robe of the white mage"
	gabe.attack = 5
	gabe.health = 15
	gabe.magic = 5
	
elif gabe.motivation < 100 and gabe.fatigue < 0 and gabe.gpa < 3.0:
	gabe.armor = "robe of the hacker"
	gabe.attack = 5
	gabe.health = 5
	gabe.magic = 20
	
elif gabe.motivation < 100 and gabe.fatigue > 0 and gabe.gpa < 3.0:
	gabe.armor = "you tried"
	gabe.attack = 5
	gabe.health = 5
	gabe.magic = 5
	
else:
	gabe.armor = "basic"
	gabe.attack = 10
	gabe.health = 10
	gabe.magic = 10
	

clearscreen()
print("as a result of your efforts, you have got this armor: ")
print(gabe.armor)
print("attack: " + str(gabe.attack))
print("health: " + str(gabe.health))
print("magic: " + str(gabe.magic))

normalizedHealth = gabe.health

a = raw_input("press any key and enter to continue.")

clearscreen()


print("Now, fight the unicorn!")
time.sleep(2)
#handle.open('http://www.youtube.com/watch?v=jbXOyXaJJBc')
#time.sleep(3)
print("loljk prepare first")

def prepare():
	clearscreen()
	print("inventory limit = 15")
	proposedPot = 0
	proposedAtt = 0
	proposedMag = 0

	proposedPot = int(raw_input("potions: "))
	proposedAtt = int(raw_input("attacks: "))
	proposedMag = int(raw_input("spells: "))

	if (proposedPot + proposedAtt + proposedMag) > 15:
		prepare()
	else:
		gabe.potionNo = proposedPot
		gabe.attackNo = proposedAtt
		gabe.magicNo = proposedMag
		return "ready to fight with " + str(gabe.potionNo) + " potions " + str(gabe.attackNo) + " attacks " + str(gabe.magicNo) + " spells."

def fight(hero, villain,attackstr=""):
	clearscreen()
	if str(villain) == "unicorn":
		attackstr = "Unicorn used rainbow sparkle infinite recursion!"
	elif str(villain) == "boba":
		attackstr = "Mutated Tapioca used Ultimate taro jasmine strike!"
	elif str(villain) == "hilfinger":
		attackstr = "Hilfinger is going straight for the GPA!"
	print("live or let die!")
	print("health = " + str(hero.health) + " potions = " + str(gabe.potionNo) + " attacks = " + str(gabe.attackNo) + " spells " + str(gabe.magicNo))
	print(str(villain) + " health = " + str(villain.health))
	command = raw_input("type in command: potion, attack, magic - ")
	if command == "potion":
		if gabe.potionNo == 0:
			print("out of potions. Opponent turn")
			time.sleep(1)
		else:
			hero.health += 4
			gabe.potionNo -= 1
			print("gabe used potion!")
			time.sleep(1)
			print("health = " + str(hero.health) + " potions = " + str(gabe.potionNo) + " attacks = " + str(gabe.attackNo) + " spells " + str(gabe.magicNo))
			print(str(villain) + " health = " + str(villain.health))
	elif command == "attack":
		if gabe.attackNo == 0:
			print("Out of attacks")
		else:
			villain.health -= hero.attack
			gabe.attackNo -= 1
			print("gabe attacks!")
			time.sleep(1)
			print("health = " + str(hero.health) + " potions = " + str(gabe.potionNo) + " attacks = " + str(gabe.attackNo) + " spells " + str(gabe.magicNo))
			print(str(villain) + " health = " + str(villain.health))
	elif command == "magic":
		if gabe.magicNo == 0:
			time.sleep(1)
			print("out of spells")
		else:
			villain.health -= hero.magic
			gabe.magicNo -= 1
			print("gabe casts spell!")
			time.sleep(1)
			print("health = " + str(hero.health) + " potions = " + str(gabe.potionNo) + " attacks = " + str(gabe.attackNo) + " spells " + str(gabe.magicNo))
			print(str(villain) + " health = " + str(villain.health))
	if villain.health <= 0:
		print('Victory!')
		time.sleep(2)
		return True
	else:
		time.sleep(1)
		print(attackstr)
		hero.health -= villain.attack
		time.sleep(1)
		print("health = " + str(hero.health) + " potions = " + str(gabe.potionNo) + " attacks = " + str(gabe.attackNo) + " spells " + str(gabe.magicNo))
		print(str(villain) + " health = " + str(villain.health))
		if hero.health <= 0:
			print("Defeat...")
			time.sleep(2)
			return False
		else:
			time.sleep(2)
			fight(hero, villain)

def checkIfWin1():
	print("Cue Dramatic Music...")
	time.sleep(2)
	handle.open('http://www.youtube.com/watch?v=jbXOyXaJJBc')
	if fight(gabe, unicorn) == True:
		time.sleep(2)
		return
	else:
		print("Time for rematch!")
		checkIfWin1()

def checkIfWin2():
	print("Cue Dramatic Music...")
	time.sleep(2)
	handle.open('http://www.youtube.com/watch?v=jbXOyXaJJBc')
	if fight(gabe, boba) == True:
		print("...a very sad victory.")
		time.sleep(2)
		return
	else:
		print("Time for rematch!")
		checkIfWin2()

def checkIfWin3():
	print("Cue Dramatic Music...")
	time.sleep(2)
	handle.open('http://www.youtube.com/watch?v=jbXOyXaJJBc')
	if fight(gabe, hilfinger) == True:
		print("It's finished.")
		time.sleep(2)
		return
	else:
		print("Time for rematch!")
		checkIfWin3()


class Baws(object):
	def __init__(self, health, attack, magic, swag):
		self.health = health
		self.attack = attack
		self.magic = magic
		self.swag = swag

	def __str__(self):
		return self.swag

unicorn = Baws(25, 1, 1, "unicorn")
boba = Baws(20, 2, 2, "boba")
hilfinger = Baws(30,2,2,"hilfinger")


prepare()
time.sleep(2)
print("OKAY FIGHT NOW")
time.sleep(1)
checkIfWin1()

clearscreen()
print("that unicorn was a creation of the CS department...of Berkeley!?")
time.sleep(1)
print("your own school is against you...and now they're mutating")
time.sleep(1)
print("a tapioca ball, your true love, into a man-eating monster!")
time.sleep(2)
clearscreen()
print("now you must fight your true love!")
time.sleep(2)
gabe.health = normalizedHealth

prepare()
time.sleep(2)
print("FIGHT YOUR LOVE")
time.sleep(1)
checkIfWin2()

clearscreen()
print("it wasn't a great victory...but it was a necessary one.")
time.sleep(1)
print("now it is time to face the ultimate villain...")
time.sleep(1)
print("the demon...WITHIN YOURSELF!")
time.sleep(3)
print("just kidding that's really cliche.")
time.sleep(1)
print("THE REAL ULTIMATE FINAL VILLAIN IS HILFINGER!!!")
time.sleep(3)
gabe.health = normalizedHealth

prepare()
time.sleep(2)
print("NOW SLAUGHTER. BEFORE YOUR GPA IS SLAUGHTERED.")
time.sleep(2)
checkIfWin3()

clearscreen()
print("You have finished the game!...and possibly killed me college career in the process.")
print("Beautiful terminal graphics by Gabriel Ruiz.")
print("gifs from many places, videos from YouTube.")
a = raw_input("press any key and enter to end this program.")




