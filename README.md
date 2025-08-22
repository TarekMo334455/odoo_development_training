# 🧩 Odoo Development Training

A comprehensive repository containing custom Odoo modules built for learning.

## 📁 Repository Structure

### Core Modules

| Module | Description |
|--------|-------------|
| hms | Hospital Management System |
| todo | Task and Time Management System |
| scraped_content | Web Content Scraping & Management System |

### External Scripts
Located in `external_scripts/`:

| Script | Purpose |
|--------|----------|
| static_page_scraping.py | VentureBeat page scraper |
| linkedin_scraping.py | LinkedIn jobs scraper |
| blog_scraping.py | TechCrunch articles scraper |
| json_rpc_pusher.py | Data pusher with validation |

## 🚀 Getting Started

### Requirements
- Python 3.8+
- Odoo 17.0
- PostgreSQL
- Docker & Docker Compose
- Git
- Additional Python packages:
  ```bash
  pip install requests beautifulsoup4 selenium xlsxwriter typing
  ```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/TarekMo334455/odoo_development_training.git
cd odoo_development_training
```

2. Set up Docker environment:
```bash
docker-compose up -d
```

3. Install modules through Odoo UI:
- Enable developer mode
- Update apps list
- Install desired modules

## 📦 Module Details

### Hospital Management System (HMS)
- Patient management
- Department handling
- Doctor assignments
- Medical records
- Custom reports

### Task Management System (Todo)
- Task tracking
- Time management
- User assignments
- Status workflows
- Report generation

### Web Content Scraper (scraped_content)
Features:
- Content scraping from multiple sources
- Data validation and deduplication
- Custom API integration
- Content management interface

Models:
- scraped.page: Web pages
- scraped.job: LinkedIn jobs
- scraped.blog: Blog articles

External Scripts:
```bash
cd external_scripts

# Run scrapers
python static_page_scraping.py
python linkedin_scraping.py
python blog_scraping.py

# Push data to Odoo
python json_rpc_pusher.py
```

## 💻 Development Guidelines

### Code Standards
- Follow Odoo guidelines
- PEP 8 compliance
- Type hints usage
- Comprehensive logging
- Error handling

### API Integration
- JSON-RPC implementation
- Idempotency support
- Retry mechanisms
- Data validation

### Security
- Role-based access
- Record rules
- Field-level permissions
- API authentication

## ⚙️ Configuration

### Docker Setup
```yaml
version: '3'
services:
  web:
    image: odoo:17.0
    volumes:
      - ./addons:/mnt/extra-addons
```

### Module Configuration
Each module includes:
- Security rules
- Data sequences
- Email templates
- Access rights

### External Scripts Config
```python
# config.py
SCRAPING_CONFIG = {
    "base_url": "http://localhost:8017",
    "db_name": "odoo_db",
    "username": "admin",
    "password": "admin"
}
```

## 🔧 Maintenance

### Log Monitoring
```bash
tail -f external_scripts/json_rpc_pusher.log
```

### Database Backup
```bash
docker exec odoo pg_dump -U odoo odoo_db > backup.sql
```

## 📝 License
LGPL-3.0 License

## 📬 Contact
- GitHub Issues
- Repository Discussions
