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
	res+="	1->1 [tjrFaim];\n"
	res+="	2->2 [remange];\n"
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
	res+="	0->2 [dg];\n"
	res+="	2->0 [reset];\n"
	res+="};;\n"
	return res

def solution1(n):
