from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .forms import OrderForm, WarehouseMovementForm, BarcodeDataForm  # import form
from .models import Order, WarehouseMovement, BarcodeData      # import models
import random
import string
from django.contrib.auth.decorators import login_required
import requests 


FLASK_API_BASE = "http://localhost:5000/api"

def home(request):
    testimonials_list = [
        {
            "name": "Priya Balna",
            "designation": "Senior Manager - Finance, Rapido Bike - India",
            "feedback": "We have been able to simplify our in-house inventory management with increased efficiency...",
            "image": ""  # You can add image URLs if available
        },
        {
            "name": "Shaji Anandan",
            "designation": "CMO - Promoter, Santhi UK, UK",
            "feedback": "When I thought of starting a new business initiative during the pandemic, I had no time for making business plans...",
            "image": ""
        },
        {
            "name": "Mahesh Kumar K",
            "designation": "Accounts Executive, Arthur's Food Company Pvt. Ltd., India",
            "feedback": "In the past, we tried different software applications for inventory management, but they only made the process more complicated...",
            "image": ""
        },
        {
            "name": "Jason Lee",
            "designation": "General Manager, Party Mojo Pte. Ltd., Singapore",
            "feedback": "We were introduced to Invenzo through Invenzo Books, which we've always used for our accounting needs...",
            "image": ""
        },
        {
            "name": "Atheeque Ahmed",
            "designation": "General Manager, TMM Paper Group, Bahrain",
            "feedback": "Invenzo is a very customizable software. We can make any changes in the app using the automations...",
            "image": ""
        },
        {
            "name": "Samantha Carter",
            "designation": "Head of Operations, GreenTech Solutions, Australia",
            "feedback": "Invenzo has significantly reduced our inventory discrepancies and improved our overall workflow.",
            "image": ""
        },
        {
            "name": "David Johnson",
            "designation": "CEO, Johnson Retail Group, USA",
            "feedback": "Switching to Invenzo was a game-changer for our supply chain management.",
            "image": ""
        },
        {
            "name": "Maria Gonzalez",
            "designation": "Logistics Manager, FreshMart Inc., Spain",
            "feedback": "We've seen a 35% improvement in efficiency since implementing Invenzo's automated inventory tracking.",
            "image": ""
        },
        {
            "name": "Liam O'Connor",
            "designation": "Warehouse Supervisor, Dublin Wholesale, Ireland",
            "feedback": "Managing large-scale stock has never been easier. Invenzo is truly a lifesaver!",
            "image": ""
        },
        {
            "name": "Emily Zhang",
            "designation": "Founder, EZ Beauty Products, China",
            "feedback": "With Invenzo, I can track all my stock across multiple warehouses in real-time!",
            "image": ""
        }
    ]

    return render(request, 'home.html', {'testimonials': testimonials_list})

def features(request):
    return render(request, 'features.html')

def solutions(request):
    return render(request, 'solutions.html')


def process_payment(request: HttpRequest):
    if request.method == "POST":
        plan = request.POST.get("plan")
        payment_method = request.POST.get("payment_method")

        payment_links = {
            "razorpay": "https://razorpay.com/payment-link",  # Replace with actual link
            "stripe": "https://stripe.com/pay",  # Replace with actual link
            "paypal": "https://paypal.com/payment",  # Replace with actual link
            "googlepay": "https://pay.google.com/",  # Replace with actual link
        }

        if payment_method in payment_links:
            return redirect(payment_links[payment_method])

    return redirect("payment")

# Dummy data for plans (You can fetch from the database)
plans_data = [
    {
        'id': 1,
        'name': 'Basic',
        'price': 999,
        'features': ['5 Users', '10GB Storage', 'Email Support'],
        'extras': ['Extra Storage', 'Priority Support']
    },
    {
        'id': 2,
        'name': 'Standard',
        'price': 2999,
        'features': ['50 Users', '100GB Storage', 'Premium Support'],
        'extras': ['Advanced Analytics', 'Custom Branding']
    },
    {
        'id': 3,
        'name': 'Premium',
        'price': 4999,
        'features': ['Unlimited Users', '1TB Storage', 'Dedicated Support'],
        'extras': ['AI Reports', 'Advanced Security']
    }
]

