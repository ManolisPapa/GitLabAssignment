# GitLabAssignment
Repo for the git lab assignment in Software Engineering in Practice course

## Your tasks for this assignment  
After this delightful presentation, you have to comlete these following, simple tasks.  
Before starting you'll need to download git in your system and configure your username and password in case you haven't already.  

## Task 1: 
Create a directory somewhere in your computer and initialize a git repository in it (ha ha).  
Download the files in the task1 folder, move them to your directory and make a commit.  

Let's assume now, for the sake of this exercise, that this is a little game your boss asked you to design.  
You just got a message saying that the eggs should be a dark red color to go with Orthodox traditions.  
Change the eggs color and commit your change.  

That's not it, your boss decided that the rainbow theme is not very nice and  
also believes you should change the keybinds for the 3rd easter egg.  
This is an important change to your project, so it should be performed in a different branch.  
Create a branch named thirdEasterEgg and start making your changes there.  
Firstly the rainbow theme should be top to bottom gradient without the line splits  
and secondly considering your boss is an avid GTA fan,  
the key bind should be the cheat code for Mega Jump in GTA San Andreas (look it up). 
You can commit your changes (two different commits) but don't merge yet

Another message comes up saying "We should add more eggs and with different colours".  
You decide, so as to not mix your previous task with this one, to create another branch from 'main' very creatively named 'moreEggs'.  
Create your branch, make your changes and commit them.  
While working on this branch, someone suggests you change the gradient from rainbow to blue-orange so you do just that.  
As always, commit your changes.

Now it's time to merge these branches back into 'main'. Start with 'thirdEasterEgg' since it has less modifications.  
Merge 'thirdEasterEgg' into 'main'. Follow it up with merging 'moreEggs' to 'main'. Something went wrong...  
You figure out there's a conflict between the two branches, because you changed the gradient in both branches.  
Make a choice, pick which gradient you like best and solve the conflicts. 

Lastly, your boss asks you to make some changes.  
Knowing how indecisive and fickle your boss can be,  
you create a new branch 'changes' from 'main' in order to commit the following:  
(Commit after every change and message accordingly, this is important)  
1. Make some of the eggs dark green.
2. Change the background colour to yellow.
3. Change the rainbow gradient into a blue-green gradient.
4. Make the eggs 20px wider.
5. Make the eggs 10px shorter (height).
6. Change the basket emoji into a candle emoji (&#x1f56f;).  
The boss doesn't like all of the changes and thinks they're too much, so you're tasked with picking 3 of them and placing them in the 'main' branch.
You should also squash them into a single commit named "Three changes". There are two git commands for this, so pick (ha ha) whichever you prefer.

To complete this task you should document your branch logs and (optionally) your command history.  
You can do this by running the following commands:  
    git log [branch_name] > branch_name-log.txt (do this for every branch after first doing git checkout branch_name)  
    doskey /history > history.txt (this returns all the commands you used that are in memory. You can remove any commands you think contain unimportant or sensitive information)  

You'll be graded based on the quality of your commits, so frequent, short and clear messages

## Task 2:
For this next task, you'll work in pairs so text one of your friends and partner up.  

One of you should create a private Github repository named git-lab-assignment-task2 and invite the other to collaborate.  
In directory task2 you will find files named stockmarket.py, requirements.txt and TASK2.md, transfer them to your private repository.  
There are six ideas for improvement labeled #E for easy to implement and #H for hard to implement. You should split your work evenly so  
each partner implements one #E task and two #H tasks.  
You'll be graded based on:  
a) The quality and quantity of your commits, that means frequent, short and proper messages  
b) The use of branches for implementing the hard features, before merging them into 'main'  

To complete this task, you need to invite me (ManolisPapa) to your repository.  
(If you can't find a partner for this task, you can complete it on your own, just make sure you specify that you went solo in task3)  

## Task 3:
This one should be fairly simple. After you complete the above tasks, you need to fork this repository and add the following:  
A directory named 'Github username-Identification number' (e.g. ManolisPapa-8220116).
In this directory you should add your .txt files from task1 and a task2.txt file in which you should provide  
1. A link to your repository for task2,  
2. Who you partnered up with and which improvements each of you implemented and  
3. Something fun or interesting about yourself (points will be deducted if I don't find what you wrote interesting)

After doing this, you need to open a pull request so your changes can be added to this repository.  


