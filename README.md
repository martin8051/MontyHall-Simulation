## Monty Hall Simulation
---

### Description
---
The Monty Hall Problem is a famous brain teaser made famous by the TV game show called “Let’s Make a Deal.” It was named after the show’s host Monty Hall. The game works as follows, a contestant is shown three doors: one which has a valuable item behind it, and two which have nothing or something of no value behind them. The Host first asks the contestant to pick a door at random. After which the host reveals one of the non-prize doors by opening it and then asks the contestant if he would like to switch doors. This is where the key part of the puzzle occurs, whether or not to switch doors. According to the mathematical claims, it makes more sense to switch doors than to keep your original choice. Although we trust our professor and the information he is giving us, we decided to run some simulations. 

The goal of this project is to simulate the game and see if choosing a different door would actually help you win more often

### Design/Approach
---
We approached the problem by creating various types of policies to be tested at different iterations to help compare our different strategies. Our first policy would be to implement the choice to switch doors after randomly picking one and being shown a non-prize door. The second policy was the opposite of the first and instead of switching to the other door, the contestant would stick with his original choice. Our third policy was the same as the first, but we decided instead of the host choosing to open a non-prize door, we pretended he slipped on a banana peel and accidentally opened a door at random, and if the opened door happened to be the prize door then the contestant would lose. Policy 4 is the same as the second policy but with the introduction of the banana peel similar to that in policy 3. We also wanted to see how these policies would affect the outcomes with an increase in another factor, the number of total doors in the game. We figured the total number of iterations for each test would also need to be considered as smaller iterations might have different averages compared to larger ones. To sum up we decided to test our four policies with five different amounts of doors: 3, 6, 9, 20 and 100. We ran these simulations and averaged the results at different amounts of tests, those being, ten, one hundred, one thousand, ten thousand, one hundred thousand and one million iterations. Our choice for implementation was to create a python program to run/output the simulation tests. For every iteration the system randomly chose a door to be the prize door and randomly chose which door the contestant would pick to keep the results fair. It took a while to code the program and run the simulations because the test time increased substantially as the number of iterations per test increased. This allowed us to get more stable estimates for the outcomes.
  
### Instructions
---
You can run our simulation using any python compiler and running `main.cpp`  and checking the terminal output for the results of each of the different policies. 
