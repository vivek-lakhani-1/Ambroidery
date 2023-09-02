from django.shortcuts import render


def homepage(request):
    userisreg = 'no'
    if 'user' in request.session:
        userisreg = 'yes'
        
    frm = {
            'user_reg' : userisreg
        }
    
        
    return render(request,'homepage.html',frm)