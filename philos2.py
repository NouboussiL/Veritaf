

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
	res+=" >{\n\n"
	prend1=""
	prend2=""
	fin=""
	arr=""
	#operations simples
	for i in range(n):



		if(i==0):
			arr+="	< arretePenser, _"
			prend1+="	< prendBag1, _"
			prend2+="	< prendBag2_mange, P"
			fin+="	< finManger, V"
			for j in range(n-2):
				arr+=", _, _"
				prend1+=", _, _"
				prend2+=", _, _"
				fin+=", _, _"
			arr+=", _, _ >;\n"
			prend1+=", _, P >;\n"
			prend2+=", _, _ >;\n"
			fin+=", _, V >;\n"
			
		elif(i!=n-1):
			prend1+="	< "
			prend2+="	< "
			fin+="	< "
			arr+="	< "
			for j in range (i-1):
				prend1+="_, _, "
				prend2+="_, _, "
				fin+="_, _, "
				arr+="_, _, "
			prend1+="_, _, prendBag1, P"
			prend2+="_, P, prendBag2_mange, _"
			fin+="_, V, finManger, V"
			arr+="_, _, arretePenser, _"
			for j in range (i,n-1):
				prend1+=", _, _ "
				prend2+=", _, _ "
				fin+=", _, _ "
				arr+=", _, _ "
			prend1+=">;\n"
			prend2+=">;\n"
			fin+=">;\n"
			arr+=">;\n"
				
		else:
			prend1+="	< "
			prend2+="	< "
			fin+="	< "
			arr+="	< "
			for j in range(n-2):
				prend1+="_, _, "
				prend2+="_, _, "
				fin+="_, _, "
				arr+="_, _, "
			prend1+="_, _, prendBag1, P >;\n"
			prend2+="_, P, prendBag2_mange, _ >;\n"
			fin+="_, V, finManger, V >;\n"
			arr+="_, _, arretePenser, _ >;\n"

	res+=arr+"\n"+prend1+"\n"+prend2+"\n"+fin+"\n"


	return res+"};;\n"


print(Philo())
print(Baguette())
print(solution2(3))

print("""/* Il est impossible que les philosophes mangent en même temps */
solution2 += conflit <- AG(!(philo1.mange && philo2.mange && philo3.mange));;

/* Chaque philosophe affamé mangera dans le futur */
solution2 += affame1 <- AG(philo1.faim2 -> AF(philo1.mange));;
solution2 += affame2 <- AG(philo2.faim2 -> AF(philo2.mange));;
solution2 += affame3 <- AG(philo3.faim2 -> AF(philo3.mange));;

/* Chaque philosophe qui pense aura faim dans le futur */
solution2 += faim1 <- AG(philo1.pense -> AF(philo1.faim1));;
solution2 += faim2 <- AG(philo2.pense -> AF(philo2.faim1));;
solution2 += faim3 <- AG(philo3.pense -> AF(philo3.faim1));;""")

print("todot solution2_ordre3.dot solution2;;")
