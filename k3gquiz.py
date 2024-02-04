import statistics
import random

print("WELCOME TO THE K3G PERSONALITY QUIZ ")
print("\nAnswer the questions by entering the answers as a,b,c, or d and get to know which character from Kabhi Khushi Kabhie Gham You are ! ")

quiz =[
{"q":"Choose a MITHAI",
"a":"Jalebi","b":"Kaju Katli","c":"Rasmalai","d":"Motichoor ke laddoo"
},
{"q":"Choose a HOLIDAY SPOT",
"a":"London","b":"New York","c":"Paris","d":"Shimla"
},
{"q":"Choose a CUISINE",
"a":"Chinese","b":"Italian","c":"Indian","d":"Continental"
},
{"q":"Choose a HOBBY",
"a":"Travelling","b":"Writing","c":"Dancing","d":"Cooking"
},
{"q":"Choose a COLOUR",
"a":"Green","b":"Black","c":"Pink","d":"Yellow"
},
{"q":"Choose an OUTFIT",
"a":"Suit salwar","b":"Saree","c":"Gown","d":"Office wear"
},
{"q":"Choose a DANCE FORM",
"a":"Jazz","b":"Bhangra","c":"Hip Hop","d":"Bollywood"
},
{"q":"Choose a DRINK",
"a":"Coffee","b":"Beer","c":"Champagne","d":"Chai"
},
{"q":"Choose a CELEBRITY ",
"a":"Kajol","b":"Jaya Bacchhan","c":"Alia Bhatt","d":"Rani Mukherjee"
},
{"q":"Choose a DIALOGUE",
"a":"Hello ji","b":"Keh diya na! bas keh diya ","c":"Sare jahan se accha Hindustan Hamara ","d":"Good looks , Good looks and Good looks !"
}
]

ans= []

for i in range(1,11):
	item = random.choice(quiz)
	print("\n")
	print(str(i)+".",item["q"])
	print("a",item["a"])
	print("b",item["b"])	
	print("c",item["c"])	
	print("d",item["d"])
	
	t = input("Enter your answer : ")
	
	ans.append(t.lower())
	quiz.remove(item)
	
v = statistics.mode(ans)
print("\n\n")

if v == "a":
	print("You're Rahul Raichand ☆")
	print("Smart and Samajhdar,Loving, Amusing and much more...")
	
elif v == "b":
	print("You're Yashwardhan Raichand ♧")
	print("Natural Leader, Classy, You love sanskar,sanskriti,sabhyata,etc.etc....")

elif v == "c" :
	print("You're the prettiest... Poo♡")
	print("Classy,PHAT,Iconic,Savage,Self-obsessed..... words fall short in your praise !")
	
elif v == "d" : 
    print("You're Anjali Sharma Raichand")
    print("The clumsy,sassy,cussy,goofy,bubbly girlie who loves her BHARAT")