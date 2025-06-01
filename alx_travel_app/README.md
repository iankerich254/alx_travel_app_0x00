
# alx_travel_app_0x00

A Django-based travel app for managing listings, bookings, and reviews. This project is a duplicate of `alx_travel_app` and includes database modeling, serializers, and sample data seeding.

---

## 📁 Project Structure

alx_travel_app_0x00/
└── alx_travel_app/
├── listings/
│ ├── models.py
│ ├── serializers.py
│ ├── management/
│ │ └── commands/
│ │ └── seed.py
│ └── fixtures/
│ └── sample_users.json
├── db.sqlite3
└── manage.py


---

## 🧱 Models

Defined in `listings/models.py`:

- **Listing**: Represents a travel listing (destination, description, price, etc.)
- **Booking**: Represents a user's booking of a listing
- **Review**: User-generated review and rating of a listing
- **User**: Custom user model (UUID primary key, extended fields)

---

## 🧩 Serializers

Located in `listings/serializers.py`:

- `ListingSerializer`
- `BookingSerializer`

These handle conversion of Django model instances to and from JSON.

---

## 🛠️ Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/alx_travel_app_0x00.git
   cd alx_travel_app_0x00/alx_travel_app

    Set up virtual environment:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Run initial migrations:

python manage.py makemigrations
python manage.py migrate

Create a superuser (optional):

    python manage.py createsuperuser

🌱 Seeding the Database

    Load sample users:

python manage.py loaddata listings/fixtures/sample_users.json

Run seed command to populate sample listings and bookings:

    python manage.py seed

▶️ Running the Server

python manage.py runserver
