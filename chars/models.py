from django.db import models
from skills.models import Core, Root, Secondary, Periphery, Special

class CharMain(models.Model):
    name = models.CharField (max_length=30 ,unique=True)
    main = models.ForeignKey(Core, related_name="char_mains", on_delete=models.CASCADE)
    other = models.ManyToManyField(Secondary, related_name="char_others", blank=True)
    special = models.ForeignKey(Special, related_name="char_specials", on_delete=models.CASCADE)

class CharSupport(models.Model):
    name = models.CharField(max_length=30 ,unique=True)
    main = models.ForeignKey(Root, related_name="supp_mains", on_delete=models.CASCADE)
    other = models.ManyToManyField(Periphery, related_name="supp_others", blank=True)
    special = models.ForeignKey(Special, related_name="supp_specials", on_delete=models.CASCADE)

