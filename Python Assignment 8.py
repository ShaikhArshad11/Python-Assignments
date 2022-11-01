#!/usr/bin/env python
# coding: utf-8
1. Is the Python Standard Library included with PyInputPlus?
ans : PyInputPlus is not a part of the Python Standard Library we must install it separately using Pip.2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?
ans : The as pypi code in the import statement saves us from typing pyinputplus each time we want to call a PyInputPlus               function. 3. How do you distinguish between inputInt() and inputFloat()?
ans : The inputInt() function returns an integer ( example : 54), while the inputFloat() function returns a float value
      (example : 54.69 number containing a decimal)4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?
ans : By using pyip.inputint(min=0, max=99)5. What is transferred to the keyword arguments allowRegexes and blockRegexes?
ans : A list of regex strings that are either explicitly allowed or denied.6. If a blank input is entered three times, what does inputStr(limit=3) do?
ans : The function will raise an Exception.7. If blank input is entered three times, what does inputStr(limit=3, default="hello") do?
ans : By default function returns the value 'hello' .