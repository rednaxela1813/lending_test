from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import settings
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes



@api_view(["POST"])
@permission_classes([AllowAny])
def contact_form_submission(request):
    """
    Обрабатывает POST-запрос с контактной формы и отправляет email.
    """
    name = request.data.get("name")
    email = request.data.get("email")
    message = request.data.get("message")

    if not name or not email or not message:
        return Response({"error": "All fields are required"}, status=400)

    # Отправляем email на вашу почту
    try:
        send_mail(
            subject=f"New Contact Form Submission from {name}",
            message=f"Name: {name}\nEmail: {email}\nMessage: {message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],  # Ваш email
        )
        return Response({"status": "success", "message": "Email sent successfully"})
    except Exception as e:
        return Response({"error": str(e)}, status=500)
