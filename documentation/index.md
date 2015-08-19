# [Sublimescheme ](index.html)

SublimeScheme allows you to easily create a Sublime text Color Scheme with a minimum of six lines of code.

## Installation

```python
   pip install sublimescheme
```

  >or otherwise download the zipped file or executable from [the Python Packaging index](https://pypi.python.org/pypi/sublimescheme)


## Modules

### [Generate](generate.html)

Contains a class **Make** that takes two arguments ``(Theme name)`` and ``(Author's name)``

**Make** has six methods which are:

* start() --> This generates the xml header.
* head() --> This generates the basic and most important features of your theme. e.g. foreground, background, caret, invisibles, line highlight, selection, find highlight, find highlight foreground, selection border and stack guide color. These are optional parameters too.
* body() --> This is completely optional and is the main area for your color scheme customization. You can add as many body methods as possible. ``If none is given, you will have a slighly customized theme similar to Python's IDLE theme``.
* complete() --> This completes the theme.
* readme() --> Although completely optional, it generates a README.md file and this is useful if you want to publish it.
* package() --> Although completely optional, it creates a packages.json file which is useful if you want to share your theme on the [Package control website](https://packagecontrol.io)


### [Scopes](scopes.html)


The **Scopes** module has 162 methods for showing several programming language scopes. The most important of all is the **scopes** method which lists all the 161 programming language supported. You can also view all the scopes directly on [Github](https://github.com/tushortz/scopes). You can then call your desired programming language name to see all the syntax highlight scopes it supports.



## Using locally

If you just want to use it locally, copy your generated `.tmTheme` into the sublime text packages 

	`Packages` --> `Color Scheme - Default`. 

You will then be able to use it by going to:

	`Preferences` --> `Color Scheme - Default` --> `Themename`


## Acknowledgements


I was inspired to write this package after creating my own Sublime text color scheme called [Wildlife](https://packagecontrol.io/packages/Wildlife). It was a really tedious and energy drenching job but thank God this is now available for anyone and makes things easier to use.

All glory belongs to God for helping me in completing this. Without him, this couldn't have been written by me.


## Contact

If further information or if help is needed, feel free to contact me on my email at taiwo.kareem36@gmail.com


<br/><br/>

### **Table of contents**

* [Homepage](index.html)
* [Scopes](scopes.html)
* [Generate](generate.html)
* [Walkthrough](walkthrough.html)