faqs = [
    {'question': 'What is Invenzo?', 'answer': 'Invenzo is an advanced inventory management system.'},
    {'question': 'Can I change my plan later?', 'answer': 'Yes, you can upgrade or downgrade anytime.'},
]

def pricing_page(request):
    return render(request, 'pricing_page.html')

@login_required
def pricing(request):
    """Render the pricing page with available plans"""
    return render(request, 'pricing.html', {'plans': plans_data, 'faqs': faqs})

@login_required
def signup_plan(request, plan_id):
    """Render the signup page for a specific plan"""
    plan = next((p for p in plans_data if p['id'] == plan_id), None)
    if not plan:
        return redirect('pricing')  # Redirect if plan ID is invalid
    return render(request, 'signup2.html', {'plan': plan})

@login_required
def payment(request):
    """Render the payment page"""
    plan_id = request.GET.get('plan')
    plan = next((p for p in plans_data if str(p['id']) == plan_id), None)
    if not plan:
        return redirect('pricing')
    return render(request, 'payment.html', {'plan': plan})


def customers(request):
    customers_list = [
        {
            "name": "Priya Balna",
            "position": "Senior Manager - Finance, Rapido Bike - India",
            "testimonial": "We have been able to simplify our in-house inventory management with increased efficiency..."
        },
        {
            "name": "Shaji Anandan",
            "position": "CMO - Promoter, Santhi UK, UK",
            "testimonial": "When I thought of starting a new business initiative during the pandemic, I had no time for making business plans..."
        },
        {
            "name": "Mahesh Kumar K",
            "position": "Accounts Executive Arthur's Food Company Pvt. Ltd., India",
            "testimonial": "In the past, we tried different software applications for inventory management, but they only made the process more complicated..."
        },
        {
            "name": "Jason Lee",
            "position": "General Manager, Party Mojo Pte. Ltd., Singapore",
            "testimonial": "We were introduced to Invenzo through Invenzo Books, which we've always used for our accounting needs..."
        },
        {
            "name": "Atheeque Ahmed",
            "position": "General Manager, TMM Paper Group, Bahrain",
            "testimonial": "Invenzo is a very customizable software. We can make any changes in the app using the automations..."
        },
        {
            "name": "Samantha Carter",
            "position": "Head of Operations, GreenTech Solutions, Australia",
            "testimonial": "Invenzo has significantly reduced our inventory discrepancies and improved our overall workflow."
        },
        {
            "name": "David Johnson",
            "position": "CEO, Johnson Retail Group, USA",
            "testimonial": "Switching to Invenzo was a game-changer for our supply chain management."
        },
        {
            "name": "Maria Gonzalez",
            "position": "Logistics Manager, FreshMart Inc., Spain",
            "testimonial": "We've seen a 35% improvement in efficiency since implementing Invenzo's automated inventory tracking."
        },
        {
            "name": "Liam O'Connor",
            "position": "Warehouse Supervisor, Dublin Wholesale, Ireland",
            "testimonial": "Managing large-scale stock has never been easier. Invenzo is truly a lifesaver!"
        },
        {
            "name": "Emily Zhang",
            "position": "Founder, EZ Beauty Products, China",
            "testimonial": "With Invenzo, I can track all my stock across multiple warehouses in real-time!"
        },
        {
            "name": "Ahmed Al-Farsi",
            "position": "Procurement Head, Gulf Electronics, UAE",
            "testimonial": "We've minimized stockouts and overstocks thanks to Invenzo's accurate demand forecasting."
        },
        {
            "name": "Jonathan Miller",
            "position": "Supply Chain Director, TechGenius, Canada",
            "testimonial": "Invenzo has transformed how we handle stock, improving our responsiveness to market demand."
        },
        {
            "name": "Fatima Hassan",
            "position": "Owner, Hassan Textiles, Pakistan",
            "testimonial": "Invenzo's intuitive interface makes inventory tracking seamless even for small businesses like ours."
        },
        {
            "name": "Ricardo Fernandes",
            "position": "Operations Lead, SuperMart Brazil, Brazil",
            "testimonial": "The automation features of Invenzo have helped us cut down on manual errors by 50%."
        },
        {
            "name": "Katarina Novak",
            "position": "Inventory Coordinator, EuroAuto Parts, Germany",
            "testimonial": "Managing automotive parts inventory is now effortless thanks to Invenzo’s robust tracking system."
        }
    ]
    return render(request, 'customers.html', {'customers': customers_list})

