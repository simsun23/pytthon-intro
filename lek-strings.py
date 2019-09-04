firstname = "simon"
middlename = "elev"
lastname = "sundberg"

nickname = "n/a"

# för.efternamn
# simon.sundberg
# firrstname[3].lastname[3]

#print(firstname[0:3].lower() + "" + lastname[0:3].lower() + "19")


username = firstname[0:5].lower()
username += "."
username += lastname[0:8].lower()
username += "@"
username += middlename[0:4].lower()

print(username)

#print(lastname.translate())





tecken = """paranteser(), 
hakparenters[], 
måsvingar{} , 
kolon:, 
semikolon;, 
komma, 
\" dubbelfnutt
\' enkelfnutt"""

#print(tecken[13:37])
