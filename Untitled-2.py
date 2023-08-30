'''def flirt(name):
    print("hello bebe " + name)


def login(name, time):
    print("Hello " + name)
    print("You have logged in at: " + time)

flirt("Lei")
login("Raymond", str(1655))

print(11//3)

def convert_to_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours*3600) // 60
    remaining_sec = seconds - hours*3600 - minutes*60
    return hours, minutes, remaining_sec

get_time = convert_to_seconds(7951)
print(get_time)



def get_grade(grade1,grade2,grade3):

    average = (int(grade1) + int(grade2) + int(grade3)) / 3
    print("Your average is: " + str(average))

get_grade(92,93,95)'''

'''def check_username():
    username = input("Select a username: ")
    if len(username) < 4:
        print("The username must be at least 4 characters.")
    else:
        print("Your username is valid!")

check_username()'''

'''meters = 0
destination = 1000

while meters < destination:
    distance = destination - meters
    print("You are still " + str(distance) + " meters away.")
    meters += 100
if meters == destination:
    print("You have arrived")
    '''
'''
values = [23, 52, 59, 37, 48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print("Total sum: " + str(sum) + " Average: " + str(sum//length))'''


'''def convert_to_celsius():
    farrenheit = input("Enter Farrenheit: ")
    celsius = (int(farrenheit)-32)*5/9
    print(celsius)

convert_to_celsius()'''

'''def convert_to_celsius(x):
    celsius = (x-32)*5/9
    return celsius

for x in range(0,51,5):
    print(x,convert_to_celsius(x))'''

'''for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str (right) + "]", end="->")
    print()'''
'''
teams = ["A", 'B', 'C', 'D']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)'''

'''teams = ["Freshmen", "Sophomores", "Juniors", "Seniors"]
day = 1
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print("Day " + str(day) + ": " + home_team + " vs " + away_team)
            day +=   1'''

'''print("Enter team names: ")
team1 = input()
team2 = input()
team3 = input()
team4 = input()

def greet_teams(teams):
    for team in teams:
        print("Welcome Team " + team)

greet_teams([team1, team2, team3, team4])'''

'''print("How many times would you like to print 'Hello World'?: ")
amount = int(input())
count = 0

while count <= amount:
    print("Hello World")
    count += 1'''
    
'''num = int(input("Check for factorial: "))
if num < 0:
    print("There is no factorial for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
        result = 1
        for x in range(1,num+1):
            result = result*x
            print("The factorial of " + str(x) + " is " + str(result))'''


'''count = 0
while count <= 100:
    if count <= 100:
        print(count)
    count += 7'''
'''
total = 0
for x in range(1,10):
  total += x**3
  print(total)'''

'''for x in range(1,10,3):
    print(x)'''

'''
team = input("Enter your team name: ")
print(team[0].upper(), end = "")
print(team[-1].upper())'''

'''team = input("Enter your team name: ")
print(team[0].upper() + team[-1].upper())'''

'''def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
    else:
        new_email = email
    print("Your old email is: " + email)
    print("Your new email is: " + new_email)

replace_domain("deopapa123@ellaclub.com", "ellaclub", "ellafanclub")'''

'''print("    y e   s ".strip())'''

'''names = "Dragons Banana Monkey Apple".split()
for teams in names:
    print(teams)'''

'''def convert_to_celsius(x):
    return (x-32)*5/9

for x in range(0,101,10):
    print("{:>5} F -> {:>10.2f} C".format(x, convert_to_celsius(x)))'''

'''sentence = "Hello World UWU"
print(sentence.replace(" ",""))'''

'''input_string = "Hello I am Deo"
new_string = input_string.lower()
reverse_string = new_string[::-1].lower()

print(reverse_string)'''

'''def is_palindrome(input_string):
    lower_input_string = input_string.lower()
    new_string = lower_input_string.replace(" ","")
    reverse_string = new_string[::-1]
    
    if new_string == reverse_string:
        return True
    else: return False

print(is_palindrome(input("Input a word: ")))'''

'''weather = "Rainfall"

print(weather[:4])'''

'''def replace_ending(sentence, old, new):
	length = len(old)
	# Check if the old string is at the end of the sentence 
	if old in sentence[-length:]:
		# Using i as the slicing index, combine the part
		# of the sentence up to the matched string at the 
		# end with the new string
		i = -length
		new_sentence = sentence[:i] + new
		return new_sentence

	# Return the original sentence if there is no match 
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"'''


