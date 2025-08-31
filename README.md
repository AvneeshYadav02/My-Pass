MyPass: A Simple Password Manager

MyPass is a lightweight and user-friendly password manager built with Python's tkinter library. It provides a simple, secure way to manage your login credentials. You can generate strong, random passwords, save them along with their associated websites and emails, and easily retrieve them when you need them.

Features

    Password Generation: Automatically creates strong, random passwords for you.

    Secure Storage: Saves your credentials in a data.json file.

    Search Functionality: Quickly find saved passwords for a specific website.

    User-Friendly Interface: A clean, intuitive graphical user interface (GUI).

Installation

To run this project, you'll need Python installed on your system.

    Clone the repository (if it's on a platform like GitHub) or download the files.

    Navigate to the project directory in your terminal.

    Run the script:
    Bash

    python main.py

Usage

    Enter Website and Email: Type the website name and your associated email in the respective fields.

    Generate a Password: Click the "Generate Password" button to create a new, random password.

    Save Credentials: Click the "Add" button to save your website, email, and password. The data will be saved to a data.json file.

    Search for Credentials: To retrieve a saved password, simply type the website name and click "Search". A pop-up will display the saved email and password.

Dependencies

This project uses standard Python libraries, so no additional installations should be necessary.

    tkinter (for the GUI)

    json (for saving and loading data)

    random (for password generation)

License

This project is open-source. Please feel free to use and modify the code as you wish.
