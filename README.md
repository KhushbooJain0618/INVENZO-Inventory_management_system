# 🧾 INVENZO - Inventory Management System
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&color=000000&width=750&lines=Welcome+to+INVENZO+-+The+Inventory+Management+System!;Modular+%7C+Scalable+%7C+Secure" alt="Typing SVG" />

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Backend-Flask-yellow?logo=flask)
![Django](https://img.shields.io/badge/Frontend-Django-green?logo=django)
![HTML5](https://img.shields.io/badge/Markup-HTML5-orange?logo=html5)
![CSS3](https://img.shields.io/badge/Style-CSS3-blue?logo=css3)
![JavaScript](https://img.shields.io/badge/Scripting-JavaScript-yellow?logo=javascript)
![Bootstrap](https://img.shields.io/badge/UI-Bootstrap_5-purple?logo=bootstrap)
![API](https://img.shields.io/badge/API-RESTful-lightgrey?logo=api)


> **A modular, scalable, and secure Inventory Management System integrating Flask and Django through RESTful APIs. Built for efficiency, extensibility, and real-world use cases.**

---

## 📽️ Overview

**INVENZO** is a feature-rich Inventory Management System that allows businesses to manage orders, stock, warehouses, users, and analytics through a beautifully designed interface. It decouples backend (Flask) and frontend (Django) layers, enabling flexibility and real-time data updates via RESTful APIs.

---

## ⚙️ Tech Stack

| Layer       | Technologies Used                          |
|-------------|--------------------------------------------|
| **Frontend** | Django, HTML5, CSS3, Bootstrap, JavaScript |
| **Backend**  | Flask, Python 3.x                          |
| **Styling**  | Bootstrap 5, Custom CSS                    |
| **Integration** | RESTful APIs, POSTMAN                   |
| **Authentication** | Flask-Login / Django Auth (role-based) |

---

## 🏗️ System Architecture

[ User ]
↓
[ Django Frontend ]
↓ (API Calls)
[ Flask Backend ]
↓
[ Database ]


- **Django** handles UI & routing.
- **Flask** processes logic, database actions, and APIs.
- **POSTMAN** is used for API testing & validation.

---

## 🔐 Authentication & Roles

- ✅ **Secure Sign-up/Login System**
- 🛡️ **Role-Based Access**
  - `Admin`: Full access + barcode scanning
  - `User`: Standard operations

---

## 🌟 Key Features

| Feature                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| 📦 **Order Management**     | Create, edit, track, and fulfill orders in real-time                         |
| 📊 **Inventory Tracking**   | Auto stock updates, low stock alerts, real-time insights                    |
| 🏬 **Warehouse Management** | Track products across multiple storage locations                            |
| 🔍 **Barcode Scanning**     | Admin-only feature for accurate and fast lookups                            |
| 📈 **Reports & Analytics**  | Generate & export reports (PDF/CSV) on inventory, orders, warehouse         |
| 🔐 **Login & Signup**       | Secure auth system with session handling & password recovery                |
| 💬 **Customer Feedback**    | Capture and display real user feedback for continuous improvement           |
| 💡 **Feature & Pricing Pages** | Transparent breakdown of modules, custom pricing options              |
| 🔌 **Integration Ready**    | REST API-first approach, easily integrates with ERP & payment systems       |
| 🧩 **Tailored Solutions**   | Retail, B2B, multi-location—adaptable for any business structure            |

---

## 🔗 API Overview

All API endpoints follow REST principles and support full CRUD operations.

| Resource     | Endpoint Path        |
|--------------|----------------------|
| Orders       | `/api/orders`        |
| Inventory    | `/api/inventory`     |
| Warehouses   | `/api/warehouse`     |
| Users        | `/api/users`         |

✅ All endpoints are tested using **POSTMAN** with proper authentication, error handling, and validations.

---

## 🧪 Testing & Validation

- 🔍 **POSTMAN**: All endpoints tested across CRUD spectrum
- 🧪 **Unit Testing**: Recommended for each module
- 🧱 **Frontend**: Responsive UI, tested across browsers

---

## 🔮 Future Enhancements

- 👤 User profile dashboard
- 💳 Payment gateway integration (Stripe, Razorpay)
- 📊 Role-specific analytics panels
- 📧 Auto-email confirmations for orders

---

🤝 Contributing

We welcome contributions and suggestions!
Please open an issue to discuss your idea before making a PR.

## 📬 Contact Us

For any queries, suggestions, or collaborations, feel free to reach out:

- 📧 **Email**: [khushboo2006june@gmail.com](mailto:khushboo2006june@gmail.com)
- 💼 **LinkedIn**: [linkedin.com/in/khushboo-jain-7003a3301](https://www.linkedin.com/in/khushboo-jain-7003a3301/)
- 📸 **Instagram**: [instagram.com/khushboo_0618](https://instagram.com/khushboo_0618)


| 👤 Name            | 💼 Role         | 🌐 Contact                                |
|--------------------|----------------|-------------------------------------------|
| **Khushboo Jain**  | Project Lead   | [LinkedIn](https://www.linkedin.com/in/khushboo-jain-7003a3301/) |


⭐ Star this repository if you found it useful.
📂 Fork if you’d like to contribute or customize it for your own use!

“Great systems are not born; they’re built — with vision, code, and collaboration.”
