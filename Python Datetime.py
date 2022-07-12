# A date in Python is not a data type of its own,
#  but we can import a module named datetime to work 
# with dates as date objects.

# Import the datetime module and display the current date:

import datetime

x = datetime.datetime.now()
print(x)

# Output --- 2022-07-08 11:52:34.606165


# Date Output

# When we execute the code from the example above the result 
# will be:  2022-07-08 11:50:38.213230

# The date contains year, month, day, hour, minute, second, 
# and microsecond.

# The datetime module has many methods to return information 
# about the date object.


# Return the year and name of weekday:

import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

# Output --- 2022 Friday


# Creating Date Objects

# To create a date, we can use the datetime()
#  class (constructor) of the datetime module.

# The datetime() class requires three parameters
#  to create a date: year, month, day.

# Create a date object:

import datetime
x = datetime.datetime(2020,5,17)
print(x)
# Output --- 2020-05-17 00:00:00

# The datetime() class also takes parameters for time and timezone
#  (hour, minute, second, microsecond, tzone), 
# but they are optional, and has a default value of 0, 
# (None for timezone).



# The strftime() Method

# The datetime object has a method for formatting date
#  objects into readable strings.

# The method is called strftime(), and takes one parameter, 
# format, to specify the format of the returned string:

# Display the name of the month:

import datetime
x = datetime.datetime(2018,6,1)
print(x.strftime("%B"))

# Output --- June


# A reference of all the legal format codes:

#Directive	Description	 Example

# %a	Weekday, short version	Wed
import datetime
x = datetime.datetime.now()
print(x.strftime("%a"))
#Output ---- Tue

# %A	Weekday, full version	Wednesday
import datetime
x = datetime.datetime.now()
print(x.strftime("%A"))
# Output --- Tuesday 

# %w	Weekday as a number 0-6, 0 is Sunday	3
import datetime
x = datetime.datetime.now()
print(x.strftime("%w"))
# Output --- day 2

# %d	Day of month 01-31	31
import datetime
x = datetime.datetime.now()
print(x.strftime("%d"))
# Output -- day of the month 12th 

# %b	Month name, short version	Dec
import datetime
x = datetime.datetime.now()
print(x.strftime("%b"))
#Output --- Jul

# %B	Month name, full version	December
import datetime
x = datetime.datetime.now()
print(x.strftime("%B"))
# Output --- July

# %m	Month as a number 01-12	12
import datetime
x = datetime.datetime.now()
print(x.strftime("%m"))
#Output --- 07

#%y	Year, short version, without century	18
import datetime
x = datetime.datetime.now()
print(x.strftime("%y"))
#Output --- 22

# %Y	Year, full version	2018
import datetime
x = datetime.datetime.now()
print(x.strftime("%Y"))
#Output --- 2022


# %H	Hour 00-23	17
import datetime
x = datetime.datetime.now()
print(x.strftime("%H"))
# Output --- time of hour 14


# %I	Hour 00-12	05
import datetime
x = datetime.datetime.now()
print(x.strftime("%I"))
# Output --- 02

# %p	AM/PM	PM
import datetime
x = datetime.datetime.now()
print(x.strftime("%p"))
# Output --- PM 

# %M	Minute 00-59	41
import datetime
x = datetime.datetime.now()
print(x.strftime("%M"))
# Output --- 20

# %S	Second 00-59	08
import datetime
x = datetime.datetime.now()
print(x.strftime("%S"))
# Output --- 12

#%f	Microsecond 000000-999999	548513
import datetime
x = datetime.datetime.now()
print(x.strftime("%f"))
# Output --- 293995


# %z	UTC offset	+0100
import datetime
x = datetime.datetime.now()
print(x.strftime("%z"))
#Output --- 550981

# %Z	Timezone	CST
import datetime
x = datetime.datetime.now()
print(x.strftime("%Z"))



# %j	Day number of year 001-366	365
import datetime
x = datetime.datetime.now()
print(x.strftime("%j"))
#Output --- 193

# %U	Week number of year, Sunday as the first day of week, 00-53
import datetime
x = datetime.datetime.now()
print(x.strftime("%U"))
#Output --- 193


# %W	Week number of year, Monday as the first day of week, 00-53	52
import datetime
x = datetime.datetime.now()
print(x.strftime("%w"))
#Output --- 2


# %c	Local version of date and time	Mon Dec 31 17:41:00 2018
import datetime
x = datetime.datetime.now()
print(x.strftime("%c"))
#Output --- Tue Jul 12 14:26:00 2022

# %C	Century	20
import datetime
x = datetime.datetime.now()
print(x.strftime("%C"))
#Output --- 20

# %x	Local version of date	12/31/18
import datetime
x = datetime.datetime.now()
print(x.strftime("%x"))
#Output --- 07/12/22


# %X	Local version of time	17:41:00
import datetime
x = datetime.datetime.now()
print(x.strftime("%X"))
#Output --- 14:27:49


# %%	A % character	%
import datetime
x = datetime.datetime.now()
print(x.strftime("%%"))
#Output --- %


# %G	ISO 8601 year	2018
import datetime
x = datetime.datetime.now()
print(x.strftime("%G"))
#Output --- 2022


# %u	ISO 8601 weekday (1-7)	1
import datetime
x = datetime.datetime.now()
print(x.strftime("%u"))
#Output --- 2


# %V	ISO 8601 weeknumber (01-53)	01
import datetime
x = datetime.datetime.now()
print(x.strftime("%V"))
#Output --- 2

