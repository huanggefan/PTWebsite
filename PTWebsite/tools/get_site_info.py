import var
from info.SiteInfo import SiteInfo
from meta.parse.parse_site_meta import parse_site_meta


def get_site_info() -> SiteInfo:
    site_meta = parse_site_meta(var.meta_work_dir)

    site_info = SiteInfo()
    site_info.name = site_meta.name
    site_info.owner = site_meta.owner
    site_info.key_words = site_meta.key_words
    site_info.description = site_meta.description
    site_info.customer_meta = site_meta.customer_meta

    return site_info
