
# SublimeScheme

SublimeScheme allows you to easily create a Sublime text Color Scheme with a minimum of six lines of code.

## Installation

```python
   pip install sublimescheme
```

> or otherwise download the zipped file or executable from [the Python Packaging index](https://pypi.python.org/pypi/sublimescheme)

## Modules


### Generate

Contains a class **Make** that takes two arguments `(Theme name)` and `(Author's name)`

**Make** has six methods which are:

* start() --> This generates the xml header.
* head() --> This generates the basic and most important features of your theme. e.g. foreground, background, caret, invisibles, line highlight, selection, find highlight, find highlight foreground, selection border and stack guide color. These are optional parameters too.
* body() --> This is completely optional and is the main area for your color scheme customization. You can add as many body methods as possible. `If none is given, you will have a slighly customized theme similar to Python's IDLE theme`.
* complete() --> This completes the theme.
* readme() --> Although completely optional, it generates a README.md file and this is useful if you want to publish it.
* package() --> Although completely optional, it creates a packages.json file which is useful if you want to share your theme on the [Package control website](https://packagecontrol.io/)


#### Example1


```python
    from sublimescheme.generate import * 		#or
    from sublimescheme.generate import Make
 
    sample = Make("Mytheme", "Author")

    sample.start()
    sample.head(fg="#000", bg="#FFFFFF", ct="#F00")

    # Optional and creates a Ruby highlighter for numbers
    sample.body('Ruby: Numbers', 'constant.numeric.ruby', fs='italic', fg='#f0f', bg='#0ff')

    sample.complete()
    sample.readme("github.com/name/themename", "name@email.com")
    make.package("github.com/name/themename", "name@email.com")
```

#### Result1

``` python

    It will generate a python IDLE lookalike with an extra Ruby number highlighter.
```


### Scopes

The **Scopes** module has 162 methods for showing several programming language scopes. The most important of all is the **scopes** method which lists all the 161 programming language supported. You can also view all the scopes directly on [Github](https://github.com/tushortz/scopes). You can then call your desired programming language name to see all the syntax highlight scopes it supports.


#### Example2

```python

    from sublimescheme.scopes import * 		#or
    from sublimescheme.scopes import scopes
    
    print("all scopes")
    scopes()

    print("C++ Scopes")
    cpp()
```

#### Result2

```python

	all scopes
	Scope Name: scope
	=================
	Actionscript: source.actionscript
	Active4D: source.active4d
	Active4D_Html: text.html.strict.active4d
	Active4D_Ini: text.active4d-ini
	Active4D_Library: source.active4d.library
	Ada: source.ada

	.... etc ......


	C++ scopes
	C++ 
	===
	Scope name: source.c++

	C++
	entity.name.function.c
	keyword.control.c++
	keyword.operator.c++
	keyword.operator.cast.c++
	meta.function.constructor.c++
	meta.function.destructor.c++
	meta.function.destructor.prototype.c++

	..... etc ......
```

## Using locally


If you just want to use it locally, copy your generated `.tmTheme` into the sublime text packages 

	`Packages` --> `Color Scheme - Default`. 

You will then be able to use it by going to:

	`Preferences` --> `Color Scheme - Default` --> `Themename`


## Acknowledgements


I was inspired to write this package after creating my own Sublime text color scheme called [Wildlife](https://packagecontrol.io/packages/Wildlife). It was a really tedious and energy drenching job but thank God this is now available for anyone and makes things easier to use.

All glory belongs to God for helping me in completing this. Without him, this couldn't have been written by me.


Contact
-------

If further information or if help is needed, feel free to contact me on my email at taiwo.kareem36@gmail.com
