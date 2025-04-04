from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from django.conf import settings

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        
        if form.is_valid():
            form.save()  # Save message to DB
            
            # Send email
            subject = form.cleaned_data["subject"]
            message = f'Name: {form.cleaned_data["name"]}\nEmail: {form.cleaned_data["email"]}\n\n{form.cleaned_data["message"]}'
            
            try:
                # Sending the email
                send_mail(subject, message, settings.EMAIL_HOST_USER, ["vortexvault.dev@gmail.com"], fail_silently=False)
                
                # If email is successfully sent, show success message
                messages.success(request, "Your message has been sent!")
                return redirect("index")  # Redirect to index after successful submission
                
            except Exception as e:
                # If there is an error while sending email, show error message
                messages.error(request, f"Error sending email: {e}")
                
        else:
            # If form is not valid, print errors for debugging
            print("Form is NOT valid!", form.errors)
            messages.error(request, "Please fix the errors in the form.")

    else:
        form = ContactForm()
    
    # Render the contact form page
    return render(request, "restaurant/contact.html", {"form": form})
