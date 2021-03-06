"""
Nombre del software: SIGETP

Descripción: Sistema Integrado de Información y Documentación Geoestadística y Tecnopolítica

Nombre del licenciante y año: Fundación CIDA (2017)

Autores: William Páez

La Fundación Centro Nacional de Desarrollo e Investigación en Tecnologías Libres (CENDITEL),
ente adscrito al Ministerio del Poder Popular para Educación Universitaria, Ciencia y Tecnología
(MPPEUCT), concede permiso para usar, copiar, modificar y distribuir libremente y sin fines
comerciales el "Software - Registro de bienes de CENDITEL", sin garantía
alguna, preservando el reconocimiento moral de los autores y manteniendo los mismos principios
para las obras derivadas, de conformidad con los términos y condiciones de la licencia de
software de la Fundación CENDITEL.

El software es una creación intelectual necesaria para el desarrollo económico y social
de la nación, por tanto, esta licencia tiene la pretensión de preservar la libertad de
este conocimiento para que contribuya a la consolidación de la soberanía nacional.

Cada vez que copie y distribuya el "Software - Registro de bienes de CENDITEL"
debe acompañarlo de una copia de la licencia. Para más información sobre los términos y condiciones
de la licencia visite la siguiente dirección electrónica:
http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/
"""
## @namespace base.admin
#
# Contiene las clases, atributos y métodos básicos del sistema a implementar en el panel administrativo
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @author <a href='www.cida.gob.ve/'>Centro de Investigaciones de Astronomía "Francisco J. Duarte"</a>
# @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
# @date 24-05-2017
# @version 1.0

from django.contrib import admin
from .models import (
    CommunalCouncil, Risk, LivingPlaceType, RoofType, WallType, FloorType, ElectricService,
    SanitarySituation, TrashDisposal, TenureType, FamilyRelationship, MaritalStatus, InstructionDegree,
    EducationalMission, SocialMission, IncomeType, CommunityOrganization, Sex, CementType,
    Valoration, Animal, Profession, Occupation, Workplace, Sport, Disease, Disability, Course
)
from .forms import CommunalCouncilAdminForm

class CommunalCouncilAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo ConsejoComunal en el panel administrativo

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    form = CommunalCouncilAdminForm
    change_form_template = 'base/admin/change_form.html'
    list_display = ('rif','name','parish',)
    list_filter = ('parish',)
    ordering = ('parish__name',)

admin.site.register(CommunalCouncil, CommunalCouncilAdmin)

class RiskAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo ConsejoComunal en el panel administrativo

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    """

    list_display = ('name',)
    ordering = ('name',)

admin.site.register(Risk, RiskAdmin)

class LivingPlaceTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(LivingPlaceType, LivingPlaceTypeAdmin)

class RoofTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(RoofType, RoofTypeAdmin)

class WallTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(WallType, WallTypeAdmin)

class ElectricServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(ElectricService, ElectricServiceAdmin)

class SanitarySituationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(SanitarySituation, SanitarySituationAdmin)

class TrashDisposalAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(TrashDisposal, TrashDisposalAdmin)

class TenureTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(TenureType, TenureTypeAdmin)

class FamilyRelationshipAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(FamilyRelationship, FamilyRelationshipAdmin)

class MaritalStatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(MaritalStatus, MaritalStatusAdmin)

class InstructionDegreeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(InstructionDegree, InstructionDegreeAdmin)

class EducationalMissionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(EducationalMission, EducationalMissionAdmin)

class SocialMissionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(SocialMission, SocialMissionAdmin)

class IncomeTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(IncomeType, IncomeTypeAdmin)

class CommunityOrganizationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(CommunityOrganization, CommunityOrganizationAdmin)

class SexAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(Sex, SexAdmin)

class CementTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(CementType, CementTypeAdmin)

class ValorationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(Valoration, ValorationAdmin)

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(Animal, AnimalAdmin)

class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(Profession, ProfessionAdmin)

class OccupationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(Occupation, OccupationAdmin)

class WorkplaceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(Workplace, WorkplaceAdmin)

class SportAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(Sport, SportAdmin)

class DiseaseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(Disease, DiseaseAdmin)

class DisabilityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(Disability, DisabilityAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('name',)
admin.site.register(Course, CourseAdmin)