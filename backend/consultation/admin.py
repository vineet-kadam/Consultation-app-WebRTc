from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Clinic, DoctorAvailability, Meeting


# =============================================================================
# 1. CUSTOM USER ADMIN
# =============================================================================

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    Custom UserAdmin to handle our extra fields.
    """
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Profile Information', {
            'fields': ('role', 'clinic', 'mobile', 'date_of_birth', 'sex', 'department', 'photo')
        }),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Profile Information', {
            'fields': (
                'role', 'clinic', 'mobile', 'date_of_birth', 'sex', 'department', 'photo',
                'first_name', 'last_name', 'email'
            )
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'clinic', 'is_staff')
    list_filter  = ('role', 'clinic', 'sex', 'is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'mobile')
    ordering = ('username',)


# =============================================================================
# 2. CLINIC & AVAILABILITY
# =============================================================================

class DoctorAvailabilityInline(admin.TabularInline):
    """
    Shows doctor schedules directly inside the Clinic admin page.
    """
    model = DoctorAvailability
    extra = 1
    autocomplete_fields = ['doctor']


@admin.register(Clinic)
class ClinicAdmin(admin.ModelAdmin):
    list_display = ('name', 'clinic_id', 'member_count')
    search_fields = ('name', 'clinic_id')
    inlines = [DoctorAvailabilityInline]

    def member_count(self, obj):
        return obj.members.count()
    member_count.short_description = 'Total Members'


@admin.register(DoctorAvailability)
class DoctorAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'clinic', 'day_name', 'start_time', 'end_time')
    list_filter = ('day_of_week', 'clinic')
    search_fields = ('doctor__username', 'doctor__first_name', 'clinic__name')
    autocomplete_fields = ['doctor', 'clinic']

    def day_name(self, obj):
        return obj.get_day_of_week_display()
    day_name.short_description = 'Day'


# =============================================================================
# 3. MEETING MANAGEMENT
# =============================================================================

@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = (
        'meeting_id',
        'scheduled_time',
        'get_patient',
        'get_doctor',
        'appointment_type',
        'status'
    )
    list_filter = (
        'status',
        'meeting_type',
        'appointment_type',
        'clinic',
        'scheduled_time'
    )
    search_fields = (
        'room_id',
        'patient__username', 'patient__email', 'patient__first_name',
        'doctor__username', 'doctor__first_name',
        'appointment_reason'
    )
    readonly_fields = ('room_id', 'created_at', 'updated_at')
    autocomplete_fields = ['patient', 'doctor', 'sales', 'clinic']

    # Organize the form into logical sections
    fieldsets = (
        ('Identifiers', {
            'fields': ('room_id', 'clinic')
        }),
        ('Participants', {
            'fields': ('patient', 'doctor', 'sales', 'participants')
        }),
        ('Schedule', {
            'fields': ('scheduled_time', 'duration', 'status', 'meeting_type', 'appointment_type')
        }),
        ('Medical Context', {
            'fields': ('appointment_reason', 'department', 'remark', 'speech_to_text'),
            'classes': ('collapse',)  # Makes this section collapsible
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    # Custom methods for List Display
    def get_patient(self, obj):
        return obj.patient.get_full_name() if obj.patient else "-"
    get_patient.short_description = 'Patient'

    def get_doctor(self, obj):
        return obj.doctor.get_full_name() if obj.doctor else "-"
    get_doctor.short_description = 'Doctor'

    # --- Custom Actions ---

    @admin.action(description='Mark selected meetings as Cancelled')
    def mark_cancelled(self, request, queryset):
        updated = queryset.update(status='cancelled')
        self.message_user(request, f"{updated} meeting(s) marked as Cancelled.")

    @admin.action(description='Mark selected meetings as Ended')
    def mark_ended(self, request, queryset):
        updated = queryset.update(status='ended')
        self.message_user(request, f"{updated} meeting(s) marked as Ended.")

    actions = [mark_cancelled, mark_ended]