import csv, difflib
               
print ("Welcome to the Python Film Finder. \nPlease select an option from below.")

foundFilms = 0
print ("Please type in a film name and we will try and match it> ")
typedFilm = input("> ").upper()
with open('Films Only.csv') as csvfile:
    filmReader = csv.DictReader(csvfile)
    for row in filmReader: 
        percentageMatch = difflib.SequenceMatcher(None, typedFilm, row['Film'])
        result = round(percentageMatch.ratio()*100,2)
        if result > 50:
            foundFilms = foundFilms + 1
            print ("Did you mean", row['Film'])
    if foundFilms == 0:
        print ("We could not find any matches, sorry")
