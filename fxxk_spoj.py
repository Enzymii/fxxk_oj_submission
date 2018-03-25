import re,requests
from bs4 import BeautifulSoup

class fxxk_spoj_:

	mainurl='http://www.spoj.com'

	def __init__(self,user_id):
		self.session=requests.session()
		self.user_id=user_id.lower()

	def login_spoj(self,password):

		logindata={
			'login_user':self.user_id,
			'password':password,
			'next_raw':'/'
		}

		r=self.session.post(fxxk_spoj_.mainurl+'/login',data=logindata)
		flag=r.url=='http://www.spoj.com/'
		if flag:
			print 'Login OK!'
		else:
			print 'Login Failed!'
		return flag

	def submit_spoj(self,code,prob_id,lang):
		'''
		language={
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
			C++ (gcc 6.3):1
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
		}
		'''
		submitdata={
			'file':code,
			'lang':lang,
			'problemcode':prob_id,
			'submit':'Submit!'
		}
		r=self.session.post(fxxk_spoj_.mainurl+'/submit/complete/',data=submitdata)
		if r.status_code != 200:
			print 'Submission Failed!'
		else:
			print 'Submitted!'
		
		shorturl=re.search('window.location.href\s=\s\"(.*)\"',r.text).group(1)
		ID=re.search('\d+',shorturl).group(0)
		# r=self.session.get(fxxk_spoj_.mainurl+shorturl)
		# print r.text
		

		matchre='^accepted|^wrong|^time|^compilation|^runtime|^\d+$'

		while True:
			found=False
			result={}
			status=fxxk_spoj_.mainurl+'/status/%s,%s'%(prob_id,self.user_id)
			r=self.session.get(status)
			soup=BeautifulSoup(r.text,'lxml')
			if r.status_code!=200:
				print 'An Erro Occur'+str(r.status_code)
				return False
			tbs=soup.find_all(stat_tab)[0]
			for i,tr in enumerate(tbs.find_all('tr')):
				if i>0:
					curID=re.search('\d+',tr.find_all('td')[0].a.contents[0]).group(0)
					if curID!=ID:
						continue
					if tr.find_all('td')[4].strong!=None:
						stat=sub_empty_char(tr.find_all('td')[4].strong.contents[0])
					elif tr.find_all('td')[4].a!=None:
						stat=sub_empty_char(tr.find_all('td')[4].contents[0]+tr.find_all('td')[4].a.contents[0])
					if stat.find('(')!=-1:
						stat=stat+')'
					if re.search(matchre,stat)!=None:
						found=True
						result['ID']=sub_empty_char(tr.find_all('td')[0].a.contents[0])
						result['RESULT']=stat
						result['TIME']=sub_empty_char(tr.find_all('td')[5].a.contents[0])
						result['MEMORY']=sub_empty_char(tr.find_all('td')[6].contents[0])
			if found:
				break
		return result

	def submit_from_file(self,filename,prob_id,lang):
		fcode=open(filename)
		code=fcode.read()
		return self.submit_spoj(code,prob_id,lang)

def sub_empty_char(src):
	return re.sub('\s|\t|\n','',src)

def stat_tab(tag):
	return tag.has_attr('class') and 'problems' in tag['class']

def __result_print_spoj(ret):

	rett=ret['RESULT']

	rett=re.sub('wronganswer','wrong answer',rett)
	rett=re.sub('compilationerror','compilation error',rett)
	rett=re.sub('timelimitexceeded','time limit exceeded',rett)
	rett=re.sub('runtimeerror','rumtime error',rett)

	print 'ID: ',ret['ID']
	print 'RESULT: ',rett
	print 'TIME: ',ret['TIME']
	print 'MEMORY: ',ret['MEMORY']
