import re,requests
from bs4 import BeautifulSoup

def get_headers(data):

	header_dict={}

	headers=data.split('\n')
	for da in headers:
		da=da.split(':')
		if len(da[0]) and len(da[1]):
			da[1]=re.sub('^\s+','',da[1])
			header_dict[da[0]]=da[1]

	return header_dict

class fxxk_bzoj_():

	mainurl='https://www.lydsy.com/JudgeOnline'

	def __init__(self,user_id,headers):
		self.session=requests.session()
		self.user_id=user_id.lower()
		self.headers=headers
		self.login=False

	def login_bzoj(self,password):

		if(self.login):
			print 'You Have Loged in!'
			return False

		self.password=password

		logindata={
			'user_id':self.user_id,
			'password':self.password,
			'submit':'Submit'
		}

		r=self.session.post(fxxk_bzoj_.mainurl+'/login.php',data=logindata, headers=self.headers)
		x=int(re.search('(\d+)',r.text).group(0))
		flag=x==2
		if flag:
			print 'Login OK!'
		else:
			print 'Login Failed!'

		self.login=flag
		return flag

	def submit_bzoj(self,code,prob_id,lang=1):

		if not self.login:
			print 'Please Login First!'
			return False

		self.prob_id=prob_id
		self.lang=lang

		submitdata={
			'id':prob_id,
			'language':lang,
			'source':code
		}
		r=self.session.post(fxxk_bzoj_.mainurl+'/submit.php',data=submitdata, headers=self.headers)
		print 'Submitted!'
		self.url=r.url
		
	def get_status(self):

		Results=[
			'Accepted',
			'Presentation_Error',
			'Wrong_Answer',
			'Time_Limit_Exceed',
			'Memory_Limit_Exceed',								
			'Output_Limit_Exceed',
			'Runtime_Error',
			'Compile_Error',
		]

		while 1:
			result={}
			found=False
			url='http'+re.search('https(.*)',self.url).group(1)
			r=requests.get(url,headers=self.headers)
			print 'Waiting for status...'
			soup=BeautifulSoup(r.text,"lxml");
			for tr in soup.find_all('table'):
				if tr.has_attr('align'):
					td=tr.find_all('tr')[1]
					ret=td.find_all('td')[3].contents[0].contents[0]
					if ret in Results:
						found=True
						result['RunID']=td.find_all('td')[0].contents[0]
						result['Result']=ret
						result['Memory']=td.find_all('td')[4].contents[0]
						result['Time']=td.find_all('td')[5].contents[0]
						result['Code_Length']=td.find_all('td')[7].contents[0]
			if found:
				break
		return result			

	def submit_from_file(self,filename,prob_id,lang=1):
		fcode=open(filename)
		code=fcode.read()
		return self.submit_bzoj(code,prob_id,lang)

	def __stat_tab(self,tag):
		'''
		ignore tables which is no the submission table
		'''
		return tag.has_attr('align') and tag['align']=='center'

	def print_result(self,ret):
		print 'RunID: ',ret['RunID']
		print 'Result: ',ret['Result']
		print 'Memory: ',ret['Memory'],'KB'
		print 'Time: ',ret['Time'],'MS'
		print 'Code_Length: ',ret['Code_Length']


def o_fxxk_bzoj(user_id,headers,password,isfile,code,prob_id,lang=1):

	fxxk=fxxk_bzoj_(user_id,headers)

	flag=fxxk.login_bzoj(password)
	if flag:
		if isfile:
			flag=fxxk.submit_from_file(code,prob_id,lang)
		else:
			fxxk.submit_bzoj(code,prob_id,lang)
		ret=fxxk.get_status()
		fxxk.print_result(ret)
	else:
		print '=Something Wrong. Program End.='
