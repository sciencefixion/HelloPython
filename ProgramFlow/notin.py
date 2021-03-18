activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")
#.casefold() is a bit like .downcase in Ruby but works a bit better in languages like German that has different characters for certain lowercase letters