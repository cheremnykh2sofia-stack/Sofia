---
description: "Add authentication system with best practices"
argument-hint: "[method]"
---

Add authentication system with best practices.

**Methods:**
| Method | Description |
|--------|-------------|
| `jwt` | JSON Web Tokens with refresh tokens |
| `oauth2` | OAuth 2.0 with multiple providers |
| `session` | Session-based auth with cookies |
| `firebase` | Firebase Authentication |
| `auth0` | Auth0 integration |
| `passport` | Passport.js strategies |

**Generated Components:**
- Auth module with middleware
- User model with password hashing
- Registration endpoint
- Login/logout endpoints
- Password reset flow
- Token refresh mechanism
- Protected route examples
- Environment variables template

**Example:**
```
/add-auth jwt
/add-auth oauth2
```

Please add authentication using: $ARGUMENTS
