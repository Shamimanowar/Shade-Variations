from django.db import models
from django.core import validators

# Create your models here.

class ShadeVariation(models.Model):
    node_id = models.IntegerField()
    R1 = models.IntegerField(validators=[validators.MaxValueValidator(255), validators.MinValueValidator(0)])
    G1 = models.IntegerField(validators=[validators.MaxValueValidator(255), validators.MinValueValidator(0)])
    B1 = models.IntegerField(validators=[validators.MaxValueValidator(255), validators.MinValueValidator(0)])
    R2 = models.IntegerField(validators=[validators.MaxValueValidator(255), validators.MinValueValidator(0)])
    G2 = models.IntegerField(validators=[validators.MaxValueValidator(255), validators.MinValueValidator(0)])
    B2 = models.IntegerField(validators=[validators.MaxValueValidator(255), validators.MinValueValidator(0)])
    R3 = models.IntegerField(validators=[validators.MaxValueValidator(255), validators.MinValueValidator(0)])
    G3 = models.IntegerField(validators=[validators.MaxValueValidator(255), validators.MinValueValidator(0)])
    B3 = models.IntegerField(validators=[validators.MaxValueValidator(255), validators.MinValueValidator(0)])
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Shade Variations'
    
    def __str__(self):
        return f'Node id {self.node_id}  Created at {self.created_at}'
