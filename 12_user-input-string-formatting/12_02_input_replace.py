# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please



result = ""

entry = str.lower(input("\ngive us a sentence there, champ.\n "))
symbol = input("\ngreat. how about a symbol then?\n ")
print("\nlet's take a look.\n")

letter_to_replace = entry[0]
for i in entry:
    if i == letter_to_replace:
        result = entry.replace(i, symbol) 
        break
print(f"\nhow's this look then?\n\n {result}\n")
        
    