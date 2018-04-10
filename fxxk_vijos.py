import requests,re,time
from bs4 import BeautifulSoup

class fxxk_vijos_():

	mainurl='https://vijos.org'

	def __init__(self,user_id):
		self.session=requests.session()
		self.user_id=user_id
		self.login=False

	def login_vijos(self,password):

		
		if self.login:
			print 'You Have Loged in!'
			return False

		self.password=password

		logindata={
			'uname':self.user_id,
			'password':self.password,
		}

		r=self.session.post(fxxk_vijos_.mainurl+'/login',logindata)

		flag=r.status_code==200
		if flag:
			print 'Login OK!'
		else:
			print 'Login Failed!'

		self.login=flag
		return flag

	def submit_vijos(self,code,prob_id,lang=1):

		languages=['c','cc','cs','pas','java','py','py3','php','rs','hs','js','go','rb']

		if not self.login:
			print 'Please Login First!'
			return False

		self.prob_id=prob_id
		self.lang=lang

		submitdata={}

		if lang in languages:
			submitdata['lang']=lang
		else:
			submitdata['lang']=languages[lang]
		submitdata['code']=code
		submitaddr=fxxk_vijos_.mainurl+'/p/'+str(prob_id)+'/submit'
		r=self.session.get(submitaddr)
		if r.status_code!=200:
			print 'Submission Failed!'
			return False

		soup=BeautifulSoup(r.text,"lxml")
		submitdata['csrf_token']=soup(attrs={'name':'csrf_token'})[0].attrs['value']

		r=self.session.post(submitaddr,data=submitdata)
		if r.status_code==200:
			print 'Submitted!'
			self.url=r.url
			return True
		else:
			print 'Submission Failed!'
			return False

		self.url=r.url

	def get_status(self):

		while 1:
			result=[]
			r=self.session.get(self.url)
			print 'Waiting for status...'

			soup=BeautifulSoup(r.text,'lxml')
			if not soup('span',class_='icon record-status--icon progress'):
				status_table=soup('div',id='status')
				content=re.sub('<.*>|\n','',status_table[0].prettify()).split('#')
				for i in content:
					i=re.sub('[^\x00-\xff]','',i)
					while re.search('\s\s\s\s',i):
						i=re.sub('\s\s\s\s',' ',i)
					result.append(i)
				return result

			time.sleep(0.3)

	def submit_from_file(self,filename,prob_id,lang=1):
		fcode=open(filename)
		code=fcode.read()
		return self.submit_vijos(code,prob_id,lang)

	def print_result(self,ret):
		for i in ret:
			print i

def o_fxxk_vijos(user_id,password,isfile,code,prob_id,lang=1):

	fxxk=fxxk_vijos_(user_id)

	flag=fxxk.login_vijos(password)
	if flag:
		if isfile:
			flag=fxxk.submit_from_file(code,prob_id,lang)
		else:
			fxxk.submit_vijos(code,prob_id,lang)
		ret=fxxk.get_status()
		fxxk.print_result(ret)
	else:
		print '=Something Wrong. Program End.='