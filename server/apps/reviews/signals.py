import mapping
from django.db.models.signals import post_save
from django.dispatch import receiver
# from accounts.models import User
from members.models import Member
from comics.models import ComicMaster, ComicVersion, ComicEpisode
from reviews.models import ReviewMaster, ReviewVersion, ReviewEpisode

@receiver(post_save, sender=Member)
def create_member_reviews(sender, instance, created, **kwargs):
  
    if created:
  
        comic_masters = ComicMaster.objects.all()
        comic_versions = ComicVersion.objects.all()
        comic_episodes = ComicEpisode.objects.all()
  
        for comic_master in comic_masters:
          
            ReviewMaster.objects.create(member=instance, comic_master=comic_master)
        
        for comic_version in comic_versions:
          
            ReviewVersion.objects.create(member=instance, comic_version=comic_version)
        
        for comic_episode in comic_episodes:
          
            ReviewMaster.objects.create(member=instance, comic_episode=comic_episode)
            

COMIC_REVIEW_MAPPING = {
    ComicMaster: {'review_model': ReviewMaster, 'field_name': 'comic_master'},
    ComicVersion: {'review_model': ReviewVersion, 'field_name': 'comic_version'},
    ComicEpisode: {'review_model': ReviewEpisode, 'field_name': 'comic_episode'},
}


@receiver(post_save, sender=ComicMaster)
@receiver(post_save, sender=ComicVersion)
@receiver(post_save, sender=ComicEpisode)
def create_reviews_for_comic(sender, instance, created, **kwargs):
  
    if created:
      
        members = Member.objects.all()
        mapping = COMIC_REVIEW_MAPPING.get(sender)

        if not mapping:
          
            return
        
        review_model = mapping['review_model']
        field_name = mapping['field_name']
          
        for member in members:
          
            review_model.objects.create(member=member, **{field_name: instance})