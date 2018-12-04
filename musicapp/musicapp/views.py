from django.shortcuts import redirect

def loginRedirect(request):
    #if request.user.is_authenticated():
        return redirect('/account/')
        #return redirect('/account/login')
