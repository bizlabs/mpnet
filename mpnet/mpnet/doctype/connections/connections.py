# Copyright (c) 2024, Doug Mattingly and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.model.document import frappe


class connections(Document):

  def before_validate(self):
    pa = frappe.db.get_value("ports",self.porta,"title")
    pb = frappe.db.get_value("ports",self.portb,"title")
    self.title = pa + " | " + pb
    pass