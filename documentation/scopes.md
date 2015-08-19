# [Sublimescheme ](index.html)

## [Scopes](scopes.html)

Scope has 162 methods useful for creating syntax highlighting for the **.tmTheme** file.

>Before you can use the scope method, you need to import it the following way

```python

	# Best way (You get access to all methods)
	# and you don't have to import 162 methods one by one
	from sublimescheme.scopes import *	

	#or simply
	from sublimescheme.scope import scope

	# or even 
	import sublimescheme 	#but then you have to use it this way
	sublimescheme.scopes.scopes
```

You can then use it by calling the method like the below example

```python
	scopes()
```

This will print a result similar to this:

```python
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
```

If you already know the language you want to use but needs it syntax highlighing scope then all you need do is call the name e.g.

```python

	cpp()
```

will give a result similar to this:

```python

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

<br/><br/>

### **Table of contents**

* [Homepage](index.html)
* [Scopes](scope.html)
* [Generate](generate.html)
* [Walkthrough](walkthrough.html)