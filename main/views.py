from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm, PostTicket, PostFollowup
from django.contrib.auth.models import User, Group
from .models import Ticket, FollowUp
from django.http import HttpResponseRedirect
from .filters import OrderFilter

# Create your views here.
@login_required(login_url='/login')
@permission_required("main.add_ticket", login_url="/login", raise_exception=True)
def home(request):
    tickets = Ticket.objects.filter(status="1").order_by('-created_at').select_related('creator')
    if request.method == "POST":
        ticket_id = request.POST.get("ticket-id")
        ticket = tickets.filter(id=ticket_id).first()
        if ticket and request.user.has_perm("main.delete_ticket") :
            ticket.status = "2"
            ticket.save()
    return render(request, 'main/home.html', {"tickets": tickets})

@login_required(login_url='/login')
@permission_required("main.add_ticket", login_url="/login", raise_exception=True)
def history_report(request):
    tickets = Ticket.objects.all().select_related('creator')
    myFilter = OrderFilter(request.GET, queryset=tickets)
    tickets = myFilter.qs
    return render(request, 'main/history.html', {"myFilter": myFilter, "tickets":tickets})
   
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user) 
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})

@login_required(login_url='/login')
@permission_required("main.add_ticket", login_url="/login", raise_exception=True)
def create_ticket(request):
    if request.method == 'POST':
        form = PostTicket(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.creator = request.user
            ticket.save()
            return redirect("/home")
    else:
        form = PostTicket()
    
    return render(request, 'main/create_ticket.html', {"form": form })

@login_required(login_url='/login')
def task(request, task_id):
    tick = Ticket.objects.get(pk=task_id)
    com = PostFollowup()
    if request.method == "POST":
        com = PostFollowup(request.POST)
        followup_id = request.POST.get("follow-up")
        if com.is_valid():
            comment = com.save(commit=False)
            comment.creator = request.user
            comment.ticket = Ticket.objects.select_related('creator').get(id=followup_id)
            comment.save()
            return redirect("/home")
        else:
            com = PostFollowup()

    return render(request, "main/task.html",{"ticket": tick,"com": com})