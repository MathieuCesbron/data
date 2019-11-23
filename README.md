# data

1. To generate data, run main.py

2. The data will be stored in the folder datafile

3. A graph will be plot to show how the data looks like

Example:

![](https://github.com/MathieuCesbron/data/blob/master/images/Capture2.PNG)

3. You can alternatively change what pair and timeframe you want for your data in main.py

# Docker

example of utilisation: 

1. docker run dataimage (run with default parameters)

2. docker run -e PAIR="LTCUSDT" -e SINCE="1 month ago UTC" dataimage (run with changed parameters)

