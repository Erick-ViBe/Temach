from rest_framework import serializers
from students.models import Student, Ratings


class SingleStudentSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Student
        fields = [
            'student_first_name',
            'student_last_name',
            'slug',
            'sex',
        ]


class StudentSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField(read_only=True)
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Student
        exclude = [
            'created_at',
            'updated_at',
        ]


class RatingsSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField(read_only=True)
    student_id = serializers.SerializerMethodField()
    average = serializers.SerializerMethodField()

    class Meta:
        model = Ratings
        fields = '__all__'


    def get_student_id(self, instance):
        return instance.student.pk


    def get_average(self, instance):
        total_rating_sum = instance.rating_1 + instance.rating_2 + instance.rating_3 + instance.rating_4 + instance.rating_5 + instance.rating_6 + instance.rating_7 + instance.rating_8 + instance.rating_9 + instance.rating_10
        grade = instance.student.teacher.grade

        if grade == 1:
            number_subjects = 7
        elif grade == 2:
            number_subjects = 9
        elif grade == 3:
            number_subjects = 10

        return round(total_rating_sum/number_subjects, 2)
