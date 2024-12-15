# AquaCare Device

A smart aquarium monitoring and control system that helps maintain optimal conditions for your aquatic pets.

## Description
AquaCare Device is the hardware component of the AquaCare system, designed to monitor and control various parameters of your aquarium including:

- **pH levels**
- **Water temperature**
- **Water level**
- **Automated feeding system**

## Features
- Real-time monitoring of aquarium metrics
- Automated feeding schedule
- Alert system for abnormal conditions
- MQTT communication with AquaCare backend
- Test mode for system verification
- QR code generation for easy device registration

## Requirements
- Python 3.8 or higher
- MQTT broker connection
- Internet connectivity
- Required Python packages (see `requirements.txt`)

## Installation
1. Clone the repository:
   ```bash
   git clone [repository URL]
   ```
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate the virtual environment:
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     source .venv/bin/activate
     ```
4. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the device:
   ```bash
   python main.py
   ```

## Configuration
The device will automatically:
- Generate a unique device ID on the first run
- Create a QR code for device registration
- Store configuration in `device_config.json`

## Usage
1. Start the device using:
   ```bash
   python main.py
   ```
2. Scan the generated QR code using the AquaCare mobile app.
3. Configure device settings through the app.
4. Monitor real-time metrics and alerts.

## Features
### Metric Monitoring
- **pH Level:** 6.0-8.0
- **Temperature:** 20-32°C
- **Water Level:** 0-100%

### Feeding System
- Scheduled feeding
- Manual feeding trigger
- Weekly schedule support

### Alert System
- Real-time alerts for abnormal conditions
- Configurable thresholds
- Critical and warning level alerts

## Testing
The device includes a test mode that can be activated through the API to simulate various conditions and verify system functionality.

## Contributing
Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## Author
- Ananda Ayu Putri
- Bintang Timurlangit
- Raqqat Amarasangga Iswahyudi

## Acknowledgments
- **MQTT** for real-time communication
- **Python community** for various libraries
