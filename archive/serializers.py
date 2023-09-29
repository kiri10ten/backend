from rest_framework import serializers

from .models import Archive, Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id', 'title',)


class ArchiveSerializer(serializers.ModelSerializer):
    subject_title = serializers.ReadOnlyField(source='subject.title')
    created_by_initials = serializers.SerializerMethodField()


    class Meta:
        model = Archive
        fields = (
            'id',
            'title',
            'subject_title',
            'description',
            'created_at_formatted',
            'created_by',
            'url',
            'created_by_initials', 

            
        )


    def get_created_by_initials(self, obj):
    # Access the related user's username and get the first three characters
        creator_username = obj.created_by.username if obj.created_by else ''
        return creator_username[:3]


class ArchiveDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = (
            'id',
            'title',
            'subject_title',
            'description',
            'created_at_formatted',
            'created_by',
            'url',
            'created_by_initials', 

        )

