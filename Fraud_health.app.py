import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import datetime
import os
import json

class HealthcareApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Healthcare Management System")
        self.root.geometry("1000x700")
        self.root.configure(bg="#f0f0f0")
        
        # Set the application icon
        # self.root.iconbitmap("healthcare_icon.ico")  # Uncomment and provide icon path if available
        
        # Initialize user state (not logged in by default)
        self.logged_in = False
        self.current_user = None
        
        # Load sample user data
        self.load_sample_data()
        
        # Start with the login screen
        self.show_login_screen()
    
    def load_sample_data(self):
        """Load sample user and healthcare data"""
        self.users = {
            "patient1": {
                "password": "password123",
                "name": "John Doe",
                "role": "patient",
                "total_visits": 15,
                "operations": 3,
                "last_visit": "2024-03-20",
                "insurance_status": "Active",
                "equid_card": {
                    "number": "XXXX-XXXX-XXXX-1234",
                    "registered_date": "2023-01-01",
                    "most_visited": "Main Hospital",
                    "last_used": "2024-03-20"
                },
                "insurance": {
                    "documents": ["policy.pdf", "coverage_details.pdf"],
                    "provider": "HealthCare Plus",
                    "policy_number": "HC123456789",
                    "coverage": "Comprehensive",
                    "valid_until": "2024-12-31",
                    "deductible": "$1000",
                    "copayment": "$20"
                },
                "billing_history": [
                    {
                        "date": "2024-03-15",
                        "procedure": "General Checkup",
                        "amount": "$150",
                        "status": "paid",
                        "documents": ["invoice.pdf", "insurance_claim.pdf"],
                        "alert": ""
                    },
                    {
                        "date": "2024-03-20",
                        "procedure": "Blood Test",
                        "amount": "$300",
                        "status": "pending",
                        "documents": ["invoice.pdf", "lab_report.pdf"],
                        "alert": "Potential Fraud"
                    }
                ]
            },
            "jashwanth": {
                "password": "jash123",
                "name": "Jashwanth Kumar",
                "role": "patient",
                "total_visits": 8,
                "operations": 1,
                "last_visit": "2024-04-10",
                "insurance_status": "Active",
                "equid_card": {
                    "number": "XXXX-XXXX-XXXX-5678",
                    "registered_date": "2023-02-15",
                    "most_visited": "City Hospital",
                    "last_used": "2024-04-10"
                },
                "insurance": {
                    "documents": ["policy.pdf", "coverage_details.pdf"],
                    "provider": "MediSecure",
                    "policy_number": "MS789456123",
                    "coverage": "Standard",
                    "valid_until": "2024-10-15",
                    "deductible": "$1500",
                    "copayment": "$25"
                },
                "billing_history": [
                    {
                        "date": "2024-04-10",
                        "procedure": "Annual Physical",
                        "amount": "$200",
                        "status": "paid",
                        "documents": ["invoice.pdf", "insurance_claim.pdf"],
                        "alert": ""
                    },
                    {
                        "date": "2024-02-18",
                        "procedure": "Allergy Test",
                        "amount": "$250",
                        "status": "paid",
                        "documents": ["invoice.pdf", "test_results.pdf"],
                        "alert": ""
                    }
                ]
            },
            "suresh": {
                "password": "suresh456",
                "name": "Suresh Reddy",
                "role": "patient",
                "total_visits": 12,
                "operations": 2,
                "last_visit": "2024-03-28",
                "insurance_status": "Active",
                "equid_card": {
                    "number": "XXXX-XXXX-XXXX-9012",
                    "registered_date": "2022-11-20",
                    "most_visited": "General Hospital",
                    "last_used": "2024-03-28"
                },
                "insurance": {
                    "documents": ["policy.pdf", "coverage_details.pdf"],
                    "provider": "HealthGuard",
                    "policy_number": "HG456789012",
                    "coverage": "Premium",
                    "valid_until": "2025-01-20",
                    "deductible": "$500",
                    "copayment": "$15"
                },
                "billing_history": [
                    {
                        "date": "2024-03-28",
                        "procedure": "Cardiology Consultation",
                        "amount": "$350",
                        "status": "pending",
                        "documents": ["invoice.pdf"],
                        "alert": ""
                    },
                    {
                        "date": "2024-01-12",
                        "procedure": "MRI Scan",
                        "amount": "$1200",
                        "status": "paid",
                        "documents": ["invoice.pdf", "insurance_claim.pdf", "scan_report.pdf"],
                        "alert": ""
                    }
                ]
            },
            "naveen": {
                "password": "naveen789",
                "name": "Naveen Singh",
                "role": "patient",
                "total_visits": 6,
                "operations": 0,
                "last_visit": "2024-04-05",
                "insurance_status": "Active",
                "equid_card": {
                    "number": "XXXX-XXXX-XXXX-3456",
                    "registered_date": "2023-05-10",
                    "most_visited": "Community Health Center",
                    "last_used": "2024-04-05"
                },
                "insurance": {
                    "documents": ["policy.pdf", "coverage_details.pdf"],
                    "provider": "InsurePlus",
                    "policy_number": "IP345678901",
                    "coverage": "Basic",
                    "valid_until": "2024-11-10",
                    "deductible": "$2000",
                    "copayment": "$30"
                },
                "billing_history": [
                    {
                        "date": "2024-04-05",
                        "procedure": "Dental Checkup",
                        "amount": "$120",
                        "status": "paid",
                        "documents": ["invoice.pdf", "dental_report.pdf"],
                        "alert": ""
                    },
                    {
                        "date": "2024-02-22",
                        "procedure": "Eye Examination",
                        "amount": "$180",
                        "status": "paid",
                        "documents": ["invoice.pdf", "prescription.pdf"],
                        "alert": ""
                    }
                ]
            },
            "umesh": {
                "password": "umesh123",
                "name": "Umesh Patel",
                "role": "patient",
                "total_visits": 20,
                "operations": 4,
                "last_visit": "2024-04-18",
                "insurance_status": "Active",
                "equid_card": {
                    "number": "XXXX-XXXX-XXXX-7890",
                    "registered_date": "2022-08-15",
                    "most_visited": "Specialty Hospital",
                    "last_used": "2024-04-18"
                },
                "insurance": {
                    "documents": ["policy.pdf", "coverage_details.pdf"],
                    "provider": "MediLife",
                    "policy_number": "ML567890123",
                    "coverage": "Comprehensive Plus",
                    "valid_until": "2025-02-15",
                    "deductible": "$750",
                    "copayment": "$10"
                },
                "billing_history": [
                    {
                        "date": "2024-04-18",
                        "procedure": "Physical Therapy",
                        "amount": "$90",
                        "status": "pending",
                        "documents": ["invoice.pdf"],
                        "alert": ""
                    },
                    {
                        "date": "2024-03-05",
                        "procedure": "Orthopedic Consultation",
                        "amount": "$275",
                        "status": "paid",
                        "documents": ["invoice.pdf", "insurance_claim.pdf"],
                        "alert": ""
                    },
                    {
                        "date": "2024-02-10",
                        "procedure": "X-Ray",
                        "amount": "$320",
                        "status": "paid",
                        "documents": ["invoice.pdf", "xray_report.pdf"],
                        "alert": ""
                    }
                ]
            },
            "teja": {
                "password": "teja456",
                "name": "Teja Krishna",
                "role": "patient",
                "total_visits": 9,
                "operations": 1,
                "last_visit": "2024-04-25",
                "insurance_status": "Active",
                "equid_card": {
                    "number": "XXXX-XXXX-XXXX-1357",
                    "registered_date": "2023-03-20",
                    "most_visited": "Regional Medical Center",
                    "last_used": "2024-04-25"
                },
                "insurance": {
                    "documents": ["policy.pdf", "coverage_details.pdf"],
                    "provider": "CarePlus",
                    "policy_number": "CP678901234",
                    "coverage": "Enhanced",
                    "valid_until": "2024-09-20",
                    "deductible": "$1200",
                    "copayment": "$22"
                },
                "billing_history": [
                    {
                        "date": "2024-04-25",
                        "procedure": "Dermatology Consultation",
                        "amount": "$175",
                        "status": "pending",
                        "documents": ["invoice.pdf"],
                        "alert": ""
                    },
                    {
                        "date": "2024-03-12",
                        "procedure": "Skin Biopsy",
                        "amount": "$450",
                        "status": "paid",
                        "documents": ["invoice.pdf", "insurance_claim.pdf", "lab_report.pdf"],
                        "alert": ""
                    }
                ]
            },
            "admin": {
                "password": "admin123",
                "name": "Admin User",
                "role": "admin"
            }
        }
    
    def show_login_screen(self):
        """Display the login screen"""
        # Clear any existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Login frame
        self.login_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Healthcare logo/title
        title_label = tk.Label(
            self.login_frame, 
            text="Healthcare Management System",
            font=("Arial", 20, "bold"),
            bg="#f0f0f0",
            fg="#2c3e50"
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        # Username
        tk.Label(
            self.login_frame, 
            text="Username:", 
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#2c3e50"
        ).grid(row=1, column=0, sticky="w", pady=10)
        
        self.username_var = tk.StringVar()
        username_entry = tk.Entry(
            self.login_frame, 
            textvariable=self.username_var,
            font=("Arial", 12),
            width=25
        )
        username_entry.grid(row=1, column=1, pady=10, padx=10)
        
        # Password
        tk.Label(
            self.login_frame, 
            text="Password:", 
            font=("Arial", 12),
            bg="#f0f0f0",
            fg="#2c3e50"
        ).grid(row=2, column=0, sticky="w", pady=10)
        
        self.password_var = tk.StringVar()
        password_entry = tk.Entry(
            self.login_frame, 
            textvariable=self.password_var,
            font=("Arial", 12),
            width=25,
            show="*"
        )
        password_entry.grid(row=2, column=1, pady=10, padx=10)
        
        # Login button
        login_button = tk.Button(
            self.login_frame,
            text="Login",
            command=self.login,
            bg="#3498db",
            fg="white",
            font=("Arial", 12),
            width=15,
            relief=tk.RAISED,
            bd=2
        )
        login_button.grid(row=3, column=0, columnspan=2, pady=20)
        
        # Forgot password link
        forgot_password = tk.Label(
            self.login_frame,
            text="Forgot Password?",
            font=("Arial", 10, "underline"),
            bg="#f0f0f0",
            fg="#3498db",
            cursor="hand2"
        )
        forgot_password.grid(row=4, column=0, columnspan=2, pady=5)
        forgot_password.bind("<Button-1>", lambda e: messagebox.showinfo("Reset Password", "Please contact the administrator to reset your password."))
        
        # Set focus on username entry
        username_entry.focus()
        
        # Bind Enter key to login
        self.root.bind("<Return>", lambda event: self.login())
    
    def login(self):
        """Handle login process"""
        username = self.username_var.get()
        password = self.password_var.get()
        
        if username in self.users and self.users[username]["password"] == password:
            self.logged_in = True
            self.current_user = username
            messagebox.showinfo("Login Successful", f"Welcome {self.users[username]['name']}!")
            self.show_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")
    
    def show_dashboard(self):
        """Display the main dashboard after login"""
        # Clear login widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Unbind the return key from login
        self.root.unbind("<Return>")
        
        # Create main application structure
        self.create_top_bar()
        self.create_sidebar()
        self.create_main_content()
    
    def create_top_bar(self):
        """Create the top navigation/header bar"""
        top_bar = tk.Frame(self.root, bg="#2c3e50", height=60)
        top_bar.pack(side=tk.TOP, fill=tk.X)
        
        # App title
        title_label = tk.Label(
            top_bar,
            text="Healthcare Management System",
            font=("Arial", 16, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title_label.pack(side=tk.LEFT, padx=20)
        
        # User info and logout
        user_frame = tk.Frame(top_bar, bg="#2c3e50")
        user_frame.pack(side=tk.RIGHT, padx=20)
        
        user_label = tk.Label(
            user_frame,
            text=f"User: {self.users[self.current_user]['name']}",
            font=("Arial", 12),
            bg="#2c3e50",
            fg="white"
        )
        user_label.pack(side=tk.LEFT, padx=10)
        
        logout_button = tk.Button(
            user_frame,
            text="Logout",
            command=self.logout,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 10),
            padx=10
        )
        logout_button.pack(side=tk.LEFT, padx=5)
    
    def create_sidebar(self):
        """Create the sidebar navigation"""
        sidebar = tk.Frame(self.root, bg="#34495e", width=200)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
        # Make sure sidebar maintains its width
        sidebar.pack_propagate(False)
        
        # Menu items
        menu_items = [
            ("Dashboard", self.show_dashboard_content),
            ("History", self.show_history_content),
            ("Billing History", self.show_billing_content),
            ("Medical History", self.show_medical_content),
            ("Operations History", self.show_operations_content)
        ]
        
        for text, command in menu_items:
            btn = tk.Button(
                sidebar,
                text=text,
                command=command,
                bg="#34495e",
                fg="white",
                font=("Arial", 12),
                bd=0,
                activebackground="#2c3e50",
                activeforeground="white",
                width=20,
                anchor="w",
                padx=10,
                pady=10
            )
            btn.pack(fill=tk.X)
    
    def create_main_content(self):
        """Create the main content area"""
        self.content_frame = tk.Frame(self.root, bg="white")
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Default to dashboard content
        self.show_dashboard_content()
    
    def show_dashboard_content(self):
        """Show the main dashboard content"""
        self.clear_content_frame()
        
        if self.current_user not in self.users or self.users[self.current_user]["role"] != "patient":
            tk.Label(
                self.content_frame,
                text="Admin Dashboard",
                font=("Arial", 16, "bold"),
                bg="white"
            ).pack(pady=20)
            return
        
        # Create dashboard stats section
        stats_frame = tk.Frame(self.content_frame, bg="white")
        stats_frame.pack(fill=tk.X, padx=20, pady=20)
        
        # Stats boxes
        stats_data = [
            ("Total Visits", str(self.users[self.current_user]["total_visits"])),
            ("Operations", str(self.users[self.current_user]["operations"])),
            ("Last Visit", self.users[self.current_user]["last_visit"]),
            ("Insurance Status", self.users[self.current_user]["insurance_status"])
        ]
        
        for i, (label, value) in enumerate(stats_data):
            stat_box = tk.Frame(stats_frame, bg="#ecf0f1", padx=15, pady=15, relief=tk.RAISED, bd=1)
            stat_box.grid(row=0, column=i, padx=10)
            
            tk.Label(
                stat_box,
                text=label,
                font=("Arial", 12, "bold"),
                fg="#7f8c8d",
                bg="#ecf0f1"
            ).pack()
            
            tk.Label(
                stat_box,
                text=value,
                font=("Arial", 16, "bold"),
                fg="#2c3e50",
                bg="#ecf0f1"
            ).pack(pady=5)
        
        # EQUID Card section
        card_frame = tk.LabelFrame(self.content_frame, text="EQUID Card Information", font=("Arial", 12, "bold"), bg="white", padx=15, pady=15)
        card_frame.pack(fill=tk.X, padx=20, pady=10)
        
        card_info = self.users[self.current_user]["equid_card"]
        
        # Card details in two columns
        card_details_frame = tk.Frame(card_frame, bg="white")
        card_details_frame.pack(fill=tk.X)
        
        # Column 1
        col1 = tk.Frame(card_details_frame, bg="white")
        col1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        tk.Label(col1, text="Card Number", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0, sticky="w", pady=2)
        tk.Label(col1, text=card_info["number"], bg="white").grid(row=0, column=1, sticky="w", padx=10, pady=2)
        
        tk.Label(col1, text="Registered Date", font=("Arial", 10, "bold"), bg="white").grid(row=1, column=0, sticky="w", pady=2)
        tk.Label(col1, text=card_info["registered_date"], bg="white").grid(row=1, column=1, sticky="w", padx=10, pady=2)
        
        # Column 2
        col2 = tk.Frame(card_details_frame, bg="white")
        col2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        tk.Label(col2, text="Most Visited", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0, sticky="w", pady=2)
        tk.Label(col2, text=card_info["most_visited"], bg="white").grid(row=0, column=1, sticky="w", padx=10, pady=2)
        
        tk.Label(col2, text="Last Used", font=("Arial", 10, "bold"), bg="white").grid(row=1, column=0, sticky="w", pady=2)
        tk.Label(col2, text=card_info["last_used"], bg="white").grid(row=1, column=1, sticky="w", padx=10, pady=2)
        
        # Insurance Information
        insurance_frame = tk.LabelFrame(self.content_frame, text="Insurance Information", font=("Arial", 12, "bold"), bg="white", padx=15, pady=15)
        insurance_frame.pack(fill=tk.X, padx=20, pady=10)
        
        insurance_info = self.users[self.current_user]["insurance"]
        
        # Document links
        doc_frame = tk.Frame(insurance_frame, bg="white")
        doc_frame.pack(fill=tk.X, pady=5)
        
        for doc in insurance_info["documents"]:
            doc_link = tk.Label(
                doc_frame,
                text=doc,
                font=("Arial", 10, "underline"),
                fg="blue",
                cursor="hand2",
                bg="white"
            )
            doc_link.pack(side=tk.LEFT, padx=5)
            doc_link.bind("<Button-1>", lambda e, doc=doc: self.open_document(doc))
        
        # Insurance details in two columns
        ins_details_frame = tk.Frame(insurance_frame, bg="white")
        ins_details_frame.pack(fill=tk.X, pady=10)
        
        # Column 1
        ins_col1 = tk.Frame(ins_details_frame, bg="white")
        ins_col1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        tk.Label(ins_col1, text="Provider", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0, sticky="w", pady=2)
        tk.Label(ins_col1, text=insurance_info["provider"], bg="white").grid(row=0, column=1, sticky="w", padx=10, pady=2)
        
        tk.Label(ins_col1, text="Policy Number", font=("Arial", 10, "bold"), bg="white").grid(row=1, column=0, sticky="w", pady=2)
        tk.Label(ins_col1, text=insurance_info["policy_number"], bg="white").grid(row=1, column=1, sticky="w", padx=10, pady=2)
        
        tk.Label(ins_col1, text="Coverage", font=("Arial", 10, "bold"), bg="white").grid(row=2, column=0, sticky="w", pady=2)
        tk.Label(ins_col1, text=insurance_info["coverage"], bg="white").grid(row=2, column=1, sticky="w", padx=10, pady=2)
        
        # Column 2
        ins_col2 = tk.Frame(ins_details_frame, bg="white")
        ins_col2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        tk.Label(ins_col2, text="Valid Until", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0, sticky="w", pady=2)
        tk.Label(ins_col2, text=insurance_info["valid_until"], bg="white").grid(row=0, column=1, sticky="w", padx=10, pady=2)
        
        tk.Label(ins_col2, text="Deductible", font=("Arial", 10, "bold"), bg="white").grid(row=1, column=0, sticky="w", pady=2)
        tk.Label(ins_col2, text=insurance_info["deductible"], bg="white").grid(row=1, column=1, sticky="w", padx=10, pady=2)
        
        tk.Label(ins_col2, text="Co-Payment", font=("Arial", 10, "bold"), bg="white").grid(row=2, column=0, sticky="w", pady=2)
        tk.Label(ins_col2, text=insurance_info["copayment"], bg="white").grid(row=2, column=1, sticky="w", padx=10, pady=2)
        
        # Navigation tabs for history sections
        tab_frame = tk.Frame(self.content_frame, bg="white")
        tab_frame.pack(fill=tk.X, padx=20, pady=10)
        
        tabs = [
            ("Dashboard", self.show_dashboard_content),
            ("History", self.show_history_content),
            ("Billing History", self.show_billing_content),
            ("Medical History", self.show_medical_content),
            ("Operations History", self.show_operations_content)
        ]
        
        for text, command in tabs:
            tab_btn = tk.Button(
                tab_frame,
                text=text,
                command=command,
                font=("Arial", 10),
                bd=0,
                padx=10,
                pady=5,
                bg="#ecf0f1" if text != "Dashboard" else "#3498db",
                fg="#2c3e50" if text != "Dashboard" else "white",
            )
            tab_btn.pack(side=tk.LEFT, padx=2)
        
        # Billing History Preview Section
        billing_frame = tk.LabelFrame(self.content_frame, text="Billing History", font=("Arial", 12, "bold"), bg="white", padx=15, pady=15)
        billing_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Create table for billing history
        billing_table = ttk.Treeview(billing_frame, columns=("date", "procedure", "amount", "status", "documents", "alert"), show="headings")
        
        # Define column headings
        billing_table.heading("date", text="Date")
        billing_table.heading("procedure", text="Procedure")
        billing_table.heading("amount", text="Amount")
        billing_table.heading("status", text="Status")
        billing_table.heading("documents", text="Documents")
        billing_table.heading("alert", text="Alert")
        
        # Set column widths
        billing_table.column("date", width=100)
        billing_table.column("procedure", width=150)
        billing_table.column("amount", width=80)
        billing_table.column("status", width=80)
        billing_table.column("documents", width=200)
        billing_table.column("alert", width=120)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(billing_frame, orient=tk.VERTICAL, command=billing_table.yview)
        billing_table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        billing_table.pack(fill=tk.BOTH, expand=True)
        
        # Insert billing history data
        for bill in self.users[self.current_user]["billing_history"]:
            documents = ", ".join(bill["documents"])
            billing_table.insert("", tk.END, values=(
                bill["date"],
                bill["procedure"],
                bill["amount"],
                bill["status"],
                documents,
                bill["alert"]
            ))
        
        # Apply custom style to table rows
        for i, bill in enumerate(self.users[self.current_user]["billing_history"]):
            item_id = billing_table.get_children()[i]
            if bill["status"] == "paid":
                billing_table.tag_configure("paid", background="#e8f8f5")
                billing_table.item(item_id, tags=("paid",))
            elif bill["alert"] == "Potential Fraud":
                billing_table.tag_configure("alert", background="#fadbd8")
                billing_table.item(item_id, tags=("alert",))
    
    def show_history_content(self):
        """Show patient visit history"""
        self.clear_content_frame()
        
        tk.Label(
            self.content_frame,
            text="Visit History",
            font=("Arial", 16, "bold"),
            bg="white"
        ).pack(pady=20)
        
        # This would be populated with actual visit history data
        # For demo purposes, we're just showing a placeholder
        history_frame = tk.Frame(self.content_frame, bg="white")
        history_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Create a treeview for visit history
        columns = ("date", "doctor", "department", "notes", "documents")
        history_table = ttk.Treeview(history_frame, columns=columns, show="headings")
        
        # Set column headings
        history_table.heading("date", text="Date")
        history_table.heading("doctor", text="Doctor")
        history_table.heading("department", text="Department")
        history_table.heading("notes", text="Notes")
        history_table.heading("documents", text="Documents")
        
        # Set column widths
        for col in columns:
            history_table.column(col, width=150)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(history_frame, orient=tk.VERTICAL, command=history_table.yview)
        history_table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        history_table.pack(fill=tk.BOTH, expand=True)
        
        # Sample data
        sample_visits = [
            ("2024-03-20", "Dr. Smith", "Cardiology", "Regular checkup", "report.pdf"),
            ("2024-02-15", "Dr. Johnson", "General Medicine", "Flu symptoms", "prescription.pdf"),
            ("2024-01-10", "Dr. Williams", "Orthopedics", "Ankle pain", "xray.pdf, notes.pdf"),
            ("2023-12-05", "Dr. Brown", "Dermatology", "Skin rash", "treatment.pdf"),
            ("2023-11-20", "Dr. Davis", "Neurology", "Headache evaluation", "mri.pdf"),
        ]
        
        # Insert sample data
        for visit in sample_visits:
            history_table.insert("", tk.END, values=visit)
    
    def show_billing_content(self):
        """Show billing history in detail"""
        self.clear_content_frame()
        
        tk.Label(
            self.content_frame,
            text="Billing History",
            font=("Arial", 16, "bold"),
            bg="white"
        ).pack(pady=20)
        
        if self.current_user not in self.users or self.users[self.current_user]["role"] != "patient":
            tk.Label(
                self.content_frame,
                text="No billing data available",
                font=("Arial", 12),
                bg="white"
            ).pack(pady=20)
            return
        
        # Billing history frame
        billing_frame = tk.Frame(self.content_frame, bg="white")
        billing_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Create filters at the top
        filter_frame = tk.Frame(billing_frame, bg="white", pady=10)
        filter_frame.pack(fill=tk.X)
        
        tk.Label(filter_frame, text="Filter by:", font=("Arial", 10), bg="white").pack(side=tk.LEFT, padx=5)
        
        status_var = tk.StringVar(value="All")
        status_filter = ttk.Combobox(filter_frame, textvariable=status_var, values=["All", "Paid", "Pending"], width=10)
        status_filter.pack(side=tk.LEFT, padx=5)
        
        tk.Label(filter_frame, text="Date range:", font=("Arial", 10), bg="white").pack(side=tk.LEFT, padx=5)
        
        from_date = tk.Entry(filter_frame, width=10)
        from_date.pack(side=tk.LEFT, padx=2)
        from_date.insert(0, "YYYY-MM-DD")
        
        tk.Label(filter_frame, text="to", font=("Arial", 10), bg="white").pack(side=tk.LEFT)
        
        to_date = tk.Entry(filter_frame, width=10)
        to_date.pack(side=tk.LEFT, padx=2)
        to_date.insert(0, "YYYY-MM-DD")
        
        filter_btn = tk.Button(filter_frame, text="Apply Filter", bg="#3498db", fg="white", padx=10)
        filter_btn.pack(side=tk.LEFT, padx=10)
        
        export_btn = tk.Button(filter_frame, text="Export CSV", bg="#2ecc71", fg="white", padx=10)
        export_btn.pack(side=tk.RIGHT, padx=10)
        
        # Create table for billing history
        columns = ("date", "procedure", "amount", "status", "documents", "alert")
        billing_table = ttk.Treeview(billing_frame, columns=columns, show="headings")
        
        # Define column headings
        billing_table.heading("date", text="Date")
        billing_table.heading("procedure", text="Procedure")
        billing_table.heading("amount", text="Amount")
        billing_table.heading("status", text="Status")
        billing_table.heading("documents", text="Documents")
        billing_table.heading("alert", text="Alert")
        
        # Set column widths
        billing_table.column("date", width=100)
        billing_table.column("procedure", width=150)
        billing_table.column("amount", width=80)
        billing_table.column("status", width=80)
        billing_table.column("documents", width=200)
        billing_table.column("alert", width=120)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(billing_frame, orient=tk.VERTICAL, command=billing_table.yview)
        billing_table.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        billing_table.pack(fill=tk.BOTH, expand=True)
        
        # Insert billing history data
        for bill in self.users[self.current_user]["billing_history"]:
            documents = ", ".join(bill["documents"])
            billing_table.insert("", tk.END, values=(
                bill["date"],
                bill["procedure"],
                bill["amount"],
                bill["status"],
                documents,
                bill["alert"]
            ))
        
        # Apply custom style to table rows
        for i, bill in enumerate(self.users[self.current_user]["billing_history"]):
            item_id = billing_table.get_children()[i]
            if bill["status"] == "paid":
                billing_table.tag_configure("paid", background="#e8f8f5")
                billing_table.item(item_id, tags=("paid",))
            elif bill["alert"] == "Potential Fraud":
                billing_table.tag_configure("alert", background="#fadbd8")
                billing_table.item(item_id, tags=("alert",))
        
        # Add detail view frame
        detail_frame = tk.LabelFrame(billing_frame, text="Transaction Details", font=("Arial", 12, "bold"), bg="white", padx=15, pady=15)
        detail_frame.pack(fill=tk.X, pady=10)
        
        # This would be populated when a row is selected
        # For now, let's add some placeholder content
        tk.Label(detail_frame, text="Select a transaction to view details", bg="white").pack(pady=10)
        
        # Define what happens when a row is selected
        def on_row_select(event):
            selected = billing_table.focus()
            if selected:
                values = billing_table.item(selected, "values")
                for widget in detail_frame.winfo_children():
                    widget.destroy()
                
                # Create details grid
                details_grid = tk.Frame(detail_frame, bg="white")
                details_grid.pack(fill=tk.X)
                
                # Column 1 - Transaction details
                col1 = tk.Frame(details_grid, bg="white")
                col1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
                
                tk.Label(col1, text="Date:", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0, sticky="w", pady=2)
                tk.Label(col1, text=values[0], bg="white").grid(row=0, column=1, sticky="w", padx=10, pady=2)
                
                tk.Label(col1, text="Procedure:", font=("Arial", 10, "bold"), bg="white").grid(row=1, column=0, sticky="w", pady=2)
                tk.Label(col1, text=values[1], bg="white").grid(row=1, column=1, sticky="w", padx=10, pady=2)
                
                tk.Label(col1, text="Amount:", font=("Arial", 10, "bold"), bg="white").grid(row=2, column=0, sticky="w", pady=2)
                tk.Label(col1, text=values[2], bg="white").grid(row=2, column=1, sticky="w", padx=10, pady=2)
                
                # Column 2 - Insurance details
                col2 = tk.Frame(details_grid, bg="white")
                col2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
                
                tk.Label(col2, text="Status:", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0, sticky="w", pady=2)
                status_label = tk.Label(col2, text=values[3], bg="white")
                status_label.grid(row=0, column=1, sticky="w", padx=10, pady=2)
                if values[3] == "paid":
                    status_label.config(fg="#27ae60")
                else:
                    status_label.config(fg="#e74c3c")
                
                tk.Label(col2, text="Documents:", font=("Arial", 10, "bold"), bg="white").grid(row=1, column=0, sticky="w", pady=2)
                
                # Create clickable document links
                docs_frame = tk.Frame(col2, bg="white")
                docs_frame.grid(row=1, column=1, sticky="w", padx=10, pady=2)
                
                for i, doc in enumerate(values[4].split(", ")):
                    doc_link = tk.Label(
                        docs_frame,
                        text=doc,
                        font=("Arial", 10, "underline"),
                        fg="blue",
                        cursor="hand2",
                        bg="white"
                    )
                    doc_link.pack(side=tk.LEFT, padx=5)
                    doc_link.bind("<Button-1>", lambda e, doc=doc: self.open_document(doc))
                
                # Alert section if applicable
                if values[5]:
                    alert_frame = tk.Frame(detail_frame, bg="#fdedec", bd=1, relief=tk.SOLID)
                    alert_frame.pack(fill=tk.X, pady=10)
                    
                    tk.Label(
                        alert_frame,
                        text=f"Alert: {values[5]}",
                        font=("Arial", 10, "bold"),
                        fg="#c0392b",
                        bg="#fdedec",
                        padx=10,
                        pady=5
                    ).pack(fill=tk.X)
                
                # Action buttons
                btn_frame = tk.Frame(detail_frame, bg="white")
                btn_frame.pack(fill=tk.X, pady=10)
                
                tk.Button(
                    btn_frame,
                    text="Print Receipt",
                    bg="#3498db",
                    fg="white",
                    padx=10,
                    pady=5
                ).pack(side=tk.LEFT, padx=5)
                
                if values[3] == "pending":
                    tk.Button(
                        btn_frame,
                        text="Pay Now",
                        bg="#27ae60",
                        fg="white",
                        padx=10,
                        pady=5
                    ).pack(side=tk.LEFT, padx=5)
                
                tk.Button(
                    btn_frame,
                    text="Dispute",
                    bg="#e74c3c",
                    fg="white",
                    padx=10,
                    pady=5
                ).pack(side=tk.LEFT, padx=5)
                
                tk.Button(
                    btn_frame,
                    text="Contact Support",
                    bg="#95a5a6",
                    fg="white",
                    padx=10,
                    pady=5
                ).pack(side=tk.RIGHT, padx=5)
        
        # Bind the function to the table
        billing_table.bind("<<TreeviewSelect>>", on_row_select)
    
    def show_medical_content(self):
        """Show medical history"""
        self.clear_content_frame()
        
        tk.Label(
            self.content_frame,
            text="Medical History",
            font=("Arial", 16, "bold"),
            bg="white"
        ).pack(pady=20)
        
        # In a real application, this would show medical history data
        # For the demo, we're showing a placeholder
        
        # Create tabs for different types of medical info
        notebook = ttk.Notebook(self.content_frame)
        notebook.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Diagnoses tab
        diagnoses_frame = tk.Frame(notebook, bg="white")
        notebook.add(diagnoses_frame, text="Diagnoses")
        
        # Medications tab
        medications_frame = tk.Frame(notebook, bg="white")
        notebook.add(medications_frame, text="Medications")
        
        # Allergies tab
        allergies_frame = tk.Frame(notebook, bg="white")
        notebook.add(allergies_frame, text="Allergies")
        
        # Lab Results tab
        lab_frame = tk.Frame(notebook, bg="white")
        notebook.add(lab_frame, text="Lab Results")
        
        # Add sample data to diagnoses tab
        diagnoses_table = ttk.Treeview(diagnoses_frame, columns=("date", "diagnosis", "doctor", "notes"), show="headings")
        diagnoses_table.heading("date", text="Date")
        diagnoses_table.heading("diagnosis", text="Diagnosis")
        diagnoses_table.heading("doctor", text="Doctor")
        diagnoses_table.heading("notes", text="Notes")
        
        for col in diagnoses_table["columns"]:
            diagnoses_table.column(col, width=150)
        
        sample_diagnoses = [
            ("2024-01-15", "Hypertension", "Dr. Smith", "Prescribed medication and lifestyle changes"),
            ("2023-10-22", "Seasonal Allergies", "Dr. Johnson", "Recommended antihistamines"),
            ("2023-08-05", "Sprained Ankle", "Dr. Williams", "Rest and ice recommended")
        ]
        
        for diag in sample_diagnoses:
            diagnoses_table.insert("", tk.END, values=diag)
        
        # Add scrollbar
        diag_scrollbar = ttk.Scrollbar(diagnoses_frame, orient=tk.VERTICAL, command=diagnoses_table.yview)
        diagnoses_table.configure(yscroll=diag_scrollbar.set)
        diag_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        diagnoses_table.pack(fill=tk.BOTH, expand=True)
        
        # Add sample data to medications tab
        med_table = ttk.Treeview(medications_frame, columns=("medication", "dosage", "frequency", "start_date", "end_date"), show="headings")
        med_table.heading("medication", text="Medication")
        med_table.heading("dosage", text="Dosage")
        med_table.heading("frequency", text="Frequency")
        med_table.heading("start_date", text="Start Date")
        med_table.heading("end_date", text="End Date")
        
        for col in med_table["columns"]:
            med_table.column(col, width=120)
        
        sample_meds = [
            ("Lisinopril", "10mg", "Once daily", "2024-01-15", "Ongoing"),
            ("Cetirizine", "5mg", "As needed", "2023-10-22", "Ongoing"),
            ("Ibuprofen", "400mg", "Every 6 hours", "2023-08-05", "2023-08-15")
        ]
        
        for med in sample_meds:
            med_table.insert("", tk.END, values=med)
        
        # Add scrollbar
        med_scrollbar = ttk.Scrollbar(medications_frame, orient=tk.VERTICAL, command=med_table.yview)
        med_table.configure(yscroll=med_scrollbar.set)
        med_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        med_table.pack(fill=tk.BOTH, expand=True)
    
    def show_operations_content(self):
        """Show operations history"""
        self.clear_content_frame()
        
        tk.Label(
            self.content_frame,
            text="Operations History",
            font=("Arial", 16, "bold"),
            bg="white"
        ).pack(pady=20)
        
        # In a real application, this would show operations history data
        # For the demo, we're showing a placeholder
        
        operations_frame = tk.Frame(self.content_frame, bg="white")
        operations_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Create table for operations history
        op_table = ttk.Treeview(
            operations_frame, 
            columns=("date", "procedure", "surgeon", "hospital", "outcome", "documents"), 
            show="headings"
        )
        
        # Define column headings
        op_table.heading("date", text="Date")
        op_table.heading("procedure", text="Procedure")
        op_table.heading("surgeon", text="Surgeon")
        op_table.heading("hospital", text="Hospital")
        op_table.heading("outcome", text="Outcome")
        op_table.heading("documents", text="Documents")
        
        # Set column widths
        for col in op_table["columns"]:
            op_table.column(col, width=100)
        
        # Add scrollbar
        op_scrollbar = ttk.Scrollbar(operations_frame, orient=tk.VERTICAL, command=op_table.yview)
        op_table.configure(yscroll=op_scrollbar.set)
        op_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        op_table.pack(fill=tk.BOTH, expand=True)
        
        # Sample operations data
        sample_ops = [
            ("2023-05-10", "Appendectomy", "Dr. Roberts", "Main Hospital", "Successful", "op_report.pdf"),
            ("2022-11-22", "Knee Arthroscopy", "Dr. Thompson", "Sports Medicine Center", "Successful", "arthroscopy.pdf"),
            ("2021-08-15", "Tonsillectomy", "Dr. Garcia", "ENT Specialists", "Successful", "discharge.pdf")
        ]
        
        # Insert sample data
        for op in sample_ops:
            op_table.insert("", tk.END, values=op)
        
        # Add detail section
        detail_op_frame = tk.LabelFrame(operations_frame, text="Operation Details", font=("Arial", 12, "bold"), bg="white", padx=15, pady=15)
        detail_op_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(detail_op_frame, text="Select an operation to view details", bg="white").pack(pady=10)
        
        # Define what happens when a row is selected
        def on_op_select(event):
            selected = op_table.focus()
            if selected:
                values = op_table.item(selected, "values")
                
                for widget in detail_op_frame.winfo_children():
                    widget.destroy()
                
                # Create details grid with two columns
                details_grid = tk.Frame(detail_op_frame, bg="white")
                details_grid.pack(fill=tk.X)
                
                # Left column
                left_col = tk.Frame(details_grid, bg="white")
                left_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
                
                tk.Label(left_col, text="Date:", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0, sticky="w", pady=2)
                tk.Label(left_col, text=values[0], bg="white").grid(row=0, column=1, sticky="w", padx=10, pady=2)
                
                tk.Label(left_col, text="Procedure:", font=("Arial", 10, "bold"), bg="white").grid(row=1, column=0, sticky="w", pady=2)
                tk.Label(left_col, text=values[1], bg="white").grid(row=1, column=1, sticky="w", padx=10, pady=2)
                
                tk.Label(left_col, text="Surgeon:", font=("Arial", 10, "bold"), bg="white").grid(row=2, column=0, sticky="w", pady=2)
                tk.Label(left_col, text=values[2], bg="white").grid(row=2, column=1, sticky="w", padx=10, pady=2)
                
                # Right column
                right_col = tk.Frame(details_grid, bg="white")
                right_col.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
                
                tk.Label(right_col, text="Hospital:", font=("Arial", 10, "bold"), bg="white").grid(row=0, column=0, sticky="w", pady=2)
                tk.Label(right_col, text=values[3], bg="white").grid(row=0, column=1, sticky="w", padx=10, pady=2)
                
                tk.Label(right_col, text="Outcome:", font=("Arial", 10, "bold"), bg="white").grid(row=1, column=0, sticky="w", pady=2)
                tk.Label(right_col, text=values[4], bg="white").grid(row=1, column=1, sticky="w", padx=10, pady=2)
                
                tk.Label(right_col, text="Documents:", font=("Arial", 10, "bold"), bg="white").grid(row=2, column=0, sticky="w", pady=2)
                
                # Create clickable document link
                doc_link = tk.Label(
                    right_col,
                    text=values[5],
                    font=("Arial", 10, "underline"),
                    fg="blue",
                    cursor="hand2",
                    bg="white"
                )
                doc_link.grid(row=2, column=1, sticky="w", padx=10, pady=2)
                doc_link.bind("<Button-1>", lambda e, doc=values[5]: self.open_document(doc))
                
                # Additional notes section
                notes_frame = tk.LabelFrame(detail_op_frame, text="Notes", font=("Arial", 10, "bold"), bg="white", padx=10, pady=10)
                notes_frame.pack(fill=tk.X, pady=10)
                
                # Sample notes based on the procedure
                sample_notes = {
                    "Appendectomy": "Emergency procedure performed due to acute appendicitis. Patient recovered well with no complications.",
                    "Knee Arthroscopy": "Arthroscopic procedure to repair torn meniscus. Physical therapy recommended for 8 weeks post-operation.",
                    "Tonsillectomy": "Standard procedure with normal recovery. Patient advised to avoid solid foods for 10 days."
                }
                
                notes_text = sample_notes.get(values[1], "No additional notes available.")
                
                tk.Label(notes_frame, text=notes_text, bg="white", justify=tk.LEFT, wraplength=600).pack(fill=tk.X)
                
                # Follow-up information
                followup_frame = tk.LabelFrame(detail_op_frame, text="Follow-up", font=("Arial", 10, "bold"), bg="white", padx=10, pady=10)
                followup_frame.pack(fill=tk.X, pady=10)
                
                # Sample follow-up information
                if values[1] == "Appendectomy":
                    followup_date = "2023-05-25"
                    followup_doctor = "Dr. Roberts"
                elif values[1] == "Knee Arthroscopy":
                    followup_date = "2022-12-10"
                    followup_doctor = "Dr. Thompson"
                else:
                    followup_date = "2021-08-30"
                    followup_doctor = "Dr. Garcia"
                
                tk.Label(followup_frame, text=f"Follow-up Date: {followup_date}", bg="white").pack(anchor="w")
                tk.Label(followup_frame, text=f"Doctor: {followup_doctor}", bg="white").pack(anchor="w")
                
                # Action buttons
                btn_frame = tk.Frame(detail_op_frame, bg="white")
                btn_frame.pack(fill=tk.X, pady=10)
                
                tk.Button(
                    btn_frame,
                    text="View Documents",
                    bg="#3498db",
                    fg="white",
                    padx=10,
                    pady=5
                ).pack(side=tk.LEFT, padx=5)
                
                tk.Button(
                    btn_frame,
                    text="Schedule Follow-up",
                    bg="#27ae60",
                    fg="white",
                    padx=10,
                    pady=5
                ).pack(side=tk.LEFT, padx=5)
                
                tk.Button(
                    btn_frame,
                    text="Request Information",
                    bg="#95a5a6",
                    fg="white",
                    padx=10,
                    pady=5
                ).pack(side=tk.RIGHT, padx=5)
        
        # Bind the function to the table
        op_table.bind("<<TreeviewSelect>>", on_op_select)
    
    def clear_content_frame(self):
        """Clear all widgets from the content frame"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def open_document(self, doc_name):
        """Handle document opening functionality"""
        messagebox.showinfo("Document Viewer", f"Opening {doc_name}...\n\nThis is a placeholder for document viewing functionality.")
    
    def logout(self):
        """Handle logout functionality"""
        self.logged_in = False
        self.current_user = None
        messagebox.showinfo("Logout", "You have been logged out successfully.")
        self.show_login_screen()

if __name__ == "__main__":
    root = tk.Tk()
    app = HealthcareApp(root)
    root.mainloop()
