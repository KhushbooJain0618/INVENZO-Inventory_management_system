# INVENZO-Inventory_management_system

# 🎞 Inventory Management System

A modular, scalable Inventory Management System using *Flask* for backend logic and *Django* as the frontend interface. This system supports features such as order processing, inventory control, warehouse tracking, user authentication, barcode scanning, and more. It integrates a RESTful API layer for communication between Flask and Django, ensuring a smooth data flow and real-time updates.

---

## 🚀 Tech Stack

| Layer       | Technology                        |
|-------------|------------------------------------|
| Frontend    | Django, HTML5, CSS3, Bootstrap, JS|
| Backend     | Flask, Python 3.x                 |
| Styling     | Bootstrap 5, Custom CSS           |
| Integration | RESTful APIs, POSTMAN             |
| Auth        | Flask Login / Django Auth (as needed) |

---

## 🧩 System Architecture

- *Flask* handles all backend operations, such as processing form submissions, managing inventory, handling orders, and authenticating users.
- *Django* acts as the frontend, fetching data from Flask APIs and rendering it in a user-friendly interface.
- The architecture is decoupled, promoting modularity, scalability, and maintainability.
- All backend routes and APIs are tested using *POSTMAN* for reliability and correctness.


 [ User ] → [ Django Frontend ] → [ Flask API ] → [ Database ]
  

---

## 🔐 Authentication & Roles

- Secure login/signup system.
- Role-based access control (Admin & User).
- Admin users have access to sensitive features like barcode scanning.

---

## 🔑 Key Features

### 1. Order Management
- Create, edit, and track customer orders in real-time.
- Complete order lifecycle support: from creation to fulfillment.

### 2. Inventory Tracking
- Real-time stock visibility.
- Auto-updates on stock changes and low-stock alerts.

### 3. Warehouse Management
- Manage multiple storage locations.
- Track inventory movement between warehouses.

### 4. Barcode Scanning (Admin Only)
- Barcode-based product lookup for speed and accuracy.
- Admin-exclusive access for added security.

### 5. Reports & Analytics
- Generate reports on inventory, orders, and warehouse status.
- Exportable formats: PDF, CSV.

### 6. Login & Signup
- Secure user registration and session handling.
- Password protection and recovery options.

### 7. Customer Feedback
- Capture and display user reviews.
- Helps improve the system based on real input.

### 8. Feature & Pricing Pages
- A complete breakdown of available features.
- Transparent and customizable pricing model.

### 9. Integration Support
- Easily extensible through REST APIs.
- Future-ready for third-party tools like ERPs or payment gateways.

### 10. Solutions
- Tailored use cases for retail, warehouses, and B2B models.
- Adaptable to different organizational structures.

---

## 🔗 API Usage

- All data operations are handled via *Flask REST APIs*.
- APIs follow standard CRUD operations: GET, POST, PUT, DELETE.
- Endpoints include:
  - /api/orders
  - /api/inventory
  - /api/warehouse
  - /api/users

*Tested with POSTMAN* to ensure:
- Valid response formats
- Error handling
- Security and authentication

---

## ⚙ How It Works

1. User interacts with the Django frontend.
2. Django sends requests to the Flask backend through APIs.
3. Flask processes data, updates the database, and returns responses.
4. Django renders the latest data on the interface.

---

## 🧪 Testing & Validation

- Backend endpoints tested with *POSTMAN* for each CRUD action.
- Unit testing (optional but recommended).
- Frontend tested for rendering, form validation, and responsiveness.

---

## 💡 Future Enhancements

- Add user profile management.
- Integrate payment gateways.
- Add role-specific dashboards.
- Generate auto-emails for order confirmations.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📬 Contact

For questions or support, feel free to contact the maintainer:

📧 *khushboo2006june@gmail.com*

---

## 👨‍💼 Contributors

- *Khushboo Jain (Leader)*  
- *Ishleen Kaur*  
- *Gurleen Kaur*  
- *Liza*  

Feel free to fork and star the repository if you find this project useful! ⭐
