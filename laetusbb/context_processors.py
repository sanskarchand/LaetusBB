from django.conf import settings

# For base template
def base(request):
    return {
        'forum_title': settings.SITE_CONFIG['general']['ForumTitle'],
        'bg_path': settings.SITE_CONFIG['general']['BackgroundImage'],
        'bg_repeat': settings.SITE_CONFIG['general']['BackgroundRepeatCSS'],
    }
