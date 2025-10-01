from django.shortcuts import render

# Set your password here - change 'dating2025' to whatever you want
SITE_PASSWORD = 'dating2025'

def index_dating_hub(request):
    # Check password in URL or session
    if request.GET.get('password') == SITE_PASSWORD:
        request.session['site_authenticated'] = True
        return render(request, 'hub/index_dating_hub.html')
    
    if request.session.get('site_authenticated'):
        return render(request, 'hub/index_dating_hub.html')
        
    return render(request, 'hub/password_gate.html')

def about(request):
    if request.session.get('site_authenticated'):
        return render(request, 'hub/about.html')
    return render(request, 'hub/password_gate.html')

def pros_cons(request):
    if request.session.get('site_authenticated'):
        return render(request, 'hub/Pros_and_cons_detailed.html')
    return render(request, 'hub/password_gate.html')

def known_websites(request):
    if request.session.get('site_authenticated'):
        return render(request, 'hub/Known_websites.html')
    return render(request, 'hub/password_gate.html')

def blog(request):
    if request.session.get('site_authenticated'):
        return render(request, 'hub/Blog_index_page.html')
    return render(request, 'hub/password_gate.html')

def blog_boundaries(request):
    if request.session.get('site_authenticated'):
        return render(request, 'hub/Blog_Post-Digital_Boundaries.html')
    return render(request, 'hub/password_gate.html')

def blog_ai(request):
    if request.session.get('site_authenticated'):
        return render(request, 'hub/Blog_Post-AI_Mathcmaking.html')
    return render(request, 'hub/password_gate.html')

def blog_micromance(request):
    if request.session.get('site_authenticated'):
        return render(request, 'hub/Blog_Post-Micro-mance.html')
    return render(request, 'hub/password_gate.html')

def privacy(request):
    if request.session.get('site_authenticated'):
        return render(request, 'hub/Privacy.html')
    return render(request, 'hub/password_gate.html')

def terms(request):
    if request.session.get('site_authenticated'):
        return render(request, 'hub/Terms.html')
    return render(request, 'hub/password_gate.html')

def subscribe_success(request):
    if request.session.get('site_authenticated'):
        return render(request, 'hub/subcribe_success.html')
    return render(request, 'hub/password_gate.html')