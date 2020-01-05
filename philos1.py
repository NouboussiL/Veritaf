def Philo():
	res=""
	res+="Philo="
	res+="[pense,mange,faim]{\n"
	res+="	etat=3;\n"
	res+="	init=0;\n"
	res+="	0=pense;\n"
	res+="	1=faim;\n"
	res+="	2=mange;\n"
	res+="	0->1 [afaim];\n"
	res+="	2->0 [finManger];\n"
	res+="	1->2 [commManger];\n"
	res+="	0->0 [repense];\n"
	res+="	1->1 [pensepas];\n"
	res+="	2->2 [pensepas];\n"
	res+="};;\n"
	return res

def Arete():
	res=""
	res+="Arete="
	res+="[nonO,droite,gauche]{\n"
	res+="	etat=3;\n"
	res+="	init=0;\n"
	res+="	0=nonO;\n"
	res+="	1=droite;\n"
	res+="	2=gauche;\n"
	res+="	0->1 [gd];\n"
	res+="	1->0 [reset];\n"
	res+="	1->1 [d];\n"
	res+="	0->2 [dg];\n"
	res+="	2->2 [g];\n"
	res+="	2->0 [reset];\n"
	res+="	0->0 [reset,rien];\n"
	res+="};;\n"
	return res

def solution1(n):
	res=""
	res+="solution1 = < "
	for i in range(n):
		res+="Philo philo"+str(i+1)+", Arete a"+str(i+1)+", "
	res = res[:len(res)-2]
	res += " >{\n\n"
	faim=""
	faimPensePas=""
	faimPensePasGauche=""
	faimPensePasDroite=""
	manger=""
	mangerDouble=""
	mangerGauche=""
	mangerDroite=""
	penser=""

	for i in range(n):
		if(i==0):
			penser="	< finManger, reset, _, _"
			manger="	< commManger, rien, _, _"
			mangerDroite="	< commManger, g, _, _"
			mangerDouble="	< commManger, g, _, _"
			mangerGauche="	< commManger, rien, _, _"
			faimPensePas="	< afaim, gd, pensepas, _"
			faimPensePasDroite="	< afaim, gd, pensepas, _"
			faimPensePasGauche="	< afaim, _, repense, _"
			faim="	< afaim, _, repense, _"
			
			for j in range(n-3):
				penser+=", _, _"
				manger+=", _, _"
				mangerDroite+=", _, _"
				mangerDouble+=", _, _"
				mangerGauche+=", _, _"
				faimPensePas+=", _, _"
				faimPensePasDroite+=", _, _"
				faimPensePasGauche+=", _, _"
				faim+=", _, _"
			penser+=", _, reset >;\n"
			manger+=", _, rien >;\n"
			mangerDroite+=", _, rien >;\n"
			mangerDouble+=", _, d >;\n"
			mangerGauche+=", _, d >;\n"
			faimPensePas+=", pensepas, dg >;\n"
			faimPensePasDroite+=", repense, _ >;\n"
			faimPensePasGauche+=", pensepas, dg >;\n"
			faim+=", repense, _ >;\n"

		elif(i!=n-1):
			penser+="	<"
			manger+="	<"
			mangerDroite+="	<"
			mangerDouble+="	<"
			mangerGauche+="	<"
			faimPensePas+="	<"
			faimPensePasDroite+="	<"
			faimPensePasGauche+="	<"
			faim+="	<"
			for j in range(i-1):
				penser+=" _, _,"
				manger+=" _, _,"
				mangerDroite+=" _, _,"
				mangerDouble+=" _, _,"
				mangerGauche+=" _, _,"
				faimPensePas+=" _, _,"
				faimPensePasDroite+=" _, _,"
				faimPensePasGauche+=" _, _,"
				faim+=" _, _,"
			penser+=" _, reset, finManger, reset, _, _"
			manger+=" _, rien, commManger, rien, _, _"
			mangerDouble+=" _, d, commManger, g, _, _"
			mangerDroite+=" _, rien, commManger, g, _, _"
			mangerGauche+=" _, d, commManger, rien, _, _"
			faimPensePas+=" pensepas, dg, afaim, gd, pensepas, _"
			faimPensePasDroite+=" repense, _, afaim, gd, pensepas, _"
			faimPensePasGauche+=" pensepas, dg, afaim, _, repense, _"
			faim+=" repense, _, afaim, _, repense, _"

			for j in range(i+1,n-1):
				penser+=", _, _"
				manger+=", _, _"
				mangerDroite+=", _, _"
				mangerDouble+=", _, _"
				mangerGauche+=", _, _"
				faimPensePas+=", _, _"
				faimPensePasDroite+=", _, _"
				faimPensePasGauche+=", _, _"
				faim+=", _, _"
			penser+=" >;\n"
			manger+=" >;\n"
			mangerDroite+=" >;\n"
			mangerGauche+=" >;\n"
			mangerDouble+=" >;\n"
			faimPensePas+=" >;\n"
			faimPensePasDroite+=" >;\n"
			faimPensePasGauche+=" >;\n"
			faim+=" >;\n"
	
		else:
			penser+="	< _, _,"
			manger+="	< _, _,"
			mangerDroite+="	< _, _,"
			mangerGauche+="	< _, _,"
			mangerDouble+="	< _, _,"
			faimPensePas+= "	< pensepas, _,"
			faimPensePasDroite+= "	< pensepas, _,"
			faimPensePasGauche+= "	< repense, _,"
			faim+= "	< repense, _,"
			for j in range(n-3):
				penser+=" _, _,"
				manger+=" _, _,"
				mangerDroite+=" _, _,"
				mangerGauche+=" _, _,"
				mangerDouble+=" _, _,"
				faimPensePas+=" _, _,"
				faimPensePasDroite+=" _, _,"
				faimPensePasGauche+=" _, _,"
				faim+=" _, _,"
			faimPensePas+=" pensepas, dg, afaim, gd >;\n"
			faimPensePasDroite+=" repense, _, afaim, gd >;\n"
			faimPensePasGauche+=" pensepas, dg, afaim, _ >;\n"
			faim+=" repense, _, afaim, _ >;\n"
			penser+=" _, reset, finManger, reset >;\n"
			manger+=" _, rien, commManger, rien >;\n"
			mangerDouble+=" _, d, commManger, g >;\n"
			mangerDroite+=" _, rien, commManger, g >;\n"
			mangerGauche+=" _, d, commManger, rien >;\n"


	res+=penser+'\n'+faim+"\n"+faimPensePas+"\n"+faimPensePasDroite+"\n"+faimPensePasGauche+"\n"+manger+"\n"+mangerDroite+"\n"+mangerGauche+"\n"+mangerDouble+"\n"+"};;\n"
	return res

print(Philo())
print(Arete())
print(solution1(3))

print("""/* Il est impossible que les philosophes mangent en même temps */
solution1 += conflit <- AG(!(philo1.mange && philo2.mange && philo3.mange));;

/* Chaque philosophe affamé mangera dans le futur */
solution1 += affame1 <- AG(philo1.faim -> AF(philo1.mange));;
solution1 += affame2 <- AG(philo2.faim -> AF(philo2.mange));;
solution1 += affame3 <- AG(philo3.faim -> AF(philo3.mange));;

/* Chaque philosophe qui pense aura faim dans le futur */
solution1 += faim1 <- AG(philo1.pense -> AF(philo1.faim));;
solution1 += faim2 <- AG(philo2.pense -> AF(philo2.faim));;
solution1 += faim3 <- AG(philo3.pense -> AF(philo3.faim));;""")

print("todot solution1.dot solution1;;")

print("erreur = solution1 -> philo1.mange && philo2.mange || philo1.mange && philo3.mange || philo2.mange && philo3.mange;;")

print("todot erreurSolution1.dot erreur;;")

