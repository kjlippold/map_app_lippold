from tethys_sdk.base import TethysAppBase, url_map_maker


class MapAppLippold(TethysAppBase):
    """
    Tethys app class for Map App.
    """

    name = 'Map App'
    index = 'map_app_lippold:home'
    icon = 'map_app_lippold/images/map.png'
    package = 'map_app_lippold'
    root_url = 'map-app-lippold'
    color = '#d35400'
    description = 'Place a brief description of your app here.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='map-app-lippold',
                controller='map_app_lippold.controllers.home'
            ),
            UrlMap(
                name='map-view',
                url='map-app-lippold/map-view',
                controller='map_app_lippold.controllers.map_view'
            ),
            UrlMap(
                name='data-services',
                url='map-app-lippold/data-services',
                controller='map_app_lippold.controllers.data_services'
            ),
            UrlMap(
                name='about',
                url='map-app-lippold/about',
                controller='map_app_lippold.controllers.about'
            ),
            UrlMap(
                name='proposal',
                url='map-app-lippold/proposal',
                controller='map_app_lippold.controllers.proposal'
            ),
            UrlMap(
                name='mockups',
                url='map-app-lippold/mockups',
                controller='map_app_lippold.controllers.mockups'
            ),
            UrlMap(
                name='gizmos',
                url='map-app-lippold/gizmos',
                controller='map_app_lippold.controllers.gizmos'
            ),
        )

        return url_maps