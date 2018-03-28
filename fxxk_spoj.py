import re,requests
from bs4 import BeautifulSoup

class fxxk_spoj_():

	mainurl='http://www.spoj.com'

	def __init__(self,user_id):
		self.session=requests.session()
		self.user_id=user_id.lower()
		self.login=False

	def login_spoj(self,password):

		if(self.login):
			print 'You Have Loged in!'
			return False

		self.password=password

		logindata={
			'login_user':self.user_id,
			'password':self.password,
			'next_raw':'/'
		}

		r=self.session.post(fxxk_spoj_.mainurl+'/login',data=logindata)
		flag=r.url=='http://www.spoj.com/'
		if flag:
			print 'Login OK!'
		else:
			print 'Login Failed!'

		self.login=flag
		return flag

	def submit_spoj(self,code,prob_id,lang=1):

		if not self.login:
			print 'Please Login First!'
			return False

		self.prob_id=prob_id
		self.lang=lang

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
		self.ID=ID

		# r=self.session.get(fxxk_spoj_.mainurl+shorturl)
		# print r.text
		
	def get_status(self):

		matchre='^accepted|^wrong|^time|^compilation|^runtime|^\d+'

		while True:
			found=False
			result={}
			status=fxxk_spoj_.mainurl+'/status/%s,%s'%(self.prob_id,self.user_id)
			r=self.session.get(status)
			print 'Waiting for status...'
			soup=BeautifulSoup(r.text,'lxml')
			if r.status_code!=200:
				print 'An Error Occur'+str(r.status_code)
				return False
			tbs=soup.find_all(self.__stat_tab)[0]
			for i,tr in enumerate(tbs.find_all('tr')):
				if i>0:
					curID=re.search('\d+',tr.find_all('td')[0].a.contents[0]).group(0)
					if curID!=self.ID:
						continue
					if tr.find_all('td')[4].strong!=None:
						stat=self.__sub_empty_char(tr.find_all('td')[4].strong.contents[0])
					elif tr.find_all('td')[4].a!=None:
						stat=self.__sub_empty_char(tr.find_all('td')[4].contents[0]+tr.find_all('td')[4].a.contents[0])
					if stat.find('(')!=-1:
						stat=stat+')'
					if re.search(matchre,stat)!=None:
						found=True
						result['ID']=self.__sub_empty_char(tr.find_all('td')[0].a.contents[0])
						result['RESULT']=stat
						result['TIME']=self.__sub_empty_char(tr.find_all('td')[5].a.contents[0])
						result['MEMORY']=self.__sub_empty_char(tr.find_all('td')[6].contents[0])
			if found:	
				break
		return result

	def submit_from_file(self,filename,prob_id,lang=1):
		fcode=open(filename)
		code=fcode.read()
		return self.submit_spoj(code,prob_id,lang)

	def __sub_empty_char(self,src):
		return re.sub('\s|\t|\n','',src)

	def __stat_tab(self,tag):
		return tag.has_attr('class') and 'problems' in tag['class']

	def print_result(self,ret):
		rett=ret['RESULT']

		rett=re.sub('accepted.*','accepted',rett)
		rett=re.sub('wronganswer.*','wrong answer',rett)
		rett=re.sub('compilationerror.*','compilation error',rett)
		rett=re.sub('timelimitexceeded.*','time limit exceeded',rett)
		rett=re.sub('runtimeerror','rumtime error',rett)

		print 'ID: ',ret['ID']
		print 'RESULT: ',rett
		print 'TIME: ',ret['TIME']
		print 'MEMORY: ',ret['MEMORY']


def o_fxxk_spoj(user_id,password,isfile,code,prob_id,lang=1):

	fxxk=fxxk_spoj_(user_id)

	flag=fxxk.login_spoj(password)
	if flag:
		if isfile:
			flag=fxxk.submit_from_file(code,prob_id,lang)
		else:
			fxxk.submit_spoj(code,prob_id,lang)
		ret=fxxk.get_status()
		fxxk.print_result(ret)
	else:
		print '=Something Wrong. Program End.='
