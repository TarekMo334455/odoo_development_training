from odoo import models, fields, api # type: ignore


class ScrapedPage(models.Model):
    _name = "scraped.page"
    _description = "Scraped Page"
    _rec_name = "title"

    title = fields.Char(string="Title")
    content = fields.Char(string="Content")
    source_url = fields.Char(string="Source URL")
    status = fields.Selection(
        selection=[
            ("vist", "Vist"),
            ("not_visit", "Not Visit"),
        ],
        string="Status",

    )

