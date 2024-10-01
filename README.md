# Password Manager 🔐

A simple **Password Manager** built using Python's **Tkinter** for the GUI, and **JSON** for data storage. This app allows users to generate random passwords, save them, and retrieve them when needed.

## Features

- **Generate Random Passwords**: Create strong, secure passwords with a mix of letters, symbols, and numbers.
- **Save Passwords**: Store your passwords along with the website name and email/username.
- **Search Passwords**: Retrieve saved passwords by entering the website name.
- **Data Persistence**: All passwords are stored in a `data.json` file for future use.

## Technologies Used

- **Python**: Core language used.
- **Tkinter**: For the graphical user interface.
- **JSON**: To store and retrieve passwords.
- **Pyperclip**: Used for copying generated passwords to the clipboard.

## Project Structure
```
Project/
├── .idea/
├── .gitignore/
├── data.json/
├── logo.png/
├── main.py
```

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/krutarthpatel28/Password-Manager.git
   cd Project/

2. **Install dependencies: You need pyperclip. You can install it via pip:**:
   ```bash
   pip install pyperclip

3. **Run the application: Run main.py using Python:**:
   ```bash
   python main.py
4. **Generate and save passwords**:
  Enter the website name, email/username, and generate a password.
  Click "Add" to save it.

5. **Search for saved passwords**:
  Enter the website name and click "Search" to retrieve the saved email and password.

## Contributing
- If you'd like to contribute, feel free to fork the repo and submit a pull request!


