from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from toys.forms import UserAdminForm
from toys.models import *

from toys.services.send_weekly_report import send_weekly_toys_count

# admin.site.register(Toy)
# admin.site.register(Tag)
# admin.site.register(User)

#Admin panelimizni nastroykalarini sozlayapmiz

# ***********************************************************************************************


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "city", "zip_code")
    list_filter = ("city",)
    search_fields = ("street", "city",)


# *********************************************************************************************

# InlineModelAdmin bu bilan ikkichi bir madelni bitta inlineda ko`rsatib beradi
# TabularInline atribuitlarni bir qatorda chiqaradi
# class UserToysInline(admin.TabularInline):
# StackedInlin atribiutlarni ustun shaklida qatorlarda beradi


class UserToysInline(admin.StackedInline):
    model = Toy
    extra = 1
    fields = ("name", "description", "type")


def send_weekly_email_report(modeladmin, request, queryset):
    if queryset.count() != 1:
        modeladmin.message_user(request, "Multiple user selected, please choose one and only one.",
                                messages.ERROR)
        return HttpResponseRedirect(request.get_full_path())

    user = queryset.first()
    if not user.email:
        modeladmin.message_user(request, "Selected user does not have email address",
                                messages.ERROR)
        return HttpResponseRedirect(request.get_full_path())

    send_weekly_toys_count(user)

    modeladmin.message_user(request, "Weekly report send to user email: %s" % user.email, messages.INFO)
    return HttpResponseRedirect(request.get_full_path())


@admin.register(User)
# class UserAdmin(admin.ModelAdmin):
# UserAdmin ModelAdmin dan inharit qib olamiz | admin panelni gurpalarga bo'lib beradi | secureti hizmatini qoshadi
class UserAdmin(UserAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "password_change_link")
    actions_on_bottom = True
    date_hierarchy = "created_at"
    empty_value_display = '-'
    # exclude = ("created_at", "updated_at")   #model adminga qo'shmedi
    readonly_fields = ('password_change_link',)
    form = UserAdminForm  #forms.py da emailni tekshiradi
    fieldsets = (
        (None, {'fields': ('username', 'password', 'password_change_link')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'phone', 'email', 'address')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    inlines = [UserToysInline]    #har bir User modelda o`zini Toy madelni qo`shib ko`rsatadi
    # inlines ni defolt qiymati 3 ga teng [3 ta qator chiqaradi]
    actions = [send_weekly_email_report]


    def password_change_link(self, obj):
        return format_html(f'<a href="/admin/toys/user/{obj.pk}/password/">Change Password</a>')


# ***********************************************************************************************


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

# ***********************************************************************************************


class ToyTagsModel(admin.TabularInline):
    model = Toy.tags.through
    # autocomplete_fields = ["tags"]
    extra = 1


@admin.register(Toy)
class ToyAdmin(admin.ModelAdmin):
    list_display = ("name", "user", "type", "price")
    autocomplete_fields = ["user"]  #userlar soni ko'p bo'lsa bazadan yuklash qiyin yuklanishini oldini oladi
    list_filter = ("type",)
    search_fields = ("name", "description")
    inlines = [ToyTagsModel]


# ***********************************************************************************************