# Django Real-Time Chat App

This guide walks you through setting up and testing the real-time WebSocket chat application.

## Important Note: Authentication

**This application does not have a custom login HTML page.** Users must authenticate through the Django admin interface.

## 1. Prerequisites

```bash
python manage.py makemigrations
python manage.py migrate
```

Ensure your server is running with Daphne (ASGI):

```bash
python manage.py runserver
```

Check the terminal output. It should say: `Starting ASGI/Daphne version X.X.X development server...`

## 2. Create a Superuser

You need to create a superuser account to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password.

## 3. Create Additional Test Users (Optional)

To test 1:1 messaging, you'll need at least two users. You can create additional users through the Django admin panel or via the Django shell.

### Option A: Via Django Admin (Recommended)

1. Start your server: `python manage.py runserver`
2. Go to <http://127.0.0.1:8000/admin/>
3. Login with your superuser credentials
4. Navigate to "Users" section
5. Click "Add user" to create new users

### Option B: Via Django Shell
Stop the server (Ctrl+C) or open a new terminal tab, then:

```bash
python manage.py shell
```

Run the following Python script to create two users:

```python
from django.contrib.auth.models import User

# Create User 1
if not User.objects.filter(username='alice').exists():
    User.objects.create_user('alice', 'alice@example.com', 'password123')
    print("Created user: alice")

# Create User 2
if not User.objects.filter(username='bob').exists():
    User.objects.create_user('bob', 'bob@example.com', 'password123')
    print("Created user: bob")
    
exit()
```

## 4. Browser Setup (The "Two Window" Method)

Since you cannot be logged into two accounts in the same browser tab, you need two separate "contexts."

- **Window A (User 1)**: Open your standard browser (Chrome/Edge/Firefox)
- **Window B (User 2)**: Open an Incognito or Private window

## 5. The Testing Walkthrough

### Step A: Login User 1

1. In Window A, go to <http://127.0.0.1:8000/admin/>
2. Login with your superuser credentials (or a test user if you created one)
3. After logging in, navigate to <http://127.0.0.1:8000/> (the chat inbox)
4. You should see the Inbox page with a list of users

### Step B: Login User 2

1. In Window B (Incognito), go to <http://127.0.0.1:8000/admin/>
2. Login with a different user account
3. Navigate to <http://127.0.0.1:8000/> (the chat inbox)
4. You should see the Inbox page

### Step C: Initiate Chat

1. In Window A (User 1), look at the sidebar under "Users"
2. Click on the username of User 2
3. This creates a Conversation in the database and redirects you to the chat room
4. **Note**: In Window B (User 2), refresh the page. You should now see User 1's name appear under the "Conversations" list. Click it to enter the same room.

### Step D: Test Real-Time Messaging

1. Arrange your windows side-by-side so you can see both simultaneously
2. In Window A (User 1): Type a message and press Enter (or click Send)
   - **Observation 1**: The input field clears immediately
   - **Observation 2**: The message appears in blue on the right side (your messages)
3. In Window B (User 2): Watch the screen closely
   - **Observation**: The message should appear instantly in grey on the left side without refreshing the page

### Step E: Test Persistence (Database Check)

Refresh Window B. The message should still be there. This confirms it was saved to the database and not just sent via WebSocket.

## 6. Troubleshooting Common Issues

### Issue: The message sends but doesn't appear on the other screen

- **Check Console**: Open Developer Tools (F12) in the browser. Look at the "Console" tab. If you see `WebSocket connection to ... failed`, your `asgi.py` or `routing.py` might be misconfigured.
- **Check Terminal**: Look for Python errors. If you see `ValueError: No handler for message type chat_message_html`, your `consumers.py` logic is missing the `chat_message_html` method.

### Issue: "TemplateDoesNotExist"

Ensure your folder structure matches: `chat/templates/chat/partials/message_bubble.html`.

### Issue: Styling looks broken

This project relies on the Tailwind CDN included in `base.html`. Ensure you have an internet connection so the script can load.

### Issue: Cannot access admin panel

Make sure you've created a superuser account using `python manage.py createsuperuser`. You need superuser credentials to access `/admin/`.
