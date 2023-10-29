import pandas as pd;
import matplotlib.pyplot as plt;
import datetime

class Chart():
	def __init__(self, val:tuple):
		self.values = val
	def DRAWW(self, d:list = [1,2,3,4,5,6,7], text_x="", text_y=""):
		if str(d) == str([1,2,3,4,5,6,7]):
			a = datetime.datetime.now().now()
			s = []
			for i in range(8):
				a = a + datetime.timedelta(days=-1)
				s.append(a)
			df=pd.DataFrame({"dates": [s[0], s[1], s[2], s[3], s[4], s[5], s[6]], "values": self.values})
			ax = df.plot(x="dates", y="values", kind="line", label="", marker="*", legend=False)
			ax.set_xlabel(text_x)
			ax.set_ylabel(text_y)
			ax.grid()
			plt.savefig('PHOTO.png')
			return 200
		else:
			s = d
			df=pd.DataFrame({"dates": s, "values": self.values})
			ax = df.plot(x="dates", y="values", kind="line", label="", marker="*", legend=False)
			ax.set_xlabel(text_x)
			ax.set_ylabel(text_y)
			ax.grid()
			plt.savefig('PHOTO.png')
			return 200