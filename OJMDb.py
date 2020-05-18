#Movie Database
import pandas as pd


FilmList = []
#Creating a Class for all the films I want to add to my database
class Films:
    def __init__ (self, Title, Director, Studio, Series, Year, RunTime, Rating):
        attributes = [Title, Director, Studio, Series]
        self.Title = Title
        self.Director = Director
        self.Studio = Studio
        self.Series = Series
        self.Year = Year
        self.RunTime = RunTime
        self.Rating = Rating

        
#This adds all of the data about each film I've added to the class into a list,
#so I dont have to hand type in each attribute of each film when I create the database
        FilmList.append([Title, Director, Studio, Series, Year, RunTime, Rating])
        

            
#The following is each film and its details I have added to my database
StarWars1 = Films("Star Wars Episode I: The Phantom Menace", "George Lucas",
                  "Lucasfilm", {"Series" : "Star Wars", "Installment": 1},
                  1999, 136, 6.5)
StarWars2 = Films("Star Wars Episode II: Attack of The Clones", "George Lucas",
                  "Lucasfilm", {"Series" : "Star Wars", "Installment": 2},
                  2002, 142, 6.5)
StarWars3 = Films("Star Wars Episode III: Revenge of The Sith", "George Lucas",
                  "Lucasfilm", {"Series" : "Star Wars", "Installment": 3},
                  2005, 140, 7.5)
StarWars4 = Films("Star Wars Episode IV: A New Hope", "George Lucas",
                  "Lucasfilm", {"Series" : "Star Wars", "Installment": 4},
                  1977, 121, 8.6)
StarWars5 = Films("Star Wars Episode V: The Empire Strikes Back", "George Lucas",
                  "Lucasfilm", {"Series" : "Star Wars", "Installment": 5},
                  1980, 124, 8.7)
StarWars6 = Films("Star Wars Episode VI: Return of The Jedi", "George Lucas",
                  "Lucasfilm", {"Series" : "Star Wars", "Installment": 6},
                  1983, 131, 8.3)
StarWars7 = Films("Star Wars Episode VII: The Force Awakens", "J.J. Abrams",
                  "Lucasfilm", {"Series" : "Star Wars", "Installment": 7},
                  2015, 138, 7.9)
StarWars8 = Films("Star Wars Episode VIII: The Last Jedi", "Rian Johnson",
                  "Lucasfilm", {"Series" : "Star Wars", "Installment": 8},
                  2017, 152, 7.0)
StarWars9 = Films("Star Wars Episode IX: The Rise of Skywalker", "J.J. Abrams",
                  "Lucasfilm", {"Series" : "Star Wars", "Installment": 9},
                  2019, 142, 6.7)
Moon = Films("Moon", "Duncan Jones",
             "Sony Pictures Classics", "'Independent'",
             2009, 97, 7.9)
Primer = Films("Primer", "Shane Carruth",
               "StudioCanal", "'Independent'",
               2009, 77, 7.9)
LoTR1 = Films("The Lord of The Rings: The Fellowship of The Ring", "Peter Jackson",
              "New Line Cinema", {"Series" : "The Lord of The Rings", "Installment": 1},
              2001, 178, 8.8)
LoTR2 = Films("The Lord of The Rings: The Two Towers", "Peter Jackson",
              "New Line Cinema", {"Series" : "The Lord of The Rings", "Installment": 2},
              2002, 179, 8.7)
LoTR3 = Films("The Lord of The Rings: The Return of The King", "Peter Jackson",
              "New Line Cinema", {"Series" : "The Lord of The Rings", "Installment": 3},
              2003, 201, 8.9)
Warcraft = Films("Warcraft", "Duncan Jones",
                 "Blizzard Entertainment", "'Independent'", 
                 2016, 123, 6.8)
SourceCode = Films("Source Code", "Duncan Jones",
                    "The Mark Gordon Company", "'Independent'", 
                    2011, 93, 7.5)
             

#This allows me to display the whole table in the shell
pd.options.display.width = 0

#this is creating lists inside a list for easy entry into the database, where each embedded list holds data on all of the films
#differentiated by the attributes stated in the class aka the column names
Db = []
for n in range(len(FilmList[0])):
    Db.append([])
    for m in range(len(FilmList)):
        if n == 3 and type(FilmList[m][n]) == dict:
            Db[n].append(FilmList[m][n]["Series"])
        else:
            Db[n].append(FilmList[m][n])

df = pd.DataFrame({"Title":Db[0], "Director":Db[1], "Studio":Db[2], "Series":Db[3], "Year":Db[4], "Run time":Db[5], "Rating":Db[6]})

df.head()

def output():
  loop = True
  print("How would you like to view the database?")
  print("You can specify by \n'Title', 'Director', 'Studio', 'Movie Series', 'Year' of release, 'Run Time' or IMDb 'Rating'")
  DbFormat = input(" - ")
  if input("Ascending or Descending? \n- ").capitalize() == "ascending":
    print(df.sort_values([DbFormat.capitalize()]))
  else:
    print(df.sort_values([DbFormat.capitalize()], ascending = False))

output()
"""
df.to_html()
df.to_csv("OJs_MDb.cvs")
"""
    
