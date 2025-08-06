from enum import Enum

from pydantic import HttpUrl, EmailStr, BaseModel, FilePath, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing_extensions import Self


class Browser(str, Enum):
    WEBKIT = "webkit"
    FIREFOX = "firefox"
    CHROMIUM = "chromium"


class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str


class TestData(BaseModel):
    image_png_file: FilePath


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",  # Указываем, из какого файла читать настройки
        env_file_encoding="utf-8",  # Указываем кодировку файла
        env_nested_delimiter=".",  # Указываем разделитель для вложенных переменных
    )

    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]  # pydantic ожидает список значений, которые точно совпадают с перечисленными в Enum
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    allure_results_dir: DirectoryPath
    browser_state_file: FilePath

    @classmethod
    def initialize(cls) -> Self:
        videos_dir = DirectoryPath('./videos')
        tracing_dir = DirectoryPath('./tracing')
        allure_results_dir = DirectoryPath('./allure-results')
        browser_state_file = FilePath('browser-state.json')

        videos_dir.mkdir(exist_ok=True)  # Если задано exist_ok=True, указание существующего каталога не вызовет ошибку
        tracing_dir.mkdir(exist_ok=True)
        allure_results_dir.mkdir(exist_ok=True)
        browser_state_file.touch(exist_ok=True)

        return Settings(
            videos_dir=videos_dir,
            tracing_dir=tracing_dir,
            allure_results_dir=allure_results_dir,
            browser_state_file=browser_state_file
        )

    def get_base_url(self) -> str:
        return f"{self.app_url}/"


# Инициализируем настройки
settings = Settings.initialize()
