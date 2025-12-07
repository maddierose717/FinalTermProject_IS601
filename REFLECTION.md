# Final Project Reflection

## What I Made

I added a profile page where users can update their info and change their password.

## The Parts

### Backend
I made 3 new API endpoints:
- GET /users/me - shows your profile
- PUT /users/me - updates your info
- PUT /users/me/password - changes password

The hardest part was making sure when someone changes their username, nobody else already has that username. Same with email.

### Frontend
Made a profile.html page with:
- Shows your current info
- Form to edit your name, email, username
- Form to change password

Just used regular JavaScript. Tried to keep it simple.

### Tests
- Made some basic tests to check if auth works
- Made an E2E test that registers a user, logs in, then checks the profile page
- Tests make sure you can't access the profile without logging in

## Problems I Ran Into

**Passwords**: Had to validate passwords in two places - once on the page with JavaScript, and again on the server with Python. Kind of annoying but I guess it makes sense for security.

**Tokens**: Getting the JWT token to work everywhere was confusing at first. Had to remember to put it in the header for every request.

**Checking duplicates**: When updating username or email, had to check if someone else is using it, but also let the user keep their own current username/email. Took me a while to get that logic right.

## What I Learned

Honestly the whole authentication flow makes a lot more sense now. Before I didn't really get how passwords get hashed, or how tokens work, or why you need them. Now I actually understand it.

Also learned:
- How to use SQLAlchemy for database queries
- Pydantic for validation (pretty useful actually)
- Playwright for testing (still figuring it out)
- Docker compose to run everything together

## What I'd Add

If I had more time:
- Let people upload a profile picture
- Send an email to verify your account
- Password reset if you forget it
- Delete account button
- Maybe show login history

## Final Thoughts

This was probably the biggest project I've done. It was confusing at times but I learned a lot. The profile feature isn't super fancy but it works and people actually need this in real apps.

The CI/CD pipeline is cool too - every time I push code it runs tests and builds a Docker image automatically. Feels pretty professional.
