# Target Observation Report

**Target:** https://owasp-juice.shop  
**Method:** Passive observation (browser interaction only, no exploitation)

![target-home-page](juice-shop-front.png)

---

## 1. Purpose of the Website 

From the visual layout and available functionality, the website appears to be an **e-commerce application**.

### Features
- Product listings with images and prices  
- Add-to-basket / shopping cart functionality  
- Search bar for products  
- User account-related actions (login / register)

The site simulates an online shopping platform, likely used for testing or demonstration rather than real commercial transactions.

---

## 2. Login Page

**Yes, a login page is present**

- A **“Login”** option is visible in the user interface  
- Clicking the option opens a login form requesting user credentials
 
Authentication is handled through a web form and is likely backed by an API on the server side.

![juice-shop-login](juice-shop-login.png)

---

## 3. Admin Panel Visibility

**No admin panel is directly visible**

### Observations
- No obvious `/admin` link observed  
- No visible admin dashboard option in the navigation menu
- Administrative functionality likely exists but is hidden or access-restricted  
- Admin pages may be accessible only after authentication or through undisclosed routes

---

## 4. Technologies Used 

Based on UI behavior, page loading patterns, and general application structure:

### Frontend
- Single Page Application (SPA) behavior  
- Dynamic page loading without full reloads  
- Likely framework: **Angular / React / Vue**  
- Angular is a stronger guess due to routing style

### Backend 
- API-driven backend returning JSON responses  
- Likely **Node.js** or a similar JavaScript runtime  
- REST-style endpoints

### Database 
- Some form of relational or lightweight database  
- Possibly **SQLite** or **MySQL**

### Other observations
- Uses modern browser-side JavaScript  
- Client-side validation is present  
- Likely session-based or token-based authentication

---

## 5. Pages / Routes Observed

Based on navigation elements and URL behavior (SPA routing):

/#/login
/#/register
/#/search
/#/basket
/#/about
/#/contact
/#/profile
/#/logout

### Notes
- Routes use hash (`#`) notation, indicating client-side routing  
- Pages load dynamically without full page refresh  
- URLs appear user-facing rather than backend API endpoints

---

## Conclusion

The target web application appears to be a modern, SPA-based e-commerce platform with user authentication, shopping functionality, and API-driven interactions. No administrative interfaces were directly visible during passive observation.