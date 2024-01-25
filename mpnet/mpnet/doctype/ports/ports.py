# Copyright (c) 2024, Doug Mattingly and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.model.document import frappe


class ports(Document):
  # def title(self):
  #   return "p" + str(self.portnum)

  def before_save(self):
    equip = frappe.db.sql('select title from tabEquipments where name = {self.equipment_id}')
    self.title = "p" + str(self.portnum) + str(self.equipment_id.title)
