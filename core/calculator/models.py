from django.db import models

class CalculatorHistory(models.Model):
  number_a = models.FloatField()
  number_b = models.FloatField()
  operation = models.CharField(max_length=10)
  operation_status = models.CharField(max_length=10)  #for success and failure 
  result = models.TextField()
  
  created_at = models.DateTimeField(
    # auto_now_add=True,   creation timestamp capture
    auto_now=True, #update timestamp capture
  )
  
  class Meta:
    db_table = "calculator_history" 
  
  def __str__(self):
    return self.result
  