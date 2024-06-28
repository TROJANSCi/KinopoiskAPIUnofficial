from typing import Literal, List

from requests import Session

MONTHS = {
    1: 'JANUARY', 2: 'FEBRUARY',
    3: 'MARCH', 4: 'APRIL',
    5: 'MAY', 6: 'JUNE',
    7: 'JULY', 8: 'AUGUST',
    9: 'SEPTEMBER', 10: 'OCTOBER',
    11: 'NOVEMBER', 12: 'DECEMBER'
}


class KinopoiskAPIUnofficial:
    URL: str = 'https://kinopoiskapiunofficial.tech/api'
    API_VERSION: str = 'v2.2'

    def __init__(self, token: str):
        self.token = token
        headers = {
            'X-API-KEY': token,
            'Content-Type': 'application/json',
        }
        self.session = Session()
        self.session.headers = headers
        self.server = f'{self.URL}/{self.API_VERSION}'

    def request(self, url: str) -> dict | None:
        """Request"""
        response = self.session.get(url=url)
        if response.status_code != 200:
            return None
        return response.json()

    def films_information(self, kip: int) -> dict | None:
        """
        Возвращает базовые данные о фильме.
        Поле lastSync показывает дату последнего обновления данных.
        """
        url: str = f'{self.server}/films/{kip}'
        response = self.request(url=url)
        return response if response else None

    def films_seasons(self, kip: int) -> dict | None:
        """Возвращает данные о сезонах для сериала."""
        url: str = f'{self.server}/films/{kip}/seasons'
        response = self.request(url=url)
        return response if response else None

    def films_facts(self, kip: int) -> dict | None:
        """
        Возвращает список фактов и ошибок в фильме.
        FACT, обозначает интересный факт о фильме.
        BLOOPER, обозначает ошибку в фильме.
        """
        url: str = f'{self.server}/films/{kip}/facts'
        response = self.request(url=url)
        return response if response else None

    def films_distributions(self, kip: int) -> dict | None:
        """Возвращает данные о прокате в разных странах."""
        url: str = f'{self.server}/films/{kip}/distributions'
        response = self.request(url=url)
        return response if response else None

    def films_box_office(self, kip: int) -> dict | None:
        """Возвращает данные о бюджете и сборах."""
        url: str = f'{self.server}/films/{kip}/box_office'
        response = self.request(url=url)
        return response if response else None

    def films_awards(self, kip: int) -> dict | None:
        """Возвращает данные о наградах и премиях фильма."""
        url: str = f'{self.server}/films/{kip}/awards'
        response = self.request(url=url)
        return response if response else None

    def films_videos(self, kip: int) -> dict | None:
        """
        Возвращает трейлеры, тизеры, видео для фильма по kinopoisk id. В данный момент доступно три site:
        YOUTUBE - в этом случае url это просто ссылка на youtube видео.
        YANDEX_DISK - в этом случае url это ссылка на yandex disk.
        KINOPOISK_WIDGET - в этом случае url это ссылка на кинопоиск виджет.
        """
        url: str = f'{self.server}/films/{kip}/videos'
        response = self.request(url=url)
        return response if response else None

    def films_similars(self, kip: int) -> dict | None:
        """получить список похожих фильмов по kinopoisk film id"""
        url: str = f'{self.server}/films/{kip}/similars'
        response = self.request(url=url)
        return response if response else None

    def films_images(self, kip: int, pg: int = 1,
                     _type: Literal['STILL', 'SHOOTING', 'POSTER',
                     'FAN_ART', 'PROMO', 'CONCEPT', 'WALLPAPER',
                     'COVER', 'SCREENSHOT'] = 'SCREENSHOT') -> dict | None:
        """
        Возвращает изображения фильма с пагинацией. Каждая страница содержит не более чем 20 фильмов.
        Доступные изображения:
        STILL - кадры
        SHOOTING - изображения со съемок
        POSTER - постеры
        FAN_ART - фан-арты
        PROMO - промо
        CONCEPT - концепт-арты
        WALLPAPER - обои
        COVER - обложки
        SCREENSHOT - скриншоты

        Default value: SCREENSHOT
        """
        url: str = f'{self.server}/films/{kip}/images?type={_type}&page={pg}'
        response = self.request(url=url)
        return response if response else None

    def films_reviews(self, kip: int, pg: int = 1,
                      order: Literal['DATE_ASC', 'DATE_DESC', 'USER_POSITIVE_RATING_ASC',
                      'USER_POSITIVE_RATING_DESC', 'USER_NEGATIVE_RATING_ASC',
                      'USER_NEGATIVE_RATING_DESC',] = 'DATE_DESC') -> dict | None:
        """
        Возвращает список рецензии зрителей с пагинацией. Каждая страница содержит не более чем 20 рецензий.
        Тип сортировки
        Available values:   DATE_ASC
                            DATE_DESC
                            USER_POSITIVE_RATING_ASC
                            USER_POSITIVE_RATING_DESC
                            USER_NEGATIVE_RATING_ASC
                            USER_NEGATIVE_RATING_DESC

        Default value: DATE_DESC
        """
        url: str = f'{self.server}/films/{kip}/reviews?page={pg}&order={order}'
        response = self.request(url=url)
        return response if response else None

    def films_external_sources(self, kip: int, pg: int = 1) -> dict | None:
        """Возвращает список сайтов с пагинацией. Каждая страница содержит не более чем 20 рецензий."""
        url: str = f'{self.server}/films/{kip}/external_sources?page={pg}'
        response = self.request(url=url)
        return response if response else None

    def films_collections(self, pg: int = 1,
                          _type: Literal['TOP_POPULAR_ALL', 'TOP_POPULAR_MOVIES',
                          'TOP_250_TV_SHOWS', 'TOP_250_MOVIES', 'VAMPIRE_THEME',
                          'COMICS_THEME', 'CLOSES_RELEASES', 'FAMILY', 'OSKAR_WINNERS_2021',
                          'LOVE_THEME', 'ZOMBIE_THEME', 'CATASTROPHE_THEME', 'KIDS_ANIMATION_THEME',
                          'POPULAR_SERIES',] = 'TOP_POPULAR_ALL') -> dict | None:
        """
        Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов.
        Тип топа или коллекции
        Available values:
                        TOP_POPULAR_ALL
                        TOP_POPULAR_MOVIES
                        TOP_250_TV_SHOWS
                        TOP_250_MOVIES
                        VAMPIRE_THEME
                        COMICS_THEME
                        CLOSES_RELEASES
                        FAMILY
                        OSKAR_WINNERS_2021
                        LOVE_THEME
                        ZOMBIE_THEME
                        CATASTROPHE_THEME
                        KIDS_ANIMATION_THEME
                        POPULAR_SERIES

        Default value: TOP_POPULAR_ALL
        """
        url: str = f'{self.server}/films/collections?type={_type}&page={pg}'
        response = self.request(url=url)
        return response if response else None

    def films_premieres(self, year: int, month: int = 1) -> dict | None:
        """
        Возвращает список кинопремьер.
        Available values:
                        1. JANUARY
                        2. FEBRUARY
                        3. MARCH
                        4. APRIL
                        5. MAY
                        6. JUNE
                        7. JULY
                        8. AUGUST
                        9. SEPTEMBER
                        10. OCTOBER
                        11. NOVEMBER
                        12. DECEMBER

        Default value: 1
        """

        url: str = f'{self.server}/films/premieres?year={year}&month={MONTHS.get(month)}'
        response = self.request(url=url)
        return response if response else None

    def films_filters(self) -> dict | None:
        """Возвращает список id стран и жанров, которые могут быть использованы в /api/v2.2/films"""
        url: str = f'{self.server}/films/filters'
        response = self.request(url=url)
        return response if response else None

    def films(self,
              countries: int | List[int] = None,
              genres: int | List[int] = None,
              order: Literal['RATING', 'NUM_VOTE', 'YEAR'] = 'RATING',
              _type: Literal['ALL', 'FILM', 'TV_SHOW', 'TV_SERIES', 'MINI_SERIES'] = 'ALL',
              min_rating: int = 0,
              max_rating: int = 10,
              year_from: int = 1000,
              year_to: int = 3000,
              keyword: str = None,
              pg: int = 1) -> dict | None:
        """
        Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов.
        Данный эндпоинт не возращает более 400 фильмов.
        Используй films/filters что-бы получить id стран и жанров.
        :param countries:
        :param genres:
        :param order:
        :param _type:
        :param min_rating:
        :param max_rating:
        :param year_from:
        :param year_to:
        :param keyword:
        :param pg:
        :return:
        """
        url: str = (f'{self.server}/films?order={order}&type={_type}&ratingFrom={min_rating}&ratingTo={max_rating}&'
                    f'yearFrom={year_from}&yearTo={year_to}&page={pg}')
        if countries:
            if type(countries) is list:
                country = ''.join([f'&countries={i}' for i in countries])
                url += country
            else:
                url += f'&countries={countries}'
        if genres:
            if type(genres) is list:
                g = ''.join([f'&genres={i}' for i in genres])
                url += g
            else:
                url += f'&genres={genres}'

        if keyword:
            url += f'&keyword={keyword}'

        response = self.request(url=url)
        return response if response else None

    def films_sequels_and_prequels(self, kip: int) -> dict | None:
        """Возвращает сиквел/приквел по кинопоиск ид"""
        url: str = f'{self.URL}/v2.1/films/{kip}/sequels_and_prequels'
        response = self.request(url=url)
        return response if response else None

    def films_search_by_keyword(self, keyword: str, pg: int = 1) -> dict | None:
        """Возвращает список фильмов с пагинацией. Каждая страница содержит не более чем 20 фильмов."""
        url: str = f'{self.URL}/v2.1/films/search-by-keyword?keyword={keyword}&page={pg}'
        response = self.request(url=url)
        return response if response else None

    def films_releases(self, year: int, month: int = 1, pg: int = 1) -> dict | None:
        """
        Возвращает список цифровых релизов.
        Например: https://www.kinopoisk.ru/comingsoon/digital/
        """
        url: str = f'{self.URL}v2.1/films/releases?year={year}&month={MONTHS.get(month)}&page={pg}'
        response = self.request(url=url)
        return response if response else None

    def staffs(self, kip: int) -> dict | None:
        """
        Набор методов для работы с данными об актерах, режиссерах и т.д.
        """
        url: str = f'{self.URL}/v1/staff?filmId={kip}'
        response = self.request(url=url)
        return response if response else None

    def staff(self, person_id: int) -> dict | None:
        """
        Данные об актере, режиссере и т.д.
        """
        url: str = f'{self.URL}/v1/staff/{person_id}'
        response = self.request(url=url)
        return response if response else None

    def person(self, name: str, pg: int = 1) -> dict | None:
        """
        Данные об актере, режиссере и т.д.
        """
        url: str = f'{self.URL}/v1/persons?name={name}&page={pg}'
        response = self.request(url=url)
        return response if response else None

    def news(self, pg: int = 1):
        """
        Получить медиа новости с сайта кинопоиск
        Одна страница может содержать до 20 элементов в items.
        :param pg: Page default 1
        :return:
        """
        url: str = f'{self.URL}/v1/media_posts?page={pg}'
        response = self.request(url=url)
        return response if response else None

    def api_keys(self, api_keys: str = None) -> dict | None:
        """
        API keys details
        """
        api_keys = self.token if api_keys is None else api_keys
        url: str = f'{self.URL}/v1/api_keys/{api_keys}'
        response = self.request(url=url)
        return response if response else None
