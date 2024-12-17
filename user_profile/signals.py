from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:  # Check if a new user is created
        subject = "Welcome to Our Platform"
        from_email = "habiburrahman191098@gmail.com"  # Replace with your email
        recipient_list = [instance.email]    # Send to the new user's email
        
        # Render email template
        context = {'user': instance}
        html_content = render_to_string('wellcome.html', context)
        text_content = strip_tags(html_content)  # Plain text version for non-HTML clients
        
        # Send the email
        email = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
        email.attach_alternative(html_content, "text/html")  # Attach the HTML version
        email.send()
