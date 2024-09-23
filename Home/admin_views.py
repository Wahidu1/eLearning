from django.shortcuts import render, redirect

def backend_dashboard(request):
    return render(request, "Home/backend/dashboard.html", {})