def integrations(request):
    return render(request, 'integrations.html')


def resources(request):
    resources_list = [
        {"icon": "📖", "title": "Help Documentation", "description": "Gain in-depth knowledge of all the features.", "link": "/help-documentation"},
        {"icon": "❓", "title": "FAQ", "description": "Find answers to common questions.", "link": "/faq"},
        {"icon": "💬", "title": "Forums", "description": "Join discussions and stay updated.", "link": "/forums"},
        {"icon": "📝", "title": "Blogs", "description": "Learn new tips and updates.", "link": "/blogs"},
        {"icon": "📊", "title": "Business Guides", "description": "Manage finances and grow successfully.", "link": "/essential-business-guides"},
        {"icon": "📅", "title": "Webinars", "description": "Join our weekly webinar sessions.", "link": "/webinar"},
    ]
    
    return render(request, 'resources.html', {'resources': resources_list})

# Inventory data
inventory_data = [
    {"name": "Retail Solutions", "url": "/solutions"},
    {"name": "Wholesale Solutions", "url": "/solutions"},
    {"name": "Pricing Plans", "url": "/pricing"},
    {"name": "Customer Stories", "url": "/customers"},
    {"name": "Integrations", "url": "/integrations"},
    {"name": "Resources & Guides", "url": "/resources"},
    {"name": "Our Team", "url": "/team"},
    {"name": "Contact Us", "url": "/contact"},
    {"name": "Webinar Registration", "url": "/webinar-registration"},
    {"name": "Item Grouping", "url": "/item-grouping"},
    {"name": "Multi-Warehouse", "url": "/multi-warehouse"},
    {"name": "Serial Tracking", "url": "/serial-tracking"},
    {"name": "Sales Order", "url": "/sales-order"},
    {"name": "Invoicing", "url": "/invoicing"},
    {"name": "Packing & Shipping", "url": "/packing-shipping"},
    {"name": "Sales Return", "url": "/sales-return"},
    {"name": "Reporting & Analytics", "url": "/reporting-analytics"},
    {"name": "SKU Generator", "url": "/sku-generator"},
    {"name": "Recorder Points", "url": "/recorder-points"},
    {"name": "Package Geometry", "url": "/package-geometry"},
    {"name": "Barcode Scanning", "url": "/barcodes"},
    {"name": "Warehouse Management", "url": "/warehouse-management"},
    {"name": "Inventory Tracking", "url": "/inventory"},
    {"name": "Order Management", "url": "/order_management"},
    {"name": "Cookies", "url": "/cookie_policy"},
    {"name": "Security", "url": "/security"},
    {"name": "Terms of Service", "url": "/terms_of_service"},
    {"name": "Reports", "url": "/reports"},
    {"name": "Privacy Policy", "url": "/privacy_policy"},
    {"name": "Login", "url": "/login"},
    {"name": "Signup", "url": "/signup"},
    {"name": "Explore", "url": "/integrations2"},
]

def search_results(request):
    query = request.GET.get('q', '').strip().lower()  # Get user input from search box

    # Filter inventory data based on the query
    filtered_results = [item for item in inventory_data if query in item["name"].lower()]

    return render(request, 'search_results.html', {'query': query, 'results': filtered_results})


# List of categories
CATEGORIES = [
    "Accessories & Jewelry", "Alcohol & Spirits", "Arts & Crafts Supplies",
    "Automotive Parts", "Baby Products", "Baking Supplies", "Beauty & Personal Care",
    "Beverages & Soft Drinks", "Books & Stationery", "Cleaning & Household Items",
    "Clothing & Apparel", "Computers & Accessories", "Construction Materials",
    "Dairy Products", "Drones & RC Vehicles", "Electrical Components",
    "Electronics", "Event & Party Supplies", "Fitness Equipment",
    "Food & Beverages", "Frozen Foods", "Furniture", "Gaming & Consoles",
    "Gardening Tools & Supplies", "Grocery & Packaged Foods",
    "Health & Wellness", "Home Appliances", "HVAC Equipment",
    "Industrial Equipment", "Kitchen Appliances", "Lighting & Fixtures",
    "Medical Supplies", "Mobile Phones & Tablets", "Music & Instruments",
    "Office Supplies", "Outdoor & Camping Gear", "Pet Supplies",
    "Pharmaceuticals", "Plumbing Supplies", "Safety & Security Equipment",
    "Shoes & Footwear", "Smart Home Devices", "Solar & Renewable Energy",
    "Sports Equipment", "Toys & Games", "Travel & Luggage",
    "Warehouse Equipment"
]
# def generate_random_barcode():
#     return ''.join(random.choices(string.digits, k=12))

@login_required  # Ensure the user is logged in
def order_management(request):
    if request.method == 'POST':
        print("✅ Django: Received POST request from form")
        
        # Get the form data from the request
        item_id = request.POST.get('item_id')
        item_name = request.POST.get('item_name')
        item_category = request.POST.get('item_category')
        
        # Handle possible missing values with defaults or errors
        try:
            quantity = int(request.POST.get('quantity', 0))  # Default to 0 if empty
            cost_per_unit = float(request.POST.get('cost_per_unit', 0.0))  # Default to 0.0 if empty
            total_cost = float(request.POST.get('total_cost', 0.0))  # Default to 0.0 if empty
            user_id = request.user.id  # ✅ Get user_id from logged-in user
        except ValueError as e:
            return render(request, 'order_management.html', {'error': 'Invalid input for numeric fields', 'categories': CATEGORIES})

        supplier_name = request.POST.get('supplier_name')
        supplier_email = request.POST.get('supplier_email')
        supplier_phone = request.POST.get('supplier_phone')
        order_status = request.POST.get('order_status')
        notes = request.POST.get('notes')

        # Prepare the form data to send to Flask API
        formdata = {
            'item_id': item_id,
            'item_name': item_name,
            'item_category': item_category,
            'quantity': quantity,
            'cost_per_unit': cost_per_unit,
            'total_cost': total_cost,
            'supplier_name': supplier_name,
            'supplier_email': supplier_email,
            'supplier_phone': supplier_phone,
            'order_status': order_status,
            'notes': notes,
            'user_id': user_id  # Ensure user_id is added correctly
        }

        # Print the form data to confirm
        print("Form data being sent to Flask API:", formdata)

        # Send the form data to Flask API
        try:
            response = requests.post(f"{FLASK_API_BASE}/order_management", json=formdata)
            print("Response from Flask:", response.status_code, response.text)

            # If Flask API responds successfully, redirect
            if response.status_code == 201:
                return redirect('inventory_tracking')  # Change this to your actual view URL name
            else:
                return render(request, 'order_management.html', {
                    'error': response.text,
                    'categories': CATEGORIES
                })
        except requests.exceptions.RequestException as e:
            # Handle errors if Flask API is unreachable or fails
            return render(request, 'order_management.html', {
                'error': f'Error contacting Flask API: {e}',
                'categories': CATEGORIES
            })

    # GET request (form view)
    return render(request, 'order_management.html', {
        'categories': CATEGORIES
    })




