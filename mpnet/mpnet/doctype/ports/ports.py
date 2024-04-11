# Copyright (c) 2024, Doug Mattingly and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.model.document import frappe


class ports(Document):

  def before_save(self):
    equip = frappe.db.get_value("Equipments",self.equipment_id,"title")
    self.title = "p" + str(self.portnum) + "- " + equip
    pass



  