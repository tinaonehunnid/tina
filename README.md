# For next time

1. Install python
2. Install Visual Studio Code
3. Create a folder on your desktop called `projects`
4. Drag this `Data-Science-w-Cristina` folder into your `projects` folder
5. Find and open your terminal application and do the following:
    - Run `pwd` to see the full path on your computer where you are.
    - Run `ls` to list the contents of the current directory that you are in.
    - Use the `cd` command to go into one of the folders that you just listed out.
    - Run `pwd` again to see how the full path has changed since you opened your terminal.
    - Run `cd ..` to go back up one directory (remember that `..` means "the parent directory relative to where you are")
    - Run `pwd` again to see how the full path has changed again.

    - Now using `ls` and `cd`, navigate to the `projects` directory that you created in step #3
        - If you get lost, you can always check the full path with `pwd`, or just close and reopen your terminal.
    - Now enter the `Data-Science-w-Cristina` folder and list the contents of the folder to make sure that everything is there.

    - Now make sure that python is installed by running `python3 --version`.
        - If it tells you the version of python you've installed, then you're a gangster
        - If it throws an error, double check that you installed python correctly.

    - Now there is a file in here called `surprise.py`, run the script by running `python3 surprise.py`
    - Now open this `Data-Science-w-Cristina` project folder in Visual Studio Code
    - Open the `surprise.py` file to see what's written inside.
    - This script uses a core programming concept called a `for loop`, where I can run the same block of code
        a certain number of times.
    - Go ahead and change the value of the variable to something else.
    - Close your terminal application.
    - Find and open the integrated terminal within Visual Studio Code
    - First, take a look at which directory THIS terminal starts you at by running `pwd`
        - It SHOULD be the full path to the `Data-Science-w-Cristina` project folder. If it's not, navigate to it.
    - Run `python3 surprise.py` to see how the ouput of the program has changed since you modified the variable.    

    - If you did all of this and you're grasping the idea of moving "into" and "out of" directories, you've literally
        already completed like a semester of computer science at a university (and that isn't an exaggeration)

6. Extra Credit

Create a new folder in your `projects` folder called something like `number-guessing-game`.
Open that project in VSCode and create a file called `index.py`. Create a game that asks for the user to guess
a random number between 1 and 10. The user will input a number and press `enter`. The game should compare the
users guess to a random number between 1 and 10. If the user gets it correct, then print out `You are literally a gangster dawg`.
And if they guess it wrong, then tell them `I think McDonalds is hiring...`.

Hints:
    - To gather user input, you can use the `input` function
    - To generate a random number you can use the `random` module that comes with python
    - You will need to use an `if` statement which you can see an example of in the `index.ipynb` notebook file that we made yesterday.