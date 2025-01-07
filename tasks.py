from celery import shared_task

@shared_task
def send_notification_email():
    # Logic to send notification email
    return "Email Sent"
