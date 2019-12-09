

def Philo():
	res=""
	res+="Philo="
	res+="[pense,mange,faim1,faim2]{\n"
	res+="	etat=4;\n"
	res+="	init=0;\n"
	res+="	0=pense;\n"
	res+="	3=mange;\n"
	res+="	1=faim1;\n"
	res+="	2=faim2;\n"
	res+="	0->1 [arretePenser];\n"
	res+="	1->2 [prendBag1];\n"
	res+="	2->3 [prendBag2_mange];\n"
	res+="	3->0 [finManger];\n"
	res+="};;\n"
	return res


def Baguette():
	res=""
	res+="Baguette="
	res+="[estPrise,estPosee]{\n"
	res+="	etat=2;\n"
	res+="	init=1;\n"
	res+="	0=estPrise;\n"
	res+="	1=estPosee;\n"
	res+="	0->1 [V];\n"
	res+="	1->0 [P];\n"
	res+="};;\n"
	return res

def solution2(n):
	res=""
	res+="solution2 = < "
	for i in range(n):
		res+="Philo philo"+str(i+1)+", Baguette b"+str(i+1)+", "

	res = res[:len(res)-2]
	res+=" >{\n"

	#operations simples
	for i in range(n):
		prend1=""
		prend2=""
		fin=""
		arr=""


		if(i==0):
			tmp=""
			res+="	<mange, P, "
			tmp+="	<finManger, V, "
			for j in range(n-2):
				res+="_, _, "
				tmp+="_, _, "
			res+="_, P>;\n"
			res+=tmp+"_, V>;\n"
		elif(i!=n-1):
			tmp="	<"
			res+="	<"
			for j in range(i-1):
				tmp+="_, _, "
				res+="_, _, "
			res+="_, P, mange, P, "
			tmp+="_, V, finManger, V, "
			for j in range(i,n-1):
				res+="_, _, "
				tmp+="_, _, "
			res = res[:len(res)-2]+">;\n"
			tmp = tmp[:len(tmp)-2]+">;\n"
			res+=tmp
		else:
			res+="	<"
			tmp="	<"
			for j in range(n-2):
				res+="_, _, "
				tmp+="_, _, "
			res+="_, P, mange, P>;\n"
			res+=tmp+"_, V, finManger, V>;\n"

		res+=prend1+"\n"+prend2+"\n"+fin+"\n"+arr

		




	return res+"};;\n"


print(Philo())
print(Baguette())
print(solution2(5))
print("todot solution2.dot solution2;;")