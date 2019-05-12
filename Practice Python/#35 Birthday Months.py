Exercise 35 (and Solution)

This exercise is Part 3 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 2, and Part 4.

In the previous exercise we saved information about famous scientists’ names and birthdays to disk. In this exercise, load that JSON file from disk, extract the months of all the birthdays, and count how many scientists have a birthday in each month.

Your program should output something like:

{
	"May": 3,
	"November": 2,
	"December": 1
}
Discussion

You already have the skills to achieve this exercise with concepts we’ve already covered: for loops, dictionaries, and basic arithmetic. However, I want to talk about a Python built-in called a Counter.

A Counter takes a list and counts how many of each element were in the list. To use the Counter, first import it from collections:

from collections import Counter
This lets you use the Counter data structure built into Python in your program. Then, give it a list:

sandwiches = ["ham", "cheese", "roast beef", "ham", "cheese", "roast beef", "ham"]
c = Counter(sandwiches)
If you print(c), you will see this:

Counter({"ham": 3, "roast beef": 2, "cheese": 2})
This means there are 3 ham, 2 roast beef, and 2 cheese sandwiches in my list. I can get this information directly from the Counter:

>>> print("There are {} ham sandwiches".format(c["ham"]))
There are 3 ham sandwiches
Hope this is useful!
