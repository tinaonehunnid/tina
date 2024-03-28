# WELCOME TRAVELER 🚀🗿🥸
---
It appears you have found that which you seek. Want to learn programming, do you? Mmm? Your powers for good, you must use them for... the dark side, you must resist. Easily tempted, the young jedi is... Learn the ways of the python, you must. Master the data science, and soon the dark side of javascript, you will no longer be tempted.

Complete these steps young padawan learner, and your lightsaber, you will obtain...

## Overview
---
The website you are on right now is called "GitHub". This is where pretty much every developer stores their code. Think of it as basically "Google Docs" but for coding.

This is going to be where we will store and share programming quests! So put on your hacker
hat, because we're about to hack the mainframe 🧑🏻‍💻👩🏻‍💻

Now that you've figured out how to use ChatGPT, your quests have grown 10 fold! But have no fear, I have full faith that you will absolutely CRUSH this 😘

There may even be some surprises along the way...? 👀

LETS GET STARTED! 🔥🚀

### Quest #1
---
The first thing you need to do is set up this project in your `projects` folder. In order to do this, you must learn how to "Clone a Repository". A "repository" is just a folder of programming files. For example, each folder in your `projects` folder on your computer, is considered a "repository".

GitHub allows you to take that repository, and push it to the cloud, so that other people can "Clone" it to their computer.

I've pushed this repository called "tina" to github, and your job is to clone it to your computer so that you can work with the files inside.

Here's how you'll do that...

1. Open your terminal application
2. Using the `cd` and `ls` commands, navigate to your `projects` folder on your desktop.
3. Look at the current contents of your projects folder, you should only see the `Data-Science-w-Cristina` folder in there so far.
4. There is a tool in your terminal (also known as your "command line") called `git`. This command is what allows you to interact with GitHub to push and pull code. And since you're SOOO SMART with ChatGPT, why do you ask HIM how to clone a repository with `git`!
5. Once you've cloned the repository, list the contents of your `projects` folder again, you should now see the `tina` folder in there. That's where we'll be working from now on :)

> But don't open VSCode just yet! I will explain what's in this folder and how to navigate it, just keep following your quests 😘

### Quest #2 - Finding the Diamond in the Rough
---
***...Back in character...***

Ahhhh so you made it through your first challenge ey?? Well rest assured, this next one will not be as easy! For I have hidden your diamond somewhere in this repository, and it's your job to find it! For even the most powerful jedi are no match for my programming powers 🧙🏻‍♂️

...alright this is getting way too nerdy... i hid a file in here, you gotta find it...

Here's how you're going to do it!

First things first, let's look at our whole directory structure right now, starting with your `projects` folder:
```
projects/                               <- this is your projects folder
    Data-Science-w-Cristina/            <- from your previous mission
    tina/                               <- our new repository for going on missions
        introduction/                   <- a copy of your first mission
        padawan-adventure/              <- your current mission!
```

1. First you need to navigate to the `projects/tina/padawan-adventure` directory to continue on your mission!

2. Once you're in the `padawan-adventure` folder, list the contents inside. There's a folder in here called "cave-of-darkness". There are many sub-directories inside of the dark and scary cave... it's your job to navigate all the way down the cave, to the depths of...uhh...darkness i guess? You'll know that you've reached the bottom when you find the HAYSTACKS that your treasure is buried within ;)

3. Somewhere in here is a file called `diamond.csv` which contains the key to your treasure! Your job is to find it! But how will you find it, with all these `.txt` files in the way? Well... that's the CHALLENGE! There's a tool for your command line called `rm` (means "remove") that you can use to absolutely OBLITERATE these haystacks. The only thing you have to pass to the `rm` command is the name of the file you want to delete.

4. Ugh... this is going to take forever though! There are SO MANY, how will you EVER find your TREASURE??? Rest assured, you can ask ChatGPT "how to remove all files in the current directory that have the `.txt` extension in the file name" (your treasure has the `.csv` extension).

5. Once you've obliterated all the haystacks you should see your `diamond.csv` file left! Now excavate this diamond and move it all the way back up through the `cave-of-darkeness` to the base of your `padawan-adventure` folder. It's time to look inside and see what we find!

### Quest #3 - Data is Beautiful :)
---
If you have gotten this far, traveler, you have indeed proven yourself to the jedi council, but you have yet to complete your biggest challenge yet! For this time I will SURELY stop you! Now... unsheath your lightsaber, and open the `tina` repository in VSCode to face your final test...

You should see both your `introduction` and `padawan-adventure` folders in your file explorer on the left hand side of VSCode. This is nice because you can always easily look back at previous missions for reference.

Here is your mission:

