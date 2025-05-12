Healthcare Management System Documentation
Overview
The Healthcare Management System is a desktop application designed to manage patient records, billing information, medical history, and insurance details. The application provides an intuitive interface for healthcare providers and patients to access and manage healthcare-related information.
User Guide
Login

Launch the application
Enter your username and password
Click the "Login" button or press Enter

Dashboard
The dashboard provides an overview of:

Patient information
Recent visits
Upcoming appointments
Billing status
EQUID card details

Navigation
Use the sidebar menu to navigate between different sections:

Home (Dashboard)
Visit History
Billing
Medical Records
Operations

Billing

View billing history
Check payment status
Process new payments
Dispute charges

Medical Records

View medical history
Access lab results
Review prescriptions
Download medical documents

Technical Documentation
Architecture
The application follows a simple MVC-like architecture:

Models: Data structures defined in sample_data.json
Views: Tkinter UI components
Controllers: Logic in the HealthcareApp class

Dependencies

Python 3.14 or higher
Tkinter (built-in)
Pillow (PIL fork)

Directory Structure
healthcare-management-system/
├── src/              # Source code
├── assets/           # Static assets
├── data/             # Data files
└── docs/             # Documentation
Data Model
User data is stored in a JSON structure with the following main components:

User authentication information
Patient details
Medical history
Billing records
Insurance information
EQUID card details

Developer Guide
See CONTRIBUTING.md for information on how to contribute to this project.
