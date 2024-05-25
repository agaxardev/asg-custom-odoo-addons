from odoo import fields, models


class EmployeePublic(models.Model):
    _inherit = "hr.employee"

    # Nuevo campo: Antiguedad
    antiguedad = fields.Selection(
        [("nuevo", "Nuevo"), ("antiguo", "Antiguo")], string="Antigüedad"
    )

    # Nuevo campo: Activo
    activo = fields.Selection([("si", "Sí"), ("no", "No")], string="Activo")

    # Nuevo campo: Centro de Costo
    centro_de_costo = fields.Selection(
        [("administrativo", "Administrativo"), ("academico", "Académico")],
        string="Centro de Costo",
    )

    # Nuevo campo: Escalafón
    escalafon = fields.Char(string="Escalafón")

    # Nuevo campo: Estado del Contrato
    estado_del_contrato = fields.Selection(
        [("no_enviado", "No Enviado"), ("enviado", "Enviado"), ("firmado", "Firmado")],
        string="Estado del Contrato",
    )

    # Nuevo campo: ARL
    arl = fields.Char(string="ARL")

    # Nuevo campo: EPS
    eps = fields.Char(string="EPS")

    # Nuevo campo: CCF
    ccf = fields.Char(string="CCF")

    # Nuevo campo: FDP
    fdp = fields.Char(string="FDP")

    # Nuevo campo: Ingreso al Helisa
    ingreso_al_helisa = fields.Selection(
        [("si", "Sí"), ("no", "No")], string="Ingreso al Helisa"
    )

    # Nuevo campo: Biométrico
    biometrico = fields.Integer(string="Biométrico")

    # Nuevo campo: Pregrado
    pregrado = fields.Char(string="Pregrado")

    # Nuevo campo: Postgrado
    postgrado = fields.Char(string="Postgrado")

    # Nuevo campo: Maestría
    maestria = fields.Char(string="Maestría")

    # Nuevo campo: Nivel de Inglés
    nivel_de_ingles = fields.Selection(
        [("b2", "B2"), ("c1", "C1"), ("c2", "C2")], string="Nivel de Inglés"
    )