def team(request):
    return render(request, 'team.html')



@login_required
def add_warehouse_movement(request):
    if request.method == "POST":
        data = {
            "product_name": request.POST.get("product_name"),
            "quantity": int(request.POST.get("quantity")),
            "from_location": request.POST.get("from_location"),
            "to_location": request.POST.get("to_location"),
            "date": request.POST.get("date"),
            "time": request.POST.get("time"),
        }

        # Send data to Flask API
        try:
            response = requests.post("http://127.0.0.1:5000/add_movement", json=data)
        except requests.exceptions.RequestException as e:
            print(f"Error posting to Flask API: {e}")

    # Always fetch the latest movements
    movements = []
    try:
        res = requests.get("http://127.0.0.1:5000/get_movements")
        if res.status_code == 200:
            movements = res.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching from Flask API: {e}")

    return render(request, "warehouse_management.html", {"movements": movements})



from django.http import HttpResponseNotAllowed

@login_required
def delete_warehouse_movement(request, movement_id):
    if request.method == "POST":
        try:
            response = requests.delete(f"http://127.0.0.1:5000/delete_movement/{movement_id}")
        except requests.exceptions.RequestException as e:
            print(f"Error deleting from Flask API: {e}")
    else:
        return HttpResponseNotAllowed(['POST'])

    return redirect("warehouse_management")





@login_required
def update_warehouse_movement(request, movement_id):
    if request.method == "POST":
        data = {
            "product_name": request.POST.get("product_name"),
            "quantity": int(request.POST.get("quantity")),
            "from_location": request.POST.get("from_location"),
            "to_location": request.POST.get("to_location"),
            "date": request.POST.get("date"),
            "time": request.POST.get("time"),
        }

        try:
            requests.put(f"http://127.0.0.1:5000/update_movement/{movement_id}", json=data)
        except requests.exceptions.RequestException as e:
            print(f"Error updating Flask API: {e}")

        return redirect("warehouse_management")

    # For GET (pre-filling form)
    movement = {}
    try:
        res = requests.get("http://127.0.0.1:5000/get_movements")
        if res.status_code == 200:
            all_movements = res.json()
            for m in all_movements:
                if m["id"] == movement_id:
                    movement = m
                    break
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for update: {e}")

    return render(request, "update_movement.html", {"movement": movement})


def superuser_check(user):
    return user.is_superuser  # Only allow superusers

@login_required
@user_passes_test(superuser_check, login_url='/error/')  # Only allow superusers
def barcode_scanning(request, item_id):
    try:
        # Send GET request to Flask API to retrieve order details, including barcode
        response = requests.get(f"{FLASK_API_BASE}/api/order_management/{item_id}")
        
        if response.status_code == 200:
            item_data = response.json()  # Parse the JSON response
        else:
            item_data = None
            error_message = "Item not found or error in fetching data."
    except requests.exceptions.RequestException as e:
        item_data = None
        error_message = f"Error contacting Flask API: {e}"

    return render(request, 'barcode_scanning.html', {
        'item_data': item_data,
        'error_message': error_message if 'error_message' in locals() else ''
    })

def error_page(request):
    return render(request, 'error.html', {'message': "You don't have permission to access this page."})

def integrations2(request):
    return render(request, "integrations2.html")




@login_required
def inventory_tracking(request):
    data = []
    error_message = ''  # Initialize error_message

    try:
        # Get data from Flask API
        response = requests.get(f"{FLASK_API_BASE}/inventory")
        
        if response.status_code == 200:
            data = response.json()
        else:
            error_message = f"Failed to fetch data from Flask API. Status Code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        error_message = f"Error contacting Flask API: {e}"

    return render(request, 'inventory_tracking.html', {'data': data, 'error': error_message})


