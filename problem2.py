"""

## Problem 2: I Came, I 'Saur, I Conquered

### Skill you're practicing: Writing conditionals with multiple conditions.

For this problem, put your solution into a file called `problem2.py`.

The mighty Tyrannosaurus rex is the king of dinosaurs, and he does whatever he pleases. When he's hungry, he eats. When he's angry, he fights. When he's bored, he roars. When he's tired, he sleeps! Write a conditional statement that selects one of the following actions for T-Rex based on his current mood. T-Rex's actions are ordered by precedence:

```
If T-Rex is angry, hungry, and bored he will eat the Triceratops.
Otherwise if T-Rex is tired and hungry, he will eat the Iguanadon.
Otherwise if T-Rex is hungry and bored, he will eat the Stegasaurus.
Otherwise if T-Rex is tired, he goes to sleep.
Otherwise if T-Rex is angry and bored, he will fight with the Velociraptor.
Otherwise if T-Rex is angry or bored, he roars.
Otherwise T-Rex gives a toothy smile.
```

#### Starter Code

```python
angry = True
bored = True
hungry = False
tired = False

# Example `if` statement:
if bored:
    print("T-Rex roars! Rawr!")
```

"""

angry = True
bored = True
hungry = False
tired = False

if angry and hungry and bored:
	print("T-Rex eats the Triceratops.")
elif tired and hungry:
	print("T-Rex eats the Iguanadon.")
elif hungry and bored:
	print("T-Rex eats the Stegasaurus.")
elif tired:
	print("T-Rex goes to sleep.")
elif angry and bored:
	print("T-Rex fihgts with the Velociraptor.")
elif angry or bored:
	print("T-Rex roars!")
else:
	print("T-Rex smiles.")

