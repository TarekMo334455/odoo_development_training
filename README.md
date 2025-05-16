🧩 Odoo Development Training
Odoo Development Training is a comprehensive repository containing multiple custom Odoo modules (addons) built and maintained as part of a personally structured learning and training process on Odoo development.
This repository is intended for me, as a developer and learner interested in building and understanding real-world business applications on top of the Odoo framework.

📁 Repository Structure
Each folder inside the addons/ directory represents a standalone custom Odoo module.
Each addon includes its own:

Manifest (__manifest__.py)
Models
Views
Security configuration
Optional: Wizards, Controllers, i18n, Reports


🚀 Getting Started
Requirements

Python 3.8+
Odoo 17.0
PostgreSQL
Docker & Docker Compose (recommended)
Git

Installation
Clone the repository:
git clone https://github.com/TarekMo334455/odoo_development_training.git
cd odoo_development_training

Set the addons path:
addons_path = addons

Install modules from Odoo UI or terminal:
Activate developer mode in Odoo and install each module from the Apps list.
⚙️ Configuration
Default configuration is provided via odoo.conf.
A docker-compose.yml file is included for quick local setup.
Add any custom sequences, email templates, or security rules in each module directory as needed.
📦 Included Modules



Module
Description



hms
Full-featured Hospital Management System


todo
Task and Time Management System


...
More addons will be added as development continues


Each addon includes its own README.md file explaining its purpose, models, and usage.
💻 Development Guidelines

Follow Odoo coding guidelines
Code style follows PEP 8
Keep logic modular and reusable
Add documentation and comments for clarity
Commit messages should be meaningful and structured

🤝 Contributing
Contributions are welcome! To contribute:

Fork the repository
Create a feature or fix branch
Submit a pull request with clear explanation

Please make sure your code:

Is tested
Does not break existing modules
Follows the structure and guidelines

📜 License
This project is licensed under the LGPL-3.0 License.
📬 Contact
For questions, suggestions, or support, please reach out via GitHub Issues or create a discussion in the repository.
