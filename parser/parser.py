from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


class ParsingResult:
    def __init__(self, result: dict) -> None:
        self.__result = result

    def get_result(self) -> dict:
        return self.__result


class Parser(ABC):
    _browser: webdriver

    def __init__(self, url: str) -> None:
        super().__init__()

        self._browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self._browser.get(url)

    @abstractmethod
    def parse(self) -> ParsingResult:
        pass

    def find_element(self, by: str, identifier: str) -> WebElement:
        return self._browser.find_element(by, identifier)


class DebankParser(Parser):
    def parse(self) -> ParsingResult:
        pass