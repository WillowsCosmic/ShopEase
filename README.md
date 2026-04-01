# ShopEase - E-Commerce Platform

A full-stack web-based e-commerce application built with **Python** and the **Django** framework, designed to provide a seamless and user-friendly online shopping experience.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django 4.2 (MVT Architecture)
- **Frontend:** HTML, CSS, Django Templates
- **Database:** SQLite / MySQL (via PyMySQL)
- **IDE:** Visual Studio Code
- **Version Control:** Git & GitHub

---

## 📦 Dependencies

| Package      | Version |
|--------------|---------|
| Django       | 4.2     |
| asgiref      | 3.11.1  |
| Pillow       | 12.1.1  |
| PyMySQL      | 1.1.2   |
| sqlparse     | 0.5.5   |
| tzdata       | 2025.3  |

---

## ✨ Features

- **User Authentication** — Register, login, logout, and session management
- **Product Listing & Categorization** — Browse products by category
- **Search & Filtering** — Search products by name or category
- **Product Detail Page** — View full product descriptions and pricing
- **Shopping Cart** — Add, view, and remove items from the cart
- **Checkout System** — Review order summary and place orders
- **Order History** — View all past orders with details
- **Admin Panel** — Manage products, categories, users, and orders

---

## 🚀 Getting Started

### 1. Clone the repository
```bash  
git clone https://github.com/your-username/shopease.git  
cd shopease  
```

### 2. Create and activate a virtual environment
```bash  
python -m venv ecenv  
source ecenv/bin/activate        # Linux/Mac  
ecenv\Scripts\activate           # Windows  
```


### 3. Apply migrations
```bash  
python manage.py migrate  
```

### 4. Create a superuser (for admin access)
```bash  
python manage.py createsuperuser  
```

### 5. Run the development server
```bash  
python manage.py runserver  
```

Visit `http://127.0.0.1:8000` in your browser.

---

## 📁 Project Structure

```  
ecommerce_project/  
├── ecommerce/          # Main app (models, views, urls)  
├── templates/          # HTML templates  
├── media/              # Uploaded product images  
├── db.sqlite3          # Database (local dev)  
├── manage.py  
└── .gitignore  
```

## Screenshots
<img width="1181" height="649" alt="image" src="https://github.com/user-attachments/assets/e1d75fab-8a37-401b-9642-443289ac8794" />

### DashBoard

<img width="1143" height="563" alt="image" src="https://github.com/user-attachments/assets/f98d7986-adf2-4ab3-8217-eff0357b8328" />

### Product details

<img width="1239" height="552" alt="image" src="https://github.com/user-attachments/assets/4fafb239-6484-4e09-b395-fa6ccf47b855" />

### Checkout 

<img width="1912" height="823" alt="Screenshot from 2026-04-01 21-46-22" src="https://github.com/user-attachments/assets/7ea3dde8-4fbe-4f4f-a668-7799b12c8fff" />

### Django Admin Panel


---

## 🔮 Future Enhancements

- Payment gateway integration
- Product reviews & ratings
- Advanced search with price and popularity filters
- Mobile-responsive design
- Product recommendation system
- Real-time inventory management
- Two-factor authentication & SSL security

---

## 📄 License

This project is for educational purposes.
