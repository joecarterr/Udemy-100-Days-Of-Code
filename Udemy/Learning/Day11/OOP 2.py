from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name:", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type:", ["Electric", "Water", "Fire"])
table.add_column("Does Ash Like?:", ["Loves", "Likes", "Likes"])

# alignments in files
table.align = "l"
print(table)
