from django.shortcuts import render
from calculator.models import CalculatorHistory

def calculator_view(request):
    context={}
    data = {}
    
    result = None
    if request.method == "POST":
        form_data=request.POST
        
        number_a:str=form_data.get("number_a")
        number_b:str=form_data.get("number_b")
        
        operation=form_data.keys()

        print(f"Recieved Number:Number a:{number_a}, and Number b: {number_b} , Operation:{operation}")

        
        if number_a.isnumeric() and number_b.isnumeric():
            number_a=float(number_a)
            number_b=float(number_b)
            
            data.update(
                number_a = number_a,
                number_b = number_b
            )
                
            if "add" in operation:
                result = number_a + number_b
                message=f"Addition of {number_b} and {number_a} is {result}"
                context.update(
                message = message
                )
                action = "add"
            elif "subtract" in operation:
                result = number_a - number_b
                message=f"Subtraction of {number_b} and {number_a} is {result}"
                context.update(
                message = message
                )
                action = "sub"
            elif "multiply" in operation:
                result = number_a * number_b
                message=f"Multiply of {number_b} and {number_a} is {result}"
                context.update(
                message = message
                )
                action = "mul"
                
            elif "divide" in operation:
                result = number_a / number_b
                message=f"Division of {number_b} and {number_a} is {result}"
                context.update(
                message = message
                )
                action = "div"
                
            data.update(
                operation=action,
                operation_status = "Success",
                result = message                    
            )
                
            #saving the object to database, any method can be used
                
            # 1)  instance = CalculatorHistory(**data)
            #  instance.save()
            # 2)
            CalculatorHistory.objects.create(**data)
                 
        else:
            message="YOU NEED TO PASS NUMERIC VALUE FOR MATH OPS"
            context.update(
                message = message
            )
    
    return render(request, "calculator.html", context)