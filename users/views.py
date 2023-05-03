from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib import messages
from users.form import NewUserForm

def dashboard(request):
    return render(request, "users/dashboard.html")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()

			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("users/dashboard.html")
		messages.error(request, "Unsuccessful registration. Invalid information.")
   
	form = NewUserForm()
    
	return render (request=request, template_name="users/register.html", context={"register_form":form})