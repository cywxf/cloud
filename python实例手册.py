	pythonʵ���ֲ�

#encoding:utf8
# �趨����-֧������

0˵��

	�ֲ�����: ѩ�� littlepy
	��������: 2013-12-19
	��ӭϵͳ��ά����QȺ: 198173206  # ��Ⱥ��ش�����

	��ʹ��"notepad++"�򿪴��ĵ�,"alt+0"�������۵��󷽱����
	����ɾ����Ϣ��ת����˵�����������Ʋ�������Ϊ��
	�����������⣬����ָ����

	# pythonʵ���ֲ����ص�ַ:
	http://hi.baidu.com/quanzhou722/item/cf4471f8e23d3149932af2a7
	
	# shellʵ���ֲ��������ص�ַ:
	http://hi.baidu.com/quanzhou722/item/f4a4f3c9eb37f02d46d5c0d9

	# LazyManage��ά���������������[shell]:
	http://hi.baidu.com/quanzhou722/item/4ccf7e88a877eaccef083d1a
	
	# LazyManage��ά���������������[python]:
	http://hi.baidu.com/quanzhou722/item/4213db3626a949fe96f88d3c

1 ����

	�鿴����
		import os
		for i in dir(os):
			print i         # ģ��ķ���
		help(os.path)       # �����İ���

	pipģ�鰲װ
		
		yum install python-pip            # centos��װpip
		sudo apt-get install python-pip   # ubuntu��װpip
		pip�ٷ���װ�ű�
			wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
			python get-pip.py
		���ػ�������
			vim /etc/profile
			export PATH=/usr/local/python27/bin:$PATH
			. /etc/profile

		pip install Package             # ��װ�� pip install requests
		pip show --files Package        # �鿴��װ��ʱ��װ����Щ�ļ�
		pip show --files Package        # �鿴��Щ���и���
		pip install --upgrade Package   # ����һ�������
		pip uninstall Package           # ж�������

	����

		r=r'\n'          # ���ʱԭ�ʹ�ӡ
		u=u'����'        # ����Ϊunicode����
		global x         # ȫ�ֱ���
		a = 0 or 2 or 1  # �������㸳ֵ,aֵΪTrue�Ȳ��������,aֵΪ2.  None���ַ���''����Ԫ��()�����б�[],���ֵ�{}��0�����ַ�������false
		name = raw_input("input:").strip()        # �����ַ�������
		num = int(raw_input("input:").strip())    # �����ַ���strתΪint��
		locals()                                  # ���оֲ�������ɵ��ֵ�
		locals().values()                         # ���оֲ�����ֵ���б�
		os.popen("date -d @{0} +'%Y-%m-%d %H:%M:%S'".format(12)).read()    # ����������ñ��� {0} �����һ������

	��ӡ

		# �ַ��� %s  ���� %d  ���� %f  ԭ����ӡ %r
		print '�ַ���: %s ����: %d ����: %f ԭ����ӡ: %r' % ('aa',2,1.0,'r')
		print 'abc',      # �ж���,�������д�ӡ,�ڴδ�ӡ����ű��д�ӡ

	�б�
		# �б�Ԫ�صĸ������ 536870912
		shoplist = ['apple', 'mango', 'carrot', 'banana']
		shoplist[2] = 'aa'
		del shoplist[0]
		shoplist.insert('4','www')
		shoplist.append('aaa')
		shoplist[::-1]    # ���Ŵ�ӡ ���ַ���ת����Ч
		shoplist[2::3]    # �ӵڶ�����ʼÿ��������ӡ
		'\t'.join(li)     # ���б�ת�����ַ���
		list(set(['qwe', 'as', '123', '123']))   # ���б�ͨ������ȥ�ظ�

	Ԫ��

		# ���ɱ�
		zoo = ('wolf', 'elephant', 'penguin')

	�ֵ�

		ab = {       'Swaroop'   : 'swaroopch@byteofpython.info',
					 'Larry'     : 'larry@wall.org',
			 }
		ab['c'] = 80      # ����ֵ�Ԫ��
		del ab['Larry']   # ɾ���ֵ�Ԫ��
		ab.keys()         # �鿴���м�ֵ
		ab.values()       # ��ӡ����ֵ
		ab.has_key('a')   # �鿴��ֵ�Ƿ����
		ab.items()        # ���������ֵ��б�

	���̽ṹ

		if�ж�

			# ����ֵ������ and or not ʵ�ֶ����ж�
			if a == b:
				print '=='
			elif a < b:
				print b
			else:
				print a
			fi

		whileѭ��

			while True:
				if a == b:
					print "=="
					break
				print "!="
			else:
				print 'over'
			
			count=0
			while(count<9):
				print count
				count += 1

		forѭ��

			sorted()           # ����һ������(�б�)
			zip()              # ����һ������(�б�)
			enumerate()        # ���ص�����(��������)
			reversed()         # �������������
			dict.iterkeys()    # ͨ��������
			dict.itervalues()  # ͨ��ֵ����
			dict.iteritems()   # ͨ����-ֵ�Ե���
			randline()         # �ļ�����
			iter(obj)          # �õ�obj������ ���obj�ǲ���һ������
			iter(a,b)          # �ظ�����a,ֱ������������һ��ֵ����b
			for i in range(1, 5):
				print i
			else:
				print 'over'

			list = ['a','b','c','b']
			for i in range(len(list)):
				print list[i]
			for x, Lee in enumerate(list):
				print "%d %s Lee" % (x+1,Lee)

		���̽ṹ��д

			[ i * 2 for i in [8,-2,5]]
			[16,-4,10]
			[ i for i in range(8) if i %2 == 0 ]
			[0,2,4,6]

	tab��ȫ

		# vim /usr/lib/python2.7/dist-packages/tab.py
		# python startup file
		import sys
		import readline
		import rlcompleter
		import atexit
		import os
		# tab completion
		readline.parse_and_bind('tab: complete')
		# history file
		histfile = os.path.join(os.environ['HOME'], '.pythonhistory')

	����

		def printMax(a, b = 1):
			if a > b:
				print a
				return a
			else:
				print b
				return b
		x = 5
		y = 7
		printMax(x, y)

	ģ��

		# Filename: mymodule.py
		def sayhi():
			print 'mymodule'
		version = '0.1'

		# ����ģ��
		import mymodule
		from mymodule import sayhi, version
		# ʹ��ģ���к���
		mymodule.sayhi()

	ȡ����

		import sys
		for i in sys.argv:
			print i

	����ķ���

		class Person:
			# ʵ������ʼ���ķ���
			def __init__(self, name ,age):
				self.name = name
				self.age = age
				print self.name
			# ��self�˺���Ϊ����
			def sayHi(self):
				print 'Hello, my name is', self.name
			#�������ŵ�ʱ�򱻵���
			def __del__(self):
				print 'over'
		# ʵ��������
		p = Person('Swaroop')
		# ʹ�ö��󷽷�
		p.sayHi()
		# �̳�
		class Teacher(Person):
			def __init__(self, name, age, salary):
				Person.__init__(self, name, age)
				self.salary = salary
				print '(Initialized Teacher: %s)' % self.name
			def tell(self):
				Person.tell(self)
				print 'Salary: "%d"' % self.salary
		t = Teacher('Mrs. Shrividya', 40, 30000)

	�ļ�����

		# ģʽ: ��'r'  д'w' ׷��'a' ��д'r+' �������ļ�'b'  'rb','wb','rb+'

		д�ļ�
			f = file('poem.txt', 'w') 
			f.write("string")
			f.write(str(i))
			f.flush()
			f.close() 

		���ļ�
			f = file('/etc/passwd','r')
			while True:
				line = f.readline()    # ����һ��
				if len(line) == 0:
					break
				x = line.split(":")                  # ð�ŷָ������
				#x = [ x for x in line.split(":") ]  # ð�ŷָ������
				#x = [ x.split("/") for x in line.split(":") ]  # ��ð�ŷָ�,��/�ָ� ��ӡx[6][1]
				print x[6],"\n",
			f.close() 
		
		���ļ�2
			f = file('/etc/passwd')
			c = f.readlines()       # ���������ļ�����,�ɷ�����ȡ,���ļ�ʱռ���ڴ�ϴ�
			for line in c:
				print line.rstrip(),
			f.close()

		���ļ�3
			for i in open('b.txt'):   # ֱ�Ӷ�ȡҲ�ɵ���,�������ڴ��ļ���ȡ,�����ɷ�����ȡ
				print i,
		
		׷����־
			log = open('/home/peterli/xuesong','a')
			print >> log,'faaa'
			log.close()
		
		with���ļ�
			with open('a.txt') as f:
				# print f.read()        # ��ӡ��������Ϊ�ַ���
				print f.readlines()     # ��ӡ�������ݰ��зָ���б�
		
		csv�������ļ�  
			192.168.1.5,web # �����ļ������ŷָ�
			list = csv.reader(file('a.txt'))
			for line in list:
				print line              #  ['192.168.1.5', 'web']

	�����쳣

		class ShortInputException(Exception):
			'''A user-defined exception class.'''
			def __init__(self, length, atleast):
				Exception.__init__(self)
				self.length = length
				self.atleast = atleast
		try:
			s = raw_input('Enter something --> ')
			if len(s) < 3:
				raise ShortInputException(len(s), 3)
		except EOFError:
			print '\nWhy did you do an EOF on me?'
		except ShortInputException, x:
			print 'ShortInputException: The input was of length %d, \
				  was expecting at least %d' % (x.length, x.atleast)
		else:
			print 'No exception was raised.' 

	�ڽ�����

		dir(sys)            # ��ʾ���������
		help(sys)           # ����ʽ����
		int(obj)            # ת��Ϊ����
		str(obj)            # תΪ�ַ���
		len(obj)            # ���ض�������г���
		open(file,mode)     # ���ļ� #mode (r ��,w д, a׷��)
		range(0,3)          # ����һ�������б�
		raw_input("str:")   # �ȴ��û�����
		type(obj)           # ���ض�������
		abs(-22)            # ����ֵ
		random              # �����
		random.randrange(9) # 9���������
		choice()            # ������ظ������е�һ��Ԫ��
		divmod(x,y)         # ������ɳ������㣬�����̺�������
		isinstance(object,int)    # ���Զ������� int 
		round(x[,n])        # �������ظ�����x����������ֵ�������nֵ����������뵽С������λ��
		xrange()            # ������range()���ƣ���xrnage()���������б����Ƿ���һ��xrange����
			xrange([lower,]stop[,step])
		strip()             # ��ȥ���ַ������˶��ڿո�,�þ���ȥ�������е������ִ����˶���Ŀո�
		del                 # ɾ���б����������
		cmp(x,y)            # �Ƚ���������    #���ݱȽϽ������һ�����������x<y���򷵻�-1�����x>y���򷵻�1,���x==y�򷵻�0
		max()               # �ַ����������ַ�
		min()               # �ַ�������С���ַ�
		sorted()            # ����������
		reversed()          # �����е���
		enumerate()         # ��������λ�úͶ�Ӧ��ֵ
		sum()               # �ܺ�
		list()              # ����б�����ڵ���
		tuple()             # ���Ԫ������ڵ���   #һ����ʼ���㲻�ܸ��ĵ����ݽṹ,�ٶȱ�list��
		zip()               # ����һ���б�
			>>> s = ['11','22','33']
			>>> t = ['aa','bb','cc']
			>>> zip(s,t)
			[('11', 'aa'), ('22', 'bb'), ('33', 'cc')]

	�ַ������ģ��

		string         # �ַ���������غ����͹���
		re             # ������ʽ
		struct         # �ַ����Ͷ�����֮���ת��
		c/StringIO     # �ַ����������,��������������file����
		base64         # Base16\32\64���ݱ����
		codecs         # ������ע��ͻ���
		crypt          # ���е��������
		difflib        # �ҳ����м�Ĳ�ͬ
		hashlib        # ���ֲ�ͬ��ȫ��ϣ�㷨����ϢժҪ�㷨��API
		hma            # HMAC��Ϣ��Ȩ�㷨��pythonʵ��
		md5            # RSA��MD5��ϢժҪ��Ȩ
		rotor          # �ṩ��ƽ̨�ļӽ��ܷ���
		sha            # NIAT�İ�ȫ��ϣ�㷨SHA
		stringprep     # �ṩ����IPЭ���Unicode�ַ���
		textwrap       # �ı���װ�����
		unicodedate    # unicode���ݿ�

	�б������ڽ�����

		list.append(obj)                 # ���б������һ������obj
		list.count(obj)                  # ����һ������obj���б��г��ֵĴ���
		list.extend(seq)                 # ������seq��������ӵ��б���
		list.index(obj,i=0,j=len(list))  # ����list[k] == obj ��kֵ,����k�ķ�Χ��i<=k<j;�����쳣
		list.insert(index.obj)           # ��������Ϊindex��λ�ò������obj
		list.pop(index=-1)               # ɾ��������ָ��λ�õĶ���,Ĭ�������һ������
		list.remove(obj)                 # ���б���ɾ������obj
		list.reverse()                   # ԭ�ط�ת�б�
		list.sort(func=None,key=None,reverse=False)  # ��ָ���ķ�ʽ�����б��г�Ա,���func��key����ָ��,����ָ���ķ�ʽ�Ƚϸ���Ԫ��,���reverse��־����ΪTrue,���б��Է�������

	�������Ͳ�����

		seq[ind]              # ��ȡ�±�Ϊind��Ԫ��
		seq[ind1:ind2]        # ����±��ind1��ind2��Ԫ�ؼ���
		seq * expr            # �����ظ�expr��
		seq1 + seq2           # ����seq1��seq2
		obj in seq            # �ж�objԪ���Ƿ������seq��
		obj not in seq        # �ж�objԪ���Ƿ񲻰�����seq��

	�ַ��������ڽ�����

		string.expandtabs(tabsize=8)                  # tab����תΪ�ո� #Ĭ��8���ո�
		string.endswith(obj,beg=0,end=len(staring))   # ����ַ����Ƿ���obj����,����Ƿ���True #���beg��endָ����ⷶΧ�Ƿ���obj����
		string.count(str,beg=0,end=len(string))       # ���str��string����ִ���
		string.find(str,beg=0,end=len(string))        # ���str�Ƿ������string��
		string.index(str,beg=0,end=len(string))       # ���str����string��,�ᱨ�쳣
		string.isalnum()                              # ���string������һ���ַ����������ַ�������ĸ�������򷵻�True
		string.isalpha()                              # ���string������һ���ַ����������ַ�������ĸ�򷵻�True
		string.isnumeric()                            # ���stringֻ���������ַ�,�򷵻�True
		string.isspace()                              # ���string�����ո��򷵻�True
		string.isupper()                              # �ַ������Ǵ�д����True
		string.islower()                              # �ַ�������Сд����True
		string.lower()                                # ת���ַ��������д�дΪСд
		string.upper()                                # ת���ַ���������СдΪ��д
		string.lstrip()                               # ȥ��string��ߵĿո�
		string.rstrip()                               # ȥ��string�ַ�ĩβ�Ŀո�
		string.replace(str1,str2,num=string.count(str1))  # ��string�е�str1�滻��str2,���numָ��,���滻������num��
		string.startswith(obj,beg=0,end=len(string))  # ����ַ����Ƿ���obj��ͷ
		string.zfill(width)                           # �����ַ�����Ϊwidth���ַ�,ԭ�ַ����Ҷ���,ǰ�����0
		string.isdigit()                              # ֻ�������ַ���True
		string.split("�ָ���")                        # ��string��Ƭ��һ���б�
		":".join(string.split())                      # ��:��Ϊ�ָ���,������Ԫ�غϲ�Ϊһ���µ��ַ���

	����������ص�ģ��

		array         # һ�������ƵĿɱ���������,Ԫ�ر�����ͬ����
		copy          # �ṩǳ���������������
		operator      # ��������������ʽ�����в����� operator.concat(m,n)
		re            # perl����������ʽ����
		StringIO      # �ѳ��ַ�����Ϊ�ļ������� ��: read() \ seek()
		cStringIO     # �ѳ��ַ�����Ϊ�ļ�����,���ٶȸ���,�����ܱ��̳�
		textwrap      # ������װ/����ı��ĺ���,Ҳ��һ����
		types         # ����python֧�ֵ���������
		collections   # ������������������

	�ֵ��ڽ�����

		dict.clear()                            # ɾ���ֵ�������Ԫ��
		dict copy()                             # �����ֵ�(ǳ����)��һ������
		dict.fromkeys(seq,val=None)             # ����������һ�����ֵ�,��seq�е�Ԫ�������ֵ�ļ�,val�����ֵ������м��Եĳ�ʼֵ
		dict.get(key,default=None)              # ���ֵ�dict�еļ�key,��������Ӧ��ֵvalue,����ֵ��в����ڴ˼�,�򷵻�defaultֵ
		dict.has_key(key)                       # ��������ֵ��д���,�򷵻�True ��in��not in����
		dicr.items()                            # ����һ�������ֵ��м���ֵ��Ԫ����б�
		dict.keys()                             # ����һ�������ֵ��м����б�
		dict.iter()                             # ����iteritems()��iterkeys()��itervalues()�����Ƕ�Ӧ�ķǵ�������һ��,��ͬ�������Ƿ���һ��������,������һ���б�
		dict.pop(key[,default])                 # �ͷ���get()����.����ֵ���key������,ɾ��������dict[key]
		dict.setdefault(key,default=None)       # ��set()����,������ֵ��в�����key��,��dict[key]=defaultΪ����ֵ
		dict.update(dict2)                      # ���ֵ�dict2�ļ�ֵ����ӵ��ֵ�dict
		dict.values()                           # ����һ�������ֵ�������ֵ���б�

		dict([container])     # �����ֵ�Ĺ����������ṩ������(container),�������е���Ŀ����ֵ�
		len(mapping)          # ����ӳ��ĳ���(��-ֵ�Եĸ���)
		hash(obj)             # ����obj��ϣֵ,�ж�ĳ�������Ƿ����һ���ֵ�ļ�ֵ		
		
	���Ϸ���

		s.update(t)                         # ��t�е�Ԫ���޸�s,s���ڰ���s��t�ĳ�Ա   s |= t
		s.intersection_update(t)            # s�еĳ�Ա�ǹ�������s��t��Ԫ��          s &= t
		s.difference_update(t)              # s�еĳ�Ա������s����������t�е�Ԫ��    s -= t
		s.symmetric_difference_update(t)    # s�еĳ�Ա����Ϊ��Щ������s��t��,������s��t���е�Ԫ��  s ^= t
		s.add(obj)                          # �ڼ���s����Ӷ���obj
		s.remove(obj)                       # �Ӽ���s��ɾ������obj;���obj���Ǽ���s�е�Ԫ��(obj not in s),������KeyError����
		s.discard(obj)                      # ���obj�Ǽ���s�е�Ԫ��,�Ӽ���s��ɾ������obj
		s.pop()                             # ɾ������s�е�����һ������,��������
		s.clear()                           # ɾ������s�е�����Ԫ��
		s.issubset(t)                       # ���s��t���Ӽ�,�򷵻�True   s <= t
		s.issuperset(t)                     # ���t��s�ĳ���,�򷵻�True   s >= t
		s.union(t)                          # �ϲ�����;����һ���¼���,�ü�����s��t�Ĳ���   s | t
		s.intersection(t)                   # ��������;����һ���¼���,�ü�����s��t�Ľ���   s & t
		s.difference(t)                     # ����һ���¼���,�ļ�����s�ĳ�Ա,������t�ĳ�Ա  s - t
		s.symmetric_difference(t)           # ����һ���¼���,�ü�����s��t�ĳ�Ա,������s��t���еĳ�Ա   s ^ t
		s.copy()                            # ����һ���¼���,���Ǽ���s��ǳ����
		obj in s                            # ��Ա����;obj��s�е�Ԫ�� ����True
		obj not in s                        # �ǳ�Ա����:obj����s��Ԫ�� ����True
		s == t                              # �ȼ۲��� �Ƿ������ͬԪ��
		s != t                              # ���ȼ۲��� 
		s < t                               # �Ӽ�����;s!=t��s������Ԫ�ض���t�ĳ�Ա
		s > t                               # ��������;s!=t��t������Ԫ�ض���s�ĳ�Ա

	���л�

		#!/usr/bin/python
		import cPickle
		obj = {'1':['4124','1241','124'],'2':['12412','142','1241']}

		pkl_file = open('account.pkl','wb')
		cPickle.down(obj,pkl_file)
		pkl_file.close()

		pkl_file = open('account.pkl','rb')
		account_list = cPickle.load(pkl_file)
		pkl_file.close()

	�ļ����󷽷�
		
		file.close()                     # �ر��ļ�
		file.fileno()                    # �����ļ���������
		file.flush()                     # ˢ���ļ����ڲ�������
		file.isatty()                    # �ж�file�Ƿ���һ����tty�豸
		file.next()                      # �����ļ�����һ��,����û��������ʱ����StopIteration�쳣
		file.read(size=-1)               # ���ļ���ȡsize���ֽ�,��δ����size�������ֵ��ʱ��,��ȡʣ��������ֽ�,Ȼ����Ϊ�ַ�������
		file.readline(size=-1)           # ���ļ��ж�ȡ������һ��(�����н�����),�򷵻����size���ַ�
		file.readlines(sizhint=0)        # ��ȡ�ļ�����������Ϊһ���б���
		file.xreadlines()                # ���ڵ���,���滻readlines()��һ������Ч�ķ���
		file.seek(off, whence=0)         # ���ļ����ƶ��ļ�ָ��,��whence(0�����ļ���ʼ,1����ǰλ��,2�����ļ�ĩβ)ƫ��off�ֽ�
		file.tell()                      # ���ص�ǰ���ļ��е�λ��
		file.truncate(size=file.tell())  # ��ȡ�ļ������size�ֽ�,Ĭ��Ϊ��ǰ�ļ�λ��
		file.write(str)                  # ���ļ�д���ַ���
		file.writelines(seq)             # ���ļ�д���ַ�������seq;seqӦ����һ�������ַ����Ŀɵ�������

	�ļ����������
		
		file.closed          # ��ʾ�ļ��ѱ��ر�,����ΪFalse
		file.encoding        # �ļ���ʹ�õı���  ��unicode�ַ�����д������ʱ,�����Զ�ʹ��file.encodingת��Ϊ�ֽ��ַ���;��file.encodingΪNoneʱʹ��ϵͳĬ�ϱ���
		file.mode            # Access�ļ���ʱʹ�õķ���ģʽ
		file.name            # �ļ���
		file.newlines        # δ��ȡ���зָ���ʱΪNone,ֻ��һ���зָ���ʱΪһ���ַ���,���ļ��ж������͵��н�����ʱ,��Ϊһ���������е�ǰ���������н��������б�
		file.softspace       # Ϊ0��ʾ�����һ���ݺ�,Ҫ����һ���ո��,1��ʾ����

	�쳣

		NameError:              # ���Է���һ��δ�����ı���
		ZeroDivisionError:      # ����Ϊ��
		SyntaxErrot:            # �������﷨����
		IndexError:             # ���������Ԫ�س������з�Χ
		KeyError:               # ����һ�������ڵ��ֵ�ؼ���
		IOError:                # ����/�������
		AttributeError:         # ���Է���δ֪�Ķ�������
		ImportError             # û��ģ��
		IndentationError        # �﷨��������
		KeyboardInterrupt       # ctrl+C
		SyntaxError             # �����﷨����
		ValueError              # ֵ����
		TypeError               # �������������Ҫ�󲻷���
		
		�����쳣

			raise exclass            # �����쳣,��exclass����һ��ʵ��(�����κ��쳣����)
			raise exclass()          # �����쳣,�����ڲ�����;ͨ���������ò�����(function calloperator:"()")��������������һ���µ�exclassʵ��,ͬ��Ҳû���쳣����
			raise exclass, args      # �����쳣,��ͬʱ�ṩ���쳣����args,������һ������Ҳ������Ԫ��
			raise exclass(args)      # �����쳣,ͬ��
			raise exclass, args, tb  # �����쳣,���ṩһ�����ټ�¼(traceback)����tb��ʹ��
			raise exclass,instance   # ͨ��ʵ�������쳣(ͨ����exclass��ʵ��)
			raise instance           # ͨ��ʵ�������쳣;�쳣������ʵ��������:�ȼ���raise instance.__class__, instance
			raise string             # �����ַ����쳣
			raise string, srgs       # �����ַ����쳣,������������args
			raise string,args,tb     # �����ַ����쳣,���ṩһ�����ټ�¼(traceback)����tb��ʹ��
			raise                    # ���´���ǰһ���쳣,���֮ǰû���쳣,����TypeError
			
		�ڽ��쳣
			
			BaseException                # �����쳣�Ļ���
			SystemExit                   # python�����������˳�
			KeyboardInterrupt            # �û��ж�ִ��
			Exception                    # �������Ļ���
			StopIteration                # ������û�и����ֵ
			GeneratorExit                # �����������쳣��֪ͨ�˳�
			SystemExit                   # python�����������˳�
			StandardError                # ���е��ڽ���׼�쳣�Ļ���
			ArithmeticError              # ������ֵ�������Ļ���
			FloatingPointError           # ����������
			OverflowError                # ��ֵ���㳬���������
			AssertionError               # �������ʧ��
			AttributeError               # ����û���������
			EOFError                     # û���ڽ�����,����EOF���
			EnvironmentError             # ����ϵͳ����Ļ���
			IOError                      # ����/�������ʧ��
			OSError                      # ����ϵͳ����
			WindowsError                 # windowsϵͳ����ʧ��
			ImportError                  # ����ģ��/����ʧ��
			KeyboardInterrupt            # �û��ж�ִ��(ͨ����ctrl+c)
			LookupError                  # ��Ч���ݲ�ѯ�Ļ���
			IndexError                   # ������û�д�����(index)
			KeyError                     # ӳ����û�������
			MemoryError                  # �ڴ��������(����python����������������)
			NameError                    # δ����/��ʼ������(û������)
			UnboundLocalError            # ����δ��ʼ���ı��ر���
			ReferenceError               # ��������ͼ�����Ѿ����������˵Ķ���
			RuntimeError                 # һ�������ʱ����
			NotImplementedError          # ��δʵ�ֵķ���
			SyntaxError                  # python�﷨����
			IndentationError             # ��������
			TabError                     # tab�Ϳո����
			SystemError                  # һ��Ľ�����ϵͳ����
			TypeError                    # ��������Ч�Ĳ���
			ValueError                   # ������Ч�Ĳ���
			UnicodeError                 # Unicode��صĴ���
			UnicodeDecodeError           # Unicode����ʱ�Ĵ���
			UnicodeEncodeError           # Unicode����ʱ�Ĵ���
			UnicodeTranslateError        # Unicodeת��ʱ����
			Warning                      # ����Ļ���
			DeprecationWarning           # ���ڱ����õ������ľ���
			FutureWarning                # ���ڹ��콫��������иı�ľ���
			OverflowWarning              # �ɵĹ����Զ�����Ϊ�����εľ���
			PendingDeprecationWarning    # �������Խ��ᱻ�����ľ���
			RuntimeWarning               # ���ɵ�����ʱ��Ϊ�ľ���
			SyntaxWarning                # ���ɵ��﷨�ľ���
			UserWarning                  # �û��������ɵľ���

		class MyException(Exception):   # �̳�Exception�쳣����,�����Լ����쳣
				pass
		try:                          # ���������쳣
				option=int(raw_input('my age:'))
				if option != 28:
						raise MyException,'a1'  #�����쳣
		except MyException,a:         # �쳣�������
				print 'MyExceptionaa'
				print a    # ��ӡ�쳣������
		except:            # ��׽������������
				print 'except'
		finally:           # ����ʲô�������ִ�� �ر��ļ���Ͽ����ӵ�
			   print 'finally' 
		else:              # ���κ��쳣 �޷���finallyͬ��
				print 'no Exception'

	����ʽ��̵��ڽ�����

		apply(func[,nkw][,kw])          # �ÿ�ѡ�Ĳ���������func,nkwΪ�ǹؼ��ֲ���,kwΪ�ؼ��ֲ���;����ֵ�Ǻ������õķ���ֵ
		filter(func,seq)                # ����һ����������func����������ÿ��seq�е�Ԫ��;����һ��ʹfunc����ֵΪtrue��Ԫ�ص�����
		map(func,seq1[,seq2])           # ������func�����ڸ�������(s)��ÿ��Ԫ��,����һ���б����ṩ����ֵ;���funcΪNone,func����Ϊһ����ݺ���,����һ������ÿ��������Ԫ�ؼ��ϵ�n��Ԫ����б�
		reduce(func,seq[,init])         # ����Ԫ����������seq���е�Ԫ��,ÿ��Я��һ��(��ǰ�Ľ���Լ���һ������Ԫ��),�����ؽ����еĽ������һ��ֵ�����ڻ�õ����Ľ����,���������ǵ�����Ϊһ����һ�ķ���ֵ;�����ʼֵinit����,��һ���Ƚϻ���init�͵�һ������Ԫ�ض��������е�ͷ����Ԫ��

	re����

		compile(pattern,flags=0)          # ��������ʽģʽpattern���б���,flags�ǿ�ѡ��ʶ��,������һ��regex����
		match(pattern,string,flags=0)     # ������������ʽģʽpatternƥ���ַ���string,flags�ǿ�ѡ��ʶ��,���ƥ��ɹ�,�򷵻�һ��ƥ�����;���򷵻�None
		search(pattern,string,flags=0)    # ���ַ���string������������ʽģʽpattern�ĵ�һ�γ���,flags�ǿ�ѡ��ʶ��,���ƥ��ɹ�,�򷵻�һ��ƥ�����;���򷵻�None
		findall(pattern,string[,flags])   # ���ַ���string������������ʽģʽpattern������(���ظ�)����:����һ��ƥ�������б�  # pattern=u'\u4e2d\u6587' ����UNICODE
		finditer(pattern,string[,flags])  # ��findall()��ͬ,�����صĲ����б���ǵ�����;����ÿ��ƥ��,�õ���������һ��ƥ�����
		split(pattern,string,max=0)       # ����������ʽpattern�еķָ������ַ�string�ָ�Ϊһ���б�,���سɹ�ƥ����б�,���ָ�max��(Ĭ������)
		sub(pattern,repl,string,max=0)    # ���ַ���string������ƥ��������ʽpattern�ĵط��滻���ַ���repl,���max��ֵû�и���,�������ƥ��ĵط������滻(subn()�᷵��һ����ʾ�滻��������ֵ)
		group(num=0)                      # ����ȫ��ƥ�����(��ָ�������num������)
		groups()                          # ����һ������ȫ��ƥ��������Ԫ��(���ûƥ��ɹ�,����һ����Ԫ��)
		
		����
			re.findall(r'a[be]c','123abc456eaec789')         # ����ƥ������б� ['abc', 'aec']
			re.match("^(1|2) *(.*) *abc$", str).group(2)     # ȡ�ڶ�����ǩ
			re.match("^(1|2) *(.*) *abc$", str).groups()     # ȡ���б�ǩ
			re.sub('[abc]','A','alex')                       # �滻
			for i in re.finditer(r'\d+',s):                  # ����
				print i.group(),i.span()                     #
		
		������ҳ��UNICODE��ʽ������
			QueryAdd='http://www.anti-spam.org.cn/Rbl/Query/Result'
			Ip='222.129.184.52'
			s = requests.post(url=QueryAdd, data={'IP':Ip})
			re.findall(u'\u4e2d\u56fd', s.text, re.S)

	����ת��

		a='����'          # ����δ���尴�����ն�utf8��gbk
		u=u'����'         # ����Ϊunicode����  uֵΪ u'\u4e2d\u6587'
		u.encode('utf8')  # תΪutf8��ʽ uֵΪ '\xe4\xb8\xad\xe6\x96\x87'
		print u           # �����ʾ ����
		print u.encode('utf8')      # תΪutf8��ʽ,����ʾ�ն˱���Ϊutf8  �����ʾ ����  ���벻һ��������
		print u.encode('gbk')       # ��ǰ�ն�Ϊutf8 ������

		ord('4')          # �ַ�תASCII��
		chr(52)           # ASCII��ת�ַ�

	�����ݹ�

		[os.path.join(x[0],y) for x in os.walk('/root/python/5') for y in x[2]]

		for i in os.walk('/root/python/5/work/server'):
			print i

