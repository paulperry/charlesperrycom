# Email Configuration

The contact and subscription forms are now configured to use Django's proper email system.

## Development Setup

In development mode (`DEBUG=True`), emails are printed to the console instead of being sent.

## Production Setup

### Gmail Setup (Recommended)

1. **Enable 2-Factor Authentication** on your Gmail account
2. **Generate an App Password**:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate a password for "Mail"
   - Use this password, not your regular Gmail password

3. **Set Environment Variables**:
```bash
export EMAIL_HOST_USER="your-email@gmail.com"
export EMAIL_HOST_PASSWORD="your-16-character-app-password"
export DEFAULT_FROM_EMAIL="noreply@charlesperry.com"
```

### Alternative Email Providers

You can use other SMTP providers by setting:
```bash
export EMAIL_HOST="smtp.your-provider.com"
export EMAIL_PORT="587"  # or 465 for SSL
export EMAIL_USE_TLS="true"  # or "false" for SSL
```

### Popular Alternatives:
- **SendGrid**: `smtp.sendgrid.net:587`
- **Mailgun**: `smtp.mailgun.org:587`
- **AWS SES**: `email-smtp.region.amazonaws.com:587`

## Testing

To test the email functionality:

1. Start the development server: `python manage.py runserver`
2. Navigate to `/bio/contact/`
3. Fill out and submit the contact form
4. Check the console output (in development) or your email (in production)

## Security Notes

- Never commit email passwords to version control
- Use environment variables for all sensitive email settings
- Consider using app-specific passwords instead of main account passwords
- In production, monitor email sending logs for any issues