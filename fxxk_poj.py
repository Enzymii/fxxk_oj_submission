import re,requests,base64
from bs4 import BeautifulSoup

class fxxk_poj_():

	mainurl='http://poj.org'

	def __init__(self,user_id):
		self.session=requests.session()
		self.user_id=user_id
		self.login=False

	def login_poj(self,password):

		if(self.login):
			print 'You Have Loged in!'
			return False

		logindata={
			'user_id1':self.user_id,
			'password1':password,
			'B1':'login',
			'url':'/'
		}
		r=self.session.post(fxxk_poj_.mainurl+'/login',data=logindata)
		r=self.session.get(fxxk_poj_.mainurl+'/send?to='+self.user_id)

		s=re.search('Error',r.text)
		self.login=s==None

		if(self.login):
			print 'Login OK!'
		else:
			print 'Login Failed!'

		return s==None

	def submit_poj(self,code,prob_id,lang=4):
		
		if not self.login:
			print 'Please Login First!'
			return False

		self.prob_id=prob_id
		self.lang=lang

		submitdata={
			'problem_id':prob_id,
			'language':lang,
			'source':str(base64.b64encode(code.encode('utf-8'))),
			'submit':'Submit',
			'encoded':1
		}
		r=self.session.post(fxxk_poj_.mainurl+'/submit',data=submitdata)
		if(r.status_code!=200):
			print 'Submit Failed!'
			return False
		else:
			print "Submitted!"

	def get_status(self):

		status=fxxk_poj_.mainurl+'/status?problem_id=%d&user_id=%s&result=&language=%d'\
		%(self.prob_id,self.user_id,self.lang)

		statusid='0'

		Results=[
			'Accepted',
			'Presentation Error',
			'Time Limit Exceeded',
			'Memory Limit Exceeded',
			'Wrong Answer',						
			'Runtime Error',
			'Output Limit Exceeded',
			'Compile Error',
			'System Error',
			'Validator Error',
		]

		while(1):
			result={}
			found=False
			res=''
			r=self.session.get(status)
			print 'Waiting for status...'
			soup=BeautifulSoup(r.text,"lxml")
			tbs=soup.find_all(self.__stat_tab)[0]
			for i,tr in enumerate(tbs.find_all('tr')):
				if statusid=='0' and i==1:
					statusid=tr.td.contents[0]
				else:
					if statusid==tr.td.contents[0]:
						res=tr.find_all('td')[3].font.contents[0]
						detail=tr
			for ret in Results:
				if ret==res:
					result['Run ID']=detail.find_all('td')[0].contents[0]
					result['Result']=res
					if len(detail.find_all('td')[4].contents)>0:
						result['Memory']=detail.find_all('td')[4].contents[0]
					else:
						result['Memory']=''
					if len(detail.find_all('td')[5].contents)>0:
						result['Time']=detail.find_all('td')[5].contents[0]
					else:
						result['Time']=''
					result['Code Length']=detail.find_all('td')[7].contents[0]
					found=True
					print 'Have Got the Result!'
					break
			if found:break
		return result

	def submit_from_file(self,filename,prob_id,lang=4):
		fcode=open(filename)
		code=fcode.read()
		return self.submit_poj(code,prob_id,lang)

	def __stat_tab(self,tag):
		'''
		ignore tables which is no the submission table
		'''
		return tag.has_attr('class') and tag['class']==['a']

	def print_result(self,ret):
		print 'Run ID: ',ret['Run ID']
		print 'Result: ',ret['Result']
		print 'Memory: ',ret['Memory']
		print 'Time: ',ret['Time']
		print 'Code Length: ',ret['Code Length']

def o_fxxk_poj(user_id,password,isfile,code,prob_id,lang=4):

	fxxk=fxxk_poj_(user_id)

	flag=fxxk.login_poj(password)
	if flag:
		if isfile:
			flag=fxxk.submit_from_file(code,prob_id,lang)
		else:
			fxxk.submit_poj(code,prob_id,lang)
		ret=fxxk.get_status()
		fxxk.print_result(ret)			
	else:
		print '=Something Wrong. Program End.='