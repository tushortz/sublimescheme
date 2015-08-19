# [Sublimescheme ](index.html)

## [Generate](generate.html)


Contains a class **Make** that takes two arguments ``(Theme name)`` and ``(Author's name)``

**Make** has six methods which are:

* start() --> This generates the xml header.
* head() --> This generates the basic and most important features of your theme. e.g. foreground, background, caret, invisibles, line highlight, selection, find highlight, find highlight foreground, selection border and stack guide color. These are optional parameters too.
* body() --> This is completely optional and is the main area for your color scheme customization. You can add as many body methods as possible. ``If none is given, you will have a slighly customized theme similar to Python's IDLE theme``.
* complete() --> This completes the theme.
* readme() --> Although completely optional, it generates a README.md file and this is useful if you want to publish it.
* package() --> Although completely optional, it creates a packages.json file which is useful if you want to share your theme on the [Package control website](https://packagecontrol.io)


#### Example

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

```python

    It will generate a python IDLE lookalike with an extra Ruby number highlighter.


<br/><br/>

### **Table of contents**

* [Homepage](index.html)
* [Scopes](scope.html)
* [Generate](generate.html)
* [Walkthrough](walkthrough.html)