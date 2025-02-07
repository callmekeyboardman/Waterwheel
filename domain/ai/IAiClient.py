from abc import abstractmethod, ABC


class IAiClient(ABC):

    @abstractmethod
    def chat(self, prompt: str):
        pass
