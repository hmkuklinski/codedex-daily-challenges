
def find_missing_colors(grid):
  # establish colors
  colors = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫"]
  # create a dictionary --> map colors to the count
  found_colors = {}
  # for each item in the row, see if exists in dict (if so? add 1: create entry and set to one)
  for row in grid:
    for entry in row:
      #entry already exists:
      if entry in found_colors:
        found_colors[entry] +=1
      #entry doesn't exist:
      else:
        found_colors[entry]= 1
  
  #check to see what colors aren't in the dictionary!
  not_found = []
  for color in colors:
    # color isn't in dictionary--> add to not_found list
    if color not in found_colors.keys():
      not_found.append(color)
  #return all colors not found
  return not_found

# input1=   [["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟥"],
#   ["🟨", "🟩", "🟦", "🟪", "🟥", "🟧", "🟨"],
#   ["🟦", "🟥", "🟧", "🟨", "🟩", "🟪", "🟦"],
#   ["🟩", "🟦", "🟪", "🟥", "🟧", "🟨", "🟩"],
#   ["🟧", "🟨", "🟩", "🟦", "🟪", "🟥", "🟧"],
#   ["🟪", "🟧", "🟨", "🟩", "🟦", "🟥", "🟪"],
#   ["🟥", "🟦", "🟩", "🟪", "🟨", "🟧", "🟦"]]

# input2 = [["🟥", "🟧", "🟨", "🟩", "🟦", "🟥", "🟧"],     
# ["🟨", "🟩", "🟦", "🟥", "🟨", "🟩", "🟦"],     
# ["🟥", "🟧", "🟨", "🟩", "🟦", "🟥", "🟨"],     
# ["🟩", "🟦", "🟥", "🟧", "🟨", "🟩", "🟦"],     
# ["🟨", "🟥", "🟧", "🟨", "🟩", "🟦", "🟥"],     
# ["🟦", "🟩", "🟨", "🟥", "🟧", "🟩", "🟦"],    
# ["🟥", "🟧", "🟨", "🟩", "🟦", "🟨", "🟥"]]

# print(find_missing_colors(input1))
# print(find_missing_colors(input2))