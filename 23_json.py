# json is an ideal format for transporting data between a client and a server as it uses JavaScript syntax

#differently from python, true and false are not capitalized in json, and instead of none you use JavaScirpt value null

# assume that we saved a json data to a txt file as movie_1.txt
# if there are non ASCII characters in the file, we save the file using utf-8 encoding.

# json.load(f) allows you to load a JSON data from a file or a file-like object
# json.load(s) allows you to load a JSON data from a string 
# json.dump(j, f) allows you to write JSON data to a file or a file-like object
# json.dumps(j) gives outputs a string in proper JSON format.

import json
json_file = open("F://data/movie_1.txt", "r", encoding="utf-8") # the first arguement is the path to the file, the second arguement is r because we are only reading the data, the third arguement is to specify the encoding as utf-8 since the data contains non ASCII characters
movie = json.load(json_file) # loading the data
json_file.close() #closing the file

value = """
	{"title": "Tron: Legacy",
	 "composer": "Daft Punk",
	 "release_year": 2010,
	 "budget": 170000000,
	 "actors": null,
	 "won_oscar": false
	}"""

#to parse this data
tron = json.loads(value)

# assume that there is a dictionary called movie about the movie Gattaca
#to store the data about Gattaca in a database or send it to a remote user we need to convert this dictionary into a valid JSON string, to dachieve that we use the dumps method
json.dumps(movie)

# when we write this code, the resulting JSON file contains numbers instead of non ASCII characters, this is because the jSON library assumes you want the output to be ASCII and will escape all non-ASCII characters.
# to avoid this and allow unicode characters in your string:
json.dumps(movie, ensure_ascii=False)

# create a new object, convert it to JSON and write it to a file.
movie2 = {}
movie2["title"] = "minority Report"
movie2["director"] = "Steven Spielberg"
movie2["composer"] = "John Williams"
movie2["actors"] = ["Tom Cruise", "Colin Farrell", "Samantha Morton", "Max von Sydow"]
movie2["is_awesome"] = True
movie2["budget"] = 102000000
movie2["cinematographer"] = "Janusz Kami\u0144ski" #the n in his last name has an accent with a unicode value of 144.

#to write this to a file in JSON format, we must first open a file in write mode with utf-8 encoding.
file2 = open("F://data/movie_2.txt", "w", encoding="utf-8")
json.dump(movie2, file2, ensure_ascii=False) # first arguement is the dictionary, second is the file
file2.close()










