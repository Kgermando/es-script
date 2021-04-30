from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from accounts.models import Profile

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request,"! vous êtes authentifiés!! .")
            return redirect('dashboard:dashboard')
        else:
            messages.error(request, "les informations d'identifications sont invalides, vérifier votre prénom")
            return redirect('login')
    return render(request, 'pages/accounts/login.html')
 

def register_view(request):
    if request.method == 'POST':
        # Get form vales
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        # statut = request.POST['statut']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Ce Nom d\'utilisateur existe déjà!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Cette email est déjà utilisé!')
                    return redirect('register')
                else:
                    #Looks good
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, "You are now loged in")
                    # return redirect('index')

                    user.save()
                    messages.success(request, 'Congratulations! Vous êtes enregistrée! Connectez vous maintenant')
                    return redirect('login')
        else:
            messages.error(request, 'Le mot de passe ne corresponds pas')
            return redirect('register')
    else:
        return render(request, 'pages/accounts/register.html')
    
    return render(request, 'pages/accounts/register.html')

def logout_view(request):
    if request.method == 'GET':
        auth.logout(request)
        messages.success(request, "Vous êtes déconnecté.")
        return redirect('login')
    else:
        return redirect('login')


@login_required(login_url='/login')
def profile(request):
    # user = request.user
    # profile = Profile.objects.get(id=user.pk)
    profile = Profile.objects.get(user=request.user)

    context = {
        'profile': profile
    }
    template_name='pages/accounts/profile.html'
    return render(request, template_name, context)


@login_required(login_url='/login')
def profile_edit(request):
    pk = request.user
    profile = Profile.objects.get(pk=pk)

    # if request.method=='POST':
    # try:
    #     profile=Profile.objects.get(user=request.user)
    # except:
    #     profile=Profile()
    #     profile.user=request.user
    
    # profile.profile_picture=request.FILES['photo']
    # profile.save()
    # post=Post()
    # post.body=request.POST['status']
    # post.user=request.user
    # post.storytype=" updated profile picture "
    # post.save()
    # postimage=PostImage()
    # postimage.url=profile.profile_picture
    # postimage.post=post
    # postimage.save()
    # add_user_to_post(post,request.user)
    # returndata={
    #     "imageid":postimage.id,
    #     "id":post.id,
    #     "name":request.user.first_name+" "+request.user.last_name,
    #     "date":post.date,
    #     "picture":str(postimage.url),
    #     "status":post.body
    # }
    # return JsonResponse(returndata)


    context = None
    template_name='pages/accounts/profile_edit.html'
    return render(request, template_name, context)
