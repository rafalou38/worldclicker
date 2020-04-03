from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile



@receiver( post_save , sender=User)
def create_profile(sender, instance, created, signal, **kwargs):
	if created:
		pass
		# print(kwargs)
		# print(dir(signal))
		# print(dir(instance))

		Profile.objects.create(user=instance)

@receiver( post_save , sender=User)
def save_profile(sender, instance, **kwargs):
	# print("-----------sender--------------------")
	# print(sender)
	# print("-----------sender--------------------")
	# print("-----------instance--------------------")
	# print(dir(instance.profile))
	# print("-----------instance--------------------")
	# print(instance.profile.pays)
	# print("-----------post_save--------------------")
	# print(dir(post_save))
	# print("-----------post_save--------------------")
	instance.profile.save()
