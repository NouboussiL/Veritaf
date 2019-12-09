def Philo():
	res=""
	res+="Philo="
	res+="[pense,mange,faim]{\n"
	res+="	etat=3;\n"
	res+="	init=0;\n"
	res+="	0=pense;\n"
	res+="	1=mange;\n"
	res+="	2=faim;\n"
	res+="	0->1 [mange];\n"
	res+="	1->0 [finManger];\n"
	res+="};;\n"
	return res