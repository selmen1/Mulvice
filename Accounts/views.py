from django.shortcuts 				import render , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth 			import login, logout , authenticate
from django.contrib.auth.forms		import AuthenticationForm , PasswordChangeForm
from .models                        import User
from django.http                    import HttpResponse
from .forms                         import RegistrationForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding          import force_bytes, force_text
from django.utils.http              import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader         import render_to_string
from .tokens                        import account_activation_token
from django.core.mail               import EmailMessage


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            
            form.save() #     type is <class 'Accounts.models.User'> 
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return render(request , 'email_confirmation.html')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})
    
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.active = True
        user.save()
        login(request, user)
        # return redirect('home')
        #return HttpResponse('Thank you for your email confirmation. Now you can <a href="{% url 'login' %}"></a> your account.')
        return render(request , 'email_confirmation_done.html')
    else:
        return HttpResponse('Activation link is invalid!')




@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST , user = request.user)

        if form.is_valid():
            form.save()

            return HttpResponse('password changed')

    else:
        form = PasswordChangeForm(user = request.user)

        args =  {'form' : form }

        return render(request , 'change_password.html' , args)