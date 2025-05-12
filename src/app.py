#!/usr/bin/env python3
"""
Healthcare Management System
Main application entry point

This script initializes and runs the Healthcare Management System application.
"""

import tkinter as tk
from healthcare_app import HealthcareApp

def main():
    """Initialize and run the Healthcare Management System application"""
    root = tk.Tk()
    app = HealthcareApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
