from django.shortcuts import render

from oss.models import Journal
from django.shortcuts import render
from dl.models import Volume, Issue


# Create your views here.

def about(request):
    journals = Journal.objects.all()
    
    jcs_journal = Journal.objects.get(title='JCS') 
    latest_volume = Volume.objects.filter(journal=jcs_journal).order_by('-year', '-volume').first()
    if latest_volume:
        # Get the latest issue for the latest volume
        latest_issue = Issue.objects.filter(volume=latest_volume).order_by('-issue').first()
    
    return render(request, 'about.html',{'journals': journals, 'latest_issue':latest_issue})

def about_ijam(request):
    journals = Journal.objects.all()
    return render(request, 'about_ijam.html',{'journals': journals})

def about_jcm(request):
    journals = Journal.objects.all()
    return render(request, 'about_jcm.html',{'journals': journals})

def about_jcs(request):
    journals = Journal.objects.all()
    
    jcs_journal = Journal.objects.get(title='JCS') 
    latest_volume = Volume.objects.filter(journal=jcs_journal).order_by('-year', '-volume').first()
    if latest_volume:
        # Get the latest issue for the latest volume
        latest_issue = Issue.objects.filter(volume=latest_volume).order_by('-issue').first()
        
    return render(request, 'about_jcs.html',{'journals': journals, 'latest_issue':latest_issue})

def aim_scope_ijam(request):
    journals = Journal.objects.all()
    return render(request, 'aim_scope_ijam.html',{'journals': journals})

def aim_scope_jcm(request):
    journals = Journal.objects.all()
    return render(request, 'aim_scope_jcm.html',{'journals': journals})

def aim_scope_jcs(request):
    journals = Journal.objects.all()
    
    jcs_journal = Journal.objects.get(title='JCS') 
    latest_volume = Volume.objects.filter(journal=jcs_journal).order_by('-year', '-volume').first()
    if latest_volume:
        # Get the latest issue for the latest volume
        latest_issue = Issue.objects.filter(volume=latest_volume).order_by('-issue').first()
    
    return render(request, 'aim_scope_jcs.html',{'journals': journals, 'latest_issue':latest_issue})

def author_center(request):
    journals = Journal.objects.all()
    
    jcs_journal = Journal.objects.get(title='JCS') 
    latest_volume = Volume.objects.filter(journal=jcs_journal).order_by('-year', '-volume').first()
    if latest_volume:
        # Get the latest issue for the latest volume
        latest_issue = Issue.objects.filter(volume=latest_volume).order_by('-issue').first()
    
    return render(request, 'author_center.html',{'journals': journals, 'latest_issue':latest_issue})

def authors_guidelines_ijam(request):
    journals = Journal.objects.all()
    return render(request, 'authors_guidelines_ijam.html',{'journals': journals})

def authors_guidelines_jcm(request):
    journals = Journal.objects.all()
    return render(request, 'authors_guidelines_jcm.html',{'journals': journals})

def authors_guidelines_jcs(request):
    journals = Journal.objects.all()
    
    jcs_journal = Journal.objects.get(title='JCS') 
    latest_volume = Volume.objects.filter(journal=jcs_journal).order_by('-year', '-volume').first()
    if latest_volume:
        # Get the latest issue for the latest volume
        latest_issue = Issue.objects.filter(volume=latest_volume).order_by('-issue').first()
    
    return render(request, 'authors_guidelines_jcs.html',{'journals': journals, 'latest_issue':latest_issue})

def contact(request):
    journals = Journal.objects.all()
    
    jcs_journal = Journal.objects.get(title='JCS') 
    latest_volume = Volume.objects.filter(journal=jcs_journal).order_by('-year', '-volume').first()
    if latest_volume:
        # Get the latest issue for the latest volume
        latest_issue = Issue.objects.filter(volume=latest_volume).order_by('-issue').first()
    
    return render(request, 'contact.html',{'journals': journals, 'latest_issue':latest_issue})


def editorial_board_members_ijam(request):
    journals = Journal.objects.all()
    return render(request, 'editorial_board_members_ijam.html',{'journals': journals})

def editorial_board_members_jcm(request):
    journals = Journal.objects.all()
    return render(request, 'editorial_board_members_jcm.html',{'journals': journals})

def editorial_board_members_jcs(request):
    journals = Journal.objects.all()
    
    jcs_journal = Journal.objects.get(title='JCS') 
    latest_volume = Volume.objects.filter(journal=jcs_journal).order_by('-year', '-volume').first()
    if latest_volume:
        # Get the latest issue for the latest volume
        latest_issue = Issue.objects.filter(volume=latest_volume).order_by('-issue').first()
    
    return render(request, 'editorial_board_members_jcs.html',{'journals': journals, 'latest_issue':latest_issue})

def faq_karpagam_ijam(request):
    journals = Journal.objects.all()
    return render(request, 'faq_karpagam_ijam.html',{'journals': journals})

def faq_karpagam_jcm(request):
    journals = Journal.objects.all()
    return render(request, 'faq_karpagam_jcm.html',{'journals': journals})

def faq_karpagam_jcs(request):
    journals = Journal.objects.all()
    
    jcs_journal = Journal.objects.get(title='JCS') 
    latest_volume = Volume.objects.filter(journal=jcs_journal).order_by('-year', '-volume').first()
    if latest_volume:
        # Get the latest issue for the latest volume
        latest_issue = Issue.objects.filter(volume=latest_volume).order_by('-issue').first()
    
    return render(request, 'faq_karpagam_jcs.html',{'journals': journals, 'latest_issue':latest_issue})

