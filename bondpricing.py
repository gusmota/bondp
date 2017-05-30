#FULL/DIRTY PRICE FOR BONDS
#Imput data
print "Welcome to clean/dirty price of bonds"
#Simple mode
#user=raw_input('press 1 to calculate one bond price, press 0 to exit')
#if user==0:
#	quit()
#elif user==1:
#	simplebond()
def simplebond():
	#Enter face value
	faceval=raw_input('Type face value of the bond')
	faceval=float(faceval)
	#Coupon rate
	couponri=raw_input('type coupon rate in 0 format e.g. 0.05 is a 5% interest rate')
	couponri=float(couponri)
	#Days to coupon
	dtc=raw_input('type how many days the bond pays coupon')
	dtc=float(dtc)
	#Days to maturity
	dtm=raw_input('type days to maturity of the bond')
	dtm=int(dtm)
	#yield to maturity
	ytm=raw_input('type market rate for similar bonds in 0 format e.g. 0.075 is a 7.5% market interest rate')
	ytm=float(ytm)
	#
	#
	#Coupons to maturity
	ctm=dtm/dtc
	print ctm, 'coupons to maturity'
	ctms=str(ctm)
	point=ctms.find('.')
	ctm=ctms[:point]
	ctm=float(ctm)
	#Days that passed from the last coupon payment
	dplcp=ctms[point:]
	diasxt=float(dplcp)
	diasxt=diasxt*dtc
	diast=dtc-diasxt
	print ctm, 'coupons left'
	print diasxt,'days to pass until next coupon payment'
	print diast, 'days passed since the last coupon payment'
	#
	#
	#Value of the coupons
	couponv=(couponri*faceval)/(360/dtc)
	print couponv, 'Value of each coupon'
	#Required rate of return
	reqr=(ytm/(360/dtc))
	print reqr, 'Required rate for discounting coupons'
	#
	#Now PV of the FV
	pvfv=faceval/((1+(reqr))**(ctm))
	print pvfv, 'present value of face value'
	#Now PV of the coupons
	pvc=couponv*((1-((1+reqr)**(-ctm)))/(reqr))
	print pvc, 'present value of coupons'	
	print pvc+pvfv, 'price of the bond'
	#
	#Future value with the last coupon
	newval=(pvc+pvfv+couponv)
	print newval, 'NEW NOMINAL FUTURE VALUE'
	#
	#Dirty price
	elfact=float(diasxt/dtc)
	dprice=newval/((1+reqr)**(elfact))
	print dprice, 'Precio sucio'
	#
	#
	#Accrued interests
	#
	print diast, 'Days of accrued interest'
	acint=couponri/360*diast*faceval
	print acint, 'Of accrued interest'
	fullprice=dprice-acint
	print fullprice, 'FULL PRICE'
simplebond()

