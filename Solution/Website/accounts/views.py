from django.shortcuts import render
from accounts.models import Users
# from django.views.decorators.csrf import csrf_exempt
# from django.core.files.storage import FileSystemStorage
# from django.contrib.auth.models import auth
# Create your views here.


def register(request):

    if request.method == 'POST':
        # agr = request.FILES.get('filepond2')
        nom_association = request.POST['nom_association']
        n_telephone = request.POST['n_telephone']
        email = request.POST['email']
        mot_de_pass = request.POST['mot_de_pass']
        # c_mot_de_pass = request.POST['c_mot_de_pass']
        location = request.POST['location']
        ccp = request.POST['ccp']
        user = Users.objects.create_user(email=email, username=nom_association, location=location,
                                         phone_number=n_telephone, ccp=ccp, img='', agr='', password=mot_de_pass)

        # user.img = request.FILES['images']
        # user.agr = request.FILES['filepond2']
        user.save()
        return render(request, 'Web_Sign_In_Y.html')
    else:
        return render(request, 'Web_Sign_In_Y.html')