@login_required
def update_inventory(request, item_id):
    item_data = None
    error_message = ''

    # Fetch the existing item data from Flask API
    try:
        response = requests.get(f"{FLASK_API_BASE}/inventory/{item_id}")
        if response.status_code == 200:
            item_data = response.json()
        else:
            error_message = "Item not found"
    except requests.exceptions.RequestException as e:
        error_message = f"Error contacting Flask API: {e}"

    if request.method == 'POST':
        updated_data = {
            'item_id': request.POST.get('item_id'),
            'item_name': request.POST.get('item_name'),
            'item_category': request.POST.get('item_category'),
            'quantity': request.POST.get('quantity'),
            'cost_per_unit': request.POST.get('cost_per_unit'),
            'total_cost': request.POST.get('total_cost'),
            'supplier_name': request.POST.get('supplier_name'),
            'supplier_email': request.POST.get('supplier_email'),
            'supplier_phone': request.POST.get('supplier_phone'),
            'order_status': request.POST.get('order_status'),
            'notes': request.POST.get('notes'),
            'barcode_number': request.POST.get('barcode_number'),
            'user_id': request.user.id
        }

        try:
            update_response = requests.put(f"{FLASK_API_BASE}/order_management/{item_id}", json=updated_data)
            if update_response.status_code == 200:
                return redirect('inventory_tracking')
            else:
                error_message = update_response.json().get('error', 'Error updating item')
        except requests.exceptions.RequestException as e:
            error_message = f"Error contacting Flask API: {e}"

    return render(request, 'update_order.html', {
        'item_data': item_data,
        'error': error_message
    })


@login_required
def delete_inventory(request, item_id):
    try:
        # Send a DELETE request to Flask API
        response = requests.delete(f"{FLASK_API_BASE}/order_management/{item_id}")
        
        # Check the response status from Flask
        if response.status_code == 200:
            return redirect('inventory_tracking')  # Redirect to your inventory tracking page
        else:
            # If there's an error, you can display it to the user
            print(response.text)
            return redirect('inventory_tracking')
    
    except requests.exceptions.RequestException as e:
        # Handle errors if Flask API is unreachable
        print(f"Error deleting item: {e}")
        return redirect('inventory_tracking')



def webinar_registration(request):
    return render(request, 'webinar_registration.html')

def inventory_view(request):
    return render(request, 'inventory.html')

def item_grouping(request):
    return render(request, 'item_grouping.html')

def multi_warehouse(request):
    return render(request, 'multi_warehouse.html')

def webinar_registration(request):
    return render(request, 'webinar-registration.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., send email or store in DB)
            form.save()  # Example, or you can email the content
            return render(request, 'contact-us.html', {'message_sent': True})
    else:
        form = ContactForm()

    return render(request, 'contact-us.html', {'form': form})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful!")
        return redirect('login')
    return render(request, 'register.html')

def help_documentation(request):
    return render(request, 'help-documentation.html')

def faq(request):
    return render(request, 'faq.html')

def forums(request):
    return render(request, 'forums.html')

def blogs(request):
    return render(request, 'blogs.html')

def essential_business_guides(request):
    return render(request, 'essential-business-guides.html')

def webinar(request):
    return render(request, 'webinar.html')

def reach_out_to_us(request):
    return render(request, 'reach-out-to-us.html')

def webinar(request):
    return render(request, 'webinar.html')

def save_webhook(request):
    # Your logic for handling the webhook
    return render({'status': 'success'})

def trigger_custom_function(request):
    # Your logic for triggering the custom function
    return render({'status': 'success'})

def signup_plan(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful!")
        return redirect('login')
    return render(request, 'signup2.html')

def inventory_view(request):
    return render(request, 'inventory_tracking.html') 


def update_warehouse(request):
    return render(request, 'update_warehouse.html')

def payment(request):
    plan = request.GET.get('plan', 'standard')  # Default to 'standard' if no plan is selected
    return render(request, 'payment.html', {'plan': plan})