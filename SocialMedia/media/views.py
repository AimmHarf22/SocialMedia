from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "media/register.html")


def register(request):
    # Check For Request method
    if request.method == 'POST':
        # Post Data
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        # VALIDATION
        
            # Check for empty boxes
        if len(first_name) == 0 or len(last_name) == 0 or len(email) == 0 or len(username) == 0 or len(password) == 0 or len(password2) == 0:
            return render(request, "register.html", {
                'message': "All Fields Must Not Be blank"
            })
        
            # Check if the passwords match
        if password != password2:
            return render(request, "register.html", {"message": "Password Does Not Match"})
        
            # Check if email is valid
        if not '@' in email:
            return render(request, "register.html", {"message": "Invalid Email"})
        
            # Check if password is strong
        if not len(password) > 4:
            return render(request, "register.html", {"message": "Password is weak"})
        

        # ADD DATA TO DATABASE
        ...