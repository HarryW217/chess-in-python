# Chess in Python using Pygame!

## You say "Wanna play Chess?", and my answer is "Yes!"

Chess is the greatest game there is. In an effort to improve my Python skills, I thought it would be a tonne of fun to recreate the game using the language. 

Following along with a tutorial from Youtuber [LeMaster Tech](https://www.youtube.com/@lemastertech), this project allows users to play a two-player Chess game. You can move all the pieces in the usual ways, view them as cool assets (also provided by LeMaster) on a drawn Chess board, and when a King is in check, a red boarder will flash on it's square indicating trouble!

In addition, captured pieces can be seen on the right side of the screen to emulate a real Chess game where this material would be placed to one side, and players can resign if they wish, declaring their opponent the winner. 

In a twist from traditional Chess, this game grants a player a winner when the King is taken by the opposing team, rather than put in Checkmate. I attemped to implement Checkmate functionality to complement the existing project, which you can currently see in [another branch](https://github.com/HarryW217/chess-in-python/tree/alternative-checkmate-functionality) that I may develop on in the future! 

## What I learned

`Python Programming`: I improved my Python programming proficiency as I had set out to do, using the appropriate syntax, data structures and functions to achieve various features. Steering away from the tutorial to try and implement Checkmate functionality especially got me to independently code a Python sequence. I feel like the next step will be to try and limit nested for loops and find cleaner alternatives!

`Game Development`: This is one of my first forays into game development, where I have explored concepts such as game loops, event handling and graphics rendering for the first time. Event handling in particular was very fun; its cool how Pygame can detect the clicks of certain buttons! It is similar to event handling I had already learned much of with JavaScript, so it was nice to expand my knowledge of this concept in a different context. 

`Pygame`: The Pygame library itself introduced me to a powerful framework for developing 2D games with Python. I now have some familiarity with Pygame's features for rendering assets, graphics and user input. 

`Algorithmic Thinking`: With Chess being quite an algorithmic game, it made sense that I would have to work with algorithms in this project. Following LeMaster's tutorials, I could easily understand move validation and piece movement algorithms, as well as how the Chess board and information sections are organised and drawn on the screen. 

## Instructions (How to play!)

Wanna work your way to becoming a GM? Or perhaps you want to build on the Checkmate feature and shape this game to be more like the traditional Chess setup? Well, you can!

Feel free to clone this repo in your terminal while in the directory you wish to house it: 

```
git clone https://github.com/HarryW217/chess-in-python.git
```

I would recommend using VS Code. If you wish to view and play the game, simply run the main.py file. 

Happy Coding (and Chess playing!)

## Acknowledgements

LeagueSpartan-Bold font provided by FontSquirrel: https://www.fontsquirrel.com/fonts/list/popular 

Special thanks to LeMaster Tech, whose tutorial I followed along with this recreate this Chess game and inspired me to look into alternative functionality! You can watch it here: https://www.youtube.com/watch?v=X-e0jk4I938&t=7465s 