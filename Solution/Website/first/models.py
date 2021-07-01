

from django.db import models


class cas(models.Model):
     categories = (
        ('Santé', 'Santé'),
        ('Education', 'SEducation'),
        ('Autres', 'Autres'),
     )
     wilayas = (

         ('Adrar', 'Adrar'),
         ('Chlef', 'Chlef'),
         ('Laghouat', 'Laghouat'),
         ('Oum El Bouaghi', 'Oum El Bouaghi'),
         ('Batna', 'Batna'),
         ('Béjaïa', 'Béjaïa'),
         ('Biskra', 'Biskra'),
         ('Béchar', 'Béchar'),
         ('Blida', 'Blida'),
         ('Bouira', 'Bouira'),
         ('Tébessa', 'Tébessa'),
         ('Tlemcen', 'Tlemcen'),
         ('Tiaret', 'Tiaret'),
         ('Tizi Ouzou', 'Tizi Ouzou'),
         ('Alger', 'Alger'),
         ('Djelfa', 'Djelfa'),
         ('Jijel', 'Jijel'),
         ('Sétif', 'Sétif'),
         ('Saïda', 'Saïda'),
         ('Skikda', 'Skikda'),
         ('Sidi Bel Abbès', 'idi Bel Abbès'),
         ('Annaba', 'Annaba'),
         ('Guelma', 'Guelma'),
         ('Constantine', 'Constantine'),
         ('Médéa', 'Médéa'),
         ('Mostaganem', 'Mostaganem'),
         ('MSila', 'MSila'),
         ('Mascara', 'Mascara'),
         ('Ouargla', 'Ouargla'),
         ('Oran', 'Oran'),
         ('El Bayadh', 'El bayedh'),
         ('Illizi', 'Illizi'),
         ('Bordj Bou Arreridj', 'Bordj Bou Arreridj'),
         ('Boumerdès', 'Boumerdès'),
         ('El Tarf', 'El Tarf'),
         ('Tindouf', 'Tindouf'),
         ('Tissemsilt', 'Tissemsilt'),
         ('El Oued', 'El Oued'),
         ('Khenchela', 'Khenchla'),
         ('Souk Ahras', 'Souk Ahras'),
         ('Tipaza', 'Tipaza'),
         ('Mila', 'Mila'),
         ('Aïn Defla', 'Aïn Defla'),
         ('Naâma', 'Naâma'),
         ('Aïn Témouchent', 'Aïn Témouchent'),
         ('Ghardaïa', 'Ghardaïa'),
         ('Relizane', 'Relizane'),
         ('Timimoun', 'Timimoun'),
         ('Bordj Badji Mokhtar', 'Bordj Badji Mokhtar'),
         ('Ouled Djellal', 'Ouled Djellal'),
         ('Béni Abbès', 'Béni Abbès'),
         ('In Salah', 'In Salah'),
         ('In Guezzam', 'In Guezzam'),
         ('Touggourt', 'Touggourt'),
         ('Djanet', 'Djanet'),
         ('El Mghair', 'El Mghair'),
         ('El Meniaa', 'El Meniaa'),
     )
     titre = models.CharField(max_length=200, null=True)
     nom = models.CharField(max_length=200, null=True)
     prenom = models.CharField(max_length=200, null=True)
     img = models.ImageField(upload_to='images', null=True)
     resumé = models.TextField(null=True)
     description = models.TextField(null=True)
     age = models.IntegerField(null=True)
     wilaya = models.CharField(max_length=200, null=True, choices=wilayas)
     email = models.EmailField(max_length=254, null=True)
     category = models.CharField(max_length=200, null=True, choices=categories)
     montant_requis = models.FloatField(null=True)
     montant_initial = models.FloatField(null=True)



class association(models.Model):

		nom_association = models.CharField(max_length=200, null=True)
		Adress = models.TextField(null=True)
		email = models.EmailField(max_length=254, null=True)
		img = models.ImageField(upload_to='images', null=True)
		N_telephone = models.IntegerField(null=True)

		description = models.TextField(null=True)











