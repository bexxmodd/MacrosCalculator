<p align="center">
  <img width="460" src="https://i.imgur.com/s7Kwl48.png">
</p>

-----
If you are into fitness/Bodybuilding probably you are familiar with what Macros are. If no, it's three main components that make your diet: Proteins, Carbs, Fats. Having a well balanced diet based on the macros distribution is a key to achieving your fitness health goals.

----
## How it Works
Input the personal physics characteristics, like weight, height, age, amount of exercise, and the app will calculate your LBM, TDEE and the Macros share for your daily calorie intake with the number of calories needed to achieve the selected goal. This can be a great guide to aide your fitness goal. If you are not sure about your body fat percentage now app can also approximate your it.
Simply enter personal information and click the **Calculate** button and *voalá*.

<p align ="center">
  <img src="https://media3.giphy.com/media/L0NAnnBYADoQ3LEaGS/giphy.gif" alt="entry" width="350"/>
</p>




## Installation
Currently, the app can be only run through the shell.

1. Copy the repo to your local machine by first opening shell/bash/cmd terminal on your computer and typing
```bash
$ git clone https://github.com/bexxmodd/MacrosCalculator.git
```

2. Go into the cloned folder.
```bash
$ cd MacrosCalculator
```
3. Install dependencies
```bash
$ pip install requirements.txt
```
4. Make sure all the tests pass
```bash
python3 test/diet_test.py
python3 test/person_test.py
python3 test/ui_test.py
```

4. Run the main.py file.
```bash
$ python3 main.py
```

After that macrosCalculator window should pop up where you can perform your diet calculation.

-----
## File Structure
```bash
MacrosCalculator/
├── test/
│   ├── diet_test.py
│   ├── person_test.py
│   └── ui_test.py
├── LICENSE
├── MacroEstimator.py
├── main.py
├── README.md
├── requirement.txt
└── user_interface.ui
```
------
## Dependencies
Project is using two Python packages:

<img align="left" width="25" height="25" src="https://upload.wikimedia.org/wikipedia/commons/0/08/Qt_%28Bibliothek%29_logo.svg">

&nbsp;[PyQT5](https://doc.qt.io/qtforpython/)

<img align="left" width="25" height="25" src="https://www.pinclipart.com/picdir/big/8-87985_whether-a-seasoned-python-programmer-or-a-python.png">

&nbsp;[webbrowser](https://docs.python.org/2/library/webbrowser.html)

----
## Release History
* `v1.0`
  * New version with PyQT GUI and Body fat % apporximation tool
* `v0.5`
  * First functional beta version.

----
## Contributors
<a href="https://github.com/bexxmodd/MacrosCalculator/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=bexxmodd/MacrosCalculator" />
</a>

----
## Meta

**Follow me on social media:**

[![Bexx Modd GitHub](https://i.imgur.com/rnEivsV.png)](https://github.com/bexxmodd) [![Bexx Modd Twitter](https://i.imgur.com/BMdn8gX.png)](https://twitter.com/bexxmodd) [![Bexx Modd LinkedIn](https://i.imgur.com/NxflDxM.png)](https://www.linkedin.com/in/bmodebadze/)

---------
Repo is distributed under the **MIT** license. See `LICENSE.txt` for more information.
