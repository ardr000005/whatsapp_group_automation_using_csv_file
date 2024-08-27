# whatsapp_group_automation_using_csv_file
Streamline your group management on WhatsApp with this automation script. This tool allows you to quickly add multiple contacts to a WhatsApp group from a CSV file, saving time and effort compared to manual entry.
# WhatsApp Group Automation

## Description

This project automates the process of adding contacts to a WhatsApp group using Selenium WebDriver and Python. The script reads phone numbers from a CSV file and adds them to a specified WhatsApp group.

## Requirements

- **Python 3.x**
- **Selenium**: Install with `pip install selenium`
- **Pandas**: Install with `pip install pandas`
- **Microsoft Edge WebDriver**: [Download Link](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH)
  - Extract the WebDriver and note the path to `msedgedriver.exe`

## Setup

1. **Install Dependencies**:
   - Create a virtual environment (optional but recommended):
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - **Windows**:
       ```bash
       venv\Scripts\activate
       ```
     - **macOS/Linux**:
       ```bash
       source venv/bin/activate
       ```
   - Install required packages from `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

2. **Download and Configure Edge WebDriver**:
   - Download the Microsoft Edge WebDriver and extract it.
   - Update the `entries.py` file with the path to `msedgedriver.exe` and the name of your WhatsApp group.

3. **Prepare Your CSV File**:
   - Ensure your CSV file with phone numbers is named `contacts.csv` and is in the same directory as your scripts.

4. **Configure `entries.py`**:
   - Set the `driver_path` and `group_name` in `entries.py`:
     ```python
     # entries.py

     # Path to the Edge WebDriver executable
     driver_path = "C:/path/to/msedgedriver.exe"  # Replace with your actual path

     # Name of the WhatsApp group you want to add contacts to
     group_name = "Your WhatsApp Group Name"  # Replace with your actual group name
     ```

## Usage

1. **Prepare WhatsApp Web**:
   - Open Microsoft Edge and go to [WhatsApp Web](https://web.whatsapp.com).
   - Log in by scanning the QR code with your phone.

2. **Run the Script**:
   - Navigate to the directory with your scripts and CSV file.
   - Execute the script:
     ```bash
     python add_to_group.py
     ```

3. **Post-Execution**:
   - **Remove your WhatsApp Web session** from linked devices after the script completes for security reasons.

## Notes

- Ensure the group name in `entries.py` matches exactly with the WhatsApp group name.
- Adjust script timeouts if necessary for slower networks or systems.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