2 ����ģ��

	osģ��

		�ļ�����
			mkfifo()/mknod()       # ���������ܵ�/�����ļ�ϵͳ�ڵ�
			remove()/unlink()      # ɾ���ļ�
			rename()/renames()     # �������ļ�
			*stat()                # �����ļ���Ϣ
			symlink()              # ������������
			utime()                # ����ʱ���
			tmpfile()              # ��������('w+b')һ���µ���ʱ�ļ�
			walk()                 # ����Ŀ¼���µ������ļ���
		
		Ŀ¼/�ļ���
			chdir()/fchdir()       # �ı䵱ǰ����Ŀ¼/ͨ��һ���ļ��������ı䵱ǰ����Ŀ¼
			chroot()               # �ı䵱ǰ���̵ĸ�Ŀ¼
			listdir()              # �г�ָ��Ŀ¼���ļ�
			getcwd()/getcwdu()     # ���ص�ǰ����Ŀ¼/������ͬ,������һ��unicode����
			mkdir()/makedirs()     # ����Ŀ¼/�������Ŀ¼
			rmdir()/removedirs()   # ɾ��Ŀ¼/ɾ�����Ŀ¼
		
		����/Ȩ��
			saccess()              # ����Ȩ��ģʽ
			chmod()                # �ı�Ȩ��ģʽ
			chown()/lchown()       # �ı�owner��groupID������ͬ,�������������
			umask()                # ����Ĭ��Ȩ��ģʽ
			
		�ļ�����������
			open()                 # �ײ�Ĳ���ϵͳopen(�����Ƚ�,ʹ�ñ�׼���ڽ�open()����)
			read()/write()         # �����ļ���������ȡ/д������ ����С��ȡ�ļ���������
			dup()/dup2()           # �����ļ���������/������ͬ,���Ǹ��Ƶ���һ���ļ�������
		
		�豸��
			makedev()              # ��major��minor�豸�Ŵ���һ��ԭʼ�豸��
			major()/minor()        # ��ԭʼ�豸�Ż��major/minor�豸��
		
		os.pathģ��

			os.path.expanduser('~/.ssh/key')   # ��Ŀ¼���ļ���ȫ·��

			�ָ�
				basename()         # ȥ��Ŀ¼·��,�����ļ���
				dirname()          # ȥ���ļ���,����Ŀ¼·��
				join()             # ������ĸ�������ϳ�һ��·����
				spllt()            # ����(dirname(),basename())Ԫ��
				splitdrive()       # ����(drivename,pathname)Ԫ��
				splitext()         # ����(filename,extension)Ԫ��
			
			��Ϣ
				getatime()         # �����������ʱ��
				getctime()         # �����ļ�����ʱ��
				getmtime()         # ��������ļ��޸�ʱ��
				getsize()          # �����ļ���С(�ֽ�)
			
			��ѯ
				exists()          # ָ��·��(�ļ���Ŀ¼)�Ƿ����
				isabs()           # ָ��·���Ƿ�Ϊ����·��
				isdir()           # ָ��·���Ƿ������Ϊһ��Ŀ¼
				isfile()          # ָ��·���Ƿ������Ϊһ���ļ�
				islink()          # ָ��·���Ƿ������Ϊһ����������
				ismount()         # ָ��·���Ƿ������Ϊһ�����ص�
				samefile()        # ����·�����Ƿ�ָ��ͬһ���ļ�
		
		���ģ��
			base64              # �ṩ�������ַ������ı��ַ�����ı���/�������
			binascii            # �ṩ�����ƺ�ASCII����Ķ������ַ�����ı���/�������
			bz2                 # ����BZ2��ʽ��ѹ���ļ�
			csv                 # ����csv�ļ�(���ŷָ��ļ�)
			csv.reader(open(file))
			filecmp             # ���ڱȽ�Ŀ¼���ļ�
			fileinput           # �ṩ����ı��ļ����е�����
			getopt/optparse     # �ṩ�������в����Ľ���/����
			glob/fnmatch        # �ṩunix��ʽ��ͨ���ƥ��Ĺ���
			gzip/zlib           # ��дGNU zip(gzip)�ļ�(ѹ����Ҫzlibģ��)
			shutil              # �ṩ�߼��ļ����ʹ���
			c/StringIO          # ���ַ��������ṩ���ļ��ӿ�
			tarfile             # ��дTAR�鵵�ļ�,֧��ѹ���ļ�
			tempfile            # ����һ����ʱ�ļ�
			uu                  # uu��ʽ�ı���ͽ���
			zipfile             # ���ڶ�ȡzip�鵵�ļ��Ĺ���
			environ['HOME']     # �鿴ϵͳ��������
		
		�ӽ���
			os.fork()    # �����ӽ���,�����Ƹ��������в���  ͨ���ж�pid = os.fork() ��pidֵ,�ֱ�ִ�и��������ӽ��̲�����0Ϊ�ӽ���
			os.wait()    # �ȴ��ӽ��̽���

		��ƽ̨osģ������

			linesep         # �������ļ��зָ��е��ַ���
			sep             # �����ָ��ļ�·�����ֵ��ַ���
			pathsep         # ���ڷָ��ļ�·�����ַ���
			curdir          # ��ǰ����Ŀ¼���ַ�������
			pardir          # ��Ŀ¼�ַ�������

	�����ʼ�

		�����ʼ�����

			#!/usr/bin/python
			#encoding:utf8
			# ���� smtplib �� MIMEText 
			import smtplib
			from email.mime.text import MIMEText

			# ���巢���б� 
			mailto_list=["272121935@qq.com","272121935@163.com"]

			# ���÷��������ơ��û����������Լ��ʼ���׺ 
			mail_host = "smtp.163.com"
			mail_user = "mailuser"
			mail_pass = "password"
			mail_postfix="163.com"

			# �����ʼ�����
			def send_mail(to_list, sub):
				me = mail_user + "<"+mail_user+"@"+mail_postfix+">"
				fp = open('context.txt')
				msg = MIMEText(fp.read(),_charset="utf-8")
				fp.close()
				msg['Subject'] = sub
				msg['From'] = me
				msg['To'] = ";".join(to_list)
				try:
					send_smtp = smtplib.SMTP()
					send_smtp.connect(mail_host)
					send_smtp.login(mail_user, mail_pass)
					send_smtp.sendmail(me, to_list, msg.as_string())
					send_smtp.close()
					return True
				except Exception, e:
					print str(e)
					return False

			if send_mail(mailto_list,"����"):
				print "���Գɹ�"
			else:
				print "����ʧ��"

		���͸���

			#!/usr/bin/python
			#encoding:utf8
			import smtplib
			from email.mime.multipart import MIMEMultipart
			from email.mime.base import MIMEBase
			from email import encoders

			def send_mail(to_list, sub, filename):
				me = mail_user + "<"+mail_user+"@"+mail_postfix+">"
				msg = MIMEMultipart()
				msg['Subject'] = sub
				msg['From'] = me
				msg['To'] = ";".join(to_list)
				submsg = MIMEBase('application', 'x-xz')
				submsg.set_payload(open(filename,'rb').read())
				encoders.encode_base64(submsg)
				submsg.add_header('Content-Disposition', 'attachment', filename=filename)
				msg.attach(submsg)
				try:
					send_smtp = smtplib.SMTP()
					send_smtp.connect(mail_host)
					send_smtp.login(mail_user, mail_pass)
					send_smtp.sendmail(me, to_list, msg.as_string())
					send_smtp.close()
					return True
				except Exception, e:
					print str(e)[1]
					return False

			# ���÷��������ơ��û����������Լ��ʼ���׺ 
			mail_host = "smtp.163.com"
			mail_user = "xuesong"
			mail_pass = "mailpasswd"
			mail_postfix = "163.com"
			mailto_list = ["272121935@qq.com","quanzhou722@163.com"]
			title = 'check'
			filename = 'file_check.html'
			if send_mail(mailto_list,title,filename):
				print "���ͳɹ�"
			else:
				print "����ʧ��"

	��ѹ��

		gzipѹ��

			import gzip
			f_in = open('file.log', 'rb')
			f_out = gzip.open('file.log.gz', 'wb')
			f_out.writelines(f_in)
			f_out.close()
			f_in.close()

		gzipѹ��1

			File = 'xuesong_18.log'
			g = gzip.GzipFile(filename="", mode='wb', compresslevel=9, fileobj=open((r'%s.gz' %File),'wb'))
			g.write(open(r'%s' %File).read())
			g.close()

		gzip��ѹ

			g = gzip.GzipFile(mode='rb', fileobj=open((r'xuesong_18.log.gz'),'rb'))
			open((r'xuesong_18.log'),'wb').write(g.read())

		ѹ��tar.gz

			import os
			import tarfile
			tar = tarfile.open("/tmp/tartest.tar.gz","w:gz")   # ����ѹ������
			for path,dir,files in os.walk("/tmp/tartest"):     # �ݹ��ļ�Ŀ¼
				for file in files:
					fullpath = os.path.join(path,file)
					tar.add(fullpath)                          # ����ѹ����
			tar.close()

		��ѹtar.gz
			
			import tarfile
			tar = tarfile.open("/tmp/tartest.tar.gz")
			#tar.extract("/tmp")                           # ȫ����ѹ��ָ��·��
			names = tar.getnames()                         # �����ļ���
			for name in names:
				tar.extract(name,path="./")                # ��ѹָ���ļ�
			tar.close()

		zipѹ��
			import zipfile,os
			f = zipfile.ZipFile('filename.zip', 'w' ,zipfile.ZIP_DEFLATED)    # ZIP_STORE ΪĬ�ϱ�ѹ��. ZIP_DEFLATED ��ѹ��
			#f.write('file1.txt')                              # ���ļ�д��ѹ����
			for path,dir,files in os.walk("tartest"):          # �ݹ�ѹ��Ŀ¼
				for file in files:
					f.write(os.path.join(path,file))           # ���ļ����д��ѹ����         
			f.close()

		zip��ѹ
			if zipfile.is_zipfile('filename.zip'):        # �ж�һ���ļ��ǲ���zip�ļ�
				f = zipfile.ZipFile('filename.zip')
				for file in f.namelist():                 # �����ļ��б�
					f.extract(file, r'/tmp/')             # ��ѹָ���ļ�
				#f.extractall()                           # ��ѹȫ��
				f.close()

	ʱ��

		import time
		time.strftime('%Y-%m-%d_%X',time.localtime( time.time() ) )

		��ʽ��ʱ��
			tomorrow.strftime('%Y%m%d_%H%M')

		��һ�������һ��
			import datetime
			lastMonth=datetime.date(datetime.date.today().year,datetime.date.today().month,1)-datetime.timedelta(1)
			lastMonth.strftime("%Y/%m")

		ǰһ��
			(datetime.datetime.now() + datetime.timedelta(days=-1) ).strftime('%Y%m%d')
			
		�ϸ���
			time.localtime()[1] - 1
			
		ʱ���ת��ɶ�ʱ��֮��ת��
			a=time.time()
			time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(a))
			time.mktime(time.strptime('2012-03-28 06:53:40', '%Y-%m-%d %H:%M:%S'))
			
		����ʱ���ʽ�ж�
		
			#encoding:utf8
			import time
			while 1:
				atime=raw_input('�����ʽ��[14.05.13 13:00]:')
				try:
					btime=time.mktime(time.strptime('%s:00' %atime, '%y.%m.%d %H:%M:%S'))
					break
				except:
					print 'ʱ���������,���������룬��ʽ��[14.05.13 13:00]'

		�������������

			import datetime
			d1 = datetime.datetime(2005, 2, 16)
			d2 = datetime.datetime(2004, 12, 31)
			(d1 - d2).days

		����10��Сʱ

			import datetime
			d1 = datetime.datetime.now()
			d3 = d1 + datetime.timedelta(hours=10)
			d3.ctime()

	hash

		import md5
		m = md5.new('123456').hexdigest()
		
		import hashlib
		m = hashlib.md5()
		m.update("Nobody inspects")    # ʹ��update�������ַ���md5����
		m.digest()                     # ���ܺ�����ƽ��
		m.hexdigest()                  # ���ܺ�ʮ���ƽ��
		hashlib.new("md5", "string").hexdigest()               # ���ַ�������
		hashlib.new("md5", open("file").read()).hexdigest()    # �鿴�ļ�MD5ֵ

	������������

		import getpass
		passwd=getpass.getpass()

	string��ӡa-z
		import string
		string.lowercase       # a-zСд
		string.uppercase       # A-Z��С

3 socket

	from socket import *         # ���� socket.socket()
	
	s.bind()         # �󶨵�ַ���׽���
	s.listen()       # ��ʼTCP����
	s.accept()       # ��������TCP�ͻ������ӣ��ȴ����ӵĵ���
	s.connect()      # ������ʼ��TCP����������
	s.connect_ex()   # connect()��������չ�汾������ʱ���س����룬�������ܳ��쳣
	s.recv()         # ����TCP����
	s.send()         # ����TCP����
	s.sendall()      # ��������TCP����
	s.recvfrom()     # ����UDP����
	s.sendto()       # ����UDP����
	s.getpeername()  # ���ӵ���ǰ�׽��ֵ�Զ�˵ĵ�ַ(TCP����)
	s.getsockname()  # ��ǰ�׽��ֵĵ�ַ
	s.getsockopt()   # ����ָ���׽��ֵĲ���
	s.setsockopt()   # ����ָ���׽��ֵĲ���
	s.close()        # �ر��׽���
	s.setblocking()  # �����׽��ֵ������������ģʽ
	s.settimeout()   # ���������׽��ֲ����ĳ�ʱʱ��
	s.gettimeout()   # �õ������׽��ֲ����ĳ�ʱʱ��
	s.filen0()       # �׽��ֵ��ļ�������
	s.makefile()     # ����һ������׽��ֹ������ļ�����

	socket.AF_UNIX	 # ֻ�ܹ����ڵ�һ��Unixϵͳ���̼�ͨ��
	socket.AF_INET 	 # ������֮������ͨ��
	socket.AF_INET6	 # IPv6

	socket.SOCK_STREAM	  # ��ʽsocket , for TCP
	socket.SOCK_DGRAM	  # ���ݱ�ʽsocket , for UDP
	socket.SOCK_RAW	      # ԭʼ�׽��֣���ͨ���׽����޷�����ICMP��IGMP�����籨�ģ���SOCK_RAW���ԣ���Σ�SOCK_RAWҲ���Դ��������IPv4���ģ����⣬����ԭʼ�׽��֣�����ͨ��IP_HDRINCL�׽���ѡ�����û�����IPͷ��

	socket.SOCK_RDM 	  # ��һ�ֿɿ���UDP��ʽ������֤�������ݱ�������֤˳��SOCK_RAM�����ṩ��ԭʼЭ��ĵͼ����ʣ�����Ҫִ��ĳЩ�������ʱʹ�ã��緢��ICMP���ġ�SOCK_RAMͨ�������ڸ߼��û������Ա���еĳ���ʹ�á�

	socket.SOCK_SEQPACKET	 # �ɿ����������ݰ�����

	SocketServer
	
		#!/usr/bin/python
		#server.py
		import SocketServer
		import os
		class MyTCP(SocketServer.BaseRequestHandler):
			def handle(self):
				while True:
					self.data=self.request.recv(1024).strip()
					if self.data == 'quit' or not self.data:break
					
					cmd=os.popen(self.data).read()
					if cmd == '':cmd= self.data + ': Command not found'
					self.request.sendall(cmd)
		if __name__ == '__main__':
			HOST,PORT = '10.0.0.119',50007
			server = SocketServer.ThreadingTCPServer((HOST,PORT),MyTCP)
			server.serve_forever()

	SocketClient

		#!/usr/bin/python
		#client.py
		import socket

		HOST='10.0.0.119'
		PORT=50007
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect((HOST,PORT))

		while True:
			while True:
				cmd=raw_input('CMD:').strip()
				if cmd != '':break
			s.sendall(cmd)      
			data=s.recv(1024).split('\n')
			print 'cmd:'
			for line in data:print line
		s.close()

	ftp

		ftpserver

			#!/usr/bin/python
			#ftpserver.py

			import SocketServer
			import os
			import cPickle
			import md5
			from time import sleep

			def filer(file1):
				try:
					f = file(file1,'rb')
					return cPickle.load(f)
				except IOError:
					return {}
				except EOFError:
					return {}
				f.close()

			def filew(file1,content):
				f = file(file1,'wb')
				cPickle.dump(content,f)
				f.close()

			class MyTCP(SocketServer.BaseRequestHandler):
				def handle(self):
					i = 0
					while i<3:
						user=self.request.recv(1024).strip()
						userinfo=filer('user.pkl')
						if userinfo.has_key(user.split()[0]):
							if md5.new(user.split()[1]).hexdigest() == userinfo[user.split()[0]]:
								results='login successful'
								self.request.sendall(results)
								login='successful'
								break
							else:
								i = i + 1
								results='Error:password not correct'
								self.request.sendall(results)
								continue
						else:
							i = i + 1
							results='Error:password not correct'
							self.request.sendall(results)
							continue
						break
					else:
						results = 'Error:Wrong password too many times'
						self.request.sendall(results)
						login='failure'
					home_path = os.popen('pwd').read().strip() + '/' + user.split()[0]
					current_path = '/'
					print home_path
					while True:
						if login == 'failure':
							break
						print 'home_path:%s=current_path:%s' %(home_path,current_path)
						cmd=self.request.recv(1024).strip()
						print cmd
						if cmd == 'quit':
							break
						elif cmd == 'dir':
							list=os.listdir('%s%s' %(home_path,current_path))
							if list:
								dirlist,filelist = '',''
								for i in list:
									if os.path.isdir('%s%s%s' %(home_path,current_path,i)):
										dirlist = dirlist + '\033[32m' + i + '\033[m\t'
									else:
										filelist = filelist + i + '\t'
								results = dirlist + filelist
							else:
								results = '\033[31mnot find\033[m'
							self.request.sendall(results)
						elif cmd == 'pdir':
							self.request.sendall(current_path)
						elif cmd.split()[0] == 'mdir':
							if cmd.split()[1].isalnum():
								tmppath='%s%s%s' %(home_path,current_path,cmd.split()[1])
								os.makedirs(tmppath)
								self.request.sendall('\033[32mcreating successful\033[m')
							else:
								self.request.sendall('\033[31mcreate failure\033[m')
						elif cmd.split()[0] == 'cdir':
							if cmd.split()[1] == '/':
								tmppath='%s%s' %(home_path,cmd.split()[1])
								if os.path.isdir(tmppath):
									current_path = cmd.split()[1]
									self.request.sendall(current_path)
								else:
									self.request.sendall('\033[31mnot_directory\033[m')
							elif cmd.split()[1].startswith('/'):
								tmppath='%s%s' %(home_path,cmd.split()[1])
								if os.path.isdir(tmppath):
									current_path = cmd.split()[1] + '/'
									self.request.sendall(current_path)
								else:
									self.request.sendall('\033[31mnot_directory\033[m')
							else:
								tmppath='%s%s%s' %(home_path,current_path,cmd.split()[1])
								if os.path.isdir(tmppath):
									current_path = current_path + cmd.split()[1] + '/'
									self.request.sendall(current_path)
								else:
									self.request.sendall('\033[31mnot_directory\033[m')
						elif cmd.split()[0] == 'get':
							if os.path.isfile('%s%s%s' %(home_path,current_path,cmd.split()[1])):
								f = file('%s%s%s' %(home_path,current_path,cmd.split()[1]),'rb')
								self.request.sendall('ready_file')
								sleep(0.5)
								self.request.send(f.read())
								f.close()
								sleep(0.5)
							elif os.path.isdir('%s%s%s' %(home_path,current_path,cmd.split()[1])):
								self.request.sendall('ready_dir')
								sleep(0.5)
								for dirpath in os.walk('%s%s%s' %(home_path,current_path,cmd.split()[1])):
									dir=dirpath[0].replace('%s%s' %(home_path,current_path),'',1)
									self.request.sendall(dir)
									sleep(0.5)
									for filename in dirpath[2]:
										self.request.sendall(filename)
										sleep(0.5)
										f = file('%s/%s' %(dirpath[0],filename),'rb')
										self.request.send(f.read())
										f.close()
										sleep(0.5)
										self.request.sendall('file_get_done')
										sleep(0.5)
									else:
										self.request.sendall('dir_get_done')
									sleep(0.5)
							else:
								self.request.sendall('get_failure')
								continue
							self.request.sendall('get_done')
					
						elif cmd.split()[0] == 'send':
							if os.path.exists('%s%s%s' %(home_path,current_path,cmd.split()[1])):
								self.request.sendall('existing')
								action=self.request.recv(1024)
								if action == 'cancel':
									continue
							self.request.sendall('ready')
							msg=self.request.recv(1024)
							if msg == 'ready_file':
								f = file('%s%s%s' %(home_path,current_path,cmd.split()[1]),'wb')
								while True:
									data=self.request.recv(1024)
									if data == 'file_send_done':break
									f.write(data)
								f.close()

							elif msg == 'ready_dir':
								os.system('mkdir -p %s%s%s' %(home_path,current_path,cmd.split()[1]))
								while True:
									dir=self.request.recv(1024)
									if dir == 'get_done':break
									os.system('mkdir -p %s%s%s' %(home_path,current_path,dir))
									while True:
										filename=self.request.recv(1024)
										if filename == 'dir_send_done':break
										f = file('%s%s%s/%s' %(home_path,current_path,dir,filename),'wb')
										while True:
											data=self.request.recv(1024)
											if data == 'file_send_done':break 
											f.write(data)
										f.close()
										self.request.sendall('%s/%s\t\033[32mfile_done\033[m' %(dir,filename))
									self.request.sendall('%s\t\033[32mdir_done\033[m' %(dir))
							elif msg == 'unknown_file':
								continue
							
						else:
							results = cmd.split()[0] + ': Command not found'
							self.request.sendall(results)

			if __name__ == '__main__':
				HOST,PORT = '10.152.14.85',50007
				server = SocketServer.ThreadingTCPServer((HOST,PORT),MyTCP)
				server.serve_forever()

		ftpmanage

			#!/usr/bin/python
			#manage_ftp.py
			import cPickle
			import sys
			import md5
			import os
			import getpass

			def filer(file1):
				try:
					f = file(file1,'rb')
					return cPickle.load(f)
				except IOError:
					return {}
				except EOFError:
					return {}
				f.close()

			def filew(file1,content):
				f = file(file1,'wb')
				cPickle.dump(content,f)
				f.close()

			while True:
				print '''
				1.add user
				2.del user
				3.change password
				4.query user
				0.exit
				'''
				i = raw_input(':').strip()
				userinfo=filer('user.pkl')
				if i == '':
					continue
				elif i == '1':
					while True:
						user=raw_input('user name:').strip()
						if user.isalnum():
							i = 0
							while i<3:
								passwd=getpass.getpass('passwd:').strip()
								if passwd == '':
									continue
								else:
									passwd1=getpass.getpass('Confirm password:').strip()
									if passwd == passwd1:
										mpasswd = md5.new(passwd).hexdigest()
										userinfo[user] = mpasswd
										os.system('mkdir -p %s' %user)
										print '%s creating successful ' %user
										break
									else:
										print "Passwords don't match "
										i = i + 1
										continue
							else:
								print 'Too many wrong'
								continue
							break
						else:
							print 'user not legal'
							continue
				elif i == '2':
					user=raw_input('user name:').strip()
					if userinfo.has_key(user):
						del userinfo[user]
						print 'Delete users successfully'
					else:
						print 'user not exist'
						continue
				elif i == '3':
					user=raw_input('user name:').strip()
					if userinfo.has_key(user):
						i = 0
						while i<3:
							passwd=getpass.getpass('passwd:').strip()
							if passwd == '':
								continue
							else:
								passwd1=getpass.getpass('Confirm password:').strip()
								if passwd == passwd1:
									mpasswd = md5.new(passwd).hexdigest()
									userinfo[user] = mpasswd
									print '%s password is changed' %user
									break
								else:
									print "Passwords don't match "
									i = i + 1
									continue
						else:
							print 'Too many wrong'
							continue
					else:
						print 'user not exist'
						continue
				elif i == '4':
					print userinfo.keys()
				elif i == '0':
					sys.exit()
				else:
					print 'select error'
					continue
				filew('user.pkl',content=userinfo)
		
		ftpclient

			#!/usr/bin/python
			#ftpclient.py

			import socket
			import os
			import getpass
			from time import sleep

			HOST='10.152.14.85'
			PORT=50007
			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.connect((HOST,PORT))
				
			while True:
				user = raw_input('user:').strip()
				if user.isalnum():
					while True:
						passwd = getpass.getpass('passwd:').strip()
						s.sendall(user + ' ' + passwd)
						servercmd=s.recv(1024)
						if servercmd == 'login successful':
							print '\033[32m%s\033[m' %servercmd
							break
						else:
							print servercmd

					while True:
						cmd=raw_input('FTP>').strip()
						if cmd == '':
							continue
						if cmd.split()[0] == 'get':
							if cmd == 'get':continue
							for i in cmd.split()[1:]:
								if os.path.exists(i):
									confirm = raw_input("\033[31mPlease confirm whether the cover %s(Y/N):\033[m" %(i)).upper().startswith('Y')
									if not confirm:
										print '%s cancel' %i
										continue
								s.sendall('get ' + i)
								servercmd=s.recv(1024)
								if servercmd == 'inexistence':
									print '%s \t\033[32minexistence\033[m' %i
									continue
								elif servercmd == 'ready_file':
									f = file(i,'wb')
									while True:
										data=s.recv(1024)
										if data == 'get_done':break 
										f.write(data)
									f.close()
									print '%s \t\033[32mfile_done\033[m' %(i)
								elif servercmd == 'ready_dir':
									try:
										os.makedirs(i)
									except:
										pass
									while True:
										serverdir=s.recv(1024)
										if serverdir == 'get_done':break 
										os.system('mkdir -p %s' %serverdir)
										print '%s \t\033[32mdir_done\033[m' %(serverdir)
										while True:
											serverfile=s.recv(1024)
											if serverfile == 'dir_get_done':break 
											f = file('%s/%s' %(serverdir,serverfile),'wb')
											while True:
												data=s.recv(1024)
												if data == 'file_get_done':break 
												f.write(data)
											f.close()
											print '%s/%s \t\033[32mfile_done\033[m' %(serverdir,serverfile)

						elif cmd.split()[0] == 'send':
						
							if cmd == 'send':continue
							for i in cmd.split()[1:]:
								if not os.path.exists(i):
									print '%s\t\033[31minexistence\033[m' %i
									continue
							
								s.sendall('send ' + i)
								servercmd=s.recv(1024)
								if servercmd == 'existing':
									confirm = raw_input("\033[31mPlease confirm whether the cover %s(Y/N):\033[m" %(i)).upper().startswith('Y')
									if confirm:
										s.sendall('cover')
										servercmd=s.recv(1024)
									else:
										s.sendall('cancel')
										print '%s\tcancel' %i
										continue
								
								if os.path.isfile(i):
									s.sendall('ready_file')
									sleep(0.5)
									f = file(i,'rb')
									s.send(f.read())
									sleep(0.5)
									s.sendall('file_send_done')
									print '%s\t\033[32mfile done\033[m' %(cmd.split()[1])
									f.close()
								elif os.path.isdir(i):
									s.sendall('ready_dir')
									sleep(0.5)
									for dirpath in os.walk(i):
										dir=dirpath[0].replace('%s/' %os.popen('pwd').read().strip(),'',1)
										s.sendall(dir)
										sleep(0.5)
										for filename in dirpath[2]:
											s.sendall(filename)
											sleep(0.5)
											f = file('%s/%s' %(dirpath[0],filename),'rb')
											s.send(f.read())
											f.close()
											sleep(0.5)
											s.sendall('file_send_done')
											msg=s.recv(1024)
											print msg

										else:
											s.sendall('dir_send_done')
											msg=s.recv(1024)
											print msg
									
								else:
									s.sendall('unknown_file')
									print '%s\t\033[31munknown type\033[m' %i
									continue
								sleep(0.5)
								s.sendall('get_done')
							
						elif cmd.split()[0] == 'cdir':
							if cmd == 'cdir':continue
							s.sendall(cmd)
							data=s.recv(1024)
							print data
							continue
						elif cmd == 'ls':
							list=os.popen(cmd).read().strip().split('\n')
							if list:
								dirlist,filelist = '',''
								for i in list:
									if os.path.isdir(i):
										dirlist = dirlist + '\033[32m' + i + '\033[m\t'
									else:
										filelist = filelist + i + '\t'
								results = dirlist + filelist
							else:
								results = '\033[31mnot find\033[m'
							print results
							continue
						elif cmd == 'pwd':
							os.system(cmd)
						elif cmd.split()[0] == 'cd':
							try:
								os.chdir(cmd.split()[1])
							except:
								print '\033[31mcd failure\033[m'
						elif cmd == 'dir':
							s.sendall(cmd)
							data=s.recv(1024)
							print data
							continue
						elif cmd == 'pdir':
							s.sendall(cmd)
							data=s.recv(1024)
							print data
							continue
						elif cmd.split()[0] == 'mdir':
							if cmd == 'mdir':continue
							s.sendall(cmd)
							data=s.recv(1024)
							print data
							continue
						elif cmd.split()[0] == 'help':
							print '''
				get [file] [dir]
				send [file] [dir]

				dir
				mdir
				cdir
				pdir
				
				pwd
				md
				cd
				ls
				
				help
				quit
				'''
							continue
						elif cmd == 'quit':
							break
						else:
							print '\033[31m%s: Command not found,Please see the "help"\033[m' %cmd
				else:
					continue		
				break
			s.close()

	ɨ���������Ŷ˿�
		#!/usr/bin/env python

		import socket

		def check_server(address,port):
			s=socket.socket()
			try:
				s.connect((address,port))
				return True
			except socket.error,e:
				return False

		if __name__=='__main__':
			from optparse import OptionParser
			parser=OptionParser()
			parser.add_option("-a","--address",dest="address",default='localhost',help="Address for server",metavar="ADDRESS")
			parser.add_option("-s","--start",dest="start_port",type="int",default=1,help="start port",metavar="SPORT")
			parser.add_option("-e","--end",dest="end_port",type="int",default=1,help="end port",metavar="EPORT")
			(options,args)=parser.parse_args()
			print 'options: %s, args: %s' % (options, args)
			port=options.start_port
			while(port<=options.end_port):
				check = check_server(options.address, port)
				if (check):
					print 'Port  %s is on' % port
				port=port+1

4 mysql
	
	#apt-get install mysql-server
	#apt-get install python-MySQLdb
	help(MySQLdb.connections.Connection)      # �鿴���Ӳ���

	conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='fortress',port=3306)    # ��������
	#conn=MySQLdb.connect(unix_socket='/var/run/mysqld/mysqld.sock',user='root',passwd='123456')   # ʹ��socket�ļ�����
	cur=conn.cursor()                                            # �����α�
	conn.select_db('fortress')                                   # ѡ�����ݿ�
	sqlcmd = 'insert into user(name,age) value(%s,%s)'           # ����sql����
	cur.executemany(sqlcmd,[('aa',1),('bb',2),('cc',3)])         # �������ֵ
	cur.execute('delete from user where id=20')                  # ɾ��һ����¼
	cur.execute("update user set name='a' where id=20")          # ��ϸ����
	sqlresult = cur.fetchall()                                   # ����ȫ�����ؽ��
	conn.commit()                                                # �ύ
	cur.close()                                                  # �ر��α�
	conn.close()                                                 # �ر�����
	
	import MySQLdb
	def mydb(dbcmdlist):
		try:
			conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='fortress',port=3306)
			cur=conn.cursor()
			
			cur.execute('create database if not exists fortress;')  # �������ݿ�
			conn.select_db('fortress')                              # ѡ�����ݿ�
			cur.execute('drop table if exists log;')                # ɾ����
			cur.execute('CREATE TABLE log ( id BIGINT(20) NOT NULL AUTO_INCREMENT, loginuser VARCHAR(50) DEFAULT NULL, remoteip VARCHAR(50) DEFAULT NULL, PRIMARY KEY (id) );')  # ������
			
			result=[]
			for dbcmd in dbcmdlist:
				cur.execute(dbcmd)           # ִ��sql
				sqlresult = cur.fetchall()   # ����ȫ�����ؽ��
				result.append(sqlresult)
			conn.commit()                    # �ύ
			cur.close()
			conn.close()
			return result
		except MySQLdb.Error,e:
			print 'mysql error msg: ',e
	sqlcmd=[]
	sqlcmd.append("insert into log (loginuser,remoteip)values('%s','%s');" %(loginuser,remoteip))
	mydb(sqlcmd)

	sqlcmd=[]
	sqlcmd.append("select * from log;")
	result = mydb(sqlcmd)
	for i in result[0]:
		print i

5 �����ź�

	�źŵĸ���

		�ź�(signal): ����֮��ͨѶ�ķ�ʽ����һ������жϡ�һ������һ�����յ��źžͻ���ԭ���ĳ���ִ�������������źš�
		�����ź�һ��������ԭ��:
			1(����ʽ)  �ں˼�⵽һ��ϵͳ�¼�.�����ӽ����˳����񸸽��̷���SIGCHLD�ź�.���̰���control+c�ᷢ��SIGINT�ź�
			2(����ʽ)  ͨ��ϵͳ����kill����ָ�����̷����ź�
		����ϵͳ�涨�˽����յ��ź��Ժ��Ĭ����Ϊ������ͨ�����źŴ��������޸Ľ����յ��ź��Ժ����Ϊ���������ź��ǲ��ɸ��ĵ� SIGTOP �� SIGKILL
		���һ�������յ�һ��SIGUSR1�źţ�Ȼ��ִ���źŰ󶨺������ڶ���SIGUSR2�ź������ˣ���һ���ź�û�б�������ϵĻ����ڶ����źžͻᶪ����
		���̽����ź� SIGTERM �� SIGKILL ������:  SIGTERM �Ƚ��Ѻã������ܲ�׽����źţ�����������Ҫ���رճ����ڹرճ���֮ǰ�������Խ����򿪵ļ�¼�ļ��������������������ĳЩ����£�����������ڽ�����ҵ���Ҳ����жϣ���ô���̿��Ժ������SIGTERM�źš�

	�����ź�
		kill -l      # �鿴linux�ṩ���ź�

		SIGHUP  1          A     # �ն˹�����߿��ƽ�����ֹ
		SIGINT  2          A     # �����ն˽���(��control+c)
		SIGQUIT 3          C     # ���̵��˳���������
		SIGILL  4          C     # �Ƿ�ָ��
		SIGABRT 6          C     # ��abort(3)�������˳�ָ��
		SIGFPE  8          C     # �����쳣
		SIGKILL 9          AEF   # Kill�ź�  ����ֹͣ
		SIGSEGV 11         C     # ��Ч���ڴ�����
		SIGPIPE 13         A     # �ܵ�����: дһ��û�ж��˿ڵĹܵ�
		SIGALRM 14         A     # �����ź� ��alarm(2)�������ź� 
		SIGTERM 15         A     # ��ֹ�ź�,���ó���ȫ�˳� kill -15
		SIGUSR1 30,10,16   A     # �û��Զ����ź�1
		SIGUSR2 31,12,17   A     # �û��Զ����ź�2
		SIGCHLD 20,17,18   B     # �ӽ��̽����Զ��򸸽��̷���SIGCHLD�ź�
		SIGCONT 19,18,25         # ���̼���������ֹͣ�Ľ��̣�
		SIGSTOP 17,19,23   DEF   # ��ֹ����
		SIGTSTP 18,20,24   D     # �����նˣ�tty���ϰ���ֹͣ��
		SIGTTIN 21,21,26   D     # ��̨������ͼ�ӿ����ն˶�
		SIGTTOU 22,22,27   D     # ��̨������ͼ�ӿ����ն�д
		
		ȱʡ������һ���е���ĸ��������:
			A  ȱʡ�Ķ�������ֹ����
			B  ȱʡ�Ķ����Ǻ��Դ��źţ������źŶ�������������
			C  ȱʡ�Ķ�������ֹ���̲������ں�ӳ��ת��(dump core),�ں�ӳ��ת����ָ�������������ڴ��ӳ��ͽ������ں˽ṹ�еĲ���������һ����ʽת�����ļ�ϵͳ�����ҽ����˳�ִ�У��������ĺô���Ϊ����Ա�ṩ�˷��㣬ʹ�����ǿ��Եõ����̵�ʱִ��ʱ������ֵ����������ȷ��ת����ԭ�򣬲��ҿ��Ե������ǵĳ���
			D  ȱʡ�Ķ�����ֹͣ���̣�����ֹͣ״���Ժ������½�����ȥ��һ�����ڵ��ԵĹ����У�����ptraceϵͳ���ã�
			E  �źŲ��ܱ�����
			F  �źŲ��ܱ�����

	Python�ṩ���ź�
		import signal
		dir(signal)
		['NSIG', 'SIGABRT', 'SIGALRM', 'SIGBUS', 'SIGCHLD', 'SIGCLD', 'SIGCONT', 'SIGFPE', 'SIGHUP', 'SIGILL', 'SIGINT', 'SIGIO', 'SIGIOT', 'SIGKILL', 'SIGPIPE', 'SIGPOLL', 'SIGPROF', 'SIGPWR', 'SIGQUIT', 'SIGRTMAX', 'SIGRTMIN', 'SIGSEGV', 'SIGSTOP', 'SIGSYS', 'SIGTERM', 'SIGTRAP', 'SIGTSTP', 'SIGTTIN', 'SIGTTOU', 'SIGURG', 'SIGUSR1', 'SIGUSR2', 'SIGVTALRM', 'SIGWINCH', 'SIGXCPU', 'SIGXFSZ', 'SIG_DFL', 'SIG_IGN', '__doc__', '__name__', 'alarm', 'default_int_handler', 'getsignal', 'pause', 'signal']

	���źŴ�����
		#encoding:utf8
		import os,signal
		from time import sleep
		def onsignal_term(a,b):
			print 'SIGTERM'      # kill -15
		signal.signal(signal.SIGTERM,onsignal_term)     # �����ź�,ִ����Ӧ����

		def onsignal_usr1(a,b):
			print 'SIGUSR1'      # kill -10
		signal.signal(signal.SIGUSR1,onsignal_usr1)

		while 1:
			print 'ID',os.getpid()
			sleep(10)

	ͨ������һ�����̷����ź�
		import os,signal
		os.kill(16175,signal.SIGTERM)    # �����źţ�16175�ǰ��źŴ������Ľ���pid����Ҫ�����޸�
		os.kill(16175,signal.SIGUSR1)

	�����̽����ӽ��̽������͵�SIGCHLD�ź�
		#encoding:utf8
		import os,signal
		from time import sleep
		   
		def onsigchld(a,b):
			print '�յ��ӽ��̽����ź�'
		signal.signal(signal.SIGCHLD,onsigchld)
		   
		pid = os.fork()                # ����һ���ӽ���,���Ƹ�����������Դ����
		if pid == 0:                   # ͨ���ж��ӽ���os.fork()�Ƿ����0,�ֱ�ͬʱִ�и��������ӽ��̲���
		   print '�����ӽ���,pid��',os.getpid()
		   sleep(2)
		else:
			print '���Ǹ�����,pid��',os.getpid()
			os.wait()      # �ȴ��ӽ��̽���

	�����źŵĳ�������һ��ʹ�ö��߳���������̷����źţ�����©һЩ�ź�
		#encoding:utf8
		import os
		import signal
		from time import sleep  
		import Queue
		QCOUNT = Queue.Queue()  # ��ʼ������  
		def onsigchld(a,b):  
			'''�յ��źź�������в���һ������1'''
			print '�յ�SIGUSR1�ź�'
			sleep(1)
			QCOUNT.put(1)       # �������д��
		signal.signal(signal.SIGUSR1,onsigchld)   # ���źŴ�����
		while 1:
			print '�ҵ�pid��',os.getpid()
			print '���ڶ�����Ԫ�صĸ�����',QCOUNT.qsize()
			sleep(2)

		���̷߳��źŶ˵ĳ���

			#encoding:utf8
			import threading
			import os
			import signal
			def sendusr1():
			print '�����ź�'
				os.kill(17788, signal.SIGUSR1)     # ����Ľ���id��Ҫдǰһ������ʵ�����е�pid
			WORKER = []
			for i in range(1, 7):                  # ����6���߳�
				threadinstance = threading.Thread(target = sendusr1)
				WORKER.append(threadinstance)  
			for i in WORKER:
				i.start()
			for i in WORKER:
				i.join()
			print '���߳����'

6 �������ݿ�

	pythonʹ��memcache

		easy_install python-memcached   # ��װ(python2.7+)
		import memcache
		mc = memcache.Client(['10.152.14.85:12000'],debug=True)
		mc.set('name','luo',60)
		mc.get('name')
		mc.delete('name1')
		
		��������

			set(key,value,timeout)      # ��keyӳ�䵽value��timeoutָ����ʲôʱ�����ӳ��ʧЧ
			add(key,value,timeout)      # �����洢�ռ��в����ڼ���ͬ������ʱ�ű���
			replace(key,value,timeout)  # �����洢�ռ��д��ڼ���ͬ������ʱ�ű���

		��ȡ����

			get(key)                    # ����key��ָ���value
			get_multi(key1,key2,key3)   # ���Է�ͬ����ͬʱȡ�ö����ֵ�� ��ѭ������get����ʮ��

	pythonʹ��mongodb

		ԭ��: http://blog.nosqlfan.com/html/2989.html
		
		easy_install pymongo      # ��װ(python2.7+)
		import pymongo
		connection=pymongo.Connection('localhost',27017)   # ��������
		db = connection.test_database                      # �л����ݿ�
		collection = db.test_collection                    # ��ȡcollection
		# db��collection������ʱ�����ģ������Documentʱ����������

		�ĵ����, _id�Զ�����
			import datetime
			post = {"author": "Mike",
				"text": "My first blog post!",
				"tags": ["mongodb", "python", "pymongo"],
				"date": datetime.datetime.utcnow()}
			posts = db.posts
			posts.insert(post)
			ObjectId('...')

		��������
			new_posts = [{"author": "Mike",
				"text": "Another post!",
				"tags": ["bulk", "insert"],
				"date": datetime.datetime(2009, 11, 12, 11, 14)},
				{"author": "Eliot",
				"title": "MongoDB is fun",
				"text": "and pretty easy too!",
				"date": datetime.datetime(2009, 11, 10, 10, 45)}]
			posts.insert(new_posts)
			[ObjectId('...'), ObjectId('...')]
		
		��ȡ����collection
			db.collection_names()    # �൱��SQL��show tables
			
		��ȡ�����ĵ�
			posts.find_one()

		��ѯ����ĵ�
			for post in posts.find():
				post

		�������Ĳ�ѯ
			posts.find_one({"author": "Mike"})

		�߼���ѯ
			posts.find({"date": {"$lt": "d"}}).sort("author")

		ͳ������
			posts.count()

		������
			from pymongo import ASCENDING, DESCENDING
			posts.create_index([("date", DESCENDING), ("author", ASCENDING)])

		�鿴��ѯ��������
			posts.find({"date": {"$lt": "d"}}).sort("author").explain()["cursor"]
			posts.find({"date": {"$lt": "d"}}).sort("author").explain()["nscanned"]

	pythonʹ��redis

		https://pypi.python.org/pypi/redis
		pip install redis  OR easy_install redis
		import redis
		r = redis.StrictRedis(host='localhost', port=6379, db=0)
		r.set('foo', 'bar')
		r.get('foo')
		r.save()
		
		��Ƭ # û�㶮
			redis.connection.Connection(host='localhost', port=6379, db=0,  parser_class=<class 'redis.connection.PythonParser'>)
			redis.ConnectionPool( connection_class=<class 'redis.connection.Connection'>, max_connections=None, **connection_kwargs)

7 webҳ�����

	paramiko [ssh�ͻ���]

		��װ
			sudo apt-get install python-setuptools 
			easy_install
			sudo apt-get install python-all-dev
			sudo apt-get install build-essential

		paramikoʵ��(�˺������¼ִ������)

			#!/usr/bin/python
			#ssh
			import paramiko
			import sys,os

			host = '10.152.15.200'
			user = 'peterli'
			password = '123456'

			s = paramiko.SSHClient()                                 # ��ʵ��
			s.load_system_host_keys()                                # ���ر���HOST�����ļ�
			s.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # �������Ӳ���know_hosts�ļ��е�����
			s.connect(host,22,user,password,timeout=5)               # ����Զ������
			while True:
					cmd=raw_input('cmd:')
					stdin,stdout,stderr = s.exec_command(cmd)        # ִ������
					cmd_result = stdout.read(),stderr.read()         # ��ȡ������
					for line in cmd_result:
							print line,
			s.close()

		paramikoʵ��(�����ļ�)

			#!/usr/bin/evn python
			import os
			import paramiko
			host='127.0.0.1'
			port=22
			username = 'peterli'
			password = '123456'
			ssh=paramiko.Transport((host,port))
			privatekeyfile = os.path.expanduser('~/.ssh/id_rsa') 
			mykey = paramiko.RSAKey.from_private_key_file( os.path.expanduser('~/.ssh/id_rsa'))   # ����key ��ʹ��key�ɲ���
			ssh.connect(username=username,password=password)           # ����Զ������
			# ʹ��key�� password=password ���� pkey=mykey
			sftp=paramiko.SFTPClient.from_transport(ssh)               # SFTPʹ��Transportͨ��
			sftp.get('/etc/passwd','pwd1')                             # ���� ���˶�Ҫָ���ļ���
			sftp.put('pwd','/tmp/pwd')                                 # �ϴ�
			sftp.close()
			ssh.close()

		paramikoʵ��(��Կִ������)

			#!/usr/bin/python
			#ssh
			import paramiko
			import sys,os
			host = '10.152.15.123'
			user = 'peterli'
			s = paramiko.SSHClient()
			s.load_system_host_keys()
			s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			privatekeyfile = os.path.expanduser('~/.ssh/id_rsa')             # ����key·��
			mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
			# mykey=paramiko.DSSKey.from_private_key_file(privatekeyfile,password='061128')   # DSSKey��ʽ password��key������
			s.connect(host,22,user,pkey=mykey,timeout=5)
			cmd=raw_input('cmd:')
			stdin,stdout,stderr = s.exec_command(cmd)
			cmd_result = stdout.read(),stderr.read()
			for line in cmd_result:
					print line,
			s.close()

		ssh����(Pool������󲢷�)

			#!/usr/bin/env python
			#encoding:utf8
			#ssh_concurrent.py

			import multiprocessing
			import sys,os,time
			import paramiko

			def ssh_cmd(host,port,user,passwd,cmd):
				msg = "-----------Result:%s----------" % host

				s = paramiko.SSHClient()
				s.load_system_host_keys()
				s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				try:
					s.connect(host,22,user,passwd,timeout=5) 
					stdin,stdout,stderr = s.exec_command(cmd)

					cmd_result = stdout.read(),stderr.read()
					print msg
					for line in cmd_result:
							print line,

					s.close()
				except paramiko.AuthenticationException:
					print msg
					print 'AuthenticationException Failed'
				except paramiko.BadHostKeyException:
					print msg
					print "Bad host key"	

			result = []
			p = multiprocessing.Pool(processes=20)
			cmd=raw_input('CMD:')
			f=open('serverlist.conf')
			list = f.readlines()
			f.close()
			for IP in list:
				print IP
				host=IP.split()[0]
				port=int(IP.split()[1])
				user=IP.split()[2]
				passwd=IP.split()[3]
				result.append(p.apply_async(ssh_cmd,(host,port,user,passwd,cmd)))

			p.close()

			for res in result:
				res.get(timeout=35)

		ssh����(ȡ�ļ�״̬�������ʼ�)

			#!/usr/bin/python
			#encoding:utf8
			#config file: ip.list

			import paramiko
			import multiprocessing
			import smtplib
			import sys,os,time,datetime,socket,re
			from email.mime.text import MIMEText

			# �����ļ�(IP�б�)
			Conf = 'ip.list'
			user_name = 'peterli'
			user_pwd = 'passwd'
			port = 22
			PATH = '/home/peterli/'

			# ���÷��������ơ��û����������Լ��ʼ���׺ 
			mail_host = "smtp.163.com"
			mail_user = "xuesong"
			mail_pass = "mailpasswd"
			mail_postfix = "163.com"
			mailto_list = ["272121935@qq.com","quanzhou722@163.com"]
			title = 'file check'

			DATE1=(datetime.datetime.now() + datetime.timedelta(days=-1) ).strftime('%Y%m%d')
			file_path = '%s%s' %(PATH,DATE1)

			def Ssh_Cmd(file_path,host_ip,user_name,user_pwd,port=22):

				s = paramiko.SSHClient()
				s.load_system_host_keys()
				s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				
				try:
					s.connect(hostname=host_ip,port=port,username=user_name,password=user_pwd)
					stdin,stdout,stderr = s.exec_command('stat %s' %file_path)
					stat_result = '%s%s' %(stdout.read(),stderr.read())
					if stat_result.find('No such file or directory') == -1:
						file_status = 'OK\t'
						stdin,stdout,stderr = s.exec_command('du -sh %s' %file_path)
						cmd1_result = '%s_%s' %(stat_result.split()[32],stat_result.split()[33].split('.')[0])
						cmd2_result = ('%s%s' %(stdout.read(),stderr.read())).split()[0] 
					else:
						file_status = 'δ����\t'
						cmd1_result = 'null'
						cmd2_result = 'null'
					q.put(['Login successful'])
					s.close()
				except socket.error:
					file_status = '������˿ڴ���'
					cmd1_result = '-'
					cmd2_result = '-'
				except paramiko.AuthenticationException:
					file_status = '�û����������'
					cmd1_result = '-'
					cmd2_result = '-'
				except paramiko.BadHostKeyException:
					file_status = 'Bad host key'
					cmd1_result = '-'
					cmd2_result = '-'
				except:
					file_status = 'ssh�쳣'
					cmd1_result = '-'
					cmd2_result = '-'
				r.put('%s\t-\t%s\t%s\t%s\t%s\n' %(time.strftime('%Y-%m-%d_%H:%M'),host_ip,file_status,cmd2_result,cmd1_result))

			def Concurrent(Conf,file_path,user_name,user_pwd,port):
				# ִ���ܼ�
				total = 0
				# ��ȡ�����ļ�
				f=open(Conf)
				list = f.readlines()
				f.close()
				# ����ִ��
				process_list = []
				log_file = file('file_check.log', 'w')
				log_file.write('���ʱ��\t\tҵ��\tIP\t\t�ļ�״̬\t��С\t����ʱ��\n') 
				for host_info in list:
					# �ж������ļ���ע��������
					if host_info.startswith('#'):
						continue
					# ȡ����,�����������δȡ��������ִ��
					try:
						host_ip=host_info.split()[0].strip()
						#user_name=host_info.split()[1]
						#user_pwd=host_info.split()[2]
					except:
						log_file.write('Profile error: %s\n' %(host_info))
						continue
					#try:
					#	port=int(host_info.split()[3])
					#except:
					#	port=22
					total +=1
					p = multiprocessing.Process(target=Ssh_Cmd,args=(file_path,host_ip,user_name,user_pwd,port))
					p.start()
					process_list.append(p)
				for j in process_list:
					j.join()
				for j in process_list:
					log_file.write(r.get())

				successful = q.qsize()
				log_file.write('ִ����ϡ� ��ִ��:%s ��¼�ɹ�:%s ��¼ʧ��:%s\n' %(total,successful,total - successful))
				log_file.flush()
				log_file.close()

			def send_mail(to_list, sub):
				me = mail_user + "<"+mail_user+"@"+mail_postfix+">"
				fp = open('file_check.log')
				msg = MIMEText(fp.read(),_charset="utf-8")
				fp.close()
				msg['Subject'] = sub
				msg['From'] = me
				msg['To'] = ";".join(to_list)
				try:
					send_smtp = smtplib.SMTP()
					send_smtp.connect(mail_host)
					send_smtp.login(mail_user, mail_pass)
					send_smtp.sendmail(me, to_list, msg.as_string())
					send_smtp.close()
					return True
				except Exception, e:
					print str(e)[1]
					return False

			if __name__ == '__main__':
				q = multiprocessing.Queue()
				r = multiprocessing.Queue()
				Concurrent(Conf,file_path,user_name,user_pwd,port)
				if send_mail(mailto_list,title):
					print "���ͳɹ�"
				else:
					print "����ʧ��"

		LazyManage������������(�жϷ�root������root����)

			#!/usr/bin/python
			#encoding:utf8
			# LzayManage.py
			# config file: serverlist.conf

			import paramiko
			import multiprocessing
			import sys,os,time,socket,re

			def Ssh_Cmd(host_ip,Cmd,user_name,user_pwd,port=22):
				s = paramiko.SSHClient()
				s.load_system_host_keys()
				s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				s.connect(hostname=host_ip,port=port,username=user_name,password=user_pwd)
				stdin,stdout,stderr = s.exec_command(Cmd)
				Result = '%s%s' %(stdout.read(),stderr.read())
				q.put('successful')
				s.close()
				return Result.strip()

			def Ssh_Su_Cmd(host_ip,Cmd,user_name,user_pwd,root_name,root_pwd,port=22):
				s = paramiko.SSHClient()
				s.load_system_host_keys()
				s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				s.connect(hostname=host_ip,port=port,username=user_name,password=user_pwd)
				ssh = s.invoke_shell()
				time.sleep(0.1)
				ssh.send('su - %s\n' %(root_name))
				buff = ''
				while not buff.endswith('Password: '):
					resp = ssh.recv(9999)
					buff +=resp
				ssh.send('%s\n' %(root_pwd))
				buff = ''
				while True:
					resp = ssh.recv(9999)
					buff +=resp
					if ': incorrect password' in buff:
						su_correct='passwd_error'
						break
					elif buff.endswith('# '):
						su_correct='passwd_correct'
						break
				if su_correct == 'passwd_correct':
					ssh.send('%s\n' %(Cmd))
					buff = ''
					while True:
						resp = ssh.recv(9999)
						if resp.endswith('# '):
							buff +=re.sub('\[.*@.*\]# $','',resp)
							break
						buff +=resp
					Result = buff.lstrip('%s' %(Cmd))
					q.put('successful')
				elif su_correct == 'passwd_error':
					Result = "\033[31mroot�������\033[m"
				s.close()
				return Result.strip()

			def Send_File(host_ip,PathList,user_name,user_pwd,Remote='/tmp',port=22):
				s=paramiko.Transport((host_ip,port))
				s.connect(username=user_name,password=user_pwd)
				sftp=paramiko.SFTPClient.from_transport(s) 
				for InputPath in PathList:
					LocalPath = re.sub('^\./','',InputPath.rstrip('/'))
					RemotePath = '%s/%s' %( Remote , os.path.basename( LocalPath ))
					try:
						sftp.rmdir(RemotePath)
					except:
						pass
					try:
						sftp.remove(RemotePath)
					except:
						pass
					if os.path.isdir(LocalPath):
						sftp.mkdir(RemotePath)
						for path,dirs,files in os.walk(LocalPath):
							for dir in dirs:
								dir_path = os.path.join(path,dir)
								sftp.mkdir('%s/%s' %(RemotePath,re.sub('^%s/' %LocalPath,'',dir_path)))
							for file in files:
								file_path = os.path.join(path,file)
								sftp.put( file_path,'%s/%s' %(RemotePath,re.sub('^%s/' %LocalPath,'',file_path)))
					else:
						sftp.put(LocalPath,RemotePath)
				q.put('successful')
				sftp.close()
				s.close()
				Result = '%s  \033[32m�������\033[m' % PathList
				return Result

			def Ssh(host_ip,Operation,user_name,user_pwd,root_name,root_pwd,Cmd=None,PathList=None,port=22):
				msg = "\033[32m-----------Result:%s----------\033[m" % host_ip
				try:
					if Operation == 'Ssh_Cmd':
						Result = Ssh_Cmd(host_ip=host_ip,Cmd=Cmd,user_name=user_name,user_pwd=user_pwd,port=port)
					elif Operation == 'Ssh_Su_Cmd':
						Result = Ssh_Su_Cmd(host_ip=host_ip,Cmd=Cmd,user_name=user_name,user_pwd=user_pwd,root_name=root_name,root_pwd=root_pwd,port=port)
					elif Operation == 'Ssh_Script':
						Send_File(host_ip=host_ip,PathList=PathList,user_name=user_name,user_pwd=user_pwd,port=port)
						Script_Head = open(PathList[0]).readline().strip()
						LocalPath = re.sub('^\./','',PathList[0].rstrip('/'))
						Cmd = '%s /tmp/%s' %( re.sub('^#!','',Script_Head), os.path.basename( LocalPath ))
						Result = Ssh_Cmd(host_ip=host_ip,Cmd=Cmd,user_name=user_name,user_pwd=user_pwd,port=port)
					elif Operation == 'Ssh_Su_Script':
						Send_File(host_ip=host_ip,PathList=PathList,user_name=user_name,user_pwd=user_pwd,port=port)
						Script_Head = open(PathList[0]).readline().strip()
						LocalPath = re.sub('^\./','',PathList[0].rstrip('/'))
						Cmd = '%s /tmp/%s' %( re.sub('^#!','',Script_Head), os.path.basename( LocalPath ))
						Result = Ssh_Su_Cmd(host_ip=host_ip,Cmd=Cmd,user_name=user_name,user_pwd=user_pwd,root_name=root_name,root_pwd=root_pwd,port=port)
					elif Operation == 'Send_File':
						Result = Send_File(host_ip=host_ip,PathList=PathList,user_name=user_name,user_pwd=user_pwd,port=port)
					else:
						Result = '����������'
					
				except socket.error:
					Result = '\033[31m������˿ڴ���\033[m'
				except paramiko.AuthenticationException:
					Result = '\033[31m�û������������\033[m'
				except paramiko.BadHostKeyException:
					Result = '\033[31mBad host key\033[m['
				except IOError:
					Result = '\033[31mԶ�������Ѵ��ڷǿ�Ŀ¼��û��дȨ��\033[m'
				except:
					Result = '\033[31mδ֪����\033[m'
				r.put('%s\n%s\n' %(msg,Result))

			def Concurrent(Conf,Operation,user_name,user_pwd,root_name,root_pwd,Cmd=None,PathList=None,port=22):
				# ��ȡ�����ļ�
				f=open(Conf)
				list = f.readlines()
				f.close()
				# ִ���ܼ�
				total = 0
				# ����ִ��
				for host_info in list:
					# �ж������ļ���ע��������
					if host_info.startswith('#'):
						continue
					# ȡ����,�����������δȡ��������ִ��
					try:
						host_ip=host_info.split()[0]
						#user_name=host_info.split()[1]
						#user_pwd=host_info.split()[2]
					except:
						print('Profile error: %s' %(host_info) )
						continue
					try:
						port=int(host_info.split()[3])
					except:
						port=22
					total +=1
					p = multiprocessing.Process(target=Ssh,args=(host_ip,Operation,user_name,user_pwd,root_name,root_pwd,Cmd,PathList,port))
					p.start()
				# ��ӡִ�н��
				for j in range(total):
					print(r.get() )
				if Operation == 'Ssh_Script' or Operation == 'Ssh_Su_Script':
					successful = q.qsize() / 2
				else:
					successful = q.qsize()
				print('\033[32mִ�����[��ִ��:%s �ɹ�:%s ʧ��:%s]\033[m' %(total,successful,total - successful) )
				q.close()
				r.close()

			def Help():
				print('''	1.ִ������
				2.ִ�нű�      \033[32m[λ��1�ű�(������ű�ͷ),��ɴ�ִ�нű�����Ҫ�İ�\�ļ�\�ļ���·��,�ո�ָ�]\033[m
				3.�����ļ�      \033[32m[���͵İ�\�ļ�\�ļ���·��,�ո�ָ�]\033[m
				�˳�: 0\exit\quit
				����: help\h\?
				ע��: �����ļ�Ĭ��Ϊ/tmp��,���Ѵ���ͬ���ļ��ᱻǿ�Ƹ���,�ǿ�Ŀ¼���жϲ���.ִ�нű��Ƚ����ؽű���������Զ��������,���͹���ͬ�����ļ�
				''')

			if __name__=='__main__':
				# ����root�˺���Ϣ
				root_name = 'root'
				root_pwd = 'peterli'
				user_name='peterli'
				user_pwd='<++(3Ie'
				# �����ļ�
				Conf='serverlist.conf'
				if not os.path.isfile(Conf):
					print('\033[33m�����ļ� %s ������\033[m' %(Conf) )
					sys.exit()
				Help()
				while True:
					i = raw_input("\033[35m[��ѡ�����]: \033[m").strip()
					q = multiprocessing.Queue()
					r = multiprocessing.Queue()
					if i == '1':
						if user_name == root_name:
							Operation = 'Ssh_Cmd'
						else:
							Operation = 'Ssh_Su_Cmd'
						Cmd = raw_input('CMD: ').strip()
						if len(Cmd) == 0:
							print('\033[33m����Ϊ��\033[m')
							continue
						Concurrent(Conf=Conf,Operation=Operation,user_name=user_name,user_pwd=user_pwd,root_name=root_name,root_pwd=root_pwd,Cmd=Cmd)
					elif i == '2':
						if user_name == root_name:
							Operation = 'Ssh_Script'
						else:
							Operation = 'Ssh_Su_Script'
						PathList = raw_input('\033[36m���ؽű�·��: \033[m').strip().split()
						if len(PathList) == 0:
							print('\033[33m·��Ϊ��\033[m')
							continue
						if not os.path.isfile(PathList[0]):
							print('\033[33m����·�� %s �����ڻ����ļ�\033[m' %(PathList[0]) )
							continue
						for LocalPath in PathList[1:]:
							if not os.path.exists(LocalPath):
								print('\033[33m����·�� %s ������\033[m' %(LocalPath) )
								break
						else:
							Concurrent(Conf=Conf,Operation=Operation,user_name=user_name,user_pwd=user_pwd,root_name=root_name,root_pwd=root_pwd,PathList=PathList)
					elif i == '3':
						Operation = 'Send_File'
						PathList = raw_input('\033[36m����·��: \033[m').strip().split()
						if len(PathList) == 0:
							print('\033[33m·��Ϊ��\033[m')
							continue
						for LocalPath in PathList:
							if not os.path.exists(LocalPath):
								print('\033[33m����·�� %s ������\033[m' %(LocalPath) )
								break
						else:
							Concurrent(Conf=Conf,Operation=Operation,user_name=user_name,user_pwd=user_pwd,root_name=root_name,root_pwd=root_pwd,PathList=PathList)
					elif i == '0' or i == 'exit' or i == 'quit':
						print("\033[34m�˳�LazyManage�ű�\033[m")
						sys.exit()
					elif i == 'help' or i == 'h' or i == '?':
						Help()

	urllib2 [������Դ����]

		import urllib2
		response = urllib2.urlopen('http://baidu.com')
		print response.geturl()       # url
		headers = response.info()
		print headers                 # webҳ��ͷ����Ϣ
		print headers['date']         # ͷ����Ϣ�е�ʱ��
		date = response.read()        # ����ҳ��������Ϣ[�ַ���]
		# date = response.readlines() # ����ҳ��������Ϣ[�б�]
		
		for i in urllib2.urlopen('http://qq.com'):    # ��ֱ�ӵ���
			print i,

		�����ļ�

			#!/usr/bin/env python
			#encoding:utf8
			import urllib2

			url = 'http://www.01happy.com/wp-content/uploads/2012/09/bg.png'
			file("./pic/%04d.png" % i, "wb").write(urllib2.urlopen(url).read())
			
		ģ�����������webҳ�� python2
		
			#!/usr/bin/env python

			import urllib2,random

			url="http://pythontab.com"

			num = random.randint(1,3)
			if num == 1:
				browser='AppleWebKit/537.11 (KHTML, like Gecko)'
			elif num == 2:
				browser='Chrome/23.0.1271.64 Safari/537.11'
			elif num == 3:
				browser='Mozilla/5.0 (Windows NT 6.1)'

			req_header = {'User-Agent':browser,
			'Accept':'text/html;q=0.9,*/*;q=0.8',
			'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
			'Connection':'close',
			'Referer':None
			}

			req_timeout = 5
			req = urllib2.Request(url,None,req_header)
			resp = urllib2.urlopen(req,None,req_timeout)
			html = resp.read()
			print(html)
			
		ģ�����������webҳ�� python3
			#! /usr/bin/env python
			# -*- coding=utf-8 -*- 
			import urllib.request

			url = "http://www.baidu.com"
			# AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11
			headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1)',
			'Accept':'text/html;q=0.9,*/*;q=0.8',
			'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
			'Connection':'close',
			'Referer':None #ע�������Ȼ����ץȡ�Ļ��������������ץȡ��վ��host
			}

			opener = urllib.request.build_opener()
			opener.addheaders = [headers]
			data = opener.open(url).read()

			print(data)
				
	requests [�ύ��ҳ����]

		#Requests��һ��Python��HTTP�ͻ��˿�
		#��װ: sudo pip install requests
		import requests
		r = requests.get('http://baidu.com')
		#r = requests.get('https://baidu.com', auth=('user', 'pass'))   # https���¼��auth
		r.status_code                  # ״̬��
		r.headers                      # ��ҳͷ��Ϣ
		r.headers['content-type']      # ��ҳͷ��Ϣ
		r.headers['content-length']    # ��ҳͷ��Ϣ
		r.text                         # ��ҳԴ��
		r.content                      # ��ҳԴ��

		import requests
		Ip='211.211.54.54'
		QueryAdd='http://www.anti-spam.org.cn/Rbl/Query/Result'
		results = requests.post(url=QueryAdd, data={'IP':Ip})        # post�����ύ��
		
		url = r'http://dict.youdao.com/search?le=eng&q={0}'.format(word.strip())
		results = requests.get(url)                                  # get�����ύ��

		if r.ok:    # �ж������Ƿ�����
			# results ��ʹ�� BeautifulSoup4 ���������ж����
			print results.content   # ��ȡ����ԭʼ����
			print results.text      # ��ԭʼ����תunicode����

	BeautifulSoup [html\xml������]

		# BeautifulSoup���Ĺٷ��ĵ�
		# http://www.crummy.com/software/BeautifulSoup/bs3/documentation.zh.html
		# http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
		
		����ģ��
			from BeautifulSoup import BeautifulSoup          # For processing HTML  �汾3.0 ��ֹͣ����
			from BeautifulSoup import BeautifulStoneSoup     # For processing XML
			import BeautifulSoup                             # To get everything
			from bs4 import BeautifulSoup                    # �汾4.0 bs4 ��װ: pip install BeautifulSoup4

		from bs4 import BeautifulSoup
		soup = BeautifulSoup(html_doc)    # ����html�ı� ������ requests �ύ���ص�ҳ�� results.content
		print(soup.prettify())            # ���������Ľṹ
		print(soup.title)                 # ָ����ǩ����
		print(soup.title.name)            # ��ǩ��
		print(soup.title.string)          # ��ǩ����
		print(soup.title.parent.name)     # �ϲ��ǩ��
		print(soup.p)                     # <p class="title"><b>The Dormouse's story</b></p>
		print(soup.p['class'])            # u'title'  class����ֵ
		print(soup.a)                     # �ҵ���һ��a��ǩ�ı�ǩ��
		print(soup.find_all('a',limit=2)) # �ҵ�a��ǩ����,���Ϊlimit��
		print(soup.find(id="link3"))      # ��ǩ��idΪlink3�ı�ǩ��
		print(soup.get_text())            # ���ĵ��л�ȡ������������
		soup.find_all("a", text="Elsie")  # ���ĵ��������ؼ���
		soup.find(text=re.compile("sisters"))  # ���ĵ������������ؼ���
		soup.find_all("a", class_="sister")    # ��CSS����
		soup.find_all(id='link2',"table",attrs={"class": "status"},href=re.compile("elsie"))   # ��������
		for link in soup.find_all('a'):   # ѭ������a��ǩ�ı�ǩ��
			print(link.get('href'))       # ȡ����ǰa��ǩ�е�����

	cookielib [����cookie��¼ҳ��]

		ck = cookielib.CookieJar()   # ͨ�� ����Ϳ���ʵ���������ȥ��COOKIE�뷢�ͻ�����COOKIEֵ�ˡ�
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(ck))   # ��ȡ��COOKIE
		urllib2.install_opener(opener)   # �˾�����urllib2��ȫ��opener
		content = urllib2.urlopen(url).read()  
		
		��¼cactiȡͼƬ
			#encoding:utf8
			import urllib2
			import urllib
			import cookielib
			def renrenBrower(url,user,password):
				#����form��ǩ�е�action�ύ��ַ
				login_page = "http://10.10.76.79:81/cacti/index.php"
				try:
					#���һ��cookieJarʵ��
					cj = cookielib.CookieJar()
					#cookieJar��Ϊ���������һ��opener��ʵ��
					opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
					#αװ��һ���������������������Щweb�������ܾ�����
					opener.addheaders = [('User-agent','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)')]
					#����Post����,���е�½�û�������,���б��ڵ�input��nameֵ
					data = urllib.urlencode({"action":"login","login_username":user,"login_password":password})
					#��post�ķ������ʵ�½ҳ�棬����֮��cookieJar���Զ�����cookie
					opener.open(login_page,data)
					#�Դ�cookie�ķ�ʽ����ҳ��
					op=opener.open(url)
					#��ȡҳ��Դ��
					data=op.read()
					#��ͼƬд������
					#file("1d.png" , "wb").write(data)
					return data
				except Exception,e:
					print str(e)
			print renrenBrower("http://10.10.76.79:81/cacti/graph_image.php?local_graph_id=1630&rra_id=0&view_type=tree&graph_start=1397525517&graph_end=1397611917","admin","admin")

		����2
			import urllib, urllib2, cookielib  
			import os, time  
			  
			headers = []  
			  
			def login():  
				cj = cookielib.CookieJar()  
				opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))  
				login_url = r'http://zhixing.bjtu.edu.cn/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'  
				login_data = urllib.urlencode({'cookietime': '2592000', 'handlekey': 'ls', 'password': 'xxx',  
						'quickforward': 'yes', 'username': 'GuoYuan'})  
				opener.addheaders = [('Host', 'zhixing.bjtu.edu.cn'),  
								   ('User-Agent', 'Mozilla/5.0 (Ubuntu; X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0'),  
								   ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),  
								   ('Accept-Language', 'en-us,en;q=0.5'),  
								   ('Accept-Encoding', 'gzip, deflate'),  
								   ('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'),  
								   ('Connection', 'keep-alive'),  
								   ('Referer', 'http://zhixing.bjtu.edu.cn/forum.php'),]  
				opener.open(login_url, login_data)  
				return opener  
			  
			if __name__ == '__main__':  
				opener = login()  
			  
				url = r'http://zhixing.bjtu.edu.cn/forum.php?mod=topicadmin&action=moderate&optgroup=2&modsubmit=yes&infloat=yes&inajax=1'      
				data = {'fid': '601', 'formhash': '0cdd1596', 'frommodcp': '', 'handlekey': 'mods',  
						 'listextra': 'page%3D62', 'moderate[]': '496146', 'operations[]': 'type', 'reason': '...',  
						 'redirect': r'http://zhixing.bjtu.edu.cn/thread-496146-1-1.html', 'typeid': '779'}  
				data2 = [(k, v) for k,v in data.iteritems()]  
				  
				cnt = 0  
				for tid in range(493022, 496146 + 1):  
					cnt += 1  
					if cnt % 20 == 0: print  
					print tid,  
					  
					data2.append(('moderate[]', str(tid)))  
					if cnt % 40 == 0 or cnt == 496146:  
						request = urllib2.Request(url=url, data=urllib.urlencode(data2))  
						print opener.open(request).read()  
						data2 = [(k, v) for k,v in data.iteritems()]  

	httplib [httpЭ��Ŀͻ���]
		import httplib
		conn3 = httplib.HTTPConnection('www.baidu.com',80,True,10) 

	��ȡ��ҳָ������
		
		#��ȡ������ҳ,�����ȡƥ����Ϣ
		#!/usr/bin/env python
		#encoding=utf-8
		import  re, urllib,datetime
		def getPageCode(url, fromCharset, toCharset):
			fr = urllib.urlopen(url)
			pageCode = fr.read()
			fr.close()
			return pageCode
		def getImgUrl(pageCode):
			pattern = re.compile(r'(\d*\-\d*\-\d* \d*:\d*:\d*)')
			return  re.findall(pattern, pageCode)

		if __name__ == '__main__':
			f = file('url.conf')
			c = f.readlines()
			f.close()
			for url in c:
				pageCode = getPageCode(url.rstrip(), 'gb2312', 'utf8')
				imgUrl = getImgUrl(pageCode)
				print imgUrl

	��ȡ��ҳͼƬ��С
		
		# ����httpͷ,�õ�content-type��ֵ
		#!/usr/bin/env python
		#encoding=utf-8
		import urllib2
		url = 'http://www.01happy.com/wp-content/uploads/2012/09/bg.png'
		reqst = urllib2.Request(url)
		opener = urllib2.build_opener()
		con = opener.open(reqst)
		Type = con.headers.dict['content-type'][:5]
		Length = int(con.headers.dict['content-length'])
		if Length > 0:
			print(Length)
			print(Type)

	�鿴��ҳͼƬ�ߴ�����
		
		#��ͼƬ�����ڴ�
		#!/usr/bin/env python
		#encoding=utf-8
		import cStringIO, urllib2, Image
		url = 'http://www.01happy.com/wp-content/uploads/2012/09/bg.png'
		file = urllib2.urlopen(url)
		tmpIm = cStringIO.StringIO(file.read())
		im = Image.open(tmpIm)
		print im.format, im.size, im.mode

	����
		
		#!/usr/bin/env python
		#encoding:utf-8
		#sudo pip install BeautifulSoup

		import requests
		from BeautifulSoup import BeautifulSoup
		import re

		baseurl = 'http://blog.sina.com.cn/s/articlelist_1191258123_0_1.html'

		r = requests.get(baseurl)

		for url in re.findall('<a.*?</a>', r.content, re.S):
			if url.startswith('<a title='):
				with open(r'd:/final.txt', 'ab') as f:
					f.write(url + '\n')

		linkfile = open(r'd:/final.txt', 'rb')
		soup = BeautifulSoup(linkfile)
		for link in soup.findAll('a'):
			#print link.get('title') + ':    ' + link.get('href')
			ss = requests.get(link.get('href'))
			for content in re.findall('<div id="sina_keyword_ad_area2" class="articalContent  ">.*?</div>', ss.content, re.S):
				with open(r'd:/myftp/%s.txt'%link.get('title').strip('<>'), 'wb') as f:
					f.write(content)
					print '%s   has been copied.' % link.get('title')

	�������ʼ��ύ����

		#���ź����������ʼ����˸İ�������֤��
		
		#!/usr/bin/env python
		#encoding:utf-8
		import requests
		import re
		
		IpList=['113.212.91.25','113.212.91.23']
		QueryAdd='http://www.anti-spam.org.cn/Rbl/Query/Result'
		ComplaintAdd='http://www.anti-spam.org.cn/Rbl/Getout/Submit'
		data = {
		'CONTENT':'''������һ�������XXX��xxxxxxx�����뽫���ǵķ��ͷ�����IP�Ƴ���������лл��
		�����ʩ��
		1.XXXX��
		2.XXXX��''',
		'CORP':'abc.com',
		'WWW':'www.abc.cm',
		'NAME':'def',
		'MAIL':'def@163.com.cn',
		'TEL':'010-50000000',
		'LEVEL':'0',
		}

		for Ip in IpList:
			query = requests.post(url=QueryAdd, data={'IP':Ip})                   # ��������ѯ
			if query.ok:
				if re.findall(u'\u7533\u8bc9\u8131\u79bb', query.text, re.S):     # ���ҹؼ��� �������� �ȱ����ں�������
					data['IP']=Ip
					complaint = requests.post(url=ComplaintAdd, data=data)        # �ύ����
					if complaint.ok:
						if re.findall(u'\u60a8\u7684\u9ed1\u540d\u5355\u8131\u79bb\u7533\u8bf7\u5df2\u63d0\u4ea4', complaint.text, re.S):
							status='�����ύ'
						elif re.findall(u'\u8131\u79bb\u7533\u8bf7\u5df2\u88ab\u4ed6\u4eba\u63d0\u4ea4', complaint.text, re.S):
							status='�ظ��ύ'
						elif re.findall(u'\u7533\u8bf7\u7531\u4e8e\u8fd1\u671f\u5185\u6709\u88ab\u62d2\u7edd\u7684\u8bb0\u5f55', complaint.text, re.S):
							status='���ھܾ�'
						else:
							status='�쳣'
				else:
					status='����'
				print '%s  %s' %(Ip,status)

	�е��ʵ�

		#!/usr/bin/env python
		import requests
		from bs4 import BeautifulSoup
		# bs4��װ: pip install BeautifulSoup4

		def youdao(word):
			url = r'http://dict.youdao.com/search?le=eng&q={0}'.format(word.strip())
			r = requests.get(url)
			if r.ok:
				soup = BeautifulSoup(r.content)
				div = soup.find_all('div', class_='trans-container')[:1]    # find_all��bs4�ķ���
				ul = BeautifulSoup(str(div[0]))
				li = ul.find_all('li')
				for mean in li:
					print mean.text

		def query():
			print('Created by @littlepy, QQ:185635687')
			while True:
				word = raw_input('>>>')
				youdao(word)

		if __name__ == '__main__':
			query()

8 ����

	#�̰߳�ȫ/��������,��/�������,ͬ��/�첽,����/������,epoll������IO,�ź���/�¼�,�̳߳�,��������ģ��,α����,΢�߳�,Э��
	#Stackless Python ��Python������Ե�һ����ǿ�汾����ʹ����Ա�ӻ����̵߳ı�̷�ʽ�л�úô��������⴫ͳ�߳��������������븴�Ӷ����⡣StacklessΪ Python������΢�߳���չ����һ�ֵͿ������������ı�������

	threading���߳�

		thread
			start_new_thread(function,args kwargs=None)    # ����һ���µ��߳�
			allocate_lock()                                # ����һ��LockType���͵�������
			exit()                                         # ���߳��˳�
			acquire(wait=None)                             # ���Ի�ȡ������
			locked()                                       # �����ȡ�������󷵻�True
			release()                                      # �ͷ���

		thread����

			#!/usr/bin/env python
			#thread_test.py
			#��֧���ػ�����
			import thread
			from time import sleep,ctime

			loops = [4,2]

			def loop(nloop,nsec,lock):
				print 'start loop %s at:%s' % (nloop,ctime())
				sleep(nsec)
				print 'loop %s done at: %s' % (nloop, ctime())
				lock.release()              # �����ѻ�õ���,�����������ͷ���Ӧ����֪ͨ���߳�

			def main():
				print 'starting at:',ctime()
				locks = []
				nloops = range(len(loops))
				
				for i in nloops:
					lock = thread.allocate_lock()     # ����һ����
					lock.acquire()                    # ���ø�������acquire()���������
					locks.append(lock)                # �����ŵ����б�locks��
				for i in nloops:
					thread.start_new_thread(loop,(i,loops[i],locks[i]))   # �����߳�
				for i in nloops:
					while locks[i].locked():pass      # �ȴ�ȫ�������ż�������
				print 'all DONE at:',ctime()

			if __name__ == '__main__':
				main()

		threading
			Thread                   # ��ʾһ���̵߳�ִ�еĶ���
				start()              # ��ʼ�̵߳�ִ��
				run()                # �����̵߳Ĺ��ܵĺ���(һ��ᱻ������д)
				join(timeout=None)   # �������̵߳ȴ��߳̽���,�������,ֱ���߳̽���;�������timeout,�����ȴ�timeout��.
				getName()            # �����̵߳�����
				setName(name)        # �����̵߳�����
				isAlive()            # ������־,��ʾ����߳��Ƿ���������
				isDaemon()           # �����̵߳�daemon��־
				setDaemon(daemonic)  # ��̨�߳�,���̵߳�daemon��־����Ϊdaemonic(һ��Ҫ�ڵ���start()����ǰ����)
				# Ĭ�����߳����˳�ʱ��ȴ��������̵߳Ľ��������ϣ�����̲߳��ȴ����̣߳��������˳�ʱ�Զ��������е����̣߳�����Ҫ�������߳�Ϊ��̨�߳�(daemon)
			Lock              # ��ԭ�����
			Rlock             # ������������.ʹ���߳̿����ڴ˻���ѻ���˵���(�ݹ�����)
			Condition         # ����������������һ���߳�ͣ����,�ȴ������߳�������ĳ������.��״̬�ı��ֵ�ĸı�
			Event             # ͨ�õ���������.����߳̿��Եȴ�ĳ���¼��ķ���,���¼�������,���е��̶߳��ᱻ����
			Semaphore         # Ϊ�ȴ������߳��ṩһ�����ƵȺ��ҵĽṹ
			BoundedSemaphore  # ��Semaphore����,ֻ�ǲ���������ʼֵ
			Time              # ��Thread����,ֻ����Ҫ�ȴ�һ��ʱ���ſ�ʼ����
			activeCount()     # ��ǰ����̶߳��������
			currentThread()   # ���ص�ǰ�̶߳���
			enumerate()       # ���ص�ǰ��̵߳��б�
			settrace(func)    # Ϊ�����߳�����һ�����ٺ���
			setprofile(func)  # Ϊ�����߳�����һ��profile����

		threading����1
			
			#!/usr/bin/env python
			#encoding:utf8
			import threading
			from Queue import Queue
			from time import sleep,ctime

			class ThreadFunc(object):
					def __init__(self,func,args,name=''):
							self.name=name
							self.func=func                    # loop
							self.args=args                    # (i,iplist[i],queue)
					def __call__(self):
							apply(self.func,self.args)        # ����apply() ִ��loop����������Ԫ�����
			def loop(nloop,ip,queue):
					print 'start',nloop,'at:',ctime()
					queue.put(ip)
					sleep(2)
					print 'loop',nloop,'done at:',ctime()
			if __name__ == '__main__':
					threads = []
					queue = Queue()
					iplist = ['192.168.1.2','192.168.1.3','192.168.1.4','192.168.1.5','192.168.1.6','192.168.1.7','192.168.1.8']
					nloops = range(len(iplist))

					for i in nloops:
							t = threading.Thread(target=ThreadFunc(loop,(i,iplist[i],queue),loop.__name__))
							threads.append(t)
					for i in nloops:
							threads[i].start()
					for i in nloops:
							threads[i].join()
					for i in nloops:
							print queue.get()

		threading����2

			#!/usr/bin/env python
			#encoding:utf8
			from Queue import Queue
			import random,time,threading
			
			class Producer(threading.Thread):
				def __init__(self, t_name, queue):
					threading.Thread.__init__(self, name=t_name)
					self.data=queue
				def run(self):
					for i in range(5):
						print "%s: %s is producing %d to the queue!\n" %(time.ctime(), self.getName(), i)
						self.data.put(i)
						self.data.put(i*i)
						time.sleep(2)
					print "%s: %s finished!" %(time.ctime(), self.getName())

			class Consumer(threading.Thread):
				def __init__(self, t_name, queue):
					threading.Thread.__init__(self, name=t_name)
					self.data=queue
				def run(self):
					for i in range(10):
						val = self.data.get()
						print "%s: %s is consuming. %d in the queue is consumed!\n" %(time.ctime(), self.getName(), val)
					print "%s: %s finished!" %(time.ctime(), self.getName())

			if __name__ == '__main__':
				queue = Queue()
				producer = Producer('Pro.', queue)
				consumer = Consumer('Con.', queue)
				producer.start()
				consumer.start()
				producer.join()
				consumer.join()

		��̨�߳�

			import threading
			import time,random

			class MyThread(threading.Thread):
				def run(self):
					wait_time=random.randrange(1,10)
					print "%s will wait %d seconds" % (self.name, wait_time)
					time.sleep(wait_time)
					print "%s finished!" % self.name

			if __name__=="__main__":
				for i in range(5):
					t = MyThread()
					t.setDaemon(True)    # ����Ϊ��̨�߳�,���߳����ʱ���ȴ����߳���ɾͽ���
					t.start()

		threading������󲢷�_��ѯ��־��IP��Ϣ

			#!/usr/bin/env python
			#coding:utf-8
			import urllib2
			import json
			import threading
			import time

			'''
			by:ĳ��ţ
			QQ:185635687
			����Ƕ��̲߳�������. ���Ҫ�ĳɶ���̣�ֻ���threading ���� mulitprocessing.Process �� �ԣ� ���ǻ������ֶ���.
			'''

			#��ȡip ������ִ���
			def ip_dic(file_obj, dic):
				for i in file_obj:
					if i:
						ip=i.split('-')[0].strip()
						if ip in dic.keys():
							dic[ip]=dic[ip] + 1
						else:
							dic[ip]=1
				return dic.iteritems()

			#Ŀ�꺯��
			def get_data(url, ipcounts):
				data=urllib2.urlopen(url).read()
				datadict=json.loads(data)
				fdata = u"ip:%s---%s,%s,%s,%s,%s" %(datadict["data"]["ip"],ipcounts,datadict["data"]["country"],datadict["data"]["region"],datadict["data"]["city"],datadict["data"]["isp"])
				print fdata

			#���߳�
			def threads(iters):
				thread_pool = []
				for k in iters:
					url = "http://ip.taobao.com/service/getIpInfo.php?ip="
					ipcounts = k[1]
					url = (url + k[0]).strip()
					t = threading.Thread(target=get_data, args=(url, ipcounts))
					thread_pool.append(t)
				return thread_pool

			#���ƶ��߳�
			def startt(t_list, max,second):
				l = len(t_list)
				n = max
				while l > 0:
					if l > max:
						nl = t_list[:max]
						t_list = t_list[max:]
						for t in nl:
							t.start()
						time.sleep(second)
						for t in nl:
							t.join()
						print '*'*15,  str(n)+ ' ip has been queried'+'*'*15
						n += max
						l = len(t_list)
						continue
					elif l <= max:
						nl = t_list
						for t in nl:
							t.start()
						for t in nl:
							t.join()
						print '>>> Totally ' + str(n+l ) + ' ip has been queried'
						l = 0

			if __name__ =="__main__":
				dic={}
				with open('access.log') as file_obj:
					it = ip_dic(file_obj, dic)
					t_list= threads(it)
					startt(t_list, 15, 1)

	Queueͨ�ö���

		q=Queue(size)       # ������Сsize��Queue����
		qsize()             # ���ض��еĴ�С(����ʱ��,���ܱ����������޸�,����ֵ)
		empty()             # �������Ϊ�շ���True������Fales
		full()              # ���������������True������Fales
		put(item,block0)    # ��item�ŵ�������,�������block(��Ϊ0),������һֱ�������������пռ�Ϊֹ
		get(block=0)        # �Ӷ�����ȡһ������,�������block(��Ϊ0),������һֱ�������������ж���Ϊֹ
		get_nowait          # Ĭ��get���������������

	multiprocessing [����̲���]

		����̲���

			#!/usr/bin/env python
			#encoding:utf8
			from multiprocessing import Process
			import time,os
			def f(name):
				time.sleep(1)
				print 'hello ',name
				print os.getppid()   # ȡ�ø�����ID
				print os.getpid()    # ȡ�ý���ID
			process_list = []

			for i in range(10):
				p = Process(target=f,args=(i,))
				p.start()
				process_list.append(p)
			for j in process_list:
				j.join()

		Queue���̼�ͨ��

			from multiprocessing import Process,Queue
			import time
			def f(name):
				time.sleep(1)
				q.put(['hello'+str(name)])
			process_list = []
			q = Queue()
			if __name__ == '__main__':
				for i in range(10):
					p = Process(target=f,args=(i,))
					p.start()
					process_list.append(p)
				for j in process_list:
					j.join()
				for i in range(10):
					print q.get()

		Pipe�ܵ�
		
			from multiprocessing import Process,Pipe
			import time
			import os

			def f(conn,name):
				time.sleep(1)
				conn.send(['hello'+str(name)])
				print os.getppid(),'-----------',os.getpid()
			process_list = []
			parent_conn,child_conn = Pipe()
			if __name__ == '__main__':
				for i in range(10):
					p = Process(target=f,args=(child_conn,i))
					p.start()
					process_list.append(p)
				for j in process_list:
					j.join()
				for p in range(10):
					print parent_conn.recv()

		���̼�ͬ��
			#������ʹĳһʱ��ֻ��һ������ print
			from multiprocessing import Process,Lock
			import time
			import os

			def f(name):
				lock.acquire()
				time.sleep(1)
				print 'hello--'+str(name)
				print os.getppid(),'-----------',os.getpid()
				lock.release()
			process_list = []
			lock = Lock()
			if __name__ == '__main__':
				for i in range(10):
					p = Process(target=f,args=(i,))
					p.start()
					process_list.append(p)
				for j in process_list:
					j.join()

		�����ڴ�

			# ͨ��ʹ��Value����Array�����ݴ洢��һ��������ڴ����
			# 'd'��'i'������num��arr�����������ͣ�d��ʾһ��˫���������ͣ�i��ʾһ�������ŵ����͡�
			from multiprocessing import Process,Value,Array
			import time
			import os

			def f(n,a,name):
				time.sleep(1)
				n.value = name * name
				for i in range(len(a)):
					a[i] = -i
			process_list = []
			if __name__ == '__main__':
				num = Value('d',0.0)
				arr = Array('i',range(10))
				for i in range(10):
					p = Process(target=f,args=(num,arr,i))
					p.start()
					process_list.append(p)
				for j in process_list:
					j.join()
				print num.value
				print arr[:]

		manager

			# �ȹ����ڴ����,������
			# ֧��list,dict,Namespace,Lock,Semaphore,BoundedSemaphore,Condition,Event,Queue,��alue,Array
			from multiprocessing import Process,Manager
			import time
			import os

			def f(d,name):
				time.sleep(1)
				d[name] = name * name
				print d
			process_list = []
			if __name__ == '__main__':
				manager = Manager()
				d = manager.dict()
				for i in range(10):
					p = Process(target=f,args=(d,i))
					p.start()
					process_list.append(p)
				for j in process_list:
					j.join()
					print d

		��󲢷���

			import multiprocessing
			import time,os

			result = []
			def run(h):
				print 'threading:' ,h,os.getpid()
			p = multiprocessing.Pool(processes=20)

			for i in range(100):
				result.append(p.apply_async(run,(i,)))
			p.close()
			
			for res in result:
				res.get(timeout=5)

	twisted  [�������첽���������]

		# ����������������Ӧ�ó���ı�̡���Ȼ Twisted Matrix ���д�����ɢ��ϵ�ģ�黯��������ÿ�ܵ����ĸ���Ƿ������첽��������һ˼�롣����ϰ�����̼߳�����ֲ�������Ŀ�����Ա��˵������һ����ӱ�ı�̷�񣬵���ȴ���ڷ��ظ��ص�����´������ߵ�Ч�ʡ�
		pip install twisted

	greenlet [΢�߳�/Э�̿��]

		# ����ԭʼ��΢�̵߳ĸ���,û�е���,���߽���Э�̡���������Ҫ������Ĵ���ʱ�����á�������Լ�����΢�̵߳� ��������Ҳ����ʹ��"greenlet"ʵ�ָ߼��Ŀ�����������������´�������������ͬ��Python�Ĺ����������ǵĹ���������Ƕ�׵ĵ��ú���������Ƕ�׵ĺ���Ҳ���� yield һ��ֵ��
		pip install greenlet

	tornado  [��������Web���������] 

		# �߿������Ժ�epoll������IO,��Ӧ����,�ɴ�����ǧ��������,�ر���������ʵʱ��Web����
		pip install tornado

	Scrapy   [webץȡ���]
		Python������һ������,�߲�ε���Ļץȡ��webץȡ��ܣ�����ץȡwebվ�㲢��ҳ������ȡ�ṹ�������ݡ�Scrapy��;�㷺���������������ھ򡢼����Զ������ԡ�

9 �㷨 

	쳲�����
		#�����������Ϊ�б������ѭ��
		def fab(max): 
		n, a, b = 0, 0, 1 
		while n < max: 
			yield b         
			a, b = b, a + b 
			n = n + 1 
		for n in fab(5): 
			print n

	�˷��ھ�

		#!/usr/bin/python
		for i in range(1,10):
			for j in range(1,i+1):
				print j,'*',i,'=',j*i,
			else:
				print ''

	��С������

		# 1-70����С������
		def c(m,n):
				a1=m
				b1=n
				r=n%m
				while r!=0:
						n=m
						m=r
						r=n%m
				return (a1*b1)/m
		d=1
		for i in range(3,71,2):
				d = c(d,i)
		print d

	�����㷨

		��������
			def insertion_sort(sort_list):
				iter_len = len(sort_list)
				if iter_len < 2:
					return sort_list
				for i in range(1, iter_len):
					key = sort_list[i]
					j = i - 1
					while j>=0 and sort_list[j]>key:
						sort_list[j+1] = sort_list[j]
						j -= 1
					sort_list[j+1] = key
				return sort_list

		ѡ������
			def selection_sort(sort_list):
				iter_len = len(sort_list)
				if iter_len < 2:
					return sort_list
				for i in range(iter_len-1):
					smallest = sort_list[i]
					location = i
					for j in range(i, iter_len):
						if sort_list[j] < smallest:
							smallest = sort_list[j]
							location = j
					if i != location:
						sort_list[i], sort_list[location] = sort_list[location], sort_list[i]
				return sort_list	

		ð�������㷨
			def bubblesort(numbers):
				for j in range(len(numbers)-1,-1,-1):
					for i in range(j):
						if numbers[i]>numbers[i+1]:
							numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
						print(i,j)
						print(numbers)

10 ����

	PILͼ����

		import Image
		im = Image.open("j.jpg")            # ��ͼƬ
		print im.format, im.size, im.mode   # ��ӡͼ���ʽ�����ؿ�͸ߡ�ģʽ
		# JPEG (440, 330) RGB
		im.show()                           # ��ʾ���¼���ͼ��
		box = (100, 100, 200, 200)
		region = im.crop(box)               # ��ͼ������ȡ��ĳ�����δ�С��ͼ��

	ͼƬ�ȱ���С

		# -*- coding: cp936 -*-
		import Image  
		import glob, os  
		  
		#ͼƬ������  
		def timage():  
			for files in glob.glob('D:\\1\\*.JPG'):  
				filepath,filename = os.path.split(files)  
				filterame,exts = os.path.splitext(filename)  
				#���·��  
				opfile = r'D:\\22\\'  
				#�ж�opfile�Ƿ���ڣ��������򴴽�  
				if (os.path.isdir(opfile)==False):  
					os.mkdir(opfile)  
				im = Image.open(files)  
				w,h = im.size  
				#im_ss = im.resize((400,400))  
				#im_ss = im.convert('P')  
				im_ss = im.resize((int(w*0.12), int(h*0.12)))  
				im_ss.save(opfile+filterame+'.jpg')  
		  
		if __name__=='__main__':  
			timage()

	ȡϵͳ����ֵ��������

		cmd = os.popen("df -Ph|awk 'NR!=1{print $5}'").readlines();
		cmd = os.popen('df -h').read().split('\n')
		cmd = os.popen('lo 2>&1').read()
		
		#ȡ����ʹ�ÿռ�
		import commands
		df = commands.getoutput("df -hP")
		[ x.split()[4] for x in df.split("\n") ] 
		[ (x.split()[0],x.split()[4]) for x in df.split("\n") if x.split()[4].endswith("%") ] 

	��ӡ���

		map = [["a","b","c"],
			   ["d","e","f"],
			   ["g","h","i"]]
		def print_board():
			for i in range(0,3):
				for j in range(0,3):
					print "|",map[i][j],
					#if j != 2:
				print '|'

	����html�ļ����

		log_file = file('check.html', 'w')
		log_file.write("""
		<!DOCTYPE HTML>
		<html lang="utr-8">
		<head>
		<meta charset="UTF-8">
		<title></title>
		</head>
		<body>
		<table align='center' border='0' cellPadding='0'  style='font-size:24px;'><tr ><td>״̬ͳ��</td></tr></table>
		<style>.font{font-size:13px}</style>
		<table  align='center' border='1' borderColor=gray cellPadding=3 width=1350  class='font'>
		<tr style='background-color:#666666'>
		  <th width=65>IP</th>
		  <th width=65>״̬</th>
		</tr>
		""")
		for i in list:
			log_file.write('<tr><td>%s</td><td>%s</td></tr>\n' %(i.split()[0],i.split()[1]) )
		log_file.write("""
		</table>
		</body>
		</html>
		""")
		log_file.flush()
		log_file.close()

	������Ϸ

		#!/usr/bin/python
		# http://www.admin10000.com/document/2506.html
		def print_board():
			for i in range(0,3):
				for j in range(0,3):
					print map[2-i][j],
					if j != 2:
						print "|",
				print ""
		 
		def check_done():
			for i in range(0,3):
				if map[i][0] == map[i][1] == map[i][2] != " " \
				or map[0][i] == map[1][i] == map[2][i] != " ":
					print turn, "won!!!"
					return True
		 
			if map[0][0] == map[1][1] == map[2][2] != " " \
			or map[0][2] == map[1][1] == map[2][0] != " ":
				print turn, "won!!!"
				return True
		 
			if " " not in map[0] and " " not in map[1] and " " not in map[2]:
				print "Draw"
				return True
		 
			return False
		 
		turn = "X"
		map = [[" "," "," "],
			   [" "," "," "],
			   [" "," "," "]]
		done = False
		 
		while done != True:
			print_board()
		 
			print turn, "'s turn"
			print
		 
			moved = False
			while moved != True:
				print "Please select position by typing in a number between 1 and 9, see below for which number that is which position..."
				print "7|8|9"
				print "4|5|6"
				print "1|2|3"
				print
		 
				try:
					pos = input("Select: ")
					if pos <=9 and pos >=1:
						Y = pos/3
						X = pos%3
						if X != 0:
							X -=1
						else:
							 X = 2
							 Y -=1
		 
						if map[Y][X] == " ":
							map[Y][X] = turn
							moved = True
							done = check_done()
		 
							if done == False:
								if turn == "X":
									turn = "O"
								else:
									turn = "X"
		 
				except:
					print "You need to add a numeric value"

	���λ���

		��Ŀ
			192.168.1
			192.168.3
			192.168.2
			172.16.3
			192.16.1
			192.16.2
			192.16.3
			10.0.4

			��������
			192.16.1-192.16.3
			192.168.1-192.168.3
			172.16.3
			10.0.4

		��
			#!/usr/bin/python

			f = file('a.txt')
			c = f.readlines()
			dic={}

			for i in c:
				a=i.strip().split('.')
				if a[0]+'.'+a[1] in dic.keys():
					key=dic["%s.%s" %(a[0],a[1])]
				else:
					key=[]
				key.append(a[2])
				dic[a[0]+'.'+a[1]]=sorted(key)

			for x,y in dic.items():
				if y[0] == y[-1]:
					print '%s.%s' %(x,y[0])
				else:
					print '%s.%s-%s.%s' %(x,y[0],x,y[-1])

	ͳ����־IP
		# ��ӡ������IP����ͳ�ƶ���IP��
		219.140.190.130 - - [23/May/2006:08:57:59 +0800] "GET /fg172.exe HTTP/1.1" 200 2350253
		221.228.143.52 - - [23/May/2006:08:58:08 +0800] "GET /fg172.exe HTTP/1.1" 206 719996
		221.228.143.52 - - [23/May/2006:08:58:08 +0800] "GET /fg172.exe HTTP/1.1" 206 713242

		#!/usr/bin/python
		dic={}
		a=open("a").readlines()
		for i in a:
			ip=i.strip().split()[0]
			if ip in dic.keys():
				dic[ip] = dic[ip] + 1
			else:
				dic[ip] = 1
		for x,y in dic.items():
			print x," ",y



�����ڸ��£��������ص�ַ��
http://hi.baidu.com/quanzhou722/item/cf4471f8e23d3149932af2a7

����ɾ����Ϣ��ֲ���棬���Ʋ�������Ϊ��

