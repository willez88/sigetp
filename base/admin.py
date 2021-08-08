from django.contrib import admin

from .forms import CommunalCouncilAdminForm
from .models import (
    Animal, CementType, CommunalCouncil, CommunityOrganization, Course,
    Disability, Disease, EducationalMission, ElectricService,
    FloorType, Gender, IncomeType, InstructionDegree,
    LivingPlaceType, MaritalStatus, Occupation, Profession, Relationship, Risk,
    RoofType, SanitarySituation, SocialMission, Sport, TenureType,
    TrashDisposal, Valoration, WallType, Workplace,
)


class CommunalCouncilAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo CommunalCouncil al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    form = CommunalCouncilAdminForm
    change_form_template = 'base/admin/change_form.html'
    list_display = ('rif', 'name', 'parish',)
    list_filter = ('parish',)
    ordering = ('parish__name',)


class RiskAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Risk al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class LivingPlaceTypeAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo LivingPlaceType al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class RoofTypeAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo RoofType al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class WallTypeAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo WallType al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class ElectricServiceAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo ElectricService al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class SanitarySituationAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo SanitarySituation al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class TrashDisposalAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo TrashDisposal al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class TenureTypeAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo TenureType al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class RelationshipAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Relationship al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class MaritalStatusAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo MaritalStatus al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class InstructionDegreeAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo InstructionDegree al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class EducationalMissionAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo EducationalMission al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class SocialMissionAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo SocialMission al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class IncomeTypeAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo IncomeType al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class CommunityOrganizationAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo CommunityOrganization al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class GenderAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Gender al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class CementTypeAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo CementType al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class ValorationAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Valoration al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class AnimalAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Animal al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class ProfessionAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Profession al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class OccupationAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Occupation al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class WorkplaceAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Workplace al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class SportAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Sport al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class DiseaseAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Disease al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class DisabilityAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Disability al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class CourseAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Course al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


class FloorTypeAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo FloorType al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('name',)
    ordering = ('name',)


admin.site.register(CommunalCouncil, CommunalCouncilAdmin)
admin.site.register(Risk, RiskAdmin)
admin.site.register(LivingPlaceType, LivingPlaceTypeAdmin)
admin.site.register(RoofType, RoofTypeAdmin)
admin.site.register(WallType, WallTypeAdmin)
admin.site.register(ElectricService, ElectricServiceAdmin)
admin.site.register(SanitarySituation, SanitarySituationAdmin)
admin.site.register(TrashDisposal, TrashDisposalAdmin)
admin.site.register(TenureType, TenureTypeAdmin)
admin.site.register(Relationship, RelationshipAdmin)
admin.site.register(MaritalStatus, MaritalStatusAdmin)
admin.site.register(InstructionDegree, InstructionDegreeAdmin)
admin.site.register(EducationalMission, EducationalMissionAdmin)
admin.site.register(SocialMission, SocialMissionAdmin)
admin.site.register(IncomeType, IncomeTypeAdmin)
admin.site.register(CommunityOrganization, CommunityOrganizationAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(CementType, CementTypeAdmin)
admin.site.register(Valoration, ValorationAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Profession, ProfessionAdmin)
admin.site.register(Occupation, OccupationAdmin)
admin.site.register(Workplace, WorkplaceAdmin)
admin.site.register(Sport, SportAdmin)
admin.site.register(Disease, DiseaseAdmin)
admin.site.register(Disability, DisabilityAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(FloorType, FloorTypeAdmin)
