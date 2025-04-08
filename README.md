# GitLabAssignment

Repo for the git lab assignment in Software Engineering in Practice course

## Your tasks for this assignment

After this delightful presentation, you have to complete the following simple tasks.  
Before starting, you'll need to download Git on your system and configure your username and email in case you haven't already.  
Also, task2 is created in Python so you will need Python 3 in your computer and pip in your path.  

---

## Task 1

1. **Initialize a Git repository**

   - Create a directory somewhere on your computer and initialize a Git repository in it (ha ha).
   - Download the files in the `task1` folder, move them to your directory, and make a commit titled 'Initial commit'.
   - Do not `fork` or `clone` this repository for task1, this is important for later.  

2. **Change egg color**

   - Assume this is a little game your boss asked you to design.
   - You got a message saying that the eggs should be a dark red color to go with Orthodox traditions.
   - Change the egg color and commit your change.

3. **Modify the theme and keybinds**

   - Your boss decided that the rainbow theme is not very nice and wants to change the keybinds for the 3rd Easter egg.
   - This is an important change, so do it on a different branch.
     - Create a branch named `thirdEasterEgg` and start making changes.
     - The rainbow theme should be a top-to-bottom gradient without the line splits.
     - The keybind should be the cheat code for Mega Jump in GTA San Andreas (look it up).
     - Make two commits (one for each change), but **don’t merge yet**.

4. **Add more eggs with different colors**

   - A new request: “We should add more eggs with different colours.”
   - Create another branch from `main` named `moreEggs`.
   - Make your changes and commit them.
   - Then, someone suggests changing the gradient from rainbow to blue-orange so you do that too, and commit the change.

5. **Merge branches and handle conflicts**

   - Start by merging `thirdEasterEgg` into `main`.
   - Follow it up by merging `moreEggs` into `main`.
   - You'll encounter a conflict because both branches changed the gradient.
   - Choose your preferred gradient and resolve the conflict.

6. **Boss-requested changes**

   - Knowing how indecisive your boss can be, create a new branch `changes` from `main` and commit the following **separately**:

     1. Make some of the eggs dark green.
     2. Change the background colour to yellow.
     3. Change the rainbow gradient into a blue-green gradient.
     4. Make the eggs 20px wider.
     5. Make the eggs 10px shorter (height).
     6. Change the basket emoji into a candle emoji (🕯).

   - The boss thinks it's too much and asks you to keep only 3 of the changes.

   - Pick 3, **squash them into a single commit** named `"Three changes"` and place them into the 'main' branch.

     - There are two Git commands for this—use whichever you prefer.

7. **Document your branch logs and (optionally) command history**

   - Run the following commands:
     ```bash
     git log > branch_name-log.txt
     ```
   - (Run `git checkout branch_name` before logging each branch.)
     
> You'll be graded based on the quality of your commits—so keep them **frequent, short, and clear**.

---

## Task 2

For this task, you'll work in pairs so find a friend and partner up.  
> *Note: this task was originally designed in Python using the Streamlit framework.
> You are free to choose any other language or framework but Python/Streamlit is highly recommended*  

1. One of you should:

   - Create a **private GitHub repository** named `git-lab-assignment-task2`.
   - Invite your partner to collaborate.

2. In the `task2` directory of this repository you will find the following files:

   - `stockmarket.py`
   - `requirements.txt`
   - `TASK2.md`
   - `STREAMLIT.md`
  
   Transfer them to your repository.

3. There are six ideas for improvement labeled:

   - `#E` for easy to implement
   - `#H` for hard to implement

4. Divide the work evenly so **each person implements:**

   - One `#E` task
   - Two `#H` tasks

5. You'll be graded based on:

   - a) Quality and quantity of commits (frequent, short, proper messages)
   - b) Use of branches for hard features before merging into `main`

6. Invite the instructor (`ManolisPapa`) to your repository.

> *If you can't find a partner, you can do it solo. Just specify that in Task 3.*

---

## Task 3

This one’s fairly simple.

1. After completing the above tasks:

   - Fork this repository.
   - Add a directory named:
     ```
     GithubUsername-IdentificationNumber
     ```
     (e.g., `ManolisPapa-8220116`)

2. In this directory, add:

   - Your `.txt` files from **Task 1**
   - A `task2.txt` file that includes:
     1. A link to your Task 2 repository
     2. Who your partner was and which improvements each of you implemented
     3. Something fun or interesting about yourself
        > (Points will be deducted if what you write isn't interesting 😄)

3. Open a **pull request** so your changes can be added to this repository.

4. And that's it. If you have any questions feel free to ask me, you can find me via email at t8220116@aueb.gr or via Instagram @manolis_pap14.
