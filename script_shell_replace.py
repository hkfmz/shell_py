from ressources.models import Vehicule as V 
for row in V.objects.all():
	v=row.matricule
	if v :
		m=v.replace(' ', '')
		row.matricule = m
		row.save()
		print(v,m)
