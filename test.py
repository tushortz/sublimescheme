from sublimescheme.generate import *
from sublimescheme.scopes import *

make = Make("Cherry", "Daniel")
make.start()
make.head(fg="#000", bg="#FFFFFF", ct="#F00", inv="#0FF", lh="#004312", se="#eeffee", fh="#00BFFF", fhf="f0f0f0", sb="#E996F7", sg="#abcdef")

make.body('Ruby: Numbers', 'constant.numeric.ruby', fs='italic', fg='#f0f', bg='#0ff')

make.complete()
make.readme("github.com/me/cherry", "daniel@aol.com")
make.package("github.com/me/cherry")