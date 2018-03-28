import re,requests
from bs4 import BeautifulSoup

class fxxk_hdu_():

	mainurl='http://acm.hdu.edu.cn'

	def __init__(self,user_id):
		self.session=requests.session()
		self.user_id=user_id
		self.login=False

	def login_hdu(self,password):

		if(self.login):
			print 'You Have Loged in!'
			return False

		logindata={
			'username':self.user_id,
			'userpass':password,
			'login':'Sign In',
		}
		r=self.session.post(fxxk_hdu_.mainurl+'/userloginex.php?action=login',data=logindata)

		if r.status_code==302:
			self.login=True
		else:
			self.login=False

		if(self.login):
			print 'Login OK!'
		else:
			print 'Login Failed!'

		return self.login

	def submit_hdu(self,code,prob_id,lang=0):
		
		if not self.login:
			print 'Please login first!'
			return False

		self.prob_id=prob_id
		self.lang=lang

		submitdata={
			'check':0,
			'problemid':prob_id,
			'language':lang,
			'usercode':code,
		}
		r=self.session.post(fxxk_hdu_.mainurl+'/submit.php?action=submit',data=submitdata)
		
		if(r.status_code!=200):
			print 'Submit Failed!'
			return False
		else:
			print "Submitted!"

	def get_status(self):
		status=fxxk_hdu_.mainurl+'/status.php?first=&pid=%d&user_id=%s&lang=%d&status=0'\
		%(self.prob_id,self.user_id,self.lang)

		statusid='0'

		Results=[
			'Accepted',
			'Presentation Error',
			'Wrong Answer',
			'Runtime Error',
			'Time Limit Exceeded',
			'Memory Limit Exceeded',
			'Output Limit Exceeded',
			'Compilation Error',
			'System Error',
			'Out Of Contest Time',
		]
		
		while(1):
			result={}
			found=False
			res=''
			r=self.session.get(status)
			print 'Waiting for status...'
			soup=BeautifulSoup(r.text,"lxml")
			# print soup.prettify()
			tbs=soup.find_all(self.__stat_tab)[0]
			for i,tr in enumerate(tbs.find_all('tr')):
				if i==0:
					continue
				else:
					if statusid=='0' and i==1:
						statusid=re.search('(\d+)',tr.td.contents[0]).group(0)
					else:
						if statusid==re.search('(\d+)',tr.td.contents[0]).group(0):
							res=re.search('([A-Za-z]+\s?[A-Za-z]+\s?[A-za-z]+)',tr.find_all('td')[2].font.contents[0]).group(0)
							detail=tr
							break
			for ret in Results:
				if ret==res:
					result['Run ID']=re.sub('\s|\t|\n','',detail.find_all('td')[0].contents[0])
					result['Result']=res
					result['Exe.Time']=re.sub('\s|\t|\n','',detail.find_all('td')[4].contents[0])
					result['Exe.Memory']=re.sub('\s|\t|\n','',detail.find_all('td')[5].contents[0])
					tmp=str(detail.find_all('td')[6])
					result['Code Len.']=re.search('(\d+\s[A-Za-z]+)',tmp).group(0)

					found=True
					print 'Have Got the Result!'
					break
			if found:
				break
		return result

	def submit_from_file(self,filename,prob_id,lang=0):
		fcode=open(filename)
		code=fcode.read()
		return self.submit_hdu(code,prob_id,lang)

	def __stat_tab(self,tag):
		'''
		ignore tables which is no the submission table
		'''
		return tag.has_attr('class') and tag['class']==['table_text']

	def print_result(self,ret):
		print 'Run ID: ',ret['Run ID']
		print 'Result: ',ret['Result']		
		print 'Time: ',ret['Exe.Time']
		print 'Memory: ',ret['Exe.Memory']
		print 'Code Length: ',ret['Code Len.']

def o_fxxk_hdu(user_id,password,isfile,code,prob_id,lang=0):

	fxxk=fxxk_hdu_(user_id)

	flag=fxxk.login_hdu(password)
	if flag:
		if isfile:
			flag=fxxk.submit_from_file(code,prob_id,lang)
		else:
			fxxk.submit_hdu(code,prob_id,lang)
		ret=fxxk.get_status()
		fxxk.print_result(ret)			
	else:
		print '=Something Wrong. Program End.='