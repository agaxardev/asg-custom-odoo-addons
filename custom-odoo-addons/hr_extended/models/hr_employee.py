from odoo import fields, models


class EmployeePublic(models.Model):
    _inherit = "hr.employee"

    antiguedad = fields.Selection(
        [("nuevo", "Nuevo"), ("antiguo", "Antiguo")], string="Antigüedad"
    )
    activo = fields.Selection([("si", "Sí"), ("no", "No")], string="Activo")
    centro_de_costo = fields.Selection(
        [("administrativo", "Administrativo"), ("academico", "Académico")],
        string="Centro de Costo",
    )
    escalafon = fields.Char(string="Escalafón")
    estado_del_contrato = fields.Selection(
        [("no_enviado", "No Enviado"), ("enviado", "Enviado"), ("firmado", "Firmado")],
        string="Estado del Contrato",
    )
    arl = fields.Char(string="ARL")
    eps = fields.Char(string="EPS")
    ccf = fields.Char(string="CCF")
    fdp = fields.Char(string="FDP")
    ingreso_al_helisa = fields.Selection(
        [("si", "Sí"), ("no", "No")], string="Ingreso al Helisa"
    )
    biometrico = fields.Integer(string="Biométrico")
    pregrado = fields.Char(string="Pregrado")
    postgrado = fields.Char(string="Postgrado")
    maestria = fields.Char(string="Maestría")
    nivel_de_ingles = fields.Selection(
        [("b2", "B2"), ("c1", "C1"), ("c2", "C2")], string="Nivel de Inglés"
    )
