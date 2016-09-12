from requests import request, HTTPError

from django.core.files.base import ContentFile


def save_profile_picture(backend, strategy, user, response, details,
                         is_new=False,*args,**kwargs):

    if is_new: 
        if backend.name == 'facebook':
            url = 'http://graph.facebook.com/{0}/picture?type=large'.format(response['id'])
        elif backend.name == 'twitter':
            url = response.get('profile_image_url', '').replace('_normal','')
        
        try:
            response = request('GET', url)
            response.raise_for_status()
        except HTTPError:
            pass
        else:
            profile = user.profile
            profile.stakeholder.picture.save('{0}_social.jpg'.format(user.username),
                                   ContentFile(response.content))
            print profile.stakeholder
            profile.save()