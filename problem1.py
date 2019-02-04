#!
"""
# Part 2: Code Challenges

## Problem 1: Most Clocks Are Normal, But Some Are Cuckoo!

### Skill you're practicing: Writing conditionals.

For this problem, put your solution into a file called `problem1.py`.

You're making a program for your coworkers that displays a message on their desktop's idle screen. Depending on the time of day, you want to print a different quote. You'll create a variable, `time`, which has an integer value between zero and 23, representing the hour of the day in [military time](https://www.thebalancecareers.com/military-time-3356971), which is a 24-hour clock. Write a conditional statement with Python code that prints exactly one message using the following rules:

```
If the time of day is before 9 a.m. --> print the quote "Morning is wonderful. Its only drawback is that it comes at such an inconvenient time of day."

Otherwise if the time of day is before or exactly 4 p.m. --> print the quote "Working hard or hardly working?"

Otherwise, if the time of day is before 8 p.m. --> print the quote "How did it get so late so soon?"

Otherwise if the time of day is before 10 p.m. --> print the quote "A day without sunshine is like, you know, night."

Otherwise, for any time 10 p.m. or later --> print the quote "Burning the midnight oil!"
```

#### Starter Code

```python
time = 8
```

> **Hint:** Test your code with different values for time of day. Make sure you are only printing one statement, regardless of the value of `time`!

---
"""


time = 8
if time < 9:
	print("Morning is wonderful. Its only drawback is that it comes at such an inconvenient time of the day")
elif time <= 16:
	print("Working hard or hardly working?")
elif time < 20: 
	print("How did it get so late so soon?")
elif time < 22:
	print("A day without sunshine is like, you know, night.")
else:
	print("Burning the midnight oil!")

