from pyexpat.errors import messages

from django.shortcuts import redirect, render
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request, "home.html")


def signup(request):
    if request.method == "POST":
        # handle sign in
        if request.POST["password"] == request.POST["password2"]:
            if (
                request.POST["username"]
                and request.POST["email"]
                and request.POST["password"]
            ):
                try:
                    user = User.objects.get(email=request.POST["email"])
                    return render(
                        request, "signup.html", {"error": "User Already Exists"}
                    )
                except User.DoesNotExist:
                    User.objects.create_user(
                        username=request.POST["username"],
                        email=request.POST["email"],
                        password=request.POST["password"],
                    )
                    messages.success(request, "Signup Successful <br> Login Here")
                    return redirect(login)
            else:
                return render(request, "signup.html", {"error": "Empty Fields"})
        else:
            return render(request, "signup.html", {"error": "Password's Don't Match"})
    else:
        return render(request, "signup.html")


def login(request):
    return render(request, "login.html")
