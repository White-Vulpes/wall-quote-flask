---

# Wall Quote Flask

**Wall Quote Flask** is a lightweight Flask application that generates random quotes for use as wallpapers. It provides a simple API that can be integrated with other services, like Apple Shortcuts, to dynamically change your wallpaper with a new quote.

## Features

- **Random Quotes:** Fetches a random quote with a specified theme.
- **Themes:** Choose from different themes to customize the look of your wallpaper.
- **API Integration:** Easy to integrate with third-party applications.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/White-Vulpes/wall-quote-flask.git
   cd wall-quote-flask
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python application.py
   ```

4. Access the application at `http://localhost:5000`.

## Usage

- **Get a Random Quote:**
  ```http
  GET /quote
  ```
  Returns a random quote.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
