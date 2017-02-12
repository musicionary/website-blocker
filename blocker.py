import time
import calendar
from datetime import datetime as dt

# store hosts path in variable
hosts_temp = "/Users/chipcarnes/Projects/python-mega-course/website-blocker/hosts"
hosts_path = "/etc/hosts"

# redirection
redirect_path = "127.0.0.1"

blocked_websites = [
                    "www.facebook.com",
                    "facebook.com",
                    "www.twitter.com",
                    "twitter.com",
                    "gmail.com",
                    "www.gmail.com",
                    ]


start_time = dt(dt.now().year, dt.now().month, dt.now().day, 8)
end_time = dt(dt.now().year, dt.now().month, dt.now().day, 16)
day_name = calendar.day_name[dt.now().weekday()]

while True:
    if start_time < dt.now() < end_time and day_name != "Saturday":
        print("Working hours...")
        # access etc/hosts file
        with open(hosts_temp, 'r+') as file:
            content = file.read()
            for site in blocked_websites:
                #skip the line/file if the websites are already listed in the file.
                if site in content:
                    pass
                else:
                    # write to file if between 9am-5pm
                    file.write(redirect_path + " " + site + "\n")
        # check time every few seconds
        time.sleep(5)
    else:
        # This section erases the added blocked websites from the file.
        with open(hosts_temp, 'r+') as file:
            # store file lines into an array
            content = file.readlines()
            # return pointer to beginning of file
            file.seek(0)
            for line in content:
                # search each line for the text of the website
                if not any(website in line for website in blocked_websites):
                    # if it doesn't find a website in the line, append the line from the array of lines
                    # this appends a copy of the file, excluding all the websites, to the top of the file
                    # pushing the lines containing the websites, furthern down in lines.
                    file.write(line)
            # pointer is at end of the copied lines, but before the sections containing the websites
            # and truncate/delete everything after the pointer.
            file.truncate()
        print("Not business time!")
        time.sleep(5)
