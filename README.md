# Catering System (Django Project)

This project is a **Django-based Catering System** that allows users to manage products, place orders, and view their order history. It also features user registration/login and profile management. The frontend is styled using **Tailwind CSS**.

---

## Features

- **User Authentication**: Users can register, log in, and manage their profiles.
- **Admin Panel**: Admins can manage products, view orders, and control the site.
- **Product Catalog**: Users can browse products, add them to the cart, and place orders.
- **Order History**: Users can view their past orders.
- **Responsive Design**: The app uses **Tailwind CSS** for a modern and mobile-responsive UI.
- **Cart Management**: Users can manage the products in their cart (update quantities, remove items).
- **Order Status**: Users can track the status of their orders (pending, delivered, etc.).

---

## Local Installation

To get this project up and running locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/NikHil12907/CateringReservation.git
    ```

2. Navigate to the project folder:

    ```bash
    cd CateringReservation
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
   
    - **Windows**:
      ```bash
      venv\Scripts\activate
      ```
    - **macOS/Linux**:
      ```bash
      source venv/bin/activate
      ```

5. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Set up the database:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser to access the Django admin panel:

    ```bash
    python manage.py createsuperuser
    ```

8. Start the development server:

    ```bash
    python manage.py runserver
    ```

9. Visit the app in your browser at: `http://127.0.0.1:8000/`

10. To Access the Admin Panel go to `http://127.0.0.1:8000/admin`
---

## Technologies Used

- **Django**: Python web framework for backend development.
- **Tailwind CSS**: Utility-first CSS framework for styling.
- **SQLite** (or PostgreSQL): Database for storing user data, products, and orders.

---

## Future Enhancements

- **Payment Gateway**: Integrate a payment system like Stripe or PayPal.
- **Advanced Product Filtering**: Allow users to filter products by categories, price, etc.
- **Email Notifications**: Add email notifications for order confirmation and status updates.
- **Real-time Features**: Implement WebSockets for real-time cart updates.

