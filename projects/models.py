from django.db import models


class Episodes(models.Model):
	number = models.CharField(max_length=100)
	ep_link = models.URLField()

	def __str__(self):
		return self.number

#class Summary(models.Model):
#	title = models.CharField(null=True, blank=True, max_length=100)
#	genre = models.TextField(null=True, blank=True)
#	author = models.TextField(null=True, blank=True)
#	release = models.TextField(null=True, blank=True)

#	def __str__(self):
#		return self.title

class Videos(models.Model):
	photo = models.ImageField(upload_to='images', default='#')
	title = models.CharField(null=True, blank=True, max_length=100)
	description = models.TextField(null=True, blank=True)
	season = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
	eps_link = models.ManyToManyField(Episodes)
	genre = models.TextField(null=True, blank=True)
	author = models.TextField(null=True, blank=True)
	release = models.TextField(null=True, blank=True)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.title

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
	videos = models.ForeignKey(Videos, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __str__(self):
		return self.choice_text