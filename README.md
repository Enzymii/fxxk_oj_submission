# Auto Submissions for OJ

From **Enzymii**

This is just a very easy project for me to study python.

My English is very poor, so maybe it is not easy to understand what I wanna say.

But I'm too lazy to rewrite it in Chinese.

## How to use it?(General)

Well, I write one python file for each oj.
So just `import fxxk_xxxx_ `, 'xxxx' is the name of oj.
There are several ways:

1. The easiest way is to use the function `o_fxxk_xxxx`
   You just need to give the following parameters and to wait for result.
   - user_id
   - headers (for bzoj only)
   - password
   - True/False (Will you submit code from a local file)
   - filepath (if last parameter is "True")/ code (Otherwise)
   - prob_id (you can find it in the url)
   - language (which can be found later in this instruction)
2. If you want to use it more freely, you can use the class `fxxk_xxxx_`
   following functions are offerered:
   - `__init__(self,user_id)`: here is the initalization, remember to fill in your user_id~
   - btw, bzoj needs a third parameter, which is the *headers*.
   - `login_xxxx(self,password)`: login with the password and the user_id given in last step.
     this function returns a bool, True for Login OK and of course, False for login Failed (The most probable reason is incorrect user_id or password, check them carefully!)
   - `submit_xxxx(self,code,prob_id,language)`: submit your code to the problem with certain language. False is the only return value, which will occur when fail to submit.
   - `get_status(self)`  the return value is a dictionary which contains the result got by the program, or it might return False if something wrong while getting the result.
   - `print_result(self,ret)`print the result(it is strongly recommended that the result given is what you get in `get_status`, or unexpected error may occur.)
3. If you don't like the code, modify it as you like~

## OJ available

- [poj](http://poj.org/)
- [hdu](http://acm.hdu.edu.cn/)
- [spoj](http://www.spoj.com/)
- [bzoj](https://www.lydsy.com)
- [vijos](https://vijos.org/)

## Language ID for each OJ

The `lang` parameter should be a number. You can look for which number to use when you want to submit with a certain language supported by the oj. The language with a mark(default) is the default language (Which means when you want to submit in it, you don't have to give the parameter `lang`)

***

## poj

g++:0
gcc:1
java:2
pascal:3
c++:4 (default)
c:5
fortran:6

***
## hdu

g++:0 (default)
gcc:1
c++:2
c:3
pascal:4
java:5
c#:6

***
## spoj

Ada95 (gnat 6.3):7
Any document (no testing):59
Assembler 32 (nasm 2.12.01):13
Assembler 32 (gcc 6.3 ):45
Assembler 64 (nasm 2.12.01):42
AWK (mawk 1.3.3):105
AWK (gawk 4.1.3):104
Bash (bash 4.4.5):28
BC (bc 1.06.95):110
Brainf**k (bff 1.0.6):12
C (clang 4.0):81
C (gcc 6.3):11
C# (gmcs 4.6.2):27
C++ (gcc 6.3):1 (default)
C++ (g++ 4.3.2):41
C++14 (clang 4.0):82
C++14 (gcc 6.3):44
C99 (gcc 6.3):34
Clips (clips 6.24):14
Clojure (clojure 1.8.0):111
Cobol (opencobol 1.1.0):118
CoffeeScript (coffee 1.12.2):91
Common Lisp (sbcl 1.3.13):31
Common Lisp (clisp 2.49):32
D (dmd 2.072.2):102
D (ldc 1.1.0):84
D (gdc 6.3):20
Dart (dart 1.21):48
Elixir (elixir 1.3.3):96
Erlang (erl 19):36
F# (mono 4.0.0):124
Fantom (fantom 1.0.69):92
Forth (gforth 0.7.3):107
Fortran (gfortran 6.3):5
Go (go 1.7.4):114
Gosu (gosu 1.14.2):98
Groovy (groovy 2.4.7):121
Haskell (ghc 8.0.1):21
Icon (iconc 9.5.1):16
Intercal (ick 0.3):9
JAR (JavaSE 6):24
Java (HotSpot 8u112):10
JavaScript (SMonkey 24.2.0):112
JavaScript (rhino 1.7.7):35
Kotlin (kotlin 1.0.6):47
Lua (luac 5.3.3):26
Nemerle (ncc 1.2.0):30
Nice (nicec 0.9.13):25
Nim (nim 0.16.0):122
Node.js (node 7.4.0):56
Objective-C (gcc 6.3):43
Objective-C (clang 4.0):83
Ocaml (ocamlopt 4.01):8
Octave (octave 4.0.3):127
Pascal (fpc 3.0.0):22
Pascal (gpc 20070904):2
PDF (ghostscript 8.62):60
Perl (perl 5.24.1):3
Perl (perl 6):54
PHP (php 7.1.0):29
Pico Lisp (pico 16.12.8):94
Pike (pike 8.0):19
PostScript (ghostscript 8.62):61
Prolog (swi 7.2.3):15
Prolog (gnu prolog 1.4.5):108
Python (cpython 2.7.13):4
Python (PyPy 2.6.0):99
Python 3 (python  3.5):116
Python 3 nbc (python 3.4):126
R (R 3.3.2):117
Racket (racket 6.7):95
Ruby (ruby 2.3.3):17
Rust (rust 1.14.0):93
Scala (scala 2.12.1):39
Scheme (guile 2.0.13):33
Scheme (stalin 0.3):18
Scheme (chicken 4.11.0):97
Sed (sed 4):46
Smalltalk (gst 3.2.5):23
SQLite (sqlite 3.16.2):40
Swift (swift 3.0.2):85
TCL (tcl 8.6):38
Text (plain text):62
Unlambda (unlambda 0.1.4.2):115
VB.net (mono 4.6.2):50
Whitespace (wspace 0.3):6

***
## bzoj

**To submit on bzoj, an http header is needed, or you'll get a 404.**

The easiest way is to copy it from your browser and make it as a dict in python.

Upd: You can just make headers as a string, and use the 'get_headers' function in fxxk_bzoj.py instead.
The return value is a dict which can be directly used as the parameter.

C:0
C++:1 (default)
Pascal:2
Java:3
Ruby:4
Bash:5
Python:6

Upd 2: add a 0.3s sleep.(Sounds useless, isn't it?) Add a rule which gives 'submission failed' sign if the post request's status code is not 200.

***

## vijos

Language in post data is a string, but you can also give a parameter as a number. You can choose either this time.

C:0 'c'
C++:1 (default) 'cc'
C#:2 'cs'
Pascal:3 'pas'
Java:4 'java'
Python:5 'py'
Python3:6 'py3'
PHP:7 'php'
Rust:8 'rs'
Haskell:9 'hs'
Javascript:10 'js'
Go:11 'go'
Ruby:12 'rb'

***
## Others

If you have any problem or advice, write an issue.

I will be sincerely appreciate if you could help me improve my skill.

This file may be updated at any time. Have fun! :D

**Recent Problems**:

- Submit a problem which is not exist is vaild now, while you may never get the result(you'll get an exception soon in spoj and a 'submission failed' sign in the lastest one(fxxk_vijos), but I may be too lazy to fix what I have coded before.

Lastest update: 2018.4.10
