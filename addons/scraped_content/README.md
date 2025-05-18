# Web Content Scraper for Odoo (scraped_content)

A comprehensive Odoo module for scraping and managing web content with external Python scripts integration.

## 🌟 Features

### Content Management

- Store scraped web pages content
- LinkedIn jobs tracking
- TechCrunch articles collection
- VentureBeat content management
- Content status tracking (Visited/Not Visited)

### Data Integration

- JSON-RPC API integration
- Bulk data import
- External scripts support
- Multiple content types handling

## 📋 Prerequisites

- Python 3.8+
- Odoo 17.0
- Required Python packages:

```bash
pip install requests beautifulsoup4 selenium
```

## 🔧 Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd odoo_projects
```

2. Copy module to Odoo addons:

```bash
cp -r addons/scraped_content /path/to/odoo/addons/
```

3. Update Odoo modules list and install:

```bash
docker exec -it odoo_projects-odoo-1 odoo -u scraped_content -d odoo_db
```

## 🤖 Running the Scrapers

### 1. Static Page Scraping

```bash
cd external_scripts
python static_page_scraping.py
```

### 2. LinkedIn Jobs Scraping

```bash
python linkedin_scraping.py
```

### 3. Blog Scraping

```bash
python blog_scraping.py
```

## 📤 Pushing Data to Odoo

1. Configure connection settings in `json_rpc_pusher.py`:

```python
url = "http://localhost:8017/jsonrpc"
db = "odoo_db"
username = "admin"
password = "password"
```

2. Run the data pusher:

```bash
python json_rpc_pusher.py
```

## 🔍 Module Usage

### Models Available:

- `scraped.page`: Web pages content
- `scraped.job`: LinkedIn jobs
- `scraped.blog`: Blog articles

### Views:

- List view for all scraped content
- Form view for detailed content
- Search filters for content status

### Access Rights:

- Manager: Full access
- User: Read-only access

## 📁 File Structure

```
scraped_content/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── scraped_page.py
│   ├── scraped_job.py
│   └── scraped_blog.py
├── security/
│   └── ir.model.access.csv
├── views/
│   ├── scraped_page_view.xml
│   ├── scraped_job_view.xml
│   └── scraped_blog_view.xml
└── external_scripts/
    ├── static_page_scraping.py
    ├── linkedin_scraping.py
    ├── blog_scraping.py
    └── json_rpc_pusher.py
```

## 🔄 Workflow

1. **Setup Scraping Environment**:

   ```bash
   cd external_scripts
   pip install -r requirements.txt
   ```

2. **Run Scrapers**:

   ```bash
   # Run all scrapers
   python static_page_scraping.py
   python linkedin_scraping.py
   python blog_scraping.py
   ```

3. **Push to Odoo**:

   ```bash
   python json_rpc_pusher.py
   ```

4. **View in Odoo**:
   - Go to Scraped Content menu
   - Browse scraped pages, jobs, and blogs
   - Filter and search content

## ⚙️ Configuration

1. **Odoo Settings**:

   - Install module
   - Configure user access rights
   - Setup automated actions (optional)

2. **Scraper Settings**:

   - Update URLs in scraping scripts
   - Configure scraping intervals
   - Set content filters

3. **API Connection**:
   - Configure Odoo URL
   - Set database name
   - Update credentials

## 🐛 Troubleshooting

1. **Connection Issues**:

   ```bash
   # Test Odoo connection
   curl http://localhost:8017
   ```

2. **Script Errors**:
   - Check Python dependencies
   - Verify file permissions
   - Review log files

## 📝 License

LGPL-3
