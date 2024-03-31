ICS Event Finder & Distance Calculator
=====

[![Python: 3.10.11](https://img.shields.io/badge/python-3.10.11-blue.svg)](https://www.python.org/downloads/release/python-31011/)
[![Code style: Ruff](https://img.shields.io/badge/code_style-Ruff-grey?logo=stackblitz&logoColor=yellow&labelColor=grey&color=%23261230)](https://github.com/astral-sh/ruff)
--------------------------------

About
-----

The origin of the project finds its need in the fact that when declaring taxes
in France, when declaring actual expenses, it is necessary to know the distance
we travel to go to work. For this, it is necessary to know the days we have
worked. This program allows you to search for the days we have worked based on
the events present in a calendar that we will have previously exported to an
*.ics file.

Project Description
--------------------

This project consists of creating a Python program that allows you to search
for events in a previously retrieved *.ics file. The *.ics file contains
calendar data in iCalendar format, such as events with their title,
description, start date and time, end date and time, etc. Then, the program
will display the events found in the *.ics file, their number, and calculate
the distance traveled during the period of the found events.

How to use it
-------------

1. **Install dependencies**

   ```shell
   pip install -r requirements.txt
   ```

2. **Using the script**

* **Example 1:**

   ```shell
   python script.py
   ```

* **Example 2:**

Project Structure
-----------------

Acknowledgements
----------------

Special thanks to the open-source community for their valuable contributions and support.