1. Open the `padawan-adventure` folder in the file explorer on the left.
2. Create a new file in there called `index.ipynb` and open that notebook file.
3. In the first cell, import the `matplotlib` package and try to run it (you can ask ChatGPT "how to import matplotlib in python").
4. You will likely get an error when you try to execute that cell. This is expected, because you probably don't have the `matplotlib` package installed. So open the VSCode integrated terminal and run `pip3 install matplotlib` to install it (you can do this in your regular terminal program too, but I just like working in the integrated terminal).
5. Once you've installed `matplotlib`, go back to your notebook file and run your first cell again to `import matplotlib`
6. Once that works, now go BACK to your first cell, and you're going to also import `pandas` (you will likely get another error if you try to run it, so go through the same steps to install `pandas`).
7. You should have both `pandas` and `matplotlib` imported into your notebook file!
8. Now create a new cell and use `pandas` to read your `diamond.csv` file into a dataframe called `df`. If you completed the previous quest, the `diamond.csv` should be in your current working directory.
9. Now print that dataframe out to see what's inside like this `print(df)`
10. Looks like we've got a bunch of `x` and `y` coordinates in here, so let's use `matplotlib` to plot this data. `matplotlib` has a function called `plot` which allows you to plot `x`,`y` coordinates on a graph. Use ChatGPT to plot the data.
11. Now that you can see the data, let's do a little bit of data science. Let's calculate the maximum, minimum, mean, standard deviation, and median values for the `x` column and the `y` column. Ask ChatGPT how to calculate each one of these statistics from a column in a pandas dataframe.
12. Save each of these statistics to a descriptive variable, something like `x_mean` or `y_standard_deviation` so that we know which variable is set to which value.
13. Then, you're going to organize these variables into a python dictionary so that we can keep this data in an organized format. Here's how the dictionary should be organized:
```python
data = {
    'x': {
        'mean': <your mean value>,
        'median': <your mean value>,
        # ... and so on
    },
    'y': {
        # ... same thing over here
    }
}
```
14. Then, I want you to save the contents of this dictionary to a file called `polished_diamond.json`. The format of this file is called `json` and it is an extremely common way of representing data in programming. `json` is almost identical to a python `dictionary` in the way that it looks. Go back to the first cell in your notebook file where you imported `matplotlib` and `pandas`, and add a new line to `import json` which is pythons built-in module for writing and reading `json` files. Execute that first cell again to import it into your environment.
15. Finally, ask chatgpt "how to dump a python dictionary into a json file called `polished_diamond.json`. And once you've done that, open the file you just created and look at it, it will look very similar to the dictionary you created in python.

### Quest #4 - I lied, THIS is your final quest
---
You have survived my most powerful blows... my powers are growing weak, but I will make one last attempt at stopping you!

Your final mission is to get this file back to me! But we are programmers, we don't use EMAIL!! We use GITHUB!!! I'm going to show you how to "Commit your changes to your repository, and push them to GitHub".

1. Go to your terminal
2. Navigate to the "Root" of this repository. (The "root" or "base" of this git repository is the `tina` folder)
3. Run the following command: `git status`
    - This will show you all the changes that you have made in this repository (in other words, which files have been modified, deleted, added, etc.)
4. Run the following command: `git add .`
    - Here's the analogy of what's happening when you do this... image you're in an auditorium with a ton of people in the audience. Each person in the audience is a file in your repository that has been modified, added, deleted, etc. When you say `git add .` you're essentially saying, "everyone in here (remember that `.` means the current directory), get up on the stage". Sometimes you don't want everyone on the stage (you can add each file individually, but `.` is a shortcut that means "everyone get up there").
5. Run the following command: `git commit -m "Cristinas first commit"`
    - Continuing with the analogy: In this part, there's a photographer that snaps a picture of everyone on the stage. Again, you might not want to take a picture with everyone from the audience, but for this example, we just assume that you want to "Commit ALL your changes".
6. Run the following command: `git push`
    - Continuing with the analogy: This part is essentially taking the photograph (or "Commit") and leaving it at the post office (i.e. GitHub). Once you've moved your photograph to the post office, now I can come pick it up (i.e. I can pull your changes from the GitHub repository).
7. And you're done!

## THE END
---
Congratulations padawan, for you have graduated to the ranks of the jedi! You must always do your best to use your new powers for good, for the world need not more malevolence... it is our duty to use our powers to make the world a better place, a long and perilous journey, but a meaningful one nonetheless. Hope you had fun on this little programming & data science adventure baby! 😘

*aaaaaaaand scene*

> P.S. If you're curious how I was able to generate the "cave-of-darkness" or how I created all the "HAYSTACKS" in the cave, I wrote python scripts to generate them! I left both of those scripts in the `padawan-adventure` folder so you can see what they look like if you're curious :)