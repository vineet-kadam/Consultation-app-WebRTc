# consultation/serializers.py

from rest_framework import serializers
from .models import Meeting, User, DoctorAvailability


class UserSerializer(serializers.ModelSerializer):
    full_name     = serializers.SerializerMethodField()
    clinic_detail = serializers.SerializerMethodField()

    class Meta:
        model  = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'full_name', 'role', 'mobile', 'date_of_birth', 'sex',
            'department', 'clinic', 'clinic_detail'
        ]

    def get_full_name(self, obj):
        return obj.get_full_name() or obj.username

    def get_clinic_detail(self, obj):
        if obj.clinic:
            return {'id': obj.clinic.id, 'name': obj.clinic.name}
        return None



class MeetingSerializer(serializers.ModelSerializer):
    """
    Serializes Meeting objects with all fields needed by both PatientHome
    and DoctorHome frontends, including computed name fields.
    """
    patient_name = serializers.SerializerMethodField()
    doctor_name  = serializers.SerializerMethodField()
    sales_name   = serializers.SerializerMethodField()
    clinic_name  = serializers.SerializerMethodField()

    # Expose full objects so frontend gets mobile/dob/sex/etc.
    patient = UserSerializer(read_only=True)
    doctor  = UserSerializer(read_only=True)
    sales   = UserSerializer(read_only=True)

    class Meta:
        model  = Meeting
        fields = [
            # -- identifiers ----------------------------------------------
            'meeting_id',
            'room_id',
            # -- scheduling ---------------------------------------------- 
            'scheduled_time',
            'duration',
            'status',
            # -- appointment meta ---------------------------------------- 
            'appointment_type',
            'meeting_type',
            'appointment_reason',
            'department',
            'remark',
            # -- transcript ---------------------------------------------- 
            'speech_to_text',
            # -- participants JSON (stores sex/mobile/dob/email per role)  
            'participants',
            # -- FK objects ---------------------------------------------- 
            'patient',
            'doctor',
            'sales',
            # -- computed names ------------------------------------------ 
            'patient_name',
            'doctor_name',
            'sales_name',
            'clinic_name',
        ]

    def get_patient_name(self, obj):
        if obj.patient:
            return obj.patient.get_full_name() or obj.patient.username
        return ''

    def get_doctor_name(self, obj):
        if obj.doctor:
            return obj.doctor.get_full_name() or obj.doctor.username
        return ''

    def get_sales_name(self, obj):
        if obj.sales:
            return obj.sales.get_full_name() or obj.sales.username
        return ''

    def get_clinic_name(self, obj):
        return obj.clinic.name if obj.clinic else ''


class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model  = DoctorAvailability
        fields = ['id', 'day_of_week', 'start_time', 'end_time', 'clinic']