'''teams = ["Freshmen", "Sophomores", "Juniors", "Seniors"]
teams[int(input("Which slot to replace: ")) - 1] = input("New team name: ")
print(teams)'''

'''animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

print(f"Total characters: {chars}\nAverage length: {chars/len(animals)}")'''

'''winners = ["Raymond", "Deo", "Tungala"]
for index, person in enumerate(winners):
    print(f"{index+1} -> {person}")'''

'''fruits = ["apples", "pears", "oranges", "fruits"]

count = 0
for element in fruits:
    print (element)
    if count == len(fruits) - 1:
        print ("The final word is: " + fruits[-1])
    count += 1'''

'''names = ["Raymond Deo", "Lei Canta", "James Sab"]
emails = ["<deopapa123@gmail.com>", "<leicanta@gmail.com>", "<jamessab@gmail.com>"]
def display_email(name, email):
    for index, name in enumerate(emails):
        print(f"Name: {name} -> Email: {email[index]}")

display_email(names, emails)'''

'''names = ["Raymond Deo", "Lei Canta", "James Sab"]
emails = ["<deopapa123@gmail.com>", "leicanta@gmail.com", "jamessab@gmail.com"]

def full_emails(name, email):
    result = []
    index = 0
    while index <= len(names)-1:
        result.append(f"{name[index]} <{email[index]}")
        index += 1
    return result

print(full_emails(names, emails))'''

# code that skips every other element
'''def skip_elements(elements):
	# code goes here
	result = []
	for index, element in enumerate(elements):
		if index % 2 == 0:
			result.append(element)

	return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']'''

'''languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
length = []
for language in languages:
    
    length.append(len(language))

print(length)'''

'''languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [ len(language) for language in languages ]

print(lengths)'''

'''z = [x for x in range(0,101) if x%3 == 0]
print(z)'''

'''z = []
for x in range(0,101):
    if x % 3 == 0:
        z.append(x)

print(z)'''


'''def introduction(firstname,middle,surname):
    message = print("My first name is {}. My middle initial is {}. My surname is {}.".format(firstname,middle,surname))
    return message

introduction("Raymond","A.","Tungala")'''

'''country = ["Philippines", "Korea", "China", "Japan", "Australia"]
letter_count = 0
for countries in country:
    letter_count += len(countries)

average_count = letter_count/len(country)
word_count = len(country)

print("The total number of words is {}. The total number of letters is {}. The average number of letters per word is {}.".format(word_count,letter_count,average_count))'''

'''def full_email(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result
    
print(full_email([("raymondtungala@gmail.com", "Raymond Tungala"), ("deobanana123@gmail.com", "Deo Banana"), ("kohanesimp1@gmail.com", "Kohane")]))'''

'''winners = ["Raymond", "Deo", "Tungala"]
for place, name in enumerate(winners):
    print("{} -> {}".format(place + 1, name))
'''

'''file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
file_counts["jpg"] = 14
print(file_counts)'''

'''file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
    print(extension)'''

'''file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for ext, amount in file_counts.items():
    print("There are {} files with the .{} extension.".format(amount, ext))'''

'''file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
total = 0
for value in file_counts.values():
    total += value
print(total)'''

'''def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("count how many letters are in this sentence"))'''

'''def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            # Now add the group to the list of
            # groups for this user, creating the entry
            # in the dictionary if necessary
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)
    return user_groups

print(groups_per_user({"local": ["admin", "userA"],
                       "public": ["admin", "userB"],
                       "administrator": ["admin"]}))'''

'''# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
	# Initialize the variable that will hold 
# the information of the city with 
# the highest elevation 
	return_city = City()

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city1.population > min_population and city1.elevation > city2.elevation and city1.elevation > city3.elevation:

		return_city = city1
	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city1.population < min_population:
		if city2.population > min_population and city2.elevation > city3.elevation:
			return_city = city2
	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city3.population > min_population and city3.elevation > city1.elevation and city3.elevation > city2.elevation:
		return_city = city3

	#Format the return string
	if return_city.name:
		return return_city.name + ", " + return_city.country
	else:
		return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""'''

'''numbers = [4,6,2,7,1]
numbers.sort()
print(numbers)

names = ["Raymond", "deo", "Tungalaaa"]
names.sort(key=len)
print(names)'''

