# Boot Buddy

<h1 align="center">
    <img src="./assets/logo.png" width="150" />
</h1>

Boot Buddy is an application designed to simplify your workflow by automatically launching your preferred applications when your system boots up. With customizable settings and a user-friendly interface, Boot Buddy ensures that your essential applications are ready to go as soon as you log in.

## Features

- **Automatic Startup**: Launches your preferred applications automatically when your system boots up.
- **Customizable Settings**: Choose which applications to launch and configure startup options according to your preferences.
- **User-Friendly Interface**: Intuitive and easy-to-use interface to manage your startup applications.
- **Minimal System Impact**: Optimized to have a minimal impact on your system's performance.

## Compatibility

- **Windows**: Fully compatible with Windows operating systems.
- **Linux**: Fully compatible with Linux operating systems.

## Installation

### Prerequisites

- Ensure you have Git installed on your system.
- Python (version 3.x) should be installed.

### Cloning the Repository

1. Open your terminal or command prompt.
2. Clone the repository using the following command:
    ```bash
    git clone https://github.com/joselucasapp/boot-buddy.git
    ```
3. Navigate to the project directory:
    ```bash
    cd boot-buddy
    ```

### Running Boot Buddy

1. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the application:
    ```bash
    python __init__.py
    ```

## Usage

1. Open a terminal or command prompt and navigate to the Boot Buddy directory.
2. Run the application using the command:
    ```bash
    python __init__.py
    ```
3. Follow the on-screen instructions to add applications to the startup list and configure their settings.

## Providing the Application Path

When adding an application to the startup list, you will need to provide the path to the application. Here’s how to find the path on different operating systems:

### Windows
1. Open the Command Prompt.
2. Use the where command to find the path of the application. For example:
   ```
   where chrome
   ```
    This will output the path to the Chrome executable, such as C:\Program Files\Google\Chrome\Application\chrome.exe.

### Linux
1. Open the Command Prompt.
2. Use the which command to find the path of the application. For example:
   ```
   which google-chrome
   ```
    This will output the path to the Chrome executable, such as /usr/bin/google-chrome.

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear and descriptive messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

## License

Boot Buddy is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For questions, suggestions, or feedback, please contact José Lucas Gonçalves Freitas at [jlgf.profissional@gmail.com](mailto:jlgf.profissional@gmail.com).

## Acknowledgements

- Thanks to all the contributors who have helped in the development of Boot Buddy.
- Special thanks to the open-source community for their invaluable resources and support.