def institutions(request):
    
    jcs_journal = Journal.objects.get(title='JCS') 
    latest_volume = Volume.objects.filter(journal=jcs_journal).order_by('-year', '-volume').first()
    if latest_volume:
        # Get the latest issue for the latest volume
        latest_issue = Issue.objects.filter(volume=latest_volume).order_by('-issue').first()
    
    return render(request, 'institutions.html',{'latest_issue':latest_issue})

def online_paper_submission(request):
    journals = Journal.objects.all()
    
    jcs_journal = Journal.objects.get(title='JCS') 
    latest_volume = Volume.objects.filter(journal=jcs_journal).order_by('-year', '-volume').first()
    if latest_volume:
        # Get the latest issue for the latest volume
        latest_issue = Issue.objects.filter(volume=latest_volume).order_by('-issue').first()
    
    return render(request, 'online_paper_submission.html',{'journals': journals, 'latest_issue':latest_issue})

def plagiarism_policy_ijam(request):
    journals = Journal.objects.all()
    return render(request, 'plagiarism_policy_ijam.html',{'journals': journals})

def plagiarism_policy_jcm(request):
    journals = Journal.objects.all()
    return render(request, 'plagiarism_policy_jcm.html',{'journals': journals})

def plagiarism_policy_jcs(request):
    journals = Journal.objects.all()
    
    jcs_journal = Journal.objects.get(title='JCS') 
    latest_volume = Volume.objects.filter(journal=jcs_journal).order_by('-year', '-volume').first()
    if latest_volume:
        # Get the latest issue for the latest volume
        latest_issue = Issue.objects.filter(volume=latest_volume).order_by('-issue').first()
    
    return render(request, 'plagiarism_policy_jcs.html',{'journals': journals, 'latest_issue':latest_issue})

def publication_fees(request):
    journals = Journal.objects.all()
    
    jcs_journal = Journal.objects.get(title='JCS') 
    latest_volume = Volume.objects.filter(journal=jcs_journal).order_by('-year', '-volume').first()
    if latest_volume:
        # Get the latest issue for the latest volume
        latest_issue = Issue.objects.filter(volume=latest_volume).order_by('-issue').first()
    
    return render(request, 'publication_fees.html',{'journals': journals, 'latest_issue':latest_issue})

def review_board_ijam(request):
    journals = Journal.objects.all()
    return render(request, 'review_board_ijam.html',{'journals': journals})

def review_board_jcm(request):
    journals = Journal.objects.all()
    return render(request, 'review_board_jcm.html',{'journals': journals})

def review_board_jcs(request):
    journals = Journal.objects.all()
    
    jcs_journal = Journal.objects.get(title='JCS') 
    latest_volume = Volume.objects.filter(journal=jcs_journal).order_by('-year', '-volume').first()
    if latest_volume:
        # Get the latest issue for the latest volume
        latest_issue = Issue.objects.filter(volume=latest_volume).order_by('-issue').first()
    
    return render(request, 'review_board_jcs.html',{'journals': journals, 'latest_issue':latest_issue})

def reviewer_policy_ijam(request):
    journals = Journal.objects.all()
    return render(request, 'reviewer_policy_ijam.html',{'journals': journals})

def reviewer_policy_jcm(request):
    journals = Journal.objects.all()
    return render(request, 'reviewer_policy_jcm.html',{'journals': journals})

def reviewer_policy_jcs(request):
    journals = Journal.objects.all()
    
    jcs_journal = Journal.objects.get(title='JCS') 
    latest_volume = Volume.objects.filter(journal=jcs_journal).order_by('-year', '-volume').first()
    if latest_volume:
        # Get the latest issue for the latest volume
        latest_issue = Issue.objects.filter(volume=latest_volume).order_by('-issue').first()
    
    return render(request, 'reviewer_policy_jcs.html',{'journals': journals, 'latest_issue':latest_issue})

def subscription_ijam(request):
    journals = Journal.objects.all()
    return render(request, 'subscription_ijam.html',{'journals': journals})

def subscription_jcm(request):
    journals = Journal.objects.all()
    return render(request, 'subscription_jcm.html',{'journals': journals})

def subscription_jcs(request):
    journals = Journal.objects.all()
    
    jcs_journal = Journal.objects.get(title='JCS') 
    latest_volume = Volume.objects.filter(journal=jcs_journal).order_by('-year', '-volume').first()
    if latest_volume:
        # Get the latest issue for the latest volume
        latest_issue = Issue.objects.filter(volume=latest_volume).order_by('-issue').first()
    
    return render(request, 'subscription_jcs.html',{'journals': journals, 'latest_issue':latest_issue})

def terms_and_conditions(request):
    journals = Journal.objects.all()
    
    jcs_journal = Journal.objects.get(title='JCS') 
    latest_volume = Volume.objects.filter(journal=jcs_journal).order_by('-year', '-volume').first()
    if latest_volume:
        # Get the latest issue for the latest volume
        latest_issue = Issue.objects.filter(volume=latest_volume).order_by('-issue').first()
    
    return render(request, 'terms_and_conditions.html',{'journals': journals, 'latest_issue':latest_issue})
