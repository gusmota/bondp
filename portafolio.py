#Portafolios 
fname=raw_input('Enter file for stock prices')
#Comprobacion del archivo
if len(fname)<1: fname='port.txt'
try: port=open(fname)
except:
	print "Invalid file name!"
count=0
sum=0
var=0
dates=list()
adjpl=list()
for line in port:
	if line.startswith('Date'): 
		continue
	count=count+1
	line=line.split()
	#aqui le sacamos las fechas y las metemos a una lista
	date=line[0]
	dates.append(date)
	#promedio
	adjp=float(line[6])
	adjpl.append(adjp)
	sum=sum+adjp
#Sacamos los datos de la lista de fechas
idate=dates[count-1]
fdate=dates[0]
avgsp=sum/count
#Varianza
for i in adjpl:
	des=i-avgsp
	var=var+des
vari=var/count
#Desvest 
desvest=var**(0.5)
#print to user
print 'INITIAL DATE:',idate
print 'FINAL DATE', fdate
print 'DAYS TRADED:', count
print 'AVERAGE STOCK PRICES', sum/count
print 'VARIANCE STOCK PRICES',vari
print 'Standard deviation', desvest
