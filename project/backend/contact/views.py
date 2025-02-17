import json
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.conf import settings
from rest_framework.permissions import AllowAny

@api_view(["POST"])
@permission_classes([AllowAny])
def contact_form_submission(request):
    """
    Обрабатывает POST-запрос с контактной формы и отправляет email.
    """

    print("\n=== DEBUG: HEADERS ===")
    print(dict(request.headers))  # 👀 Логируем заголовки запроса

    print("\n=== DEBUG: CONTENT TYPE ===")
    print(f"Content-Type: {request.content_type}")  # 👀 Проверяем Content-Type

    print("\n=== DEBUG: RAW REQUEST BODY ===")
    print(request.body.decode("utf-8"))  # 👀 Выводим тело запроса

    # Проверяем, что запрос содержит JSON
    if request.content_type != "application/json":
        print("\n=== ERROR: Неверный Content-Type ===")
        return Response({"error": "Invalid content type, expected application/json"}, status=400)

    # Парсим JSON вручную
    try:
        request_data = request.data  # DRF автоматически парсит JSON
    except Exception as e:
        print("\n=== ERROR: JSON Decode Failed ===")
        print(str(e))
        return Response({"error": "Invalid JSON format"}, status=400)

    print("\n=== DEBUG: PARSED REQUEST DATA ===")
    print(request_data)  # 👀 JSON после парсинга

    # Проверяем наличие всех полей
    name = request_data.get("name")
    email = request_data.get("email")
    message = request_data.get("message")

    if not all([name, email, message]):
        print("\n=== ERROR: Отсутствуют обязательные поля ===")
        return Response({"error": "All fields (name, email, message) are required"}, status=400)

    # Отправляем email
    try:
        send_mail(
            subject=f"Новое сообщение от {name}",
            message=f"Имя: {name}\nEmail: {email}\nСообщение: {message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER],
        )
        return Response({"status": "success", "message": "Email sent successfully"})
    except Exception as e:
        print("\n=== ERROR: EMAIL SENDING FAILED ===")
        print(str(e))
        return Response({"error": str(e)}, status=500)
