# SR_Dev_Test
Software engineer coding exercise for Sports Reference, October 2022.

This python program outputs out Cristiano Ronaldo's domestic league statistics in an HTML table to the file `joezobel_sr_test.html` and prints the table to console.

## Installation/Run Instructions
To generate `joezobel_sr_test.html` containing Cristiano Ronaldo's domestic league statistics, simply execute `main.py` on your system:

```
python3 main.py
```

## Requirements
This program was created and tested on a MacOS 13.0 system using Python 3.9.10 and requires the `pandas` and `datetime` libraries. The program will likely run on any system running Python 3.6+ with the required libraries installed.

## Assumptions and Potential Improvements
- Though not stated in the instructions, this program both prints the HTML table to console and outputs the table to an HTML file. This extra step allowed me to more quickly visualize the table and make corrections.

- I was not able to correctly order the player's club appearances when the player appeared for more than one club due to the limitation of the `season` column. To catch most of these instances, I could add logic to assume that the player continued with their previous team before moving. This would fix Cristiano Ronaldo's move from Juventus to Manchester United, but could be wrong in the case a player moved to a new club and then returned.



