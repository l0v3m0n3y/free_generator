import requests
class Client():
	def __init__(self):
		self.api="http://free-generator.ru/generator.php"
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
	def random_numder(self,count:int=1,min:int=1,max:int=100):
		return requests.get(f"{self.api}?action=number&count={count}&min={min}&max={max}&src=range&list=&duble=0",headers=self.headers).json()
	def random_name(self,pol:int=1,name:int=1,lastname:int=1,first2name:int=1):
		return requests.get(f"{self.api}?action=name&pol={pol}&firstname={name}&lastname={lastname}&first2name={first2name}",headers=self.headers).json()
	def random_password(self,len:int=6,numbers:int=1,lower_words:int=1,upper_words:int=1,spec_words:int=0,remove_duble:int=0):
		return requests.get(f"{self.api}?action=password&len={len}&numbers={numbers}&lower_words={lower_words}&upper_words={upper_words}&spec_words={spec_words}&remove_duble={remove_duble}",headers=self.headers).json()
	def random_word(self,type:int=3):
		return requests.get(f"{self.api}?action=word&type={type}",headers=self.headers).json()
	def random_slogan(self,name,category:int=35):
		return requests.get(f"{self.api}?action=slogan&category={category}&name={name}",headers=self.headers).json()
	def random_quote(self,src:int=0):
		return requests.get(f"{self.api}?action=quote&src={src}",headers=self.headers).json()
	def random_compliment(self,pol:int=1,type:int=2):
		return requests.get(f"{self.api}?action=compliment&pol={pol}&type={type}",headers=self.headers).json()
	def random_joke(self):
		return requests.get(f"{self.api}?action=joke",headers=self.headers).json()