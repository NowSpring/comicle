from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage

from comics.models import ComicMaster, ComicVersion, ComicEpisode

@receiver(post_delete, sender=ComicEpisode)
@receiver(post_delete, sender=ComicMaster)
@receiver(post_delete, sender=ComicVersion)
def delete_related_files(sender, instance, **kwargs):
    
    if instance.cover:
      
        if default_storage.exists(instance.cover.name):
          
            default_storage.delete(instance.cover.name)
    
    if hasattr(instance, 'pdf') and instance.pdf:
      
        if default_storage.exists(instance.pdf.name):
          
            default_storage.delete(instance.pdf.name)
