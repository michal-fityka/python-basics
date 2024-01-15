programming_dictionary = {}
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again."
}

print (programming_dictionary["Bug"])
programming_dictionary["New_item"] = "This is a new item"
print (programming_dictionary)
for key in programming_dictionary:
  print (key)
  print (programming_dictionary[key])

#Nesting

#Nesting dictionary inside a dictionary
travel_log = {
  "France": {"cities_visited": ["Paris","Dijon","Lille"], "total_visits": 12 }, 
  "Poland": {"cities_visited": ["Warsaw","Cracow","Katowice"], "total_visits": 6 },
  "Spain": {"cities_visited": ["Madrid", "Barcelona", "Seville"], "total_visits": 4 }
}

print (travel_log["France"]["cities_visited"][0])
print (travel_log["France"]["total_visits"])

#Nesting dictionary inside a list
travel_log_nested = [
  {
    "country_visited":"France",
    "cities_visited": ["Paris","Dijon","Lille"], 
    "total_visits": 12 
  }, 
  
  {
    "country_visited":"Poland",
    "cities_visited": ["Warsaw","Cracow","Katowice"], 
    "total_visits": 6 
  },
  {
    "country_visited":"Spain",
    "cities_visited": ["Madrid", "Barcelona", "Seville"], 
    "total_visits": 4 
  }
]

print(travel_log_nested[0]["cities_visited"][0])
