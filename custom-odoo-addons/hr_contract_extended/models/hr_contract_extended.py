import datetime
from datetime import datetime

from dateutil.relativedelta import relativedelta
from odoo import api, fields, models


class HrContractExtended(models.Model):
    _inherit = "hr.contract"

    dias_tomados_vacaciones = fields.Integer(string="Días Tomados de Vacaciones")

    dias_vacaciones = fields.Integer(
        string="Días de Vacaciones", compute="_compute_dias_vacaciones", store=True
    )
    dias_pendientes_vacaciones = fields.Integer(
        string="Días Pendientes de Vacaciones",
        compute="_compute_dias_pendientes_vacaciones",
        store=True,
    )
    contrato_mes_dia = fields.Char(
        string="Contrato en Meses y Días",
        compute="_compute_contrato_mes_dia",
        store=True,
    )
    dias_periodo_prueba = fields.Integer(
        string="Días de Periodo de Pruebas",
        compute="_compute_dias_periodo_prueba",
        store=True,
    )
    fecha_fin_prueba = fields.Date(
        string="Fecha Fin de Prueba", compute="_compute_fecha_fin_prueba", store=True
    )
    dias_faltantes_prueba = fields.Integer(
        string="Días Faltantes para el periodo de prueba",
        compute="_compute_dias_faltantes_prueba",
        store=True,
    )
    porcentaje_dias_faltantes_prueba = fields.Float(
        string="% Prueba",
        compute="_compute_porcentaje_dias_faltantes_prueba",
    )
    dias_trabajados = fields.Integer(
        string="Días Trabajados", compute="_compute_dias_trabajados", store=True
    )

    @api.depends("dias_faltantes_prueba", "dias_periodo_prueba")
    def _compute_porcentaje_dias_faltantes_prueba(self):
        for record in self:
            if record.dias_periodo_prueba > 0:
                record.porcentaje_dias_faltantes_prueba = (
                    100
                    - (record.dias_faltantes_prueba / record.dias_periodo_prueba) * 100
                )
            else:
                record.porcentaje_dias_faltantes_prueba = 0

    @api.depends("date_start", "date_end")
    def _compute_dias_vacaciones(self):
        for record in self:
            if record.date_start:
                today = datetime.today().date()
                dias_trabajados = (today - record.date_start).days
                record.dias_vacaciones = int((2.5 / 30) * (dias_trabajados / 2))
            else:
                record.dias_vacaciones = 0

    @api.depends("dias_vacaciones", "dias_tomados_vacaciones")
    def _compute_dias_pendientes_vacaciones(self):
        for record in self:
            dias_pendientes = record.dias_vacaciones - record.dias_tomados_vacaciones
            record.dias_pendientes_vacaciones = max(dias_pendientes, 0)

    @api.depends("date_start", "date_end")
    def _compute_contrato_mes_dia(self):
        for record in self:
            if record.date_start and record.date_end:
                delta = relativedelta(record.date_end, record.date_start)
                record.contrato_mes_dia = (
                    f"{delta.years * 12 + delta.months} meses y {delta.days} días"
                )
            else:
                record.contrato_mes_dia = ""

    @api.depends("date_start", "date_end")
    def _compute_dias_periodo_prueba(self):
        for record in self:
            if record.date_start and record.date_end:
                duration = (record.date_end - record.date_start).days
                record.dias_periodo_prueba = min(duration // 5, 60)
            else:
                record.dias_periodo_prueba = 0

    @api.depends("date_start", "dias_periodo_prueba")
    def _compute_fecha_fin_prueba(self):
        for record in self:
            if record.date_start and record.dias_periodo_prueba:
                record.fecha_fin_prueba = record.date_start + relativedelta(
                    days=record.dias_periodo_prueba
                )
            else:
                record.fecha_fin_prueba = False

    @api.depends("date_start", "date_end", "dias_periodo_prueba")
    def _compute_dias_faltantes_prueba(self):
        for record in self:
            if record.date_start and record.date_end and record.dias_periodo_prueba:
                today = datetime.today().date()
                dias_trabajados = (today - record.date_start).days

                if dias_trabajados >= record.dias_periodo_prueba:
                    record.dias_faltantes_prueba = 0
                else:
                    record.dias_faltantes_prueba = (
                        record.dias_periodo_prueba - dias_trabajados
                    )
            else:
                record.dias_faltantes_prueba = 0

    @api.depends("date_start")
    def _compute_dias_trabajados(self):
        for record in self:
            if record.date_start:
                today = datetime.today().date()
                record.dias_trabajados = (today - record.date_start).days
            else:
                record.dias_trabajados = 0
