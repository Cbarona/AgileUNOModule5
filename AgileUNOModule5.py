"""
Carlos Barona
Agile UNO Module 5
Strings and Lists
"""

from sys import exit # Import 'exit' from the 'sys' library
import sys # Import the 'sys' library

import requests # Import the 'requests' library

site_data = {} # Setting an empty dictionary

with open("sites.csv", "r") as infile: # Using a context manager to open 'sites.csv' file as 'infile'
    data = infile.read() # Setting 'data' variable to 'infile' with a .read() method
    sites = data.split(",") # Setting 'sites' variable to 'data' with a .split() method

for site in sites: # For loop that will iterate through 'sites'
    site_data[site] = requests.get(site) # Setting 'site_data[site]' to the information received from the 'requests' module using the .get() method

for key, value in site_data.items(): # For loop that will iterate through both the 'key' and 'value' in 'site_data' using the .items() method
    print(f"\n{key} : {value}\n") # Print out the formated strings of the iterated 'key', 'value' pairs


#1
###########################################
"""
Using string slicing, print out each URL extention below.
Example:

edu
com
edu
"""
extentions = [data[16:19], data[39:42], data[59:63]] # Variable set to a list of three different string slices

for i in extentions: # For loop that will iterate through 'extentions'
    print(i + "\n") # Print out the iterations for 'exentions' and adding a newline inbetween each one

#2
###########################################
"""
Print out any sites that end with .com below.
"""
for key in sites: # For loop that will iterate through 'sites'
    if '.com' in key: # Conditional that will trigger if '.com' is in a 'key'
        print(key + "\n") # Print out any 'key' with '.com' and add a newline

#3
###########################################
"""
Convert all site names to Upper case and print out each below.
"""
for key in sites: # For loop that will iterate through the 'key's in 'sites'
    print(key.upper() + "\n") # Print out all of the 'key's in upper case letters and adding a new line

#4
###########################################
"""
Using the list of sites, add a new site to it,
using the input() method to get the name of the site from the user
then reverse the order of the list and print it out.
"""
add = input("Please enter a site: ") # Setting the 'add' variable to the input of the user
if add not in sites: # Conditional that will trigger if 'add' variable's user input is not in 'sites'
    sites.append(add) # 'Sites' will be appended with the .append() method adding the user input
print(sites[::-1]) # Print out the 'sites' in reverse order

#5
###########################################
"""
Print out the 'Server' of the responce of the URL request of the items from your list

look here for more information:
    https://requests.readthedocs.io/en/master/user/quickstart/#responce-content
example:
    print(f"{mySiteData.headers.get('Server')}\n")
"""
for i in sites: # For loop that will iterate through 'sites'
    r = requests.get(i) # Setting variable 'r' to the information received through the 'requests' module using the .get() method
    print("######################################################\n") # Print out a string of '#'s to help delineate between requests
    print(r.headers) # Print out the information in the 'r' variable using the .headers() method

#6
###########################################
"""
Exit the program using the sys module's exit function we
imported at the beginning of the code
"""
sys.exit() # An exit function imported from 'sys' library