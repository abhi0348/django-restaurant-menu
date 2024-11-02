from django.shortcuts import render, redirect
from .models import Category,dish
from .forms import MenuForm ,SignUpForm,ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail



@login_required
def view_menu(request):
    
    category_id = request.GET.get('category')
    categories = Category.objects.all()
    if category_id:
        # Filter dishes by selected category
        dishes = dish.objects.filter(category_id=category_id)
    else:
        # Show all dishes if no category is selected
        dishes = dish.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save form data to the Contact model
            subject = 'Thank You for Your Message'
            message = 'We have received your message and will get back to you soon.'
            from_email = 'kuchbhi00348@gmail.com'
            recipient_list = [form.cleaned_data['email']]
            send_mail(subject, message, from_email, recipient_list)
            return redirect('menu')  # Redirect to the same page or another page on success
    else:
        form = ContactForm()
    context = {
        'categories' : categories,
        'dishes' : dishes,
        'form' : form
    }
    return render(request,'menu/menu1.html',context)

@login_required
def sugg_view(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()        
            return redirect(request.path)
    else:
        form = MenuForm()

    return render(request, 'sugg.html', {'form': form})        


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            return redirect('login')  # Redirect to login page
    else:
        form = SignUpForm()

    return render(request, 'menu/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/menu')  # Redirect to your desired page
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'registration/login.html')  # Ensure this points to your login template

            # print("wrong")

    return render(request, 'login.html')  # Replace with your template name

