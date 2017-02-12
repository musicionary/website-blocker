# Website Blocker

This app allows you to add a list of websites that you want blocked on a server or your computer using a python script.

### Installation

Open Terminal and clone the repository.  
```
$ cd Desktop
$ git clone https://github.com/musicionary/website-blocker.git
```

For demonstration purposes, make a copy of your system's hosts file into the clone directory.  I also recommend creating a backup of the hosts file before running any CRON jobs with this script, for system security reasons.  

Adjust the list of websites in the python script to the websites you desire to be blocked, and adjust the start time and end time variables for the timeframe that you want the sites blocked.

Run blocker.py in terminal which alter your hosts file depending on the time parameters set in the file.
```
$ python blocker.py
```


License
-------

MIT License. Copyright &copy; 2017 "Chip Carnes"
