# coding: utf-8

from django.conf import settings


TERMS_IGNORED_TAGS = getattr(settings, 'TERMS_IGNORED_TAGS',
    [
        'head',
        'style',
        'script',
        'a',
        'textarea',
        'button',
        'code',
        'samp',
        'kbd',
    ]
)
if hasattr(settings, 'TERMS_ADDITIONAL_IGNORED_TAGS'):
    TERMS_IGNORED_TAGS.extend(settings.TERMS_ADDITIONAL_IGNORED_TAGS)


TERMS_IGNORED_CLASSES = set(
    getattr(settings, 'TERMS_IGNORED_CLASSES',
        (
            'cms_reset',
        )
    )
)
if hasattr(settings, 'TERMS_ADDITIONAL_IGNORED_CLASSES'):
    TERMS_IGNORED_CLASSES |= set(settings.TERMS_ADDITIONAL_IGNORED_CLASSES)


TERMS_IGNORED_IDS = getattr(settings, 'TERMS_IGNORED_IDS',
    [
    ]
)
if hasattr(settings, 'TERMS_ADDITIONAL_IGNORED_IDS'):
    TERMS_IGNORED_IDS.extend(settings.TERMS_ADDITIONAL_IGNORED_IDS)


TERMS_REPLACE_FIRST_ONLY = getattr(settings, 'TERMS_REPLACE_FIRST_ONLY', True)


TERMS_CACHE_TIMEOUT = getattr(settings, 'TERMS_CACHE_TIMEOUT',
                              30)  # seconds


TERMS_IGNORED_APPS = getattr(settings, 'TERMS_IGNORED_APPS',
    [
        'admin',
    ]
)
if hasattr(settings, 'TERMS_ADDITIONAL_IGNORED_APPS'):
    TERMS_IGNORED_APPS.extend(settings.TERMS_ADDITIONAL_IGNORED_APPS)
