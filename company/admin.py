from django.contrib import admin
from company.models import *
from django.utils.translation import gettext_lazy as _


@admin.register(CompanyAddress)
class CompanyAddressAdmin(admin.ModelAdmin):
    list_display = ("street", "city", "zip_code")
    list_filter = ("city",)
    search_fields = ("street", "city",)


class CompanyEmployeeAdmin(admin.StackedInline):
    model = Employee
    extra = 1
    fields = ("first_name", "last_name", "specialist")


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("company_name", "category", "company_email", "reception_phone", "address")
    actions_on_bottom = True
    date_hierarchy = "created_at"
    empty_value_display = '-'
    # fieldsets = (
    #     # (None, {'fields': ('username', 'password', 'password_change_link')}),
    #     (_('Company info'), {'fields': ('company_name', 'category', 'phone', 'email', 'address')}),
    #     (_('Contact the Company '), {
    #         'fields': ('company_email', 'reception_phone', 'address'),
    #     }),
    #     # (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    # )
    inlines = [CompanyEmployeeAdmin]    #har bir User modelda o`zini Toy madelni qo`shib ko`rsatadi

# ************************************** Employee Admin ***********************************************************


@admin.register(EmployeeAddress)
class EmployeeAddressAdmin(admin.ModelAdmin):
    list_display = ("street", "city", "zip_code")
    list_filter = ("city",)
    search_fields = ("street", "city",)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "company", "specialist")
    # autocomplete_fields = ["company"]  #userlar soni ko'p bo'lsa bazadan yuklash qiyin yuklanishini oldini oladi
    list_filter = ("specialist",)
    search_fields = ("first_name",)




# ****************************************************************
# from django.utils.translation import gettext_lazy as _
# # Register your models here.
#
#
# @admin.register(Address)
# class AddressAdmin(admin.ModelAdmin):
#     empty_value_display = '-empty-'
#     list_display = ('country', 'city', 'street', 'zip_code')
#     # fields = ('country', 'city')
#     fields = (('country', 'city'), 'street')
#     # exclude = ('country', 'city',)
#
#
# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     fieldsets = (
#         # (None, {
#         #     'fields': ('first_name', 'last_name', 'content', 'sites')
#         # }),
#         (_('Personal info'), {'fields': ('first_name', 'last_name', 'photo')}),
#         (_('Reference'), {'fields': ('specialist', 'phone', 'city', 'company')}),
#         (_('Permissions'), {
#             'fields': ('is_active',),
#         }),
#         # ('Advanced options', {
#         #     'classes': ('collapse',),
#         #     'fields': ('registration_required', 'template_name'),
#         # }),
#     )
#
#
# # ******************************************************
#
#
# class CompanyEmployeeInline(admin.StackedInline):
#     model = Employee
#     extra = 1
#     fields = ("first_name", "last_name", "phone")
#
#
#
#
# @admin.register(Company)
# class CompanyAdmin(admin.ModelAdmin):
#     search_fields = ["name"]
#     inlines = [CompanyEmployeeInline]
#
#
#
#
# # @admin.register(Employee)
# # class EmployeeAdmin(admin.ModelAdmin):
# #     fieldsets = (
# #         # (None, {
# #         #     'fields': ('first_name', 'last_name', 'content', 'sites')
# #         # }),
# #         (_('Personal info'), {'fields': ('first_name', 'last_name', 'photo')}),
# #         (_('Reference'), {'fields': ('specialist', 'phone', 'city', 'company')}),
# #         (_('Permissions'), {
# #             'fields': ('is_active',),
# #         }),
# #         # ('Advanced options', {
# #         #     'classes': ('collapse',),
# #         #     'fields': ('registration_required', 'template_name'),
# #         # }),
# #     )