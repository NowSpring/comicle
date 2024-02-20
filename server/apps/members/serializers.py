from drf_writable_nested import WritableNestedModelSerializer
from members.models import Member

class MemberSerializer(WritableNestedModelSerializer):
  
    class Meta:
      
        model = Member
        fields = ["id", "user_name"] 