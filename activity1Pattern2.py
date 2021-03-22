"""
Pattern of asterisks that is based on user input. Example:

"
How many totalNumberOfLines do you want? User enters 5
     *    (1 asterisk with 5 spaces before)
    * *   (2 asterisks with 4 spaces before)
   * * *  (3 asterisks with 3 spaces before)
  * * * * (4 asterisks with 2 spaces before)
 * * * * *(5 asterisks with 1 space before)
"

The asterisks are separated by a space, which seems to be hard to remove without messing up the pattern
"""

totalNumberOfLines = int(input("How many lines do you want? "))

# One iteration of this loop prints a line of the pattern
for numberOfCurrentLine in range(0, totalNumberOfLines):
    # Loop for spaces
    for space in range(0, totalNumberOfLines - numberOfCurrentLine):
        print(end=" ")

    # Loop for asterisks
    for asterisk in range(0, numberOfCurrentLine + 1):
        print("*", end=" ")

    # This will make a new line for the next step of the pattern
    print()
