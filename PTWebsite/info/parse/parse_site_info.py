from info.SiteInfo import SiteInfo
from meta.SiteMeta import SiteMeta


def parse_site_info(site_meta: SiteMeta) -> SiteInfo:
    site_info = SiteInfo()
    site_info.name = site_meta.name
    site_info.owner = site_meta.owner
    site_info.key_words = site_meta.key_words
    site_info.description = site_meta.description
    site_info.customer_meta = site_meta.customer_meta

    return site_info


if __name__ == "__main__":
    from meta.parse.parse_site_meta import parse_site_meta

    site_meta = parse_site_meta("../../../demo/meta.json")
    site_info = parse_site_info(site_meta)
    print(site_info)
