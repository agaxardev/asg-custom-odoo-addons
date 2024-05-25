# -*- coding: utf-8 -*-
{
    "name": "hr_extended",
    "summary": "Short (1 phrase/line) summary of the module's purpose",
    "description": "Empleados extendidos con campos adicionales.",
    "author": "My Company",
    "website": "https://www.yourcompany.com",
    "category": "Uncategorized",
    "version": "1.0",
    "depends": ["base", "hr"],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_employee_views.xml",
    ],
    "installable": True,
    "application": True,
}
