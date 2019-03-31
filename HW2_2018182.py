# CSE 101 - IP HW2
# K-Map Minimization 
# Name:Rohith Rajesh
# Roll Number:2018182
# Section:A
# Group:6
# Date:7/10/2018




def minFunc(n,s):
	'''Function finds the minimised boolean expression when given the proper min terms and the don't care minterms along with
	the nuber of variables.
	Inputs: n= number of variables n<=4
			s=minterms and don't care minterms in the format : '(m1,m2,m3) d(d1,d2,d3)'. Leave d- if no don't care.
	outputs: minimised boolean expression.
	 '''
	#if userinputs an empty string or makes variables 0 then the function gives output 0
	if n!=0 and s!='':
		a,d=s.split(' d')
		a=a[1:-1]
		if '-' in d:
			d=[]
			a=a.split(',')
			a=list(map(int,a))
		else:
			d=d[1:-1]
			a=a.split(',')
			d=d.split(',')
			a=list(map(int,a))
		
			d=list(map(int,d))

		
		def same(s1,s2):
			'''Function takes two strings as input and returns whether s1 includes s2.
			input: 4 character string with either 0,1,*
					*- the digit can be either 0 or 1.
			output:boolean of whether s1 includes s2
			'''
			flag=True
			for x in range(len(s1)):

				if s1[x]=='*':
					continue
				if s1[x]!=s2[x]:
					flag=False
					break

			return flag
		def converter(x,n):
			'''Function which converts an binary to the alphabetical representation.
			inputs: x=binary consisting of 0,1, or *
			output: n=number of variables.
			'''
			k=''
			s=''
			
			for i in range(4-n,4):
				if x[i]!='*':
					if i==0:
						if x[i]=='0':
							s+='w\''
						else:
							s+='w'
					if i==1:
						if x[i]=='0':
							s+='x\''
						else:
							s+='x'
					if i==2:
						if x[i]=='0':
							s+='y\''
						else:
							s+='y'
					if i==3:
						if x[i]=='0':
							s+='z\''
						else:
							s+='z'
			if k =='':
				k=s
			else:
				k=k + ' + '+ s
			if k=='':
				k=str(1)
			return k
		
		g_pi=0
		if g_pi==0:
			#converting the minterms in decimal to binary and storing th ebinaries of proper minterms in 'u' and binaries of 
			#don't care minterms in 'v' 
			u=[]
			v=[]
			for x in a:
				if x<=1:
					u.append('000'+bin(x)[2:])
				elif 1<x<=3:
					u.append('00'+bin(x)[2:])
				elif  3<x<=7:
					u.append('0'+bin(x)[2:])
				else:
					u.append(bin(x)[2:])
			for x in d:
				if x<=1:
					v.append('000'+bin(x)[2:])
				elif 1<x<=3:
					v.append('00'+bin(x)[2:])
				elif  3<x<=7:
					v.append('0'+bin(x)[2:])
				else:
					v.append(bin(x)[2:])
			
			#initially assuming value of all don't care minterms to be '1'
			y=u+v
			k={}
			x='*'
			m='0'
			z='1'
			for i in x,m,z:
				for j in x,m,z:
					for f in x,m,z:
						for l in x+m+z:
							h=i+j+f+l
							k[h]=[]

			#a dictionary k with 4 i bit keys having all possible combinations of 0,1,*, where * is either 0 or 1
			#basically creating all the possible sets of implicants which may or may not be formed. 
			for x in k.keys():
				for r in y:
					if same(x,r):
						k[x].append(r)
			#appending the binaries as values to 'k' checking whether they follow the condition in the key by passing them through function same()

			
			for x in list(k.keys()):
				if len(k[x])!= 2**(x.count('*')):
					del k[x]
			#deleting the unwanted keys,i.e the keys which don't have 2**(number of * in the key) values. If this is not
			#satisfied then the particular list of values in that key cannot form an implicant

			new={}
			for x in k.keys():
				flag=0
				for i in k[x]:
					if not(i in v):
						flag+=1
				if flag!=0:
					new[x]=k[x] 
			
			# deleting all the keys whose values comprise entirely of don't care minterms.

			l1=[]
			for x in new.keys():
				for y in new.keys():
					if x!=y:
						if same(x,y):
							if not(y in l1):

								l1.append(y)
						else:
							continue			

			for x in l1:
				del new[x]
			#removing all the keys which are already a subset of another key. 
			#for example: all values in '00**' will be present is '0***' hence 00** is redundant and is removed.   
			
			# implementing PETRICK METHOD	
			p=[]
			for x in new.keys():
				l=[]
				for j in u:
					if j in new[x]:
						l.append(1)
					else:
						l.append(0)
				p.append(l)

			q='klmnopqrstuvwxyz'
			con=[]
			for x in range(len(new.keys())):
				con.append(q[x])

			p1={}
			for x in range(len(p)):
				p1[con[x]]=p[x]
				
			listing=[]
			for i in range(len(u)):
				o=[]
				for x in list(p1.keys()):
					if p1[x][i]==1:
						o.append(x)
				listing.append(o)
			
			
			
			while len(listing)>1 :
				
				i=0
				listing.append([])
				while i < len(listing[0]) :
					k=0
					while k<(len(listing[-2])):

						listing[-1].append(listing[0][i] + listing[-2][k])
						
						k+=1
					i+=1
				listing.pop(0)
				listing.pop(-2)
				b=listing[0]
				for x in b:
					s5=''
					for i in x:
						if not(i in s5):
							s5+=i
					b[b.index(x)]=s5

								
			reference={}
			y=0
			for x in new.keys():
				reference[con[y]]=x
				y+=1

			mini=b[0]
			for x in b:
				if len(x)<len(mini):
					mini=x
			

			felina=''
			for x in mini:
				y=converter(reference[x],n)
				if felina != '':
					felina=felina+ ' + ' +y
				else:
					felina=y

			lexilist= felina.split(' + ')
			lexilist.sort()
			felina=''
			for x in lexilist:
				if felina!='':
					felina=felina + ' + ' + x
				else:
					felina=x
	else:
		felina='0'

	return